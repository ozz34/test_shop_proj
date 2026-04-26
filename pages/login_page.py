from .base_page import BasePage
from .locators import LoginPageLocators
import faker

class LoginPage(BasePage):
    def create_user(self):
        f = faker.Faker()
        email = f.email()
        password = f.password()
        return (email, password)

    def register_new_user(self, email, password):
        register_email_field = self.is_element_visible(*LoginPageLocators.REGISTRATION_EMAIL)
        register_email_field.send_keys(email)
        register_password_field1 = self.is_element_visible(*LoginPageLocators.REGISTRATION_PASSWORD1)
        register_password_field1.send_keys(password)
        register_password_field2 = self.is_element_visible(*LoginPageLocators.REGISTRATION_PASSWORD2)
        register_password_field2.send_keys(password)
        registration_button = self.is_element_clickable(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()