import os

structure = {
            'Music': ['Rock', 'Jazz', 'Pop'],
            'Documents': ['Facture', 'Travail', 'Maison'],
            'Images': ['Vacances', 'Famille'],
            'Videos': ['Chat', 'Facebook']
            }


def create_folder(folder):
    for key, values in folder.items():
        for value in values:
            folder = '{0}/{1}/{2}'.format(base, key, value)
            os.makedirs(folder)
            print('Folder Creation {0}'.format(folder))


base = r'C:\Users\dclairvoyant\OneDrive - Ubisoft\Documents\GitHub\FolderStructures\Structure'
base.replace('\\', '/')
