import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

list1 = ['피카츄', '파이리', '꼬부기', '이상해씨', '잠만보', '푸린', '이브이', '치코리타']
dict1 = {"피카츄":('아이유', '걸스데이 유라', '워너원 강다니엘'),
        "파이리":('트와이스 다현', '슈퍼주니어 동해', '구구단 김세정'),
        "꼬부기":('트와이스 나연','마마무 솔라','레드벨벳 예리', '브레이브걸스 유정', '하연수', '샤이니 민호'),
        "이상해씨":('트와이스 정연', '양세형', '여자친구 엄지'),
        "잠만보":('유민상', '김신영','문세윤', '홍윤화'),
        "푸린":('AOA 초아', '트와이스 지효', '여자친구 은하'),
        "이브이":('트와이스 쯔위', 'bts 뷔', '오마이걸 유이', '비투비 육성재'),
        "치코리타":('레드벨벳 아이린', '트와이스 채영', 'exid 정화', 'bts 정국')}

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("https://www.google.com/webhp?sa=X&hl=ko&output=search&tbm=isch&tbo=u&ved=0ahUKEwibpLqQma_2AhW4slYBHRb9AeIQ0tQDCBAoAQ")

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WoW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

for poketmon in list1:
    for person in dict1[poketmon]:
        elem = driver.find_element_by_name("q")
        elem.clear();
        elem.send_keys(person)
        elem.send_keys(Keys.RETURN)

        SCROLL_PAUSE_SEC = 2

        # 스크롤 높이 가져옴
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # 끝까지 스크롤 다운
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 2초 대기
            time.sleep(SCROLL_PAUSE_SEC)

            # 스크롤 다운 후 스크롤 높이 다시 가져옴
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                try:
                    driver.find_element_by_css_selector(".mye4qd").click()
                except:
                    break
            last_height = new_height


        images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
        count = 1
        for image in images:
            try:
                image.click()
                time.sleep(1)
                imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")
                if not os.path.exists(os.getcwd() + "/img/" + str(poketmon) + "/" + str(person)):
                   os.mkdir(os.getcwd() + "/img/" + str(poketmon) + "/" + str(person)) 
                imgName = os.getcwd() + "/img/" + str(poketmon) + "/" + str(person) + "/" + str(count) + ".jpg"
                urllib.request.urlretrieve(imgUrl, imgName)
                count = count + 1
                if count > 100 :
                    break                
            except:
                pass
            
driver.close()
