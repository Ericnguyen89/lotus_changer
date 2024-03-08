import os

def replace_in_file(file_path, replacements):
    encodings = ['utf-8', 'latin-1']  # Add more encodings if necessary
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding, errors="ignore") as file:
                filedata = file.read()

            for old_str, new_str in replacements.items():
                filedata = filedata.replace(old_str, new_str)

            with open(file_path, 'w', encoding=encoding) as file:
                file.write(filedata)

            break  # Exit the loop if the file was successfully read and written
        except UnicodeDecodeError:
            print(f"Failed to read file '{file_path}' with encoding '{encoding}'. Trying another encoding...")
        except Exception as e:
            print(f"An error occurred while processing file '{file_path}': {e}")

def find_replace_in_folder(folder_path, replacements):
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if os.path.isfile(file_path):
                replace_in_file(file_path, replacements)

def read_replacements_from_config(config_file):
    replacements = {}
    with open(config_file, 'r') as file:
        for line in file:
            line = line.strip()
            if '=' in line:
                old_str, new_str = line.split('=')
                replacements[old_str] = new_str
            else:
                print(f"Skipping line: {line} in config file.")
    return replacements

def main():
    folder_path = input("Enter the folder path: ")
    config_file = "list.conf"
    
    if not os.path.isfile(config_file):
        print(f"Config file '{config_file}' not found.")
        return

    replacements = read_replacements_from_config(config_file)
    find_replace_in_folder(folder_path, replacements)
    print("Replacement completed.")

if __name__ == "__main__":
    main()
