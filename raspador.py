import requests
from bs4 import BeautifulSoup

# URL de exemplo (pode ser qualquer site de notícias ou blog)
url = "https://www.bbc.com/portuguese"

# Faz a requisição HTTP
response = requests.get(url)

# Cria o objeto BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Encontra os títulos das notícias (nesse caso, tags <h3>)
titulos = soup.find_all("h3")

print("Manchetes encontradas:\n")
for i, titulo in enumerate(titulos[:10], start=1):  # mostra só 10 para não ficar enorme
    print(f"{i}. {titulo.get_text(strip=True)}")



