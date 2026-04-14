import requests
from bs4 import BeautifulSoup

# URL BBC.
url = "https://www.bbc.com/portuguese"

# Faz a requisição HTTP
response = requests.get(url)

# Cria o objeto BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Encontra os títulos das notícias (nesse caso, tags <h3>)
titulos = soup.find_all("h3")

print("Manchetes encontradas:\n")
for i, titulo in enumerate(titulos[:5], start=1):  # 5 primeiros titulos h3 do jornal
    print(f"{i}. {titulo.get_text(strip=True)}")



