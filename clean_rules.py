import os
from ruamel.yaml import YAML

# --- Configuration ---
english_dir = 'content/English/rules'
french_dir = 'content/french/rules'
keys_to_sync = ['title', 'abstract', 'Meo', 'objectif', 'Controle']

# Configuration du moteur YAML pour préserver les quotes et le style
yaml = YAML()
yaml.preserve_quotes = True
yaml.width = 4096 # Évite de couper les lignes trop tôt

def get_parts(filepath):
    """
    Lit le fichier et sépare le Front Matter (YAML) du contenu (Markdown).
    Retourne: (yaml_object, content_string, original_separator)
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # On sépare sur les '---'. 
    # parts[0] = vide (avant le 1er ---), parts[1] = YAML, parts[2] = Reste
    parts = content.split('---', 2)
    
    if len(parts) < 3:
        return None, None, None
        
    # Charge le YAML en mode "Round-Trip" (garde l'ordre et les quotes)
    yaml_data = yaml.load(parts[1])
    return yaml_data, parts[2], parts[0]

def sync_translations():
    if not os.path.exists(english_dir) or not os.path.exists(french_dir):
        print("Erreur: Dossiers introuvables.")
        return

    for filename in os.listdir(english_dir):
        if not filename.endswith('.md') or filename == '_index.md':
            continue

        en_filepath = os.path.join(english_dir, filename)
        fr_filepath = os.path.join(french_dir, filename)

        if not os.path.exists(fr_filepath):
            print(f"Ignoré (FR manquant): {filename}")
            continue

        try:
            # 1. Charger les données
            fr_data, _, _ = get_parts(fr_filepath)
            en_data, en_content, en_preamble = get_parts(en_filepath)

            if fr_data is None or en_data is None:
                print(f"Erreur de format (--- manquant) : {filename}")
                continue

            changes_made = False

            # 2. Remplacer les valeurs
            for key in keys_to_sync:
                if key in fr_data:
                    # Si la valeur française est différente de l'anglaise
                    if en_data.get(key) != fr_data[key]:
                        # Affectation directe : ruamel gère le style automatiquement.
                        # Si fr_data[key] avait des quotes, elles seront conservées.
                        en_data[key] = fr_data[key]
                        changes_made = True

            # 3. Sauvegarder
            if changes_made:
                with open(en_filepath, 'w', encoding='utf-8') as f:
                    # Réécrire le préambule (généralement vide)
                    f.write(en_preamble) 
                    f.write('---\n')
                    # Dumper le YAML modifié (l'ordre et les quotes sont préservés)
                    yaml.dump(en_data, f)
                    f.write('---')
                    # Réécrire le contenu Markdown inchangé
                    f.write(en_content)
                
                print(f"Mis à jour avec succès : {filename}")
            else:
                print(f"Aucun changement : {filename}")

        except Exception as e:
            print(f"Erreur sur {filename}: {e}")

if __name__ == "__main__":
    print("Démarrage de la synchronisation (Preservation des quotes)...")
    sync_translations()
    print("Terminé.")