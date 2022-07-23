from selenium import webdriver

txt_element_class = "quantumWizTextinputPaperinputInput"
submit_element_class = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span'

url = "https://forms.gle/EjmBKTnsmgmR7d586"
# ensure that chromedriver installed is the same version as current google version
driver = webdriver.Chrome(executable_path="/Users/ron.quah/Downloads/chromedriver")

driver.get(url)


def text_fields(driver, element_class):
    name = "<list/database of names>"
    email = "<list/database of names>"
    text_answers = [name, email]  # following the order in the form
    text_questions = driver.find_elements_by_class_name(element_class)
    for a, q in zip(text_answers, text_questions):
        q.send_keys(a)

    return driver

def file_upload(driver):
    iframe = driver.find_element_by_class_name('picker-frame')
    driver.switch_to.frame(iframe)
    input_field = driver.find_element_by_xpath('//input[@type="file"]')
    input_field.send_keys("<File Path of Image to be Uploaded>")
    driver.switch_to.default_content()

    return driver


def submit(driver, element_class):
    driver.find_element_by_xpath(element_class).click()
    return driver


driver = text_fields(driver, element_class=txt_element_class)
driver = file_upload(driver)
driver = submit(driver, element_class=submit_element_class)