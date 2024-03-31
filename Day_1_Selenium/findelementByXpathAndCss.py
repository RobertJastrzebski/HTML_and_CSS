from selenium import webdriver
from selenium.webdriver.common.by import By


class FindElementByXpathAndCss:
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_experimental_option("detach", True)
        # driver = webdriver.Chrome(options=chrome_options)
        element_By_ID = driver.find_element(By.XPATH, "//input[@id='displayed-text']")

        if element_By_ID is not None:
            print("We found an element by XPATH")
        else:
            print("We could not find an element by XPATH")

        element_By_Name = driver.find_element(
            By.CSS_SELECTOR, "input[id='displayed-text']"
        )

        if element_By_Name is not None:
            print("We found an element by CSS_SELECTOR")
        else:
            print("We could not find an element by CSS_SELECTOR")


runtest = FindElementByXpathAndCss()
runtest.test()
