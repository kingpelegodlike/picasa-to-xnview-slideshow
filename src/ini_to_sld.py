""" Convert a Picasa INI file to a SLD file. """
import os
from pathlib import Path
import logging
import logging.config
from picasa_ini_parser import PicasaIniParser # pylint: disable=import-error
logger = logging.getLogger("ini_to_sld")

def ini_to_sld(base_path, sld_path):
    """Convert a Picasa INI file to a SLD file."""
    with open(sld_path, 'w', encoding="utf-8") as sld_file:
        sld_file.write("# Slide Show Sequence v2\n")
    for file_path in Path(base_path).rglob('.picasa.ini'):
        logger.info("Parse Picasa INI file '%s'", file_path)
        parser_base_path = str(file_path.parent.absolute()).split(base_path)[1][1:]
        logger.debug("Picasa INI parser base path is '%s'", parser_base_path)
        parser = PicasaIniParser(parser_base_path, file_path)
        parser.parse()
        with open(sld_path, 'a', encoding="utf-8") as sld_file:
            for favorite_file in parser.favorite_files:
                sld_file.write(f"\"{favorite_file}\"\n")

if __name__ == '__main__':
    os.makedirs("log", exist_ok=True)
    logging.config.fileConfig('src/ini_to_sld.conf')
    ini_to_sld(os.path.join('tests', 'data', 'Perso'), "star.sld")
