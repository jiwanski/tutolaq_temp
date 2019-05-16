from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class ConjugationPage(BasePage):
    """ Page Objects for conjugation page. """

    def __init__(self, driver, tense: str, person: str):
        super().__init__(driver)
        self.tense = tense
        self.person = person
        self.XPATH_VERB_HOVER = "//div[@class='blue-box-wrap'][p/text() = '" + tense + "']/ul/li[" + person + "]"
        self.XPATH_VERB_HOVERED = "//div[@class='blue-box-wrap'][p/text() = '" + tense + "']/ul/li[" + person + "]/a"
        self.ID_LINK_DECLINATION_PAGE = "replaceLinkOnHover"

    def hover_verb(self):
        """ Hovers over element (with scroll). """
        el = self._driver.find_element_by_xpath(self.XPATH_VERB_HOVER)
        self._driver.execute_script("return arguments[0].scrollIntoView(false);", el)
        el_hover = ActionChains(self._driver).move_to_element(el)
        el_hover.perform()

    def click_hovered(self):
        """ Clicks link which appears after hover. """
        wait = WebDriverWait(self._driver, 3)
        wait.until(ec.visibility_of_element_located((By.ID, self.ID_LINK_DECLINATION_PAGE)))
        el = self._driver.find_element_by_id(self.ID_LINK_DECLINATION_PAGE)
        el.click()  # NOTE: this opens new tab and switches to it while driver is focused on old tab

    def switch_tab(self):
        """ Performs tab switch. """
        self._driver.switch_to.window(self._driver.window_handles[-1])
