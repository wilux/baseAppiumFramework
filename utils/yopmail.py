from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def get_code(mail, flow):
    print("yopmail")
    options = Options()
    options.headless = True
    chrome_driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    chrome_driver.implicitly_wait(10)
    chrome_driver.get('https://yopmail.com/')
    chrome_driver.find_element(By.XPATH, '//input[@id="login"]').send_keys(mail)
    chrome_driver.find_element(By.XPATH, '//i[@class="material-icons-outlined f36"]').click()
    chrome_driver.switch_to.frame('ifmail')
    if flow == "device":
        mode = 'h4:nth-of-type(1) > strong'
        code = chrome_driver.find_element(By.CSS_SELECTOR, mode).text
        print(code)
    else:
        mode = '(//div[@id="mail"]//span)[2]'
        code = chrome_driver.find_element(By.XPATH, mode).text
        print(code)
    if chrome_driver.service.process is not None:
        chrome_driver.quit()
    return code


def recaptcha(chrome_driver):
    try:
        print("Try Captcha")
        WebDriverWait(chrome_driver, 5).until(EC.frame_to_be_available_and_switch_to_it(
            (By.CSS_SELECTOR, "[title='reCAPTCHA']")))
        WebDriverWait(chrome_driver, 2).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()
    except:
        pass
