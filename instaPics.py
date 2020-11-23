from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from secrets import username,password
from selenium.webdriver.chrome.options import Options

#Configure Chrome
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})


driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=option)
driver.get('https://instagram.com/accounts/login')
sleep(2)

def fbLogin():
	#Click the Facebook Login Button
	usrField = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/button')
	usrField.click()
	sleep(2)

	#Switch to facebook page
	base_window = driver.window_handles[0]
	driver.switch_to_window(driver.window_handles[0])

	#Enter in Facebook credentials 
	userField = driver.find_element_by_xpath('//*[@id="email"]')
	userField.send_keys(username)

	sleep(2)

	passField = driver.find_element_by_xpath('//*[@id="pass"]')
	passField.send_keys(password)

	#Click login button
	logIn = driver.find_element_by_xpath('//*[@id="loginbutton"]')
	logIn.click()
	base_window = driver.window_handles[0]
	driver.switch_to_window(driver.window_handles[0])

	accept = driver.find_element_by_xpath('//*[@id="u_0_11"]/div[1]/div/div/div[3]/button[1]')
	accept.click()
	sleep(2)
	base_window = driver.window_handles[0]
	driver.switch_to_window(driver.window_handles[0])

def goToPage(userName):
	search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
	search.send_keys(userName)
	search.send_keys(u'\ue007')	
fbLogin()
goToPage('jonnycross10')
