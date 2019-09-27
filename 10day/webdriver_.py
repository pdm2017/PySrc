#import datetime
#from datetime import datetime
#from datetime import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
path = "C:/PySrc/__tools/chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get('https://news.naver.com/main/read.nhn?mode=LPOD&mid=sec&oid=001&aid=0010712114&isYeonhapFlash=Y&rc=N')
html = driver.page_source
#soup = BeautifulSoup(html,features="lxml")
WebE = '''return document.getElementsByClassName('media_end_head_autosummary_button _toggle_btn nclicks(sum_summary)')[0].click();'''
print(WebE)
res = driver.execute_script(WebE)
print(res)
#print(driver.execute_script('window.__jindo2_callback._8881()'))
driver.execute_script("window.__jindo2_callback._8881()").click()
#soup2 = soup.find_all('div', {"class": "_contents_body"})

#for i in soup2:
   # list_of_titles_daum[i.text] = i.get('href')
#    print(i.text)
    #print(i.get('href'))

print("___________________________________________")
