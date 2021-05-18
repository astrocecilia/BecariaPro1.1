from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Esta linea abre una ventana de firefox
driver = webdriver.Firefox()
#Esta linea abre la url de autocompara
driver.get("https://www.autocompara.com/")
#Amos a esperar tantito pa que la pagina carge
time.sleep(2)

driver.find_element_by_xpath('//*[@id="quotationData"]/div/div[2]/ac-vehicle-data/section/div/div[2]/div[2]/ng-select/div/div/div[2]').click()

time.sleep(1)
yearInput = driver.find_element_by_xpath('//*[@id="year"]')
#yearInput.send_keys("2018")
#yearInput.click()

time.sleep(5)

driver.close()
print("Terminando programa")