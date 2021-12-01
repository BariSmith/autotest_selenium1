import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




PATH = '/home/barismith/PycharmProjects/autotest_selenium/chromedriver'
driver = webdriver.Chrome(PATH)
# 1. Перейти по ссылке на главную
#     страницу сайта Netpeak (https://netpeak.ua/)
driver.get('https://netpeak.ua/')
driver.current_window_handle[0]
print(driver.current_window_handle)


# 2. Нажать на кнопку "О нас" и в выпавшем списке
#     нажать кнопку "Команда"
AboutUsButton = driver.find_element_by_xpath\
    ('//*[@id="rec278727844"]/div/div/div/div[1]/div/nav/div[1]/div[1]/ul/li[3]')
AboutUsButton.click()

TeamButton = driver.find_element_by_link_text('Команда')
TeamButton.click()
time.sleep(2)

# 3. Нажать кнопку "Стать частью команды"
#     и убедится что в новой вкладке открылась страница Работа в Нетпик
become_part_of_teamButton = driver.find_element_by_xpath('//*[@id="rec278626926"]/div/div/div[10]/a')
become_part_of_teamButton.click()
time.sleep(2)

def status_current_tab():
    driver.switch_to.window(driver.window_handles[1])
    tab_title = driver.title
 

    target_string = 'Работа в Netpeak'
    if target_string in tab_title:
        print('Correct tab')
    else:
        print("Uncorrect tab")

status_current_tab()
# 4. Убедится что на странице есть кнопка "Я хочу
#  работать в Netpeak" и на нее можно кликнуть

def work_in_teamButton_status():
    work_in_teamButton = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/a')
    print(work_in_teamButton.is_enabled())
work_in_teamButton_status()

# 5. Вернутся на предыдущую вкладку и нажать кнопку  "Личный кабинет"
driver.switch_to.window(driver.window_handles[0])
TeamButton = driver.find_element_by_link_text('Личный кабинет')
TeamButton.click()
'''Начиная с этого места и до конца у меня не получаэться найти ниже указаные обьекты через программу. 
Все что смог найти перепробовал, но без результатно. Оставляю тот вариант который на мое субьективное мнение 
самый подходящий'''
# 6. На странице личного кабинета заполнить
#     Логин и Пароль случайными данными.
def get_random_string(length):

    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))

username = driver.find_element(By.NAME, 'Логин').click()
username.send_keys(get_random_string(8))
password = driver.find_element_by_(By.NAME, 'Пароль"]').click()
password.send_keys(get_random_string(8))


# 7. Проверить что кнопка "Войти" не доступна
submitButton= driver.find_element_by_xpath('//*[@id="loginForm"]/div[5]/button/span')
prop = submitButton.get_property('disabled')
print (prop)

# 8. Отметить чекбокс "Авторизируясь, вы соглашаетесь с
#     Политикой конфиденциальности"
checkbox = driver.find_element_by_xpath('//*[@id="loginForm"]/div[4]/div/md-checkbox').click()
# 9. Нажать на кнопку войти и проверить наличие нотификации
#     о неправильном логине или пароле
submitButton= driver.find_element_by_xpath('//*[@id="loginForm"]/div[5]/button/span').click()
wait = WebDriverWait(driver, 10)
wait.until(EC.alert_is_present())

alert = driver.switch_to.alert
assert "Непраильный логин или пароль" in alert.text
alert.accept()

# 10. Проверить что Логин и Пароль подсветились красным цветом

#Тут вообще пока что не знаю как найти цвет и как это обработать.
