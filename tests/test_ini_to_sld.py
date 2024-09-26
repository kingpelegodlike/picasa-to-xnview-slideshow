"""Module providing a unit testing of picasa_ini_parser module"""

import os
from src.ini_to_sld import ini_to_sld

def test_ini_to_sld():
    """Test the __init__ method."""
    ini_to_sld(os.path.join('tests', 'data', 'Perso'), "star.sld")


def test_ini_to_sld_with_and_rule_and_no_contacts():
    """ Test the ini_to_sld method
        with 'and' rule and no contacts.
    """
    ini_to_sld(os.path.join('tests', 'data', 'Perso'), "star.sld", ["Unknown Contact"], "and")


def test_ini_to_sld_with_and_rule_and_one_contact():
    """ Test the ini_to_sld method
        with 'and' rule and one contact.
    """
    ini_to_sld(os.path.join('tests', 'data', 'Perso'), "star.sld", ["Xavier DUVAL"], "and")


def test_ini_to_sld_with_and_rule_and_many_contacts():
    """ Test the ini_to_sld method
        with 'and' rule and one contact.
    """
    ini_to_sld(os.path.join('tests', 'data', 'Perso'), "star.sld", ["Xavier DUVAL", "Varunah DUVAL"], "and")


def test_ini_to_sld_with_or_rule_and_no_contacts():
    """ Test the ini_to_sld method
        with 'or' rule and no contacts.
    """
    ini_to_sld(os.path.join('tests', 'data', 'Perso'), "star.sld", ["Unknown Contact"], "or")


def test_ini_to_sld_with_or_rule_and_one_contact():
    """ Test the ini_to_sld method
        with 'or' rule and one contact.
    """
    ini_to_sld(os.path.join('tests', 'data', 'Perso'), "star.sld", ["Xavier DUVAL"], "or")


def test_ini_to_sld_with_or_rule_and_many_contacts():
    """ Test the ini_to_sld method
        with 'or' rule and one contact.
    """
    ini_to_sld(os.path.join('tests', 'data', 'Perso'), "star.sld", ["Xavier DUVAL", "Varunah DUVAL"], "or")
