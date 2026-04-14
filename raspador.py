import requests
from bs4 import BeautifulSoup

def raspador_bbc():
    url = "https://www.bbc.com/portuguese"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    titulos = soup.find_all("h3")
    print("\nManchetes da BBC:\n")
    for i, titulo in enumerate(titulos[:5], start=1):
        print(f"{i}. {titulo.get_text(strip=True)}")

def raspador_estadao():
    url = "https://www.estadao.com.br/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    titulos = soup.find_all("h3")
    print("\nManchetes do Estadão:\n")
    for i, titulo in enumerate(titulos[:5], start=1):
        print(f"{i}. {titulo.get_text(strip=True)}")

# Programa principal
if __name__ == "__main__":
    raspador_bbc()
    raspador_estadao()




