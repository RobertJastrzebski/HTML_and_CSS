import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class DriverInteractions:
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        # Window Maximize
        driver.maximize_window()
        # Open the Url
        driver.get(baseUrl)
        radioButtonsList=driver.find_elements(By.XPATH,"//input[@type='radio']")
        size=len(radioButtonsList)
        print(f"size of listy is {size}")

        for radioButton in radioButtonsList:
            if radioButton.is_selected():
                print("Radio buttton is selected")
            else:
                radioButton.click()
        time.sleep(5)
        driver.quit()


test = DriverInteractions()
test.test()
