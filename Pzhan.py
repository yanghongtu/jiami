import requests
import re
from bs4 import BeautifulSoup
import os


def save_file(my_url, filePath, referer):
    header = {
        'Referer': 'https://www.pixiv.net/member_illust.php?mode=manga&illust_id=75452679',
        'Sec-Fetch-Mode': 'no-cors',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
    }
    header['Referer'] = referer
    file_content = requests.get(my_url, headers=header).content
    f = open(filePath, 'wb')
    f.write(file_content)
    f.close()
    print(filePath+" download finish")


def find_last(string, find_str):
    last_position = -1
    while True:
        position = string.find(find_str, last_position+1)
        if position == -1:
            return last_position
        last_position = position


def save_weburl(string, localpath, referer):
    tempFImFileName = string[find_last(string, "/") + 1:]
    save_file(string, localpath + "/" + tempFImFileName, referer)


def get_main_pic(main_url, local_path):
    header={
        'authority': 'www.pixiv.net',
        'method': 'GET',
        'path': '/member_illust.php?mode=manga&illust_id=75452679',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip,deflate,br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
    }
    proxies = {
        'http': '127.0.0.1:44235',
        'https': '127.0.0.1:44235'
    }
    last_index = find_last(main_url, '/')
    header['path'] = main_url[last_index:]
    # print(header['path'])
    main_page = requests.get(main_url, headers=header, proxies=proxies).text
    main_page = main_page.replace("\/", "/")
    main_scripts = BeautifulSoup(main_page, "html.parser").find("section", class_="manga").find_all("script")
    # print(main_scripts)
    for im in main_scripts:
        imgs = re.findall("\"(http.*?\.jpg)\"", str(im))
        for img in imgs:
            if ("square" not in img):
                save_weburl(img, local_path,main_url)


def get_manga_medium(medium_url):
    header = {
        'authority': 'www.pixiv.net',
        'method': 'GET',
        'path': '/member_illust.php?mode=medium&illust_id=75452679',
        'scheme': 'https',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1'
        # 'cookie': 'first_visit_datetime_pc=2019-08-10+11%3A32%3A45; p_ab_id=0; p_ab_id_2=4; p_ab_d_id=261901071; __utmc=235335808; __utmz=235335808.1565404380.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); login_bc=1; _ga=GA1.2.191834094.1565404380; _gid=GA1.2.1389252435.1565404400; device_token=1968aa321bad13b8af1f5760ad90d38c; privacy_policy_agreement=1; c_type=28; a_type=0; b_type=1; module_orders_mypage=%5B%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; is_sensei_service_user=1; yuid_b=IhUZkVQ; login_ever=yes; ki_t=1565404503115%3B1565404503115%3B1565404503115%3B1%3B1; ki_r=; limited_ads=%7B%22responsive%22%3A%22%22%7D; __gads=ID=86ae8dfa57f033e2:T=1565404559:S=ALNI_MZJDjS21K_cf2LzQ2lZak3X2nalbA; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=39849687=1^9=p_ab_id=0=1^10=p_ab_id_2=4=1^11=lang=en=1; OX_plg=pm'
    }
    header['path'] = medium_url[find_last(medium_url, '\\'):]
    proxies = {
        'http': '127.0.0.1:44235',
        'https': '127.0.0.1:44235'

    }
    respone = requests.get(medium_url, headers=header, proxies=proxies)
    dom = BeautifulSoup(respone.text, "html.parser")
    # main_img = dom.find_all("div", class_="img-container")
    # main_url = "https://www.pixiv.net/" + main_img[0].a.attrs["href"]
    # print(main_url)
    ul = dom.find_all("section", class_="works")[0].ul
    lis = ul.find_all("li")
    # print(lis)
    result = []
    for i in lis:
        # print(i)
        medium = i.a.attrs["href"]
        result.append(medium.replace("medium", "manga"))
    print(result)
    return result



url = "https://www.pixiv.net/member_illust.php?mode=medium&illust_id=75452679"
login_url = "https://accounts.pixiv.net/login"

file_root_path = r"/home/yang/Downloads/test"
# 访问数据之前  先创建一个文件夹保存
if not os.path.exists(file_root_path):
    os.mkdir(file_root_path)
os.chdir(file_root_path)
all_url = []

is_any_data = True

while is_any_data:
    is_any_data = False
    for i in get_manga_medium(url):
        if i not in all_url:
            get_main_pic("https://www.pixiv.net"+i, file_root_path)
            all_url.append(i)
            is_any_data = True


print("all finish!")






