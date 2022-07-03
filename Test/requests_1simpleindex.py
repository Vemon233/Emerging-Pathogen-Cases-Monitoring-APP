import requests
#1指定url
url = 'https://promedmail.org/promed-post/?id=20211008.8698907'
#2发起请求
response = requests.get(url=url)
#3获取响应数据
page_text = response.text
#4存储
with open('./promedtest.html','w',encoding='utf-8') as fp:
    fp.write(page_text)
print('完成！！！')
