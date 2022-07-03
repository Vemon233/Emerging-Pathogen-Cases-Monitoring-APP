import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
}
url = 'https://promedmail.org/promed-post/?id=20211008.8698907'

response = requests.get(url=url,headers=headers)

page_text = response.text

with open('aaa.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print("完成2！！！")
