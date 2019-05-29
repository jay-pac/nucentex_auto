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
        result1 = self.lp.verifyLoginTitle()
        self.ts.mark(result1, 'Verify Title for About Us Page')

        self.tn.navigateDirectSales()
        result2 = self.lp.verifyLoginTitle()
        self.ts.mark(result2, 'Verify Title for Direct Sales page')

        self.tn.navigateProducts()
        result3 = self.lp.verifyLoginTitle()
        self.ts.mark(result3, 'Verify Title for Products page')

        self.tn.navigateContactUs()
        result4 = self.lp.verifyLoginTitle()
        self.ts.mark(result4, 'Verify Title Contact Us page')

        self.tn.navigateRentalServices()
        result5 = self.lp.verifyLoginTitle()
        self.ts.mark(result5, 'Verify Title Rental Services')

