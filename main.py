import os
import json


def create_folder_structure(base_path, structure):
    """
    Creates nested directories according to a given structure.
    """
    for main_category, sub_categories in structure.items():
        for category in sub_categories:
            directory_path = os.path.join(base_path, main_category, category)
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
                print(f'Folder created: {directory_path}')
            else:
                print(f'Folder already exists: {directory_path}')


def write_structure_to_json(json_filepath, data):
    """
    Writes the given data structure to a JSON file.
    """
    with open(json_filepath, 'w') as file:
        json.dump(data, file, indent=4)


def print_folder_hierarchy(json_filepath):
    """
    Prints the folder hierarchy from a JSON file.
    """
    with open(json_filepath, 'r') as file:
        structure = json.load(file)
        print('Folder hierarchy:')
        for main_category, sub_categories in structure.items():
            print(f'. {main_category}')
            for category in sub_categories:
                print(f'--- {category}')
            print('=' * 25)


def manage_structure(base, structure):
    """
    Manages the folder structure: creates the folders and writes them to JSON if not existing,
    otherwise prints the folder hierarchy.
    """
    base_path = os.path.join(os.environ['USERPROFILE'], 'Downloads/Structures')
    json_filepath = os.path.join(base_path, 'settings.json')

    if not os.path.exists(base_path):
        os.makedirs(base_path)
        print(f'Base directory created at: {base_path}')

    if os.path.isfile(json_filepath):
        print_folder_hierarchy(json_filepath)
    else:
        create_folder_structure(base_path, structure)
        write_structure_to_json(json_filepath, structure)


user_base_path = os.path.join(os.environ['USERPROFILE'], 'Downloads/Structures')

folder_structure = {
            'Music': ['Rock', 'Jazz', 'Pop'],
            'Documents': ['Facture', 'Travail', 'Maison'],
            'Images': ['Vacances', 'Famille'],
            'Videos': ['Chat', 'Facebook']
            }

manage_structure(user_base_path, folder_structure)