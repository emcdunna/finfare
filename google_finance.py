from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoAlertPresentException
from enum import Enum
import time


# Class to interact with the web application for finance info
class GoogleFinance:
    def __init__(self):
        # Initialize WebDriver and URLs
        self.driver = webdriver.Chrome()
        self.title = "Google Finance - Stock Market Prices, Real-time Quotes & Business News"
        self.url = "https://www.google.com/finance"
        self.you_may_be_interested_xpath = "//div[@id='smart-watchlist-title']"

    def setup(self) -> None:
        # Load the web application
        self.driver.get(self.url)

        # Wait for the page to load
        wait = WebDriverWait(self.driver, 10)

    def get_you_may_be_interested_in_stock_names(self) -> list[str]:
        names = []

        # find the "you may be interested in" section element
        parent_element = self.driver.find_element(By.XPATH, self.you_may_be_interested_xpath).parent

        # find all li elements as children to the parent element
        list_elements = parent_element.find_elements(By.TAG_NAME, 'li')

        # remove the "market trends" elements from this list
        list_elements = list_elements[0:6]

        for li in list_elements:
            # add the stock title name from the child elements
            names.append(li.text.split("\n")[0])
        return names

    def teardown(self) -> None:
        # Close the browser
        self.driver.quit()