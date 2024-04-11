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
        # Get Title
        title = driver.title
        print(f"Title of the web page is:{title} ")
        # Get Current Url
        currentUrl = driver.current_url
        print(f"Current Url of the web page is:{currentUrl} ")
        # Browser Refresh
        driver.refresh()
        print("Browser Refreshed 1st time")
        driver.get(driver.current_url)
        print("Browser Refreshed 2nd time")
        # Open another Url
        driver.get(
            "https://sso.teachable.com/secure/42299/users/sign_in?reset_purchase_session=1"
        )
        time.sleep(5)
        currentUrl = driver.current_url
        print(f"Current Url of the web page is: {currentUrl}")

        # Browser Back
        print("Go one step back in browser history")

        driver.back()
        time.sleep(5)
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        # Browser Forward
        print("Go one step forward in browser history")

        driver.forward()
        time.sleep(5)
        currentUrl = driver.current_url
        print("Current Url of the web page is: " + currentUrl)

        # Get Page Source
        # pageSource = driver.page_source
        # print(pageSource)
        # Browser Close / Quit
        # driver.close()
        driver.quit()


test = DriverInteractions()
test.test()
