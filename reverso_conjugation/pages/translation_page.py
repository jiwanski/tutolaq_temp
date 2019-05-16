from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base_page import BasePage


class TranslationPage(BasePage):
    """ Page Objects for translation page. """

    def __init__(self, driver):
        super().__init__(driver)
        self.examples = {"examples": []}
        self.XPATH_EXAMPLES = "//section[@id='examples-content']/div[@class='example']"
        self.XPATH_PT = ".//div[1]/span[@class='text']"
        self.XPATH_EN = ".//div[2]/span[@class='text']"
        self.XPATH_CONTEXT = "//section[@id='examples-content']/div[1]//button[@title='']"
        self.XPATH_CONTEXT_BUTTON = "./descendant::button[contains(@class,'more-context')]"
        self.XPATH_CLOSE_BUTTON = "//button[@class='close']"
        self.XPATH_CLOSE_BUTTON_REGISTER = "//button[@class='icon cancel']"
        self.XPATH_CONTEXT_CONTENT = "//div[@class='popup context ui-draggable']//div[@class='body wide-container']/div"
        self.XPATH_CONTEXT_POPUP = "//div[@id='popups-container']"

    def find_examples(self, wait: int):
        """ Locates and returns Web Elements with Example Sentences. """
        wait = WebDriverWait(self._driver, wait)
        wait.until(ec.visibility_of_element_located((By.XPATH, self.XPATH_EXAMPLES)))
        els = self._driver.find_elements_by_xpath(self.XPATH_EXAMPLES)
        return els

    def hover_element(self, el):
        """ Generic hover function. """
        el_hover = ActionChains(self._driver).move_to_element(el)
        el_hover.perform()

    def click_context_button(self, el):
        """ Locates, hovers upon and clicks button to invoke Context Popup. """
        wait = WebDriverWait(self._driver, 3)
        wait.until(ec.visibility_of_element_located((By.XPATH, self.XPATH_EXAMPLES)))
        el_context_button = el.find_element_by_xpath(self.XPATH_CONTEXT_BUTTON)
        self.hover_element(el_context_button)
        el_context_button.click()

    def append_context(self, els, count):
        """ Adds Context (up to 5 sentences) to main example. """
        for el_context in els:
            context_pt = el_context.find_element_by_xpath("./span[1]").text
            context_en = el_context.find_element_by_xpath("./span[2]").text
            # JSON: append context to example
            self.examples["examples"][count]["context"].append({"context_pt": context_pt, "context_en": context_en})

    def store_examples(self, els) -> dict:
        """ Creates nested JSON structure for all translations with Context. """
        for count, el in enumerate(els):
            text_pt = el.find_element_by_xpath(self.XPATH_PT).text
            text_en = el.find_element_by_xpath(self.XPATH_EN).text
            # JSON: append example
            self.examples["examples"].append({"pt": text_pt, "en": text_en, "context": []})
            self.hover_element(el)
            el_context_button = el.find_element_by_xpath(self.XPATH_CONTEXT_BUTTON)
            try:
                el_context_button.click()
            except Exception:
                pass
            els_context = self.find_context(5)
            # JSON: append context to example
            self.append_context(els_context, count)
            ActionChains(self._driver).send_keys(Keys.ESCAPE).perform()
            wait = WebDriverWait(self._driver, 5)
            wait.until_not(ec.visibility_of_element_located((By.XPATH, self.XPATH_CONTEXT_POPUP)))
            self._driver.execute_script("return arguments[0].scrollIntoView(false);", el)
            self._driver.execute_script("window.scrollBy(0, 200);")
        return self.examples

    def close_register(self):
        """ Close register popup. """
        el_close_button = self._driver.find_element_by_xpath(self.XPATH_CLOSE_BUTTON_REGISTER)
        el_close_button.click()

    def close_popup(self):
        """ Close popup. """
        el_close_button = self._driver.find_element_by_xpath(self.XPATH_CLOSE_BUTTON)
        el_close_button.click()
        self._driver.implicitly_wait(1)

    def find_context(self, wait: int):
        """ Locates HTML containers with Context translation. """
        wait = WebDriverWait(self._driver, wait)
        try:
            wait.until(ec.visibility_of_element_located((By.XPATH, self.XPATH_CONTEXT_CONTENT)))
        except Exception:
            pass
        els = self._driver.find_elements_by_xpath(self.XPATH_CONTEXT_CONTENT)
        return els
