from selenium import webdriver
from selenium.webdriver.common.by import By


class findelementByLinkTextAndPartialLinkText:
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_experimental_option("detach", True)
        # driver = webdriver.Chrome(options=chrome_options)
        element_By_ID = driver.find_element(By.LINK_TEXT, "ALL COURSES")

        if element_By_ID is not None:
            print("We found an element by LINK_TEXT")
        else:
            print("We could not find an element by LINK_TEXT")

        element_By_Name = driver.find_element(By.PARTIAL_LINK_TEXT, "COURSES")

        if element_By_Name is not None:
            print("We found an element by PARTIAL_LINK_TEXT")
        else:
            print("We could not find an element by PARTIAL_LINK_TEXT")


runtest = findelementByLinkTextAndPartialLinkText()
runtest.test()
