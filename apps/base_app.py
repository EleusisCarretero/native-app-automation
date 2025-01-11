class BaseApp:
    def __init__(self, driver):
        self.base_driver = driver
    
    def click_app_button(self, locator):
        button_obj = self.base_driver.find_element(*locator)
        button_obj.click()
