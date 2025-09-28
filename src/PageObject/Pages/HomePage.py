from selenium.webdriver.common.by import By
import time

url_base = "https://testautomationpractice.blogspot.com/"

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wikipedia_search = "//*[@class = 'wikipedia-search-input']"
        self.name = "name"
        self.email = "email"
        self.phone = "phone"
        self.address = "textarea"
        self.gender_male = "male"
        self.gender_female = "female"
        self.sunday = "sunday"
        self.monday = "monday"
        self.tuesday = "tuesday"
        self.wednesday = "wednesday"
        self.thursday = "thursday"
        self.friday = "friday"
        self.saturday = "saturday"
        self.country = "country"
        self.date_picker = "datepicker"
        self.field1 = "field1"
        self.field2 = "field2"
        self.submit = "//*[(@class='submit-btn') and text() = 'Submit']"

    def get_wikipedia(self):
        return self.driver.find_elements(By.XPATH, self.wikipedia_search)

    def get_name(self):
        return self.driver.find_element(By.ID, self.name)
    
    def get_email(self):
        return self.driver.find_element(By.ID, self.email)

    def get_phone(self):
        return self.driver.find_element(By.ID, self.phone)
    
    def get_address(self):
        return self.driver.find_element(By.ID, self.address)

    def get_gender_male(self):
        return self.driver.find_element(By.ID, self.gender_male)

    def get_gender_female(self):
        return self.driver.find_element(By.ID, self.gender_female)

    def get_sunday(self):
        return self.driver.find_element(By.ID, self.sunday)

    def get_monday(self):
        return self.driver.find_element(By.ID, self.monday)

    def get_tuesday(self):
        return self.driver.find_element(By.ID, self.tuesday)

    def get_wednesday(self):
        return self.driver.find_element(By.ID, self.wednesday)

    def get_thursday(self):    
        return self.driver.find_element(By.ID, self.thursday)

    def get_friday(self):
        return self.driver.find_element(By.ID, self.friday)

    def get_saturday(self): 
        return self.driver.find_element(By.ID, self.saturday)

    def get_country(self):
        return self.driver.find_element(By.ID, self.country)

    def get_date_picker(self):
        return self.driver.find_element(By.ID, self.date_picker)

    def get_field1(self):
        return self.driver.find_element(By.ID, self.field1)

    def get_field2(self):
        return self.driver.find_element(By.ID, self.field2)

    def get_submit_button(self):
        return self.driver.find_element(By.XPATH, self.submit)

    def sign_up(self, name, email, phone, country, address):
        self.get_name().send_keys(name)
        self.get_email().send_keys(email)
        self.get_phone().send_keys(phone)
        self.get_country().send_keys(country)
        self.get_address().send_keys(address)
        time.sleep(3)
    
    def click_sign_up(self):
        self.get_submit_button().click()

    @staticmethod
    def get_url_base():
        return url_base
    