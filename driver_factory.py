from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from msedge.selenium_tools import Edge, EdgeOptions


class DriverFactory:
    @staticmethod
    def get_driver(browser):
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("start-maximized")
            return webdriver.Chrome(ChromeDriverManager().install(),options=options)

            #options = EdgeOptions()
            #options.use_chromium = True
            #options.add_argument("start-maximized")
            #webdriver = Edge(options = options)
            #return Edge()
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("start-maximized")
            return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
        raise Exception('Provide valid driver name')