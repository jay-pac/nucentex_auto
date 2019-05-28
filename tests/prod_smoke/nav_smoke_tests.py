from utilities.teststatus import Status
from pages.navigation.top_nav import TopNav
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class NavSmokeTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.tn = TopNav(self.driver)
        self.ts = Status(self.driver)

    @pytest.mark.run(order=1)
    def nav_tests(self):
        self.tn.navigateAboutUs()
        self.tn.navigateDirectSales()
        self.tn.navigateProducts()
        self.tn.navigateContactUs()
        self.tn.navigateRentalServices()

