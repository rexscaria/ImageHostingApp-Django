# -*- coding: utf-8 -*-
from django.conf import settings
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from django.test import LiveServerTestCase

class UserLoginWithWrongEmail(LiveServerTestCase):
    fixtures = ['testdata.json']


    def setUp(self):
        self.driver = settings.WEB_DRIVER
        self.driver.implicitly_wait(30)
        self.base_url = self.live_server_url
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_user_login_with_invalid_email_address(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("abc@3")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("1235645")
        driver.find_element_by_xpath("//input[@value='Login now']").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "ul.errorlist > li"))
        self.assertRegexpMatches(driver.current_url, r"^[\s\S]*/login$")
        self.assertEqual("Enter a valid email address.", driver.find_element_by_css_selector("ul.errorlist > li").text)

    def test_user_login_with_invalid_password_and_email_address(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_xpath("//input[@value='Login now']").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "ul.errorlist > li"))
        self.assertRegexpMatches(driver.current_url, r"^[\s\S]*/login$")
        self.assertEqual("This field is required.", driver.find_element_by_css_selector("ul.errorlist > li").text)

    def test_user_login_error_with_non_existing_email(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("nonexistant@email.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("password")
        driver.find_element_by_xpath("//input[@value='Login now']").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "ul.errorlist > li"))
        self.assertEqual("Login Error!", driver.find_element_by_css_selector("ul.errorlist > li").text)
        self.assertRegexpMatches(driver.current_url, r"^[\s\S]*/login$")

    def test_user_login_error_by_wrong_password(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("abc@abc.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("wrongpassword")
        driver.find_element_by_xpath("//input[@value='Login now']").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "ul.errorlist > li"))
        self.assertEqual("Login Error!", driver.find_element_by_css_selector("ul.errorlist > li").text)
        self.assertRegexpMatches(driver.current_url, r"^[\s\S]*/login$")

    def test_user_login_success(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("abc@abc.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("123123")
        driver.find_element_by_xpath("//input[@value='Login now']").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.container.home"))
        self.assertRegexpMatches(driver.current_url, r"^[\s\S]*/home$")

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
