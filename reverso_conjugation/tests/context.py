import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.conjugation_page import ConjugationPage
from pages.translation_page import TranslationPage
import fixtures.fixtures as fixtures
import helpers.dump as dumpers
from input import test_data
