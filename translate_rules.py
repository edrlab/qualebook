import os
import json
import time
import google.generativeai as genai
from ruamel.yaml import YAML

API_KEY = ""

ENGLISH_DIR = 'content/English/rules'
KEYS_TO_TRANSLATE = ['title', 'abstract', 'Meo', 'objectif', 'Controle']

# Configuration du modèle Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-3-flash-preview') # ou 'gemini-1.5-flash'

# Configuration YAML pour préserver le style (quotes, blocs, etc.)
yaml = YAML()
yaml.preserve_quotes = True
yaml.width = 4096
yaml.indent(mapping=2, sequence=4, offset=2) # Ajustez selon votre préférence d'indentation

def get_translation_from_gemini(filename, full_content):
    
    prompt = f"""
    You are an expert translator specializing in digital accessibility, web quality, and ebook standards.
    You are working on the "Qualebook" project, which is inspired by the "Opquast" quality checklist.
    
    TASK:
    Translate the French values found in the YAML Front Matter of the provided Markdown file into English.
    
    CONTEXT:
    - "Meo" stands for "Mise en œuvre" (Implementation).
    - "Controle" stands for "Control" or "Audit".
    - "Objectif" stands for "Objective".
    - Keep the tone professional, technical, and concise.
    - Terminology: Use standard W3C/WCAG/EPUB accessibility terminology (e.g., "Landmarks" for "Points de repère").
    
    INSTRUCTIONS:
    1. Read the provided Markdown file content below.
    2. Extract and translate the values for ONLY these specific keys: {KEYS_TO_TRANSLATE}.
    3. If a value is a list (bullet points), keep it as a list in English.
    4. If a value is a string, keep it as a string.
    5. RETURN ONLY A VALID JSON OBJECT. Do not add markdown formatting (like ```json).
    
    MARKDOWN CONTENT ({filename}):
    {full_content}
    """

    try:
        # On demande une réponse en JSON
        response = model.generate_content(
            prompt,
            generation_config={"response_mime_type": "application/json"}
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"❌ Erreur API Gemini pour {filename}: {e}")
        return None

def process_files():
    if not os.path.exists(ENGLISH_DIR):
        print(f"Erreur : Le dossier {ENGLISH_DIR} n'existe pas.")
        return

    files = [f for f in os.listdir(ENGLISH_DIR) if f.endswith('.md') and f != '_index.md']
    total = len(files)
    
    print(f"🚀 Démarrage de la traduction pour {total} fichiers...")

    for index, filename in enumerate(files):
        filepath = os.path.join(ENGLISH_DIR, filename)
        
        # 1. Lire le fichier brut pour le prompt (contexte total)
        with open(filepath, 'r', encoding='utf-8') as f:
            raw_content = f.read()

        # 2. Lire le YAML proprement pour l'édition
        parts = raw_content.split('---', 2)
        if len(parts) < 3:
            print(f"⚠️ Ignoré (Format invalide) : {filename}")
            continue
            
        try:
            yaml_data = yaml.load(parts[1])
        except Exception as e:
            print(f"⚠️ Erreur parsing YAML {filename}: {e}")
            continue

        # 3. Appel API Gemini
        print(f"[{index+1}/{total}] Traduction de {filename}...")
        translated_json = get_translation_from_gemini(filename, raw_content)

        if not translated_json:
            continue

        # 4. Mise à jour des valeurs
        changes_made = False
        for key in KEYS_TO_TRANSLATE:
            if key in translated_json and key in yaml_data:
                # Vérification simple pour éviter des remplacements inutiles
                yaml_data[key] = translated_json[key]
                changes_made = True
            elif key in translated_json and key not in yaml_data:
                 yaml_data[key] = translated_json[key]
                 changes_made = True

        # 5. Sauvegarde
        if changes_made:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(parts[0]) # Préambule (souvent vide)
                f.write('---\n')
                yaml.dump(yaml_data, f)
                f.write('---\n') # Ruamel ne remet pas toujours le séparateur de fin
                body = parts[2]
                if body.startswith('\n'):
                    f.write(body[1:]) # Évite de doubler le saut de ligne
                else:
                    f.write(body)
            
            print(f"✅ Sauvegardé : {filename}")
        else:
            print(f"Science : Pas de changements pour {filename}")

        time.sleep(1) 

if __name__ == "__main__":
    process_files()