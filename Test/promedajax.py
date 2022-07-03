import json
import urllib.request,urllib.error
import re

def main():
    url = "https://promedmail.org/wp-admin/admin-ajax.php"
    askURL(url)

def askURL(url):
    head = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37'
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("gbk")
        print("try")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print("error1")
            print(e.code)
        if hasattr(e, "reason"):
            print("error2")
            print(e.reason)
        return html

if __name__ == "__main__":
    main()