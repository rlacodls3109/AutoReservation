#에러 날 경우 크롬드라이버 버전 확인

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def inputText(nameID,text):
    name = driver.find_element(By.ID, nameID)
    name.send_keys(text)
    name.send_keys(Keys.RETURN)

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

#로그인
driver.get('https://fms.friendsscreen.kr/account')

driver.find_element(By.CLASS_NAME,"login-btn").click()
try:
    driver.find_element(By.CLASS_NAME,"common-pop-cancel").click()
except:
    print("정산완료")

driver.find_element(By.XPATH,"//*[@id=\"wrapper\"]/ul/li[2]/a").click()

driver.find_element(By.CLASS_NAME, "date-ico").click()
time.sleep(0.3)
driver.find_element(By.CLASS_NAME, "ui-datepicker-next").click()
#날짜선택반복
for i in range(1,7):
   for j in range(1,8):

        try:
            date = driver.find_element(By.XPATH, f"//*[@id=\"ui-datepicker-div\"]/table/tbody/tr[{i}]/td[{j}]/a")

        except:
            print("날짜없음")

        else :
            date.click()
            time.sleep(0.5)
            # 1~23 타석 예약하는 코드
            while (1):
                while(1):
                    try:
                        driver.find_element(By.XPATH,
                                            f"// *[ @ id = \"reservationTbl\"] / tbody / tr[50] / td[1]").click()
                    except:
                        break
                    else:
                        time.sleep(0.5)
                        driver.find_element(By.XPATH,
                                            "//*[@id=\"bookingFrm\"]/table/tbody/tr[4]/td/div/div[1]/div/div[2]/b").click()
                        try:
                            driver.find_element(By.XPATH,
                                                "//*[@id=\"bookingFrm\"]/table/tbody/tr[4]/td/div/div[1]/div/div[3]/div/ul/li[18]").click()
                        except:
                            driver.find_element(By.XPATH,
                                                "//*[@id=\"bookingFrm\"]/table/tbody/tr[4]/td/div/div[1]/div/div[3]/div/ul/li[13]").click()
                        inputText("bookingNm", "타석예약")
                        inputText("bookingHp", "031")
                        inputText("managerNm", "김채인")

                        driver.find_element(By.CLASS_NAME, "btn-type-bk").click()
                        time.sleep(0.5)
                        driver.find_element(By.XPATH, "//*[@id=\"reservationMessage\"]/div/div[3]/a[1]").click()
                try:
                    driver.find_element(By.CLASS_NAME, "month-next").click()
                except:
                    driver.find_element(By.CLASS_NAME, "date-ico").click()
                    time.sleep(0.3)
                    break
                else:
                    continue

