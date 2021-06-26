class home_page():
    def __init__(self,driver):
        self.driver=driver
        self.welcome='//*[@id="welcome"]'
        self.logout='//*[@id="welcome-menu"]/ul/li/a[@href="/index.php/auth/logout"]'

    def click_welcome(self):
        self.driver.find_element_by_xpath(self.welcome).click()
    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout).click()
