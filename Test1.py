import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:/Users/Isabel/Workspaces/test-lab/chromedriver.exe")
try:
    driver.get("https://www3.animeflv.net/")
    time.sleep(20)
    link_serie = driver.find_element(By.CSS_SELECTOR, "#mCSB_1_container > ul > li:nth-child(1) > a")
    link_serie.click()
    link_episodio = driver.find_element(By.CSS_SELECTOR, "#episodeList > li:nth-child(2) > a > p")
    assert link_episodio.text == "Episodio 998"
    print("nuevo episodio")
finally:
    driver.quit()
