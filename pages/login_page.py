class login_Page():
    def __init__(self,driver):
        self.driver=driver
        self.user_xpath='//*[@id="divUsername"]/input'
        self.psswrd_xpath='//*[@id="divPassword"]/input'
        self.login_xpath='//*[@id="btnLogin"]'
    def enter_username(self,user):
        self.driver.find_element_by_xpath(self.user_xpath).send_keys(user)
    def enter_password(self,password):
        self.driver.find_element_by_xpath(self.psswrd_xpath).send_keys(password)
    def click_login(self,):
        self.driver.find_element_by_xpath(self.login_xpath).click()