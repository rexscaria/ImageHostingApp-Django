# -*- coding: utf-8 -*-
from django.conf import settings
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from django.test import LiveServerTestCase


class UserSignout(LiveServerTestCase):
    fixtures = ['testdata.json']

    def setUp(self):
        self.driver = settings.WEB_DRIVER
        self.driver.implicitly_wait(30)
        self.base_url = self.live_server_url
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_user_signout(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("abc@abc.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("123123")
        driver.find_element_by_xpath("//input[@value='Login now']").click()
        self.assertRegexpMatches(driver.current_url, r"^[\s\S]*/home$")
        driver.find_element_by_link_text("Logout").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.alert-success"))
        self.assertRegexpMatches(driver.find_element_by_css_selector("div.alert-success").text, r"^[\s\S]*See you later\. Login anytime you wish$")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

