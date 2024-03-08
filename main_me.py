import os

def replace_in_file(file_path, replacements):
    with open(file_path, 'r') as file:
        filedata = file.read()

    for old_str, new_str in replacements.items():
        filedata = filedata.replace(old_str, new_str)

    with open(file_path, 'w') as file:
        file.write(filedata)

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
            old_str, new_str = line.strip().split('=')
            replacements[old_str] = new_str
    return replacements

def main():
    folder_path = input("Enter the folder path: ")
    config_file = os.path.join(folder_path, "list.conf")
    
    replacements = read_replacements_from_config(config_file)
    find_replace_in_folder(folder_path, replacements)

if __name__ == "__main__":
    main()
