import pytest
from .context import ConjugationPage
from .context import TranslationPage
from .context import dumpers
from .context import test_data


class TestConjugation:
    """ Test class for verb conjugation. """

    @pytest.mark.usefixtures("chrome_headless")
    @pytest.mark.parametrize("verb", test_data.verbs)
    def test_verbs(self, verb):
        url = "http://conjugator.reverso.net/conjugation-portuguese-verb-" + verb + ".html"
        self.driver.get(url)

        conjugation_page = ConjugationPage(self.driver, tense=test_data.default_tense, person=test_data.default_person)
        conjugation_page.hover_verb()
        conjugation_page.click_hovered()
        conjugation_page.switch_tab()

        translation_page = TranslationPage(self.driver)
        translation_page.close_register()
        els = translation_page.find_examples(3)
        examples = translation_page.store_examples(els)

        dumpers.dump_conjugation(examples, verb, test_data.default_tense, test_data.default_person)

        assert len(examples["examples"]) >= 1
