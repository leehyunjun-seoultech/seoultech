from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

# driver = webdriver.Chrome()
options = webdriver.ChromeOptions() 
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options, executable_path=r'C:/Users/Coke/Desktop/chromedriver_win32/chromedriver.exe')
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("동형암호")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight") 

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
    last_height = new_height

# imgs = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click()
# img_url = driver.find_element_by_xpath("./html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div/div[2]/a/img").get_attribute("src")
# print(img_url)
# urllib.request.urlretrieve(img_url, "1.jpg")

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    image.click()
    time.sleep(3)
    img_url = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
    urllib.request.urlretrieve(img_url, str(count) + ".jpg")
    count = count + 1 

driver.close()