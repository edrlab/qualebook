import glob
import os

# --- CONFIGURATION ---
DIR_PATH = "content/English/rules"

# The EXACT text to look for. 
# We include the hyphen and quotes to be sure we don't replace the wrong thing.
# We do NOT include the indentation spaces (the code handles that).
TARGET_STRING = '- "design"'

# The EXACT text to replace it with.
# Change this to "Editorial design" if you prefer that over "editorial planning"
NEW_STRING = '- "Editorial planning"'

def process_files():
    search_path = os.path.join(DIR_PATH, "*.md")
    files = glob.glob(search_path)
    count = 0

    print(f"Scanning {DIR_PATH} for simple text replacement...")

    for file_path in files:
        # Skip the index file
        if os.path.basename(file_path) == "_index.md":
            continue

        try:
            # 1. Read the file as a list of lines (strings)
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            new_lines = []
            file_modified = False

            # 2. Check each line one by one
            for line in lines:
                # We check if our target is in this line
                if TARGET_STRING in line:
                    # .replace() keeps the surrounding spaces/indentation intact!
                    new_line = line.replace(TARGET_STRING, NEW_STRING)
                    new_lines.append(new_line)
                    file_modified = True
                else:
                    # Keep the line exactly as it was
                    new_lines.append(line)

            # 3. Save only if we actually changed something
            if file_modified:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.writelines(new_lines)
                print(f"✅ Modified: {os.path.basename(file_path)}")
                count += 1

        except Exception as e:
            print(f"❌ Error processing {file_path}: {e}")

    print(f"Done. {count} files updated.")

if __name__ == "__main__":
    process_files()