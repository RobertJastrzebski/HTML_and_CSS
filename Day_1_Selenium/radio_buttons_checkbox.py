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
        bmwRadioBtn = driver.find_element(By.ID, "bmwradio")
        bmwRadioBtn.click()
        benzRadopBtn = driver.find_element(By.ID,"benzradio")
        benzRadopBtn.click()
        hondaRadioBtn= driver.find_element(By.ID,"hondaradio")
        hondaRadioBtn.click()

        bmwCheckBox=driver.find_element(By.ID,"bmwcheck")
        bmwCheckBox.click()
        benzCheckBox=driver.find_element(By.ID,"benzcheck")
        benzCheckBox.click()

        print(f"Bmw radio button is sellected {bmwRadioBtn.is_selected()}")
        print(f"Bmw checkbox is sellected {bmwCheckBox.is_selected()}")

        time.sleep(5)
        driver.quit()


test = DriverInteractions()
test.test()
