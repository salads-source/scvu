from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert

chromedriver_location = "/Users/ron.quah/Downloads/chromedriver"

driver = webdriver.Chrome(chromedriver_location)
driver.get("https://indentyourration.web.app/")

# login
user_field = "/html/body/div/div/form/div/input[1]"
pass_field = "/html/body/div/div/form/div/input[2]"
login_field = "/html/body/div/div/form/div/button"

user = driver.find_element_by_xpath(user_field)
user.send_keys("ronquahkaiyi")
password = driver.find_element_by_xpath(pass_field)
password.send_keys("r0nqu@hkaiyi")

login_button = driver.find_element_by_xpath(login_field).click()

# indent ration for respective days
days = ['monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        ]
base_num = [
    '/html/body/div/div/div[5]/div[3]/div[2]/div/button[2]',
    '/html/body/div/div/div[5]/div[4]/div[2]/div/button[2]',
    '/html/body/div/div/div[5]/div[5]/div[2]/div/button[2]',
    '/html/body/div/div/div[5]/div[6]/div[2]/div/button[2]',
    '/html/body/div/div/div[5]/div[7]/div[2]/div/button[2]',
]
meal_type = [
    '/html/body/div/div/div[5]/div[3]/div[2]/button[2]',
    '/html/body/div/div/div[5]/div[4]/div[2]/button[2]',
    '/html/body/div/div/div[5]/div[5]/div[2]/button[2]',
    '/html/body/div/div/div[5]/div[6]/div[2]/button[2]',
    '/html/body/div/div/div[5]/div[7]/div[2]/button[2]',
]

submit_field = '/html/body/div/div/div[5]/button'
logout_field_i = '/html/body/div/nav/div/div[2]/button'
logout_field_f = '/html/body/div/nav/div[2]/button'


driver.implicitly_wait(10)  # driver pauses for 10 seconds for webpage to load
zipped_list = list(zip(days, meal_type))
user_input = input("Are you indenting rations for the entire week? (Yes/No): ")
if user_input.lower() == 'yes':
    for item in meal_type:
        driver.find_element_by_xpath(item).click()

else:
    user_input_specific = input("Enter days that you are not indenting ration for (separated by a space): ")
    day_list = user_input_specific.lower().split(' ')
    print(day_list)
    for item in day_list:
        for items in zipped_list:
            if items[0] == item:
                zipped_list.remove(items)
    print(zipped_list)
    for item in zipped_list:
        driver.find_element_by_xpath(item[1]).click()

for item in base_num:
    driver.find_element_by_xpath(item).click()

submit = driver.find_element_by_xpath(submit_field).click()

try:
    WebDriverWait(driver, 5).until(EC.alert_is_present(), 'Waiting for alert timed out')
    alert = Alert(driver).accept()
    print('Alert Accepted')

except TimeoutException:
    print('No Alert Detected')

logout_i = driver.find_element_by_xpath(logout_field_i).click()
logout_f = driver.find_element_by_xpath(logout_field_f).click()

driver.close()






