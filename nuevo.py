import requests
from bs4 import BeautifulSoup
import pandas as pd

def run():
    url = "https://www.elsotano.com/"
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            break
        else:
            print(f"Error: {response.status_code}")

    generos_enlace = {}
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    contenedor = soup.find('ul',class_="materias")
    generos = contenedor.find_all('a')
    
    data_titulos = []
    data_generos = []
    data_valoracion = []
    data_precio = []
    data_editorial = []
    data_año_edicion = []
    data_ISBN = []
    data_paginas = []
    data_encuadernacion = []
    
    
    for genero in generos:
        generos_enlace[genero.text] = genero['href']
    
    y = 0
    for genero, enlace in generos_enlace.items():
        if(y == 1):
            break
        while True:
            response_genero = requests.get(url + enlace)
            if response_genero.status_code == 200:
                break
            else:
                print(response_genero.status_code)

        html_content = response_genero.text
        soup2 = BeautifulSoup(html_content,'html.parser')
        
        libros = soup2.find_all('div',class_="so-frontcover")
        enlaces_libros = []
        
        for libro in libros:
            enlaces = libro.find_all('a')
            info = enlaces[0]
            #print(info)
            if(info['href'][1:9] != "producto"):
                enlaces_libros.append(url+info['href'])
            print(url+info['href'])
        x = 0
        for enlace_libro in enlaces_libros:
            if(x == 1):
                break
            while True:
                response_subpagina = requests.get(enlace_libro)
                if response_subpagina.status_code == 200:
                    break
                else:
                    print(enlace_libro)
                    print(response_subpagina.status_code)

            html_content = response_subpagina.text
            libro_soup = BeautifulSoup(html_content, 'html.parser')
            data_precio.append(libro_soup.find('div',class_="so-postbookcontent precioDetalle").find('ins').text)
            data_titulos.append(libro_soup.find('h3',id = "titulo").text)
            print(libro_soup.find('h3',id = "titulo").text)
            data_generos.append(genero)
            data_valoracion.append(len(libro_soup.find_all('i',class_="fas fa-star active")))
            detalles = libro_soup.find('ul', class_="so-productinfo").find_all('li')
            detalles_libro = []

            for info_libro in detalles:
                detalles_libro.append(info_libro.find_all('span')[1].text)
            
            data_editorial.append(detalles_libro[0])
            data_año_edicion.append(detalles_libro[1])
            data_ISBN.append(detalles_libro[3])
            data_paginas.append(detalles_libro[4])
            data_encuadernacion.append(detalles_libro[5])
            x += 1
        y +=1    
    data = {}
    
    data["ISBN"] = data_ISBN
    data["Titulo"] = data_titulos
    data["Genero"] = data_generos
    data["Precio"] = data_precio
    data["Valoracino"] = data_valoracion
    data["Paginas"] = data_paginas
    data["Año edicion"] = data_año_edicion
    data["Encuadernacion"] = data_encuadernacion
    
    df = pd.DataFrame(data)
    df.to_csv("Data.csv")
    
    
if __name__ == '__main__':
    run()