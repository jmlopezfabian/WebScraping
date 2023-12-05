from bs4 import BeautifulSoup
import requests

url = 'https://latam.casadellibro.com/libros/literatura/121000000'
response = requests.get(url)

#Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener el contenido HTML de la respuesta
    html_content = response.text
    #print(html_content)
else:
    # Imprimir un mensaje de error si la solicitud no fue exitosa
    print(f"Error: {response.status_code}")

#Crear un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(html_content, 'html.parser')
#book_section = soup.find("div", class_="grid-view mt-4")

libros = soup.find_all('div', class_="compact-product")
print(libros)

#print(book_section)

#for book in book_section:
#    info_book = book.find("div", class_="compact-product")
#    print(info_book)
#
