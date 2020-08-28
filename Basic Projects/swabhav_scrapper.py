import requests
from bs4 import BeautifulSoup


def load_st(query):
    url = 'https://swabhavtechlabs.com/' \
          + query + '.html'
    print(url)
    page = requests.get(url)
    if page.status_code != 200:
        print('Error')
    return page.content


def about_swabhav_techlabs():
    query = 'about-techlabs'
    page = load_st(query)
    if not page:
        print('Page not found')
    dom = BeautifulSoup(page, 'html.parser')
    if not dom:
        print('error in bs4')
    content = dom.find(id='content ')
    if not content:
        print('Error')
    lst = content.find(class_='col-md-7').find_all('p')
    if not lst:
        return None
    return lst


ab = about_swabhav_techlabs()
if not ab:
    print('Not found')
else:
    for i in ab:
        print(i.text)
