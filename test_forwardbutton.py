from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import unittest
from selenium.common.exceptions import NoAlertPresentException

print("start---------")
#s = Service("/usr/local/bin/chromedriver")
#drivers = webdriver.Chrome(service=s)



class testPython(unittest.TestCase):

    def test_wronganswer(self):
        self.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
        print(dir(self.driver))
        url = "file:///Users/zhaoriqi/web/index.html"
        self.driver.get(url)
        self.driver.maximize_window()
        print("window have already")
        self.position = self.driver.get_window_position()
        print("position:", self.position)
        self.driver.set_window_position(0, 0)
        self.position = self.driver.get_window_position()
        print("current position:", self.position)
        time.sleep(3)


        self.driver.find_element_by_id("next-btn").click()
        time.sleep(2)
        self.driver.find_element_by_id("next-btn").click()
        time.sleep(2)
        self.driver.find_element_by_id("next-btn").click()
        time.sleep(2)
        self.driver.find_element_by_id("forward-btn").click()
        time.sleep(2)
        self.driver.find_element_by_id("forward-btn").click()
        time.sleep(2)


# enter
if __name__ == "__main__":
    unittest.main(verbosity=0)