# -*- coding: utf-8 -*-
import os
from django.conf import settings
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from django.test import LiveServerTestCase

class FailedImageUploadDueToCorruptFile(LiveServerTestCase):
    fixtures = ['testdata.json']

    def setUp(self):
        self.driver = settings.WEB_DRIVER()
        self.driver.implicitly_wait(30)
        self.base_url = self.live_server_url
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_failed_image_upload_due_to_corrupt_file(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("abc@abc.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("123123")
        driver.find_element_by_xpath("//input[@value='Login now']").click()
        driver.find_element_by_link_text("Upload Photo").click()
        driver.find_element_by_id("id_image").send_keys(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_images','corrupt_image.png'))
        driver.find_element_by_css_selector("input.pull-right").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "ul.errorlist > li"))
        self.assertEqual("Upload a valid image. The file you uploaded was either not an image or a corrupted image.", driver.find_element_by_css_selector("ul.errorlist > li").text)


    def test_failed_image_upload_due_to_non_existing_file(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("abc@abc.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("123123")
        driver.find_element_by_xpath("//input[@value='Login now']").click()
        driver.find_element_by_link_text("Upload Photo").click()
        driver.find_element_by_id("id_image").send_keys(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_images','corrupt_image.png'))
        driver.find_element_by_css_selector("input.pull-right").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "ul.errorlist > li"))
        self.assertEqual("Upload a valid image. The file you uploaded was either not an image or a corrupted image.", driver.find_element_by_css_selector("ul.errorlist > li").text)

    def test_successful_image_upload(self):
        driver = self.driver
        driver.get(self.base_url + "/login")
        driver.find_element_by_id("id_email").clear()
        driver.find_element_by_id("id_email").send_keys("abc@abc.com")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("123123")
        driver.find_element_by_xpath("//input[@value='Login now']").click()
        driver.find_element_by_link_text("Upload").click()
        driver.find_element_by_id("id_image").send_keys(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_images','1.png'))
        driver.find_element_by_css_selector("input.pull-right").click()
        self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "div.alert-success"))
        driver.find_element_by_link_text("Home").click()
        self.assertRegexpMatches( driver.find_element_by_id("image0").get_attribute("src"), "/media/1.*\.png")
        self.assertTrue(self.is_element_present(By.ID, "image0"))

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
