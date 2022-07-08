import requests
from bs4 import BeautifulSoup as bs


def images():
    request = requests.get(f'https://powermens.ru/?modul=catfiles&p=viewfiles&idkatf=32')
    html = bs(request.content, 'lxml')
    b = html.select('.col img')

    for i in range(2, 10):
        request = requests.get(f'https://powermens.ru/?modul=catfiles&p=viewfiles&idkatf=32&n={i}')
        html = bs(request.content, 'lxml')
        a = html.select('.col img')
        b.extend(a)
    with open('image_href.txt', 'a') as f:
        for i in b:
            if not 'PowerMens' in str(i) and not 'Нам 10 лет' in str(i):
                f.write(f'{i.get("alt")}:https://powermens.ru{i.get("src")}\n')
    

def sites():
    request = requests.get(f'https://powermens.ru/?modul=catfiles&p=viewfiles&idkatf=32')
    html = bs(request.content, 'lxml')
    b = html.select('.catfiles-item>h3>a')

    for i in range(2, 10):
        request = requests.get(f'https://powermens.ru/?modul=catfiles&p=viewfiles&idkatf=32&n={i}')
        html = bs(request.content, 'lxml')
        a = html.select('.catfiles-item>h3>a')
        b.extend(a)
    with open('exercise_href.txt', 'a') as f:
        for i in b:
            if not 'PowerMens' in str(i) and not 'Нам 10 лет' in str(i):
                f.write(f'{i.text}:https://powermens.ru{i.get("href")}\n')
    

def get_advices(link=None):
    if link:
        request = requests.get(link)
        html = bs(request.content, 'lxml')
        b = html.select('.desc>ol>li')
        for i, el in enumerate(b):
            print(i+1, el.text)
    else: 
        with open('exercise_advice.txt', 'a') as f:
            for i in [35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 166, 167, 168, 169, 170, 171, 172, 173, 174]:
                request = requests.get(f'https://powermens.ru/?modul=catfiles&p=more&idfile={i}')
                html = bs(request.content, 'lxml')
                b = html.select('.desc>ol>li')
                c = html.select('.desc>b')
                d = []
                for j, el in enumerate(b):
                    d.append(f'{j+1}.{el.text}')
                f.write(f'{c[0].text}:{":".join(d)}\n')
                

def exercise_group():
    request = requests.get(f'https://powermens.ru/?modul=catfiles&p=viewfiles&idkatf=47')
    html = bs(request.content, 'lxml')
    b = html.select('.catfiles-item>h3>a')
    d = html.select('.desc>i')
    request = requests.get(f'https://powermens.ru/?modul=catfiles&p=viewfiles&idkatf=47&n=2')
    html = bs(request.content, 'lxml')
    c = html.select('.catfiles-item>h3>a')
    e = html.select('.desc>i')
    b.extend(c)
    d.extend(e)
    with open('excercise_group.txt', 'a') as f:
        for i, el in enumerate(b):
            f.write(f'{el.text}:{d[i].text}:Ноги\n')

    request = requests.get(f'https://powermens.ru/?modul=catfiles&p=viewfiles&idkatf=46&n=1')
    html = bs(request.content, 'lxml')
    b = html.select('.catfiles-item>h3>a')
    d = html.select('.desc>i')
    request = requests.get(f'https://powermens.ru/?modul=catfiles&p=viewfiles&idkatf=46&n=2')
    html = bs(request.content, 'lxml')
    c = html.select('.catfiles-item>h3>a')
    e = html.select('.desc>i')

    b.extend(c)
    d.extend(e)

    with open('excercise_group.txt', 'a') as f:
        for i, el in enumerate(b):
            f.write(f'{el.text}:{d[i].text}:Спина\n')

    request = requests.get(f'https://powermens.ru/?modul=catfiles&p=viewfiles&idkatf=45')
    html = bs(request.content, 'lxml')
    b = html.select('.catfiles-item>h3>a')
    d = html.select('.desc>i')

    with open('excercise_group.txt', 'a') as f:
        for i, el in enumerate(b):
            f.write(f'{el.text}:{d[i].text}:Дельтовидные мышцы\n')

    request = requests.get(f'https://powermens.ru/?modul=catfiles&p=viewfiles&idkatf=44&n=1')
    html = bs(request.content, 'lxml')
    b = html.select('.catfiles-item>h3>a')
    d = html.select('.desc>i')
    request = requests.get(f'https://powermens.ru/?modul=catfiles&p=viewfiles&idkatf=44&n=2')
    html = bs(request.content, 'lxml')
    c = html.select('.catfiles-item>h3>a')
    e = html.select('.desc>i')

    b.extend(c)
    d.extend(e)

    with open('excercise_group.txt', 'a') as f:
        for i, el in enumerate(b):
            f.write(f'{el.text}:{d[i].text}:Грудь\n')

    request = requests.get(f'https://powermens.ru/?modul=catfiles&p=viewfiles&idkatf=43')
    html = bs(request.content, 'lxml')
    b = html.select('.catfiles-item>h3>a')
    d = html.select('.desc>i')

    with open('excercise_group.txt', 'a') as f:
        for i, el in enumerate(b):
            f.write(f'{el.text}:{d[i].text}:Трапеция\n')

    request = requests.get(f'https://powermens.ru/?modul=catfiles&p=viewfiles&idkatf=34')
    html = bs(request.content, 'lxml')
    b = html.select('.catfiles-item>h3>a')
    d = html.select('.desc>i')

    with open('excercise_group.txt', 'a') as f:
        for i, el in enumerate(b):
            f.write(f'{el.text}:{d[i].text}:Пресс\n')

    request = requests.get(f'https://powermens.ru/?modul=catfiles&p=viewfiles&idkatf=33&n=1')
    html = bs(request.content, 'lxml')
    b = html.select('.catfiles-item>h3>a')
    d = html.select('.desc>i')
    request = requests.get(f'https://powermens.ru/?modul=catfiles&p=viewfiles&idkatf=33&n=2')
    html = bs(request.content, 'lxml')
    c = html.select('.catfiles-item>h3>a')
    e = html.select('.desc>i')

    b.extend(c)
    d.extend(e)

    with open('excercise_group.txt', 'a') as f:
        for i, el in enumerate(b):
            f.write(f'{el.text}:{d[i].text}:Руки\n')    
        

# exercise_group()

for i in range(25):
    with open(f'men_program/program{i+1}.txt', 'w') as f:
        f.write('\n')

