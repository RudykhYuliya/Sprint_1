from selenium.webdriver.common.by import By


class RegistrationPageMesto:
    email_field = [By.ID, 'email']
    password_field = [By.ID, 'password']
    registration_button = [By.CLASS_NAME, 'auth-form__button']

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_registration_button(self):
        self.driver.find_element(*self.registration_button).click()

    def register(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_registration_button()
