from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd

START = 26000
END = 27000

options = Options()
options.add_experimental_option('prefs',{'profile.default_content_setting_values.notifications':1})

driver = "./chromedriver"
browser = webdriver.Chrome(executable_path=driver, chrome_options=options)

result = []

pageNum = START
while pageNum < END:
    url = "https://linkareer.com/cover-letter/" + str(pageNum) + "?page=1&sort=PASSED_AT&tab=all"
    browser.get(url)
    browser.implicitly_wait(3)  # 3초 대기

    try:
        idx = pageNum - START
        field = browser.find_element(By.XPATH,
                                     '// *[ @ id = "__next"] / div[1] / div[3] / div / div[2] / div / div[2] / '
                                     'div[1] / div / div / div[2] / h1').text
        spec = browser.find_element(By.XPATH,
                                    '//*[@id="__next"]/div[1]/div[3]/div/div[2]/'
                                    'div/div[2]/div[1]/div/div/div[3]/p').text
        content = browser.find_element(By.XPATH, '//*[@id="coverLetterContent"]').text
        result.append([idx, field, spec, content])

    except:
        print("err")

    pageNum += 1

dataset = pd.DataFrame(result)
dataset.columns = ['번호', '분야', '스펙', '내용']
dataset.to_csv('자소서크롤링5.csv')
