from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import unittest
from selenium.common.exceptions import NoAlertPresentException

print("start---------")
#s = Service("/usr/local/bin/chromedriver")
#drivers = webdriver.Chrome(service=s)



class testPython(unittest.TestCase):

    def test_link(self):
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
        self.length = len(self.driver.find_elements_by_tag_name("a"))
        for x in range(0, self.length):
            self.links = self.driver.find_elements_by_tag_name("a")
            self.link = self.links[x]
            if not ("_blank" in self.link.get_attribute("target") or not "http" in self.link.get_attribute("href")):
                self.link.click()
                if x==0:
                    a=self.driver.find_element_by_xpath("//div//h1").text
                    self.assertEqual(a,"Python 3.10.0 documentation",msg="success")
                elif x==1:
                    b = self.driver.find_element_by_xpath("//div//h2").text
                    self.assertEqual(b, "A Python 3 implementation for client-side web programming", msg="success")
                time.sleep(3)
                self.driver.back()
                time.sleep(3)


# enter
if __name__ == "__main__":
    unittest.main(verbosity=0)