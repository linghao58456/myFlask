from webAuto.public.base import Base


class Login(Base):
    def __init__(self, browser):
        self.driver = self.open_browser(browser)

    def login_username(self, username, password):
        self.send_key_value("id", "login_form_username", username)
        self.send_key_value("id", "login_form_password", password)
        self.click_btn("id", "")
        return
