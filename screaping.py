from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def sriping_vega(search_text: str, How_much):
    driver = webdriver.Chrome()
    driver.get("https://vega.am/am")
    time.sleep(5)

        # Find the search box by name="q"
    search_box = driver.find_element(By.NAME, "search2")
    search_box.clear()
    search_box.send_keys(search_text)
    time.sleep(5)

    search_box.send_keys(Keys.RETURN)



    wait = WebDriverWait(driver, 60)
    results_container = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.product-grid.active")))

    for container in results_container:
        titles = container.find_elements(By.TAG_NAME, "a")
        title_list = [] 
        for title in titles:  
            text = title.text.strip()
            if text:
                title_list.append(text) 
    for price_cont in  results_container:
        prices = price_cont.find_elements(By.CSS_SELECTOR, "div.right span")
        price_list = []
        for price in prices:
            price_new = price.text.strip()
            if price_new:
                price_list.append(price_new)

    new_price_list = []
    new_title_list = title_list[5:]
    for i in price_list:
        new_price_list.append(int(i[:-1].replace(" ","")))
    new_total_list = list(zip(new_title_list, new_price_list))
    # print(new_total_list)
    time.sleep(5)
    driver.quit()
    return new_price_list[0:How_much], new_title_list[0:How_much]


