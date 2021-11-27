from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://netpeak.ua/')
AboutUsButton = driver.find_element_by_xpath\
    ('//*[@id="rec278727844"]/div/div/div/div[1]/div/nav/div[1]/div[1]/ul/li[3]')
AboutUsButton.click()
TeamButton = driver.find_element_by_link_text('Команда')
TeamButton.click()
become_part_of_teamButton = driver.find_element_by_xpath('//*[@id="rec278626926"]/div/div/div[10]/a')
become_part_of_teamButton.click()