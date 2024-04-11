import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DriverInteractions:
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)

        # Window Maximize
        driver.maximize_window()
        # Open the Url
        driver.get(baseUrl)
        dropDown = driver.find_element(By.ID, "carselect")
        selection = Select(dropDown)
        selection.select_by_visible_text("Benz")
        time.sleep(5)
        selection.select_by_index(0)
        selection.select_by_value("honda")
        time.sleep(5)
        driver.quit()


test = DriverInteractions()
test.test()
