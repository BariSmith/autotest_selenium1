from selenium import webdriver
from selenium.webdriver.common.keys import Keys

brovser = webdriver.Chrome()
brovser.get("https://www.netpeak.ua")
assert "О нас" in brovser.title
elem = brovser.
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in brovser.page_source
# brovser.close()