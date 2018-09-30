from selenium import webdriver
if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    browser = webdriver.Chrome("E:\python_workspace\chromedriver_win32\chromedriver.exe",options=options)
    browser.get("http://www.baidu.com")
    browser.save_screenshot("baidu.png")
    browser.quit()