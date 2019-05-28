from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class TopNav(SeleniumDriver):

    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# locators
    _about_us = 'Image3'
    _direct_sales = 'Image4'
    _rental_services = 'Image5'
    _products = 'Image6'
    _contact_us = 'Image7'

    def navigateAboutUs(self):
        self.elementClick(self._about_us, locatorType='id')

    def navigateDirectSales(self):
        self.elementClick(self._direct_sales, locatorType='id')

    def navigateRentalServices(self):
        self.elementClick(self._rental_services, locatorType='id')

    def navigateProducts(self):
        self.elementClick(self._products, locatorType='id')

    def navigateContactUs(self):
            self.elementClick(self._contact_us, locatorType='id')

    def verifyAboutUs(self):
        

