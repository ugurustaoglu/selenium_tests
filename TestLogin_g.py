import subprocess
import time
from windowstasks import taskKill
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(executable_path=r"c:\Python27\drivers\chromedriver.exe")
#driver = webdriver.Ie("c:\Python27\drivers\IEDriverServer.exe")


try:
    caps = webdriver.DesiredCapabilities.EDGE
    driver = webdriver.Edge(executable_path=r"c:\Python27\drivers\MicrosoftWebDriver.exe", capabilities=caps)
    driver.implicitly_wait(10)
except:
    print("Cannot Find Driver or Driver Incompatible")
    driver.quit()



try:
    driver.get("https://xxx/index.aspx")
    print("URL successfully Accessed")
except:
    print("Page load Timeout Occured. Quiting !!!")
    driver.quit()




WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="_ctl0_MusNoText"]'))
)


try:
    musno_box = driver.find_element_by_xpath('//*[@id="_ctl0_MusNoText"]')
    musno_box.send_keys('345235425')
except StaleElementReferenceException as Exception:
    print 'StaleElementReferenceException while trying to access object:_ctl0_MusNoText'
    driver.quit();


muspass_box = driver.find_element_by_xpath('//*[@id="ParolaText"]')
muspass_box.send_keys('213411')
login_button = driver.find_element_by_xpath('//*[@id="_ctl0_SubeLogin01_btnGiris"]')
login_button.click()
time.sleep(5)

WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="ParolaText"]'))
)

musno_box = driver.find_element_by_xpath('//*[@id="_ctl0_MusNoText"]')
musno_box.send_keys('3532452435')
captcha_box = driver.find_element_by_xpath('//*[@id="captcha"]')
captcha_box.send_keys('2345243')
parole_box = driver.find_element_by_xpath('//*[@id="ParolaText"]')
parole_box.send_keys('24352354')

time.sleep(10)


driver.close()

