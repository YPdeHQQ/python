import requests
def get_page(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
    }
    datd = {
        
    }
    session = requests.session()

    response = session.post(url,headers=headers,data=data)