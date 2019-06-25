from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
import HtmlTestRunner
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))

class MOC_bot2(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Firefox(executable_path="C:/Users/QA/Desktop/work/Завдання У ПРОЦЕССІ/MOC site/Autotest/Drivers/geckodriver-v0.24.0-win64/geckodriver.exe")
        cls.driver.maximize_window()

    def test_input_data(self):
        self.driver.get("https://mocnewstage.mocstage.com/")
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='top_bar']/nav/a").click()
        self.driver.find_element_by_class_name("accept_cookies").click()

        #Enter user name
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='bot-form__input']").send_keys("Hi, my name is John")
        self.driver.find_element_by_xpath("//*[@id='bot-form__input']").send_keys(Keys.ENTER)

        #Select project type
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='bot-form__projecttype']/label[2]/span").click()
        self.driver.find_element_by_xpath("//*[@id='bot-form__input-form']/div/button").click()

        #Enter the neame of project
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='bot-form__input']").send_keys("My project is really interesting")
        self.driver.find_element_by_xpath("//*[@id='bot-form__input-form']/div/button").click()

        #Enter a launce date
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='bot-form__input']").send_keys("I'm going to start my project in the 14th of May")
        self.driver.find_element_by_xpath("//*[@id='bot-form__input-form']/div/button").click()

        #Select price option
        time.sleep(3)
        #self.driver.find_element_by_xpath("//*[@id='high']").click()                               #high option
        self.driver.find_element_by_xpath("//*[@id='mid']").click()                                 #mid option
        #self.driver.find_element_by_xpath("//*[@id='low']").click()                                #low option
        self.driver.find_element_by_xpath("//*[@id='bot-form__input-form']/div/button").click()

        #Enter company name
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='bot-form__input']").send_keys("Auto-test CO")
        self.driver.find_element_by_xpath("//*[@id='bot-form__input-form']/div/button").click()

        #Enter email address
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='bot-form__input']").send_keys("testemail@qwe.com")
        self.driver.find_element_by_xpath("//*[@id='bot-form__input-form']/div/button").click()
#       self.error_message = self.driver.find_element_by_xpath("//*[@id='bot-form__conversation-wrapper']/li[13]/div[2]")
#       assert self.error_message.text != 'Your email address is invalid. Please enter a valid address.'

        #Enter Phone number
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='skip']").click()                                # tap on the "skip" button
#       self.driver.find_element_by_xpath("//*[@id='bot-form__input']").send_keys("123456789")      # enter phone value
#       self.driver.find_element_by_xpath("//*[@id='bot-form__input-form']/div/button").click()     # send phone value

        #Summary message
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='ok']").click()                                #looks Good! button
#       self.driver.find_element_by_xpath("//*[@id='bot-summary__buttons']/div/a").click()          #Restart Conversation! button

        #End bot flow
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='bot__to-contacts']").click()                    #Contact Us button
#       self.driver.find_element_by_xpath("//*[@id='bot__to-portfolio']").click()                   #View Our Works button


    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(5)
        cls.driver.close()
        print("Test completed!!!")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/QA/PycharmProjects/POM_01/SampleProjects/POMprojectDEMO/reports'))