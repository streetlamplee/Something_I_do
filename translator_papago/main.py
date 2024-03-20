from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium import webdriver
from selenium.webdriver.common.by import By
import time



parsing_dict = {'한국어' : 2,
                '영어' : 3,
                '일본어' : 4,
                '중국어(간체)' : 5,
                '중국어(번체)' : 6,
                '스페인어' : 7,
                '프랑스어' : 8,
                '독일어' : 9,
                '러시아어' : 10,
                '포르투갈어' : 11,
                '이탈리아어' : 12,
                '베트남어' : 13,
                '태국어' : 14,
                '인도네시아어' : 15,
                '힌디어' : 16,
                '아랍어' : 17}

src = '한국어'
dest = '영어'
with open("translation.txt", 'r', encoding = 'utf-8') as f:
    inp = f.readlines()
output_li = []
browser = webdriver.Chrome()
browser.get("https://papago.naver.com/")
time.sleep(2)
browser.find_element(By.XPATH, f'/html/body/div/div/div[1]/section/div/div[1]/div[2]/div/div[2]/div[1]/div/div[1]/button[2]/span').click()
browser.find_element(By.XPATH, f'/html/body/div/div/div[1]/section/div/div[1]/div[2]/div/div[2]/div[1]/div/div[2]/ul/li[{parsing_dict[src]}]').click()
browser.find_element(By.XPATH, f'/html/body/div/div/div[1]/section/div/div[1]/div[3]/div/div[1]/div/div/div[1]/button[2]/span').click()
browser.find_element(By.XPATH, f'/html/body/div/div/div[1]/section/div/div[1]/div[3]/div/div[1]/div/div/div[2]/ul/li[{parsing_dict[dest] - 1}]').click()
for idx, value in enumerate(inp):
    browser.find_element(By.XPATH, f'/html/body/div/div/div[1]/section/div/div[1]/div[2]/div/div[3]/label/textarea').click()
    browser.find_element(By.XPATH, f'/html/body/div/div/div[1]/section/div/div[1]/div[2]/div/div[3]/label/textarea').send_keys(value.strip())
    time.sleep(3)
    output = browser.find_element(By.XPATH, f'/html/body/div/div/div[1]/section/div/div/div[3]/div/div[5]/div').text
    output_li.append(output)
    browser.find_element(By.XPATH, '/html/body/div/div/div[1]/section/div/div/div[2]/div/div[3]/button').click()
with open('result.txt', 'w') as f:
    for i in range(len(output_li)):
        f.write(output_li[i] + "\n")

