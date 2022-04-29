from dotenv import load_dotenv
load_dotenv()
import requests
import os
from urllib.parse import urlparse
import argparse


def shorten_link(request_headers, long_url):
    payload = {
        'long_url': long_url
    }
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(url, headers=request_headers, json=payload)
    response.raise_for_status()
    return response.json().get('id')


def count_clicks(request_headers, bitlink):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(url, headers=request_headers)
    response.raise_for_status()
    return response.json().get('total_clicks')


def is_bitlink(request_headers, bitlink):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    response = requests.get(url, headers=request_headers)
    return response.ok


def check_url_accessibility(input_url):
    response = requests.get(input_url)
    response.raise_for_status()


def main():
    parser = argparse.ArgumentParser(description='Программа создает короткие ссылки')
   # parser.parse_args()
    parser.add_argument('url', help='Ваше ссылка')
    args = parser.parse_args()
    token = os.getenv('TOKEN_BITLY')
    request_headers = {
        'Authorization': f'Bearer {token}'
    }
    input_url = args.url
    url_parsed = urlparse(input_url)
    url_without_protocol = url_parsed.netloc + url_parsed.path
    try:
        check_url_accessibility(input_url)
        if is_bitlink(request_headers, url_without_protocol):
            counter = count_clicks(request_headers, url_without_protocol)
            print('Счетчик:', counter)
        else:
            bitlink = shorten_link(request_headers, input_url)
            print('Битлинк:', bitlink)
    except requests.exceptions.HTTPError:
        print ('Ошибка ответа сервера')
    except requests.exceptions.ConnectionError:
        print ('Нет ответа от сервера  или сервер не существует')
    except requests.exceptions.MissingSchema:
        print ('В адресе не указан http:// или https://')
    except requests.exceptions.InvalidURL:
        print ('В адресе не указан сервер')          

if __name__ == '__main__':
    main()
