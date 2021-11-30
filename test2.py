import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located



# PATH = 'D:\chromedriver.exe'
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
    # НЕ СОВСЕМ ПОНЯЛ ВТОРУЮ ЧАСТЬ 3ГО ПУНКТА:
     #   В ДЕЙСТВИТЕЛЬНОСТИ ПРОВЕРЕТЬ НАЗВАНИЕ 'Работа в Нетпик' ИЛИ ЖЕ ВСЕТАКИ 'Работа в Netpeak'. ПО ЭТОМУ ДЕЛАЮ 2 ВАРИАНТА (ТАК КАК ВРЕМЯ ПОДЖИМАЕТ А В СТОЛЬ ПОЗНИЙ ЧАС ПЕРЕСПРОСИТЬ НЕ МОГУ) КАКОЙ НЕ НУЖНО ТОТ ЗАКОМЕНТИРУЙТЕ

    target_string = 'Работа в Netpeak'
    # target_string = 'Работа в Нетпик'
    if target_string in tab_title:
        print('Correct tab')
    else:
        print("Uncorrect tab")

status_current_tab()
# 4. Убедится что на странице есть кнопка "Я хочу
#  работать в Netpeak" и на нее можно кликнуть
# work_in_teamButton = driver.find_element_by_name('Я хочу  работать в Netpeak')
def work_in_teamButton_status():
    work_in_teamButton = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/a')
    print(work_in_teamButton.is_enabled())
work_in_teamButton_status()

# 5. Вернутся на предыдущую вкладку и нажать кнопку
#     "Личный кабинет"
driver.switch_to.window(driver.window_handles[0])
TeamButton = driver.find_element_by_link_text('Личный кабинет')
TeamButton.click()

#
# 6. На странице личного кабинета заполнить
#     Логин и Пароль случайными данными.
def get_random_string(length):

    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
LoginForm =driver.find_element_by_xpath('//*[@id="loginForm"]').click()
username = driver.find_element(By.NAME, 'Логин').click()
username.send_keys('get_random_string(8)')
# password = driver.find_element_by_xpath('//*[@id="password"]').click()
# password.send_keys(get_random_string(8))


# 7. Проверить что кнопка "Войти" не доступна

# 8. Отметить чекбокс "Авторизируясь, вы соглашаетесь с
#     Политикой конфиденциальности"
#
# 9. Нажать на кнопку войти и проверить наличие нотификации
#     о неправильном логине или пароле
#
# 10. Проверить что Логин и Пароль подсветились красным цветом
