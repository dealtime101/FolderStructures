import os
import json

structure = {
            'Music': ['Rock', 'Jazz', 'Pop'],
            'Documents': ['Facture', 'Travail', 'Maison'],
            'Images': ['Vacances', 'Famille'],
            'Videos': ['Chat', 'Facebook']
            }


def create_folder(base, folder_path):
    for key, values in folder_path.items():
        for value in values:
            folder_path = '{0}/{1}/{2}'.format(base, key, value)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                print(f'Folder created: {folder_path}')
            else:
                print(f'Folder already exists: {folder_path}')


base = os.path.join(os.environ['USERPROFILE'], 'Downloads/Structures')
json_file = os.path.join(base, 'settings.json')


def write_json(json_file, data):
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)


create_folder(base, structure)
write_json(json_file, structure)
