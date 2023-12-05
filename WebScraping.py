import requests
from bs4 import BeautifulSoup
import scrapy
import pandas as pd

def run():
    url = "https://www.amazon.com.mx/gp/bestsellers/books?rw_useCurrentProtocol=1&ref_=amb_link_xhe_VErHQXG8_y9k-eSzJA_1"
    
    while(True):
        response = requests.get(url)
        if response.status_code == 200:
            break
        else:
            print(f"Error: {response.status_code}")

    html_content = response.text
    #print(html_content)
    soup = BeautifulSoup(html_content, 'lxml')
    page = soup.find('div', id ="a-page")
    contenedor = page.find('div',class_="a-column a-span12 apb-browse-left-nav apb-browse-col-pad-right")
    print(contenedor)
    
    
    #categorias = contenedor.find_all('div')
    #for i in categorias:
    #    print("\n\n\n")
    #    e = i.find_all('div')
    #    for a in e:
    #        print("\n")
    #        print(a)
    #a = categorias.find('div',class_="a-section a-spacing-none apb-browse-refinements")
    #print(a)
if __name__ == '__main__':
    run()