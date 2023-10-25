from selenium import webdriver
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
import requests
import json
from kakao_token import refresh_tk

# ChromeDriverManager().install()
class Kakao():
    def __init__(self):
        try:
            self.kind_of_news = int(input('보고싶은 뉴스 주제를 입력해주세요\n정치 : 1, 경제 : 2, 사회 : 3, 생활/문화 : 4, IT/과학 : 5, 세계 : 6\n'))
        except ValueError:
            print('아무것도 입력받지 못했거나 잘못된 값을 받았습니다.')
            return
        if self.kind_of_news not in [1,2,3,4,5,6]:
            print('잘못된 값을 받았습니다.')
            return
        self.pipeline(self.kind_of_news)



    def pipeline(self,x = 5):
        self.browser = webdriver.Chrome()
        self.browser.get("https://news.naver.com")
        self.browser.find_element(By.XPATH, f'/html/body/section/header/div[2]/div/div/div/div/div/ul/li[{x+1}]/a').click()
        self.browser.find_element(By.CLASS_NAME, "cluster_more_inner").click()
        self.li1 = self.browser.find_elements(By.CLASS_NAME, "sh_item")
        self.title = []
        self.lnk = []
        for news in self.li1:
            self.title.append(news.find_element(By.CLASS_NAME, 'sh_text_headline').text)
            self.lnk.append(news.find_element(By.CLASS_NAME, 'sh_text_headline').get_attribute('href'))

        self.data = {
            'len' : len(self.title),
            'self.title' : self.title,
            'link' : self.lnk
        }

        self.msg = ''
        for i in range(self.data['len']):
            self.msg = self.msg + f'{self.title[i]}\n\n'

        refresh_tk()

        with open('./src/kakaopipeline/kakao_token.json', 'r') as fp:
            self.tokens = json.load(fp)

        self.url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

        self.headers={
            "Authorization" : "Bearer " + self.tokens["access_token"]
        }

        self.data = {
            'object_type': 'text',
            'text': self.msg,
            'link': {
                'web_self.url': 'https://developers.kakao.com',
                'mobile_web_self.url': 'https://developers.kakao.com'
            },
            'button_self.title': '뉴스 바로가기'
        }
        
        self.data = {'template_object': json.dumps(self.data)}
        requests.post(self.url, headers=self.headers, data=self.data)

    