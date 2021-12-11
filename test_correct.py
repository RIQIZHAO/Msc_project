from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import unittest
from selenium.common.exceptions import NoAlertPresentException

print("start---------")
#s = Service("/usr/local/bin/chromedriver")
#drivers = webdriver.Chrome(service=s)
answer_list=['2',
 '5',
 'True',
 'True',
 'True',
 'True',
 'True',
 '\'Hello,"Ricky!"\'',
 '"Don\'t"',
 '22',
 '15',
 '"Hello, Ricky"',
 '"Hello, Ricky"',
 '"Hello, Ricky"',
 '"Hello, "',
 "'true'",
 "'true'",
 "'values: 1 and two'",
 "'values: two, 1, 1 and two!'",
 "'pin'",
 "'p'",
 '97',
 'True',
 "['apple', 'pear', 'orange']",
 "['apple', 'pear', 'orange', 'cherry']",
 "'I like apple'",
 "'Apple'",
 "'APPLE'",
 "'apple'",
 "'I Like Apple'",
 "'i lIKE aPPLE'",
 'dict',
 '0',
 '2',
 "'apple'",
 'True',
 'True',
 '2',
 '2',
 'True',
 'False',
 'False',
 'True',
 '5',
 '66',
 '0',
 '[]',
 '[1]',
 '[1, 2]',
 '[1, 2, 333]',
 "'pineapple'",
 "'cherry'",
 "['apple']",
 "['apple', 'pear']",
 '[]',
 "['banana', 'pineapple']",
 '[]',
 '[]',
 "['banana', 'pineapple']",
 "['apple', 'pear']",
 'range',
 'False',
 '[0, 1, 2, 3, 4]',
 '[5, 6, 7, 8]',
 '[0, 2, 4, 6]',
 '[1, 4, 7]',
 '[5, 1, -3]',
 '[5, 1, -3, -7]',
 "['apple', 'pear', 'pineapple', 'banana']",
 "[10, 20, 30, 40, 'last']",
 "'last'",
 "[10, 30, 40, 'last']",
 "'Ricky'",
 "['Ricky', 'Leslie']",
 "'Miss'",
 "['Ricky', 'Leslie']",
 "'Zhao'",
 "{'apple', 'orange', 'pear'}",
 'True',
 'True',
 'set',
 'dict',
 'dict',
 'True',
 'True',
 "['1', '2', '3']",
 "{'orange'}",
 "{'apple', 'orange', 'pear', 'pineapple'}",
 "{'apple', 'pear'}",
 "{'orange', 'pineapple'}",
 'True',
 'True',
 'True',
 'True',
 'False',
 '3',
 "('R', 'i', 'c', 'k', 'y', '!')",
 "('ricky', (1, 2, 'z'), (2, 3, 'r'))",
 "'pie'",
 '"\'tuple\' object does not support item assignment"',
 '"\'tuple\' object does not support item assignment"',
 "'true'",
 "'true value'",
 "'true value'",
 '6',
 '6',
 '[1, 3, 5, 7, 9]',
 "['APPLE', 'PEAR', 'ORANGE']",
 "'true'",
 "'false'",
 "'false'",
 "'false'",
 "'false'",
 "'false'",
 "'false'",
 "'false'",
 "'false'",
 "'true'",
 "'true'",
 "'true'",
 "'true'",
 "'true'",
 "'Pineapple'",
 '2',
 "'pearpearpear'",
 "'pear and chicken'",
 "{'a', 'b', 'c', 'e'}",
 'False',
 'True',
 "['apple jam', 'pear jam', 'orange jam']",
 '2',
 '2',
 "['apple', 'apple', 'apple']",
 '[]',
 "['apple', 'pear', 'pineapple', 'cherry']",
 "'apple'",
 "'pear'",
 '[4, 9, 16]',
 '[2, 5, 9]',
 '3',
 "'with value'",
 "'no value'",
 "'no value'",
 '6',
 "'orange'",
 "'Ran out of iterations'",
 'map',
 '[6, 7, 8]',
 '[2, 4, 6]',
 "'cherry'",
 'int',
 '6',
 '12',
 '4',
 '3',
 'True',
 "[1, 'default_value']",
 '()',
 "('one',)",
 "('one', 'two')",
 "'missing 2 required positional arguments'",
 "'missing 2 required positional arguments'",
 'True',
 'True',
 'True',
 'True',
 'True',
 "'Ricky'",
 "'now sitting'",
 "'sad'",
 "'sound,husky'"]

class testPython(unittest.TestCase):

        def test_correctAnswer(self):
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

                i = 0
                while i < len(answer_list):
                    self.driver.find_element_by_id("input").send_keys(answer_list[i])
                    self.driver.find_element_by_id("submit-btn").click()
                    self.welldone_alert = self.driver.switch_to.alert
                    self.assertEqual('well done!', self.welldone_alert.text, msg='this is not correct answer')
                    # time.sleep(2)
                    self.welldone_alert.accept()
                    # time.sleep(2)
                    self.driver.find_element_by_id("next-btn").click()
                    i = i + 1


# enter
if __name__ == "__main__":
    unittest.main(verbosity=0)