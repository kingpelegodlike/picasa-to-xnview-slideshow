"""Module providing a unit testing of picasa_ini_parser module"""

import os
from src.ini_to_sld import ini_to_sld

def test_ini_to_sld():
    """Test the __init__ method."""
    ini_to_sld(os.path.join('tests', 'data', 'Perso'), "star.sld")
