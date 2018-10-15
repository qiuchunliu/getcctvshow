# 获取CCTV的每个频道的栏目

import requests
from bs4 import BeautifulSoup

# url = 'http://tv.cctv.com/zhuchiren/'


def get_htsoup(url):
    ht = requests.get(url)
    ht.encoding = ht.apparent_encoding
    hts = BeautifulSoup(ht.text, 'html.parser')
    return hts


def get_eachtv(soup):
    eachtv = []
    for i in range(1, 16):
        idvl = 'bottom_{}'.format(i)
        eachtv.append(soup.find_all('div', id=idvl)[0])
    return eachtv


def get_ectvna(tag_list):
    echtvna = []
    for i in tag_list:
        echtvna.append(i.get('lang'))
    return echtvna


def get_tvshows(tag_lis):
    all_show = []
    show_dic = {}
    for td in tag_lis:
        show_name = []
        show_link = []
        for name in td.find_all('td'):
            show_name.append(name.text)
            show_link.append(name.a.get('href'))
            show_dic = dict(zip(show_name, show_link))
        all_show.append(show_dic)
    return all_show


def main():
    url = 'http://tv.cctv.com/zhuchiren/'
    get_soup = get_htsoup(url)
    eachtv = get_eachtv(get_soup)
    eachtvname = get_ectvna(eachtv)
    tvshows = get_tvshows(eachtv)
    result = {}
    for i in range(15):
        result[eachtvname[i]] = tvshows[i]
    return result


if __name__ == '__main__':
    dicc = main()
    for ii in dicc:
        print(ii, dicc[ii])
