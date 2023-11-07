from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from seleniumwire import webdriver
from selenium_stealth import stealth
import time

global driver
def initialize_driver():
    options = webdriver.ChromeOptions()
    
    options.add_argument('--disable-gpu')
    options.add_argument('--mute-audio')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--disable-infobars')
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--no-sandbox')
    options.add_argument('--no-zygote')
    options.add_argument('--log-level=3')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-web-security')
    options.add_argument('--disable-features=VizDisplayCompositor')
    options.add_argument('--disable-breakpad')
    
    driver = webdriver.Chrome(options=options)
    
    stealth(driver,
        user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )
    
    driver.implicitly_wait(2)
    driver.set_window_position(980, 0, windowHandle='current')
    return driver


driver = initialize_driver()


time.sleep(10)  # import time