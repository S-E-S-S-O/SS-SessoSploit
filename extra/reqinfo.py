import requests
from requests.exceptions import RequestException

def op():
    try:
        link = input('Link: ')
        req = requests.get(link)
        output = {
            'url': req.url,
            'status': req, 
            'encoding': req.encoding,
            'raw': req.raw
        }
        print("Here the datas:\n")
        print(output)
        option = input('Show the finerprint? (text and content) y/n\n')
        if option == "y" or "Y":
            print(req.text, req.content)
        else:
            return
    except RequestException:
        print("[!] ERROR: you are retarded")
