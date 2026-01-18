import glob
import os

# --- CONFIGURATION ---
DIR_PATH = "content/french/rules"
KEYS_TO_FIX = ['abstract', 'objectif', 'Meo', 'Control', 'Controle']

def fix_line_punctuation(line):
    # 1. Basic Cleanup to find the end
    r_stripped = line.rstrip()
    if not r_stripped: return line
    
    # 2. Check if line ends with a quote
    last_char = r_stripped[-1]
    if last_char not in ['"', "'"]: 
        return line
    
    # 3. Analyze content BEFORE the closing quote
    # Index of the last quote
    quote_index = len(r_stripped) - 1
    
    # Everything before the quote
    content_raw = line[:quote_index]
    
    # Strip spaces from the right of the content to find the REAL end of the sentence
    # e.g. '  abstract: "Hello. ' -> '  abstract: "Hello.'
    content_clean = content_raw.rstrip()
    
    # Safety: If string is empty or just the opening quote, skip
    if not content_clean: return line
    if content_clean[-1] in ['"', "'", ':']: return line

    # 4. Check for existing punctuation
    # We look at the last character of the CLEAN content
    if content_clean[-1] in ['.', '?', '!']:
        # Punctuation exists! (Even if there was a space after it)
        # We return the ORIGINAL line to avoid changing spacing unnecessarily, 
        # OR we could return the cleaned version if you want to remove the space.
        # For safety/minimal diffs, we return the original line.
        return line

    # 5. If missing, ADD the dot
    # We construct the new line using the CLEAN content.
    # This automatically removes any accidental trailing spaces inside the quote.
    # Old: '  abstract: "Hello "' -> New: '  abstract: "Hello."'
    
    # Rebuild: [Clean Content] + [.] + [Closing Quote] + [Original Newline/Spacing]
    new_line = content_clean + "." + line[quote_index:]
    
    return new_line

def process_files():
    search_path = os.path.join(DIR_PATH, "*.md")
    files = glob.glob(search_path)
    count = 0

    print(f"Scanning {DIR_PATH} (ignoring trailing spaces)...")

    for file_path in files:
        if os.path.basename(file_path) == "_index.md":
            continue

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            new_lines = []
            file_modified = False
            current_key = None
            in_frontmatter = False

            for line in lines:
                if line.strip() == '---':
                    in_frontmatter = not in_frontmatter
                    new_lines.append(line)
                    continue
                
                if not in_frontmatter:
                    new_lines.append(line)
                    continue

                # Identify Key
                stripped_start = line.lstrip()
                potential_key_match = False
                for key in KEYS_TO_FIX:
                    if stripped_start.startswith(key + ":"):
                        current_key = key
                        potential_key_match = True
                        break
                
                if not potential_key_match and ":" in stripped_start and not stripped_start.startswith("-"):
                    current_key = None

                # Process
                if current_key in KEYS_TO_FIX:
                    is_list_item = stripped_start.startswith("-")
                    is_inline_val = stripped_start.startswith(current_key + ":")
                    
                    if is_list_item or is_inline_val:
                        fixed_line = fix_line_punctuation(line)
                        if fixed_line != line:
                            new_lines.append(fixed_line)
                            file_modified = True
                        else:
                            new_lines.append(line)
                    else:
                        new_lines.append(line)
                else:
                    new_lines.append(line)

            if file_modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(new_lines)
                print(f"✅ Fixed: {os.path.basename(file_path)}")
                count += 1

        except Exception as e:
            print(f"❌ Error in {file_path}: {e}")

    print(f"Done. {count} files updated.")

if __name__ == "__main__":
    process_files()