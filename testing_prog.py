from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import string


chrome_driver = webdriver.Chrome(executable_path=r"C:/programming/chrome/chromedriver.exe")
wait = WebDriverWait(chrome_driver, 10)

#1. Перейти по ссылке на главную страницу сайта Netpeak. (https://netpeak.ua/)
chrome_driver.get("https://netpeak.ua/")
assert "Netpeak" in chrome_driver.title
original_window = chrome_driver.current_window_handle 

#2. Перейдите на страницу "Работа в Netpeak", нажав на кнопку "Карьера"

career_button = chrome_driver.find_element_by_link_text('Карьера')
career_button.click()
wait.until(EC.number_of_windows_to_be(2))
for window_handle in chrome_driver.window_handles:
        if window_handle != original_window:
            chrome_driver.switch_to.window(window_handle)
            break
assert "Работа" in chrome_driver.title

#3. Перейти на страницу заполнения анкеты, нажав кнопку - "Я хочу работать в Netpeak"
wait.until(EC.presence_of_element_located((By.LINK_TEXT , "Я хочу работать в Netpeak")))
want_to_work_button = chrome_driver.find_element_by_link_text('Я хочу работать в Netpeak')
want_to_work_button.click()

#4. Загрузить файл с недопустимым форматом в блоке "Резюме", например png, и проверить что на странице появилось сообщение, 
# о том что формат изображения неверный.
wait.until(EC.presence_of_element_located((By.ID , "upload")))
upload_resume = chrome_driver.find_element_by_name('up_file')
chrome_driver.find_element_by_css_selector('input[type=file]').send_keys('C:\\test_jpg.jpg')
alert_Xpath = '//div[@id="up_file_name"]/label[1]'
wait.until(EC.text_to_be_present_in_element((By.XPATH, alert_Xpath), 
    'Ошибка: неверный формат файла (разрешённые форматы: doc, docx, pdf, txt, odt, rtf).'))

#5. Заполнить случайными данными блок "3. Личные данные"
string_consistance = string.ascii_letters + string.punctuation + string.digits
random_string1 = ''.join(random.choice(string_consistance) for x in range(12))
random_string2 = ''.join(random.choice(string_consistance) for x in range(12))
input_name = chrome_driver.find_element_by_id('inputName')
input_name.clear()
input_name.send_keys(random_string1)
input_lastname = chrome_driver.find_element_by_id('inputLastname')
input_lastname.clear()
input_lastname.send_keys(random_string2)

#6. Нажать на кнопку отправить резюме
chrome_driver.find_element_by_id('submit').click()

#7. Проверить что сообщение на текущей странице  - "Все поля являются обязательными для заполнения" - подсветилось красным цветом
all_fields_required_color = chrome_driver.find_element_by_class_name('warning-fields').value_of_css_property('color')
assert all_fields_required_color == "rgba(255, 0, 0, 1)"

#8. Перейти на страницу "Курсы" нажав соответствующую кнопку в меню и убедиться что открылась нужная страница.
chrome_driver.find_element_by_link_text('Курсы').click()
assert 'курсы по SEO, PPC, PHP в Одессе' in chrome_driver.title

chrome_driver.quit()