import requests
from bs4 import BeautifulSoup

def run():
    url = "https://latam.casadellibro.com/"
    
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            break
        else:
            print(f"Error: {response.status_code}")

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')  
    menu = soup.find('div', class_="inline-menu")
    categorias = menu.find_all('div', class_='link-menu')
    links_generos = []
    
    for categoria in categorias:
        nombre_categoria = categoria.text.strip()
        print(f"\n\nCategoria: {nombre_categoria}")
        if((nombre_categoria in ['Entrega inmediata','Imprescindibles','eBooks'])):
            continue
        else:
            enlaces = categoria.find_all('a')
            for enlace in enlaces:
                links_generos.append(enlace['href'])
                #print("Texto del enlace:")
                #print(enlace.text.strip())  # Obtén el texto del enlace y usa strip() para eliminar espacios en blanco
            print("="*40)
        
    for i in links_generos:
        print(i)
if __name__ == '__main__':
    run()