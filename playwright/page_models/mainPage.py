from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from final_project.playwright.page_models.basicPage import BasicPage


class MainPage(BasicPage):
    def __init__(self, driver: webdriver):
        super().__init__(driver)

    locator_dictionary = {

    }


