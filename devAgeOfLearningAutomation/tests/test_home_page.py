from pages.home_page import HomePage

def test_home_page_sign_up(page):
    home_page = HomePage(page)
    home_page.go_to_home_page()
    home_page.click_sign_up_button()
    home_page.verify_become_member_text()
    home_page.verify_registration_page()
    home_page.enter_email_and_submit()
    home_page.verify_subscription_page()
