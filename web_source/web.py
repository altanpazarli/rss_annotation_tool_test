from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Web(object):
    __TIMEOUT = 10

    def __init__(self, web_driver):
        super().__init__()
        self._web_driver_wait = WebDriverWait(web_driver, Web.__TIMEOUT)
        self._web_driver = web_driver

    def open(self, url):
        self._web_driver.get(url)

    def current_url(self):
        return self._web_driver.current_url

    def find_by_id(self, _id):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.ID, _id)))

    def find_by_css(self, css):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))

    def find_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))

    def finds_by_xpath(self, xpath):
        return self._web_driver_wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
