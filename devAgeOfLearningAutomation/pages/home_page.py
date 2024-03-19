from configparser import ConfigParser
from playwright.sync_api import Page, expect

config = ConfigParser()
config.read(r'/Users/dieter/python/devAgeOfLearningAutomation/config.ini')
base_url = config.get("abcmouse","url")
email = config.get("abcmouse", "email")

class HomePage:
    def __init__(self, page: Page):
        self.page = page

    # go to abcmouse.com
    def go_to_home_page(self):
        self.page.goto(base_url)

    # on abcmouse.com, click the "sign up" button
    def click_sign_up_button(self):
        self.page.get_by_label("Sign Up for ABCmouse.com").click()

    def verify_become_member_text(self):
        expect(self.page.get_by_role("heading", name="Become a Member!")).to_be_visible()

    def verify_registration_page(self):
        expect(self.page).to_have_url(url_or_reg_exp="https://www.abcmouse.com/abc/prospect-register/")

    def enter_email_and_submit(self):
        self.page.get_by_placeholder("Email Address").type(email, delay=200)
        self.page.get_by_role("button", name="Submit", exact=True).click()

    def verify_subscription_page(self):
        expect(self.page).to_have_url(url_or_reg_exp="https://www.abcmouse.com/abc/subscription/")
