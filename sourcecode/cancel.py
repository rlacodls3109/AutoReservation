from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)


#평일에 공휴일일 경우 10~22시로 변경해야 하는 날짜에 들어간 후 실행
while (1):
    for i in range(2,13):
        try: # 공휴일 (10~22) 설정되어있는 경우 취소하고싶으면 tr[49]로 변경
            driver.find_element(By.XPATH,
                                f"//*[@id=\"reservationTbl\"]/tbody/tr[1]/td[{i}]/a").click()
        except:
            continue
        else:
            time.sleep(0.5)
            driver.find_element(By.XPATH,
                                "//*[@id=\"reservationInfo\"]/div/div[3]/a[1]").click()
            time.sleep(0.3)
            driver.find_element(By.XPATH, "//*[@id=\"reservationCancel\"]/div/div[3]/a[2]").click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, "//*[@id=\"commonAlert\"]/div/div[3]/a").click()
    try:
        driver.find_element(By.CLASS_NAME, "month-next").click()
    except:
        break
    else:
        continue
