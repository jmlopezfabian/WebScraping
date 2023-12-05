import requests
from bs4 import BeautifulSoup

url = "https://www.elsotano.com/libro/lenguaje-de-los-caballos-el-las-aventuras-y-sabiduria-de-uno-de-los-jinetes-mas-reconocidos-de-america_10543617"

response = requests.get(url)

html_content = response.text

soup = BeautifulSoup(html_content,'html.parser')
detalles = soup.find('ul', class_="so-productinfo").find_all('li')

detalles_libro = []

for info_libro in detalles:
    detalles_libro.append(info_libro.find_all('span')[1].text)

for i in detalles_libro:
    print(i)

editorial = i[0].text
año = i[1].text
