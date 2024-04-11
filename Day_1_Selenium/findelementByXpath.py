from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementByXpath:
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        driver.maximize_window()

        course_name = driver.find_element(
            By.XPATH, "//table[@id='product']//td[text()='Python Programming Language']"
        )
        if course_name is not None:
            print("We found an element by XPATH")
        else:
            print("We could not find an element by XPATH")

        course_price = driver.find_element(
            By.XPATH,
            "//table[@id='product']//td[text()='Python Programming Language']//following-sibling::td",
        )
        print(course_name.text)

        if course_price is not None:
            print("We found an element by XPATH")
        else:
            print("We could not find an element by XPATH")
        print(course_price.text)


runtest = FindElementByXpath()
runtest.test()
