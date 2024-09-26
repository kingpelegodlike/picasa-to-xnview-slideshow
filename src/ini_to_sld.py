""" Convert a Picasa INI file to a SLD file. """
import os
from pathlib import Path
import argparse
import logging
import logging.config
from picasa_ini_parser import PicasaIniParser # pylint: disable=import-error
logger = logging.getLogger("ini_to_sld")

def ini_to_sld(base_path, sld_path, contact_list=None, rule=None):
    """Convert a Picasa INI file to a SLD file."""
    with open(sld_path, 'w', encoding="utf-8") as sld_file:
        sld_file.write("# Slide Show Sequence v2\n")
    if contact_list and rule:
        contact_files = {}
        for file_path in Path(base_path).rglob('.picasa.ini'):
            logger.info("Parse Picasa INI file '%s'", file_path)
            parser_base_path = str(file_path.parent.absolute()).split(base_path)[1]
            logger.debug("Picasa INI parser base path is '%s'", parser_base_path)
            ini_parser = PicasaIniParser(parser_base_path, file_path)
            ini_parser.parse()
            for contact_name, file_list in ini_parser.contact_files.items():
                if contact_name not in contact_files:
                    contact_files[contact_name] = file_list
                else:
                    for file_name in file_list:
                        contact_files[contact_name].append(file_name)
        contact_file_list = []
        logger.debug("Check contact list with contact retrieved from INI files")
        tmp_contact_list = contact_list.copy()
        for contact_name in tmp_contact_list:
            if contact_name not in contact_files:
                logger.warning("Contact '%s' not found in INI files", contact_name)
                contact_list.remove(contact_name)
        if rule == 'and':
            if len(contact_list) == 0:
                logger.warning("No contacts found in INI files")
            elif len(contact_list) == 1:
                for file_name in contact_files[contact_list[0]]:
                    contact_file_list.append(file_name)
            else:
                logger.debug("Get files for first contact '%s'", contact_list[0])
                for file_name in contact_files[contact_list[0]]:
                    contact_file_list.append(file_name)
                for other_contact_name in contact_list[1:]:
                    logger.debug("Check files with other contact '%s'", other_contact_name)
                    tmp_contact_file_list = contact_file_list.copy()
                    for tmp_contact_file in tmp_contact_file_list:
                        if tmp_contact_file not in contact_files[other_contact_name]:
                            contact_file_list.remove(tmp_contact_file)
        else:
            if len(contact_list) == 0:
                logger.warning("No contacts found in INI files")
            elif len(contact_list) == 1:
                for file_name in contact_files[contact_list[0]]:
                    contact_file_list.append(file_name)
            else:
                for contact_name in contact_list:
                    for file_name in contact_files[contact_name]:
                        if file_name not in contact_file_list:
                            contact_file_list.append(file_name)
        with open(sld_path, 'a', encoding="utf-8") as sld_file:
            for file_name in contact_file_list:
                sld_file.write(f"\"{file_name}\"\n")
    else:
        for file_path in Path(base_path).rglob('.picasa.ini'):
            logger.info("Parse Picasa INI file '%s'", file_path)
            parser_base_path = str(file_path.parent.absolute()).split(base_path)[1]
            logger.debug("Picasa INI parser base path is '%s'", parser_base_path)
            ini_parser = PicasaIniParser(parser_base_path, file_path)
            ini_parser.parse()
            with open(sld_path, 'a', encoding="utf-8") as sld_file:
                for favorite_file in ini_parser.favorite_files:
                    sld_file.write(f"\"{favorite_file}\"\n")

if __name__ == '__main__': # pragma: no cover
    os.makedirs("log", exist_ok=True)
    logging.config.fileConfig('src/ini_to_sld.conf')
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--folder-path", help="Folder path")
    parser.add_argument("-r", "--rule", choices=['and', 'or'], help="rule to apply")
    parser.add_argument("-c", "--contacts", help="contact list")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="increase output verbosity")
    args = parser.parse_args()
    if args.verbose:
        for handler in logger.handlers[:]:
            handler.setLevel(logging.DEBUG)
    if args.rule:
        if not args.contacts:
            parser.error("rule requires --contacts")
    contacts = None
    if args.contacts:
        if not args.rule:
            parser.error("rule requires --rule")
        contacts = args.contacts.split(',')
    # ini_to_sld(os.path.join('tests', 'data', 'Perso'), "star.sld")
    if os.path.isabs(args.folder_path):
        logger.debug("Absolute Folder path")
        absolute_folder_path = args.folder_path
    else:
        logger.debug("Relative Folder path")
        absolute_folder_path = os.path.join(os.getcwd(), args.folder_path.replace(f".{os.sep}", ""))
    logger.info("Folder path is '%s'", absolute_folder_path)
    ini_to_sld(absolute_folder_path, "star.sld", contacts, args.rule)
