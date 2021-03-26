from bs4 import BeautifulSoup
from urllib import request
import urllib
import time


def take_class(class_name):
    from bs4 import BeautifulSoup
    from urllib import request
    import urllib
    import time
    class_name = urllib.parse.quote(class_name)
    # urllib.parse.quote 將中文加密成url
    # 其中的parse因為python所以將上去
    # 網路上的都是 urllib.quote
    url = 'https://tw.stock.yahoo.com/h/kimosel.php?tse=1&cat={}&form=pfnew&form_id=id[0]&form_name=name[0]&domain=1'.format(
        class_name)
    response = request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    all_stock = soup.find_all(class_='none')
    stocks_list = []
    for num, stock in enumerate(all_stock):
        stocks_list.append(stock.string.strip())
    puzzle_all = []
    puzzle_name = ''
    for i in stocks_list:
        for j in i:
            if j == ' ':
                break
            puzzle_name += j
        puzzle_all.append(puzzle_name)
        puzzle_name = ''
    time.sleep(5)
    return puzzle_all


def pick_class():
    from bs4 import BeautifulSoup
    from urllib import request
    url = 'https://tw.stock.yahoo.com/h/kimosel.php?tse=1&cat=%E6%B1%BD%E8%BB%8A&form=pfnew&form_id=id[0]&form_name=name[0]&domain=1'
    response = request.urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')
    classes = soup.find_all(class_='c3')
    save_class = []
    for num, i in enumerate(classes):
        if num == 0:
            continue
        elif num == 28:
            break
        elif i.string == '上櫃':
            continue
        save_class.append(i.string)
    return save_class


sep_stocks = {i: take_class(i) for i in pick_class()}
