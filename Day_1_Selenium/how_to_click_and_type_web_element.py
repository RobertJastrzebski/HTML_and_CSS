import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class DriverInteractions:
    def test(self):
        baseUrl = "https://www.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        # Window Maximize
        driver.maximize_window()
        # Open the Url
        driver.get(baseUrl)
        driver.find_element(By.XPATH, "//a[text()='Sign In']").click()
        time.sleep(5)
        email = driver.find_element(
            By.XPATH, "//input[@id='email' and @placeholder='Email Address']"
        )
        email.send_keys("test@gmail.com")
        password = driver.find_element(By.XPATH, "//input[@type='password']")

        password.send_keys("test")
        time.sleep(5)

        email.clear()
        password.clear()
        time.sleep(5)
        email.send_keys("test2")
        password.send_keys("test2")
        time.sleep(5)
        driver.quit()


test = DriverInteractions()
test.test()
