"""Picasa tool INI file parser ."""

import os
import re

class PicasaIniParser:
    """Class representing a Picasa tool INI file parser."""
    def __init__(self, basepath, filepath):
        self.basepath = basepath
        self.filepath = filepath
        self.favorite_files = []
        self.contact_files = {}

    def parse(self):
        """Parse the INI file."""
        with open(self.filepath, 'r', encoding="utf-8") as ini_file:
            lines = ini_file.readlines()
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
                    self.favorite_files.append(f"{self.basepath}{os.sep}{picture_file_name}")
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
                for tag, contact_name in contact_tags.items():
                    if face == tag:
                        print(f"{picture_file_name} - {contact_name}")
                        if contact_name not in self.contact_files:
                            self.contact_files[contact_name] = []
                        self.contact_files[contact_name].append(\
                            f"{self.basepath}{os.sep}{picture_file_name}")
