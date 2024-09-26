"""Module providing a unit testing of picasa_ini_parser module"""

import os
from src.picasa_ini_parser import PicasaIniParser

def test_init():
    """Test the __init__ method."""
    parser = PicasaIniParser('basepath', 'filepath')
    assert parser.basepath == 'basepath'
    assert parser.filepath == 'filepath'
    assert not parser.favorite_files
    assert not parser.contact_files

def test_parse():
    """Test the __init__ method."""
    base_path = f"2001{os.sep}20010601-20010603.Mariage.Varunah.et.Xavier"
    dir_path = \
        f"tests{os.sep}data{os.sep}Perso{os.sep}2001{os.sep}" \
        f"20010601-20010603.Mariage.Varunah.et.Xavier"
    parser = PicasaIniParser(base_path, f"{dir_path}{os.sep}.picasa.ini")
    parser.parse()
    assert parser.basepath == base_path
    assert parser.filepath == f"{dir_path}{os.sep}.picasa.ini"
    assert len(parser.favorite_files) == 26, \
        f"Number of favorite files is '{len(parser.favorite_files)}' instead of 26"
    assert parser.favorite_files == [
        f"{base_path}{os.sep}20010601_210000.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_110000.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_120000.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_120020.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_121000.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_121100.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_122000.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_122400.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_123000.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_124000.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_130000.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_130110.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_130220.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_130330.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_130440.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_190000.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_200000.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_201000.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_201200.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_202000.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_231000.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_231200.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_231300.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_231400.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_232000.Mariage.Varunah.et.Xavier.JPG",
        f"{base_path}{os.sep}20010602_232100.Mariage.Varunah.et.Xavier.JPG" ]
    assert parser.contact_files == {
        "Varunah DUVAL" : [
            f"{base_path}{os.sep}20010602_110000.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_120000.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_121000.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_121100.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_122000.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_123000.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_130220.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_130330.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_130440.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_201000.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_202000.Mariage.Varunah.et.Xavier.JPG"
        ],
        "Xavier DUVAL" : [
            f"{base_path}{os.sep}20010602_120000.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_121000.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_121100.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_122400.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_123000.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_130220.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_201000.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_202000.Mariage.Varunah.et.Xavier.JPG",
            f"{base_path}{os.sep}20010602_231400.Mariage.Varunah.et.Xavier.JPG"
        ],
        "Oormila BULLY" : [
            f"{base_path}{os.sep}20010602_190000.Mariage.Varunah.et.Xavier.JPG"
        ],
        "Mezhoura BOYJONAUTH" : [
            f"{base_path}{os.sep}20010602_231300.Mariage.Varunah.et.Xavier.JPG"
        ]
    }
