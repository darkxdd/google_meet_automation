from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def Glogin(mail_address, password):
    
	driver.get(
		'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')

	
	driver.find_element(By.ID, "identifierId").send_keys(mail_address)
	driver.find_element(By.ID, "identifierNext").click()
	driver.implicitly_wait(10)

	
	driver.find_element(By.XPATH,
		'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
	driver.implicitly_wait(10)
	driver.find_element(By.ID, "passwordNext").click()
	driver.implicitly_wait(10)

	
	driver.get('https://google.com/')
	driver.implicitly_wait(100)


def turnOffMicCam():

	time.sleep(2)
	driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[1]/div[1]/div/div[6]/div[1]/div/div/div[1]').click()


	time.sleep(1)
	driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[1]/div[1]/div/div[6]/div[2]/div/div[1]').click()



def joinNow():
	
	print(1)
	time.sleep(5)
	driver.implicitly_wait(2000)
	driver.find_element(By.XPATH,
		'//*[@id="yDmH0d"]/c-wiz/div/div/div[14]/div[3]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[2]/div[1]/div[1]/button').click()
	print(1)

mail_address = 'YOUR_EMAIL'
password = 'EMAIL_PASSWORD'


opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_experimental_option("prefs", {
	"profile.default_content_setting_values.media_stream_mic": 1,
	"profile.default_content_setting_values.media_stream_camera": 1,
	"profile.default_content_setting_values.geolocation": 0,
	"profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(options=opt)


Glogin(mail_address, password)


driver.get('https://meet.google.com/MEETING_ID')
turnOffMicCam()

joinNow()
