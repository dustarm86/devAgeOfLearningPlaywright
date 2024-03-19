from configparser import ConfigParser
from playwright.sync_api import Page, expect

config = ConfigParser()
config.read(r'/Users/dieter/python/devAgeOfLearningAutomation/config.ini')
base_url = config.get("abcmouse","url")
email = config.get("abcmouse", "email")

# creates the class HomePage to build methods for the actual test within test_home_page.py file
class HomePage:
    def __init__(self, page: Page):
        self.page = page

    # method from HomePage class to go to abcmouse.com
    def go_to_home_page(self):
        self.page.goto(base_url)

    # method from HomePage class to go abcmouse.com, then click the "sign up" button
    def click_sign_up_button(self):
        self.page.get_by_label("Sign Up for ABCmouse.com").click()

    # method from HomePage class that checks for the "Become a Member" text
    def verify_become_member_text(self):
        expect(self.page.get_by_role("heading", name="Become a Member!")).to_be_visible()

    # method from HomePage class to verify registration page URL is correct
    def verify_registration_page(self):
        expect(self.page).to_have_url(url_or_reg_exp="https://www.abcmouse.com/abc/prospect-register/")

    # method from HomePage class to enter the email address within the config.ini file then click the "Submit" button
    def enter_email_and_submit(self):
        self.page.get_by_placeholder("Email Address").type(email, delay=200)
        self.page.get_by_role("button", name="Submit", exact=True).click()

    # method from HomePage class to verify subscription page URL is correct
    def verify_subscription_page(self):
        expect(self.page).to_have_url(url_or_reg_exp="https://www.abcmouse.com/abc/subscription/")
