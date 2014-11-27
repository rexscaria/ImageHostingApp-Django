# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from django.test import LiveServerTestCase
from django.conf import settings

class UserRegistrationSuccess(LiveServerTestCase):
    fixtures = ['testdata.json']

    def setUp(self):
        self.driver = settings.WEBDRIVER
        self.driver.implicitly_wait(30)
        self.base_url = self.live_server_url
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_user_registration_success(self):
        driver = self.driver
        driver.get(self.base_url + "/register")
        driver.find_element_by_css_selector("div.span3.offset1 > form > fieldset > #id_email").clear()
        driver.find_element_by_css_selector("div.span3.offset1 > form > fieldset > #id_email").send_keys("new@email.com")
        driver.find_element_by_id("id_first_name").clear()
        driver.find_element_by_id("id_first_name").send_keys("New")
        driver.find_element_by_id("id_second_name").clear()
        driver.find_element_by_id("id_second_name").send_keys("User")
        driver.find_element_by_css_selector("div.span3.offset1 > form > fieldset > #id_password").clear()
        driver.find_element_by_css_selector("div.span3.offset1 > form > fieldset > #id_password").send_keys("password")
        driver.find_element_by_xpath("//input[@value='Register now']").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.alert-success"))
        self.assertRegexpMatches(driver.find_element_by_css_selector("div.alert-success").text, r"Registration success")


    def test_user_registration_fails_when_email_already_exists(self):
        driver = self.driver
        driver.get(self.base_url + "/register")
        driver.find_element_by_css_selector("div.span3.offset1 > form > fieldset > #id_email").clear()
        driver.find_element_by_css_selector("div.span3.offset1 > form > fieldset > #id_email").send_keys("abc@abc.com")
        driver.find_element_by_id("id_first_name").clear()
        driver.find_element_by_id("id_first_name").send_keys("John")
        driver.find_element_by_id("id_second_name").clear()
        driver.find_element_by_id("id_second_name").send_keys("Lennon")
        driver.find_element_by_css_selector("div.span3.offset1 > form > fieldset > #id_password").clear()
        driver.find_element_by_css_selector("div.span3.offset1 > form > fieldset > #id_password").send_keys("password")
        driver.find_element_by_xpath("//input[@value='Register now']").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "ul.errorlist > li"))
        self.assertEqual("User with this Email already exists.", driver.find_element_by_css_selector("ul.errorlist > li").text)
        self.assertRegexpMatches(driver.current_url, r"^[\s\S]*/register$")

    def test_user_register_fails_with_empty_fields(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_xpath("//input[@value='Register now']").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "ul.errorlist > li"))
        self.assertEqual("This field is required.", driver.find_element_by_css_selector("ul.errorlist > li").text)
        self.assertRegexpMatches(driver.current_url, r"^[\s\S]*/register$")

    def test_user_register_with_invalid_email(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_css_selector("div.span3.offset1 > form > fieldset > #id_email").clear()
        driver.find_element_by_css_selector("div.span3.offset1 > form > fieldset > #id_email").send_keys("ivalidemail")
        driver.find_element_by_id("id_first_name").clear()
        driver.find_element_by_id("id_first_name").send_keys("First")
        driver.find_element_by_id("id_second_name").clear()
        driver.find_element_by_id("id_second_name").send_keys("Second")
        driver.find_element_by_css_selector("div.span3.offset1 > form > fieldset > #id_password").clear()
        driver.find_element_by_css_selector("div.span3.offset1 > form > fieldset > #id_password").send_keys("password")
        driver.find_element_by_xpath("//input[@value='Register now']").click()
        self.assertRegexpMatches(driver.current_url, r"^[\s\S]*/login$")


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
