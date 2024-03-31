from selenium import webdriver
from selenium.webdriver.common.by import By

class FindElementByIdName:
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get( baseUrl)
        driver.implicitly_wait(10)
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=chrome_options)
        element_By_ID=driver.find_element(By.ID, "displayed-text")

        if element_By_ID is not None:
            print("We found an element by ID")
        else:
            print("We could not find an element by ID")
        
        element_By_Name=driver.find_element(By.NAME, "enter-name")

        if element_By_Name is not None:
            print("We found an element by Name")
        else:
            print("We could not find an element by Name")

runtest= FindElementByIdName()
runtest.test()