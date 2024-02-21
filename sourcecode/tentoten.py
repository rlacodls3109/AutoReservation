from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)


#평일에 공휴일일 경우 10~22시로 변경해야 하는 날짜 창에 들어간 후 실행
while (1):
    for i in range(2,13):
        try:
            driver.find_element(By.XPATH,
                                f"//*[@id=\"reservationTbl\"]/tbody/tr[1]/td[{i}]/a").click()
        except:
            continue
        else:
            time.sleep(0.5)
            driver.find_element(By.XPATH,
                                "//*[@id=\"reservationInfo\"]/div/div[3]/a[2]").click()
            time.sleep(0.5)
            #시작시간
            driver.find_element(By.XPATH,
                                "//*[@id=\"bookingFrm\"]/table/tbody/tr[3]/td/div/div[1]/div/div[2]/b").click()

            driver.find_element(By.XPATH,
                                "//*[@id=\"bookingFrm\"]/table/tbody/tr[3]/td/div/div[1]/div/div[3]/div/ul/li[5]").click()

            #종료시간
            driver.find_element(By.XPATH,
                                "//*[@id=\"bookingFrm\"]/table/tbody/tr[4]/td/div/div[1]/div/div[2]/b").click()

            driver.find_element(By.XPATH,
                                "//*[@id=\"bookingFrm\"]/table/tbody/tr[4]/td/div/div[1]/div/div[3]/div/ul/li[17]").click()

            driver.find_element(By.XPATH, "//*[@id=\"reservationInput\"]/div/div[3]/a[2]").click()
            time.sleep(0.5)
            driver.find_element(By.XPATH, "//*[@id=\"reservationMessage\"]/div/div[3]/a[1]").click()
    try:
        driver.find_element(By.CLASS_NAME, "month-next").click()
    except:
        break
    else:
        continue
