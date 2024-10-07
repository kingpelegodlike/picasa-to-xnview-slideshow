"""Module providing a unit testing of picasa_ini_parser module"""

import os
from src.ini_to_sld import ini_to_sld

def test_ini_to_sld_all_contacts():
    """Test the __init__ method."""
    output_file_name = "output/test_ini_to_sld_all_contacts.sld"
    base_path = os.path.join('tests', 'data', 'Perso') + os.sep
    ini_to_sld(base_path, output_file_name)


def test_ini_to_sld_with_and_rule_and_no_contacts():
    """ Test the ini_to_sld method
        with 'and' rule and no contacts.
    """
    output_file_name = "output/test_ini_to_sld_with_and_rule_and_no_contacts.sld"
    base_path = os.path.join('tests', 'data', 'Perso') + os.sep
    ini_to_sld(base_path, output_file_name, ["Unknown Contact"], "and")


def test_ini_to_sld_with_and_rule_and_one_contact():
    """ Test the ini_to_sld method
        with 'and' rule and one contact.
    """
    output_file_name = "output/test_ini_to_sld_with_and_rule_and_one_contact.sld"
    base_path = os.path.join('tests', 'data', 'Perso') + os.sep
    ini_to_sld(base_path, output_file_name, ["Xavier DUVAL"], "and")


def test_ini_to_sld_with_and_rule_and_many_contacts():
    """ Test the ini_to_sld method
        with 'and' rule and one contact.
    """
    output_file_name = "output/test_ini_to_sld_with_and_rule_and_many_contacts.sld"
    base_path = os.path.join('tests', 'data', 'Perso') + os.sep
    ini_to_sld(base_path, output_file_name, ["Xavier DUVAL", "Varunah DUVAL"], "and")


def test_ini_to_sld_with_or_rule_and_no_contacts():
    """ Test the ini_to_sld method
        with 'or' rule and no contacts.
    """
    output_file_name = "output/test_ini_to_sld_with_or_rule_and_no_contacts.sld"
    base_path = os.path.join('tests', 'data', 'Perso') + os.sep
    ini_to_sld(base_path, output_file_name, ["Unknown Contact"], "or")


def test_ini_to_sld_with_or_rule_and_one_contact():
    """ Test the ini_to_sld method
        with 'or' rule and one contact.
    """
    output_file_name = "output/test_ini_to_sld_with_or_rule_and_one_contact.sld"
    base_path = os.path.join('tests', 'data', 'Perso') + os.sep
    ini_to_sld(base_path, output_file_name, ["Xavier DUVAL"], "or")


def test_ini_to_sld_with_or_rule_and_many_contacts():
    """ Test the ini_to_sld method
        with 'or' rule and one contact.
    """
    output_file_name = "output/test_ini_to_sld_with_or_rule_and_many_contacts.sld"
    base_path = os.path.join('tests', 'data', 'Perso') + os.sep
    ini_to_sld(base_path, output_file_name, ["Xavier DUVAL", "Varunah DUVAL"], "or")
