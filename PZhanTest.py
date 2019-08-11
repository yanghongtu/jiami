import requests

header = {
    'Referer': 'https://accounts.pixiv.net/login',
    'Sec-Fetch-Mode': 'no-cors',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
}
proxies = {
    'http': '127.0.0.1:44235',
    'https': '127.0.0.1:44235'
}
