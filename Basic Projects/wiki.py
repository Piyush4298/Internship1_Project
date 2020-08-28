import requests as re
from bs4 import BeautifulSoup


def get_info_table(page):
    dom = BeautifulSoup(page, 'html.parser')
    content = dom.find(id='mw-content-text')
    print(type(content))
    if not content:
        return None
    return content.find('table', class_='infobox')


def load_page(query):
    url = 'https://en.wikipedia.org/wiki/' \
          + query
    page = re.get(url)
    if page.status_code != 200:
        return None
    return page.content


def parse_info_table(table):
    info = {}
    rows = table.find_all('tr')
    if not rows:
        return None
    for row in rows:
        head = row.find('th')
        if not head:
            continue
        data = row.find('td')
        if not data:
            continue
        info[head.text] = data.text
    return info


query = input("Enter the query: ")
page = load_page(query)
if not page:
    print('Page not found ')
    quit()

info_table = get_info_table(page)
print(type(info_table))
req_dict = parse_info_table(info_table)
if not req_dict:
    print('data not found')
    quit()

for head, data in req_dict.items():
    print('{0}: {1}'.format(head, data))
