from selenium.webdriver.common.by import By


class HomePageMesto:
    # кликнуть на кнопку добавить
    add_new_place_button = [By.CLASS_NAME, 'profile__add-button']
    # ввести название
    name_field = [By.NAME, 'name']
    # ввести ссылку на изображение
    link_to_picture_field = [By.NAME, 'link']
    # кликнуть на кнопку Сохранить
    save_button = [By.XPATH, ".//form[@name='new-card']/button[text()='Сохранить']"]

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_place_button(self):
        self.driver.find_element(*self.add_new_place_button).click()

    def set_name(self):
        new_title = "Новое место"
        self.driver.find_element(*self.name_field).send_keys(new_title)

    def set_link_to_picture_field(self):
        self.driver.find_element(*self.link_to_picture_field).send_keys("Ссылка на новое изображение")

    def click_save_button(self):
        self.driver.find_element(*self.save_button).click()

    def add_new_place(self):
        self.click_add_new_place_button()
        self.set_name()
        self.set_link_to_picture_field()
        self.click_save_button()
