""" Convert a Picasa INI file to a SLD file. """
import os
from pathlib import Path
from picasa_ini_parser import PicasaIniParser # pylint: disable=import-error

def ini_to_sld(base_path, sld_path):
    """Convert a Picasa INI file to a SLD file."""
    with open(sld_path, 'w', encoding="utf-8") as sld_file:
        sld_file.write("# Slide Show Sequence v2\n")
    for file_path in Path(base_path).rglob('.picasa.ini'):
        print(f"Parse Picasa INI file '{file_path}'")
        parser_base_path = str(file_path.parent.absolute()).split(base_path)[1][1:]
        print(f"Picasa INI parser base path is '{parser_base_path}'")
        parser = PicasaIniParser(parser_base_path, file_path)
        parser.parse()
        with open(sld_path, 'a', encoding="utf-8") as sld_file:
            for favorite_file in parser.favorite_files:
                sld_file.write(f"\"{favorite_file}\"\n")

if __name__ == '__main__':
    ini_to_sld(os.path.join('tests', 'data', 'Perso'), "star.sld")
