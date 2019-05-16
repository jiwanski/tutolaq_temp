import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def chrome_headless(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument("--proxy-server='direct://'")
    options.add_argument('--proxy-bypass-list=*')
    driver = webdriver.Chrome(options=options, service_log_path='/dev/null')
    driver.set_window_size(1500, 1200)
    request.cls.driver = driver
    yield driver
    driver.quit()
