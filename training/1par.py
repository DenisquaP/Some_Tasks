from bs4 import BeautifulSoup
import requests
import csv


def parcer(soup, title):
    # Цикл по всем товарам на странице
    for i in soup.find_all(class_='views-row col-12 col-sm-4'):
        link = i.find(class_='views-field views-field-name-i18n').find(class_="field-content").find("a").get('href')  # noqa 501
        url_page = requests.get('https://rusgroupp.ru/' + link)
        soup2 = BeautifulSoup(url_page.text, 'lxml')

        label = soup2.find_all(class_='form-group row align-items-center')  # noqa 501
        text = soup2.find_all(class_='form-group row align-items-center')  # noqa 501
        info = ''
        id = ' '.join(soup2.find(class_='page_title').text.split())
        price = ' '.join(soup2.find(class_='price').find('span').text.split())  # noqa 501
        description = soup2.find(class_='fullContent col-12').find_all('p')
        description = ' '.join([i.text for i in description[:-1]])
        description = description.replace('\n', ' ')
        links = soup2.find(class_='row').find_all('a')
        photos = ''
        # Достаю ссылки на картинки товара
        for i in links:
            link = i.get('href')
            template = 'assets/images/products'
            if isinstance(link, str) and template in link:
                photos += 'https://rusgroupp.ru' + i.get('href') + ' '

        # Достаю характеристики, 2 переменные так как они в таблице
        for lab, t in zip(label, text):
            lab = lab.find(class_='_title').text
            t = ' '.join(t.find('div').text.split())
            info += lab + t + ' '

        # ну и запись в файл
        with open(f'{title}.csv', 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow((id, price, description, info, photos))

    # Возвращает ссылку на следующую страницу
    return soup.find_all(class_='page-item')[-2].find('a')['href']


urls = [
    'https://rusgroupp.ru/store/promyishlennyie-sistemyi-ohlazhdeniya/',
    'https://rusgroupp.ru/store/kompressornoe-oborudovanie/',
    'https://rusgroupp.ru/store/podgotovka-szhatogo-vozduha/',
    'https://rusgroupp.ru/store/promyshlennye-nasosy/',
    'https://rusgroupp.ru/store/ustanovki-vozduhorazdeleniya/'
]

# Проходим по всем нужным разделам
for i in range(len(urls)):
    url = requests.get(urls[i])

    soup = BeautifulSoup(url.text, 'lxml')

    title = soup.find(class_='page_title').text.split()
    title = '_'.join(title)

    with open(f'{title}.csv', 'w', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(('Название', 'Цена', 'Описание', 'Характеристики', 'Фото'))  # noqa 501

    while 1:
        # Цикл для перехода к следующей странице
        # Парсинг и запись в файл внутри функции
        new_link = parcer(soup, title)
        if new_link != '#':
            new_page = requests.get('https://rusgroupp.ru/' + new_link)
            soup = BeautifulSoup(new_page.text, 'lxml')
        else:
            break
