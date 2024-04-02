from selenium import webdriver
from selenium.webdriver.common.by import By


class findelementByClassNameTagName:
    def test(self):
        baseUrl = "https://www.letskodeit.com/practice"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        driver.implicitly_wait(10)
        # chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_experimental_option("detach", True)
        # driver = webdriver.Chrome(options=chrome_options)
        element_By_ClassName = driver.find_element(By.CLASS_NAME, "class1")
        print(element_By_ClassName.text)

        if element_By_ClassName is not None:
            print("We found an element by ClassName")
        else:
            print("We could not find an element by ClassName")

        element_By_TagName = driver.find_element(By.TAG_NAME, "h1")
        print(element_By_TagName.text)

        if element_By_TagName is not None:
            print("We found an element by TagName")
        else:
            print("We could not find an element by TagName")


runtest = findelementByClassNameTagName()
runtest.test()
