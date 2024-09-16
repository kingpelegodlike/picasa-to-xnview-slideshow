"""Picasa tool INI file parser ."""

import re

class PicasaIniParser:
    """Class representing a Picasa tool INI file parser."""
    def __init__(self, basepath, filepath):
        self.basepath = basepath
        self.filepath = filepath
        self.favorite_files = []

    def parse(self):
        """Parse the INI file."""
        with open(self.filepath, 'r', encoding="utf-8") as file:
            lines = file.readlines()
        is_picture_line = False
        is_contact_line = False
        picture_file_name = ''
        pictures_faces = {}
        contact_tags = {}
        for line in lines:
            if line.startswith('[') and line.endswith(']\n'):
                if line == '[Contacts2]\n':
                    print("get contacts")
                    is_contact_line = True
                    is_picture_line = False
                else:
                    is_contact_line = False
                    is_picture_line = True
                    picture_file_name = line[1:-2]
                print(line)
                continue
            if is_picture_line:
                find_faces = re.match(r'faces=(.*)\n', line)
                if line == 'star=yes\n':
                    self.favorite_files.append(f"{self.basepath}/{picture_file_name}")
                if find_faces:
                    print(find_faces.group(1))
                    faces = find_faces.group(1).split(',')
                    pictures_faces[picture_file_name] = faces
                continue
            if is_contact_line:
                find_contact = re.match(r'(.*)=(.*);;+\n', line)
                if find_contact:
                    print(find_contact.group(1), find_contact.group(2))
                    contact_tags[find_contact.group(1)] = find_contact.group(2)
                continue
        for picture_file_name, faces in pictures_faces.items():
            for face in faces:
                for tag, contact in contact_tags.items():
                    if face == tag:
                        print(f"{picture_file_name} - {contact}")

# Usage example
parser = \
    PicasaIniParser(\
        '2001/20010601-20010603.Mariage.Varunah.et.Xavier',\
        'tests/data/Perso/2001/20010601-20010603.Mariage.Varunah.et.Xavier/.picasa.ini')
parser.parse()
print(len(parser.favorite_files))
