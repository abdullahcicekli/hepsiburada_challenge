import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def before_feature(context,feature):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.option=Options()
    context.browser.implicitly_wait(10)
    context.browser.maximize_window()

    context.option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})
    context.option.add_argument("--disable-extensions")
    context.option.add_argument("--disable-notifications")
    context.option.add_argument("--disable-infobars")


    context.link="https://www.hepsiburada.com/"
    context.username = 'baykustasarimm@outlook.com'
    context.password = '0Px_nya36-'
    # context.username = 'email_address'
    # context.password = 'Password'


def after_feature(context,feature):
    time.sleep(10)
    context.browser.quit()
