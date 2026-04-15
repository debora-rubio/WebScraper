import requests
from bs4 import BeautifulSoup

class Raspador:
    def __init__(self, nome, url):                 # contrutor da classe, executa objeto criado (url jornal). 
        self.nome = nome                           # atributos da classe, nome dos jornais e url para acessar as manchetes.
        self.url = url

    def coletar_manchetes(self, limite=5):         # método para coletar as manchetes, limite de 5 manchetes por jornal.
        print(f"\nManchetes do {self.nome}:\n")    
        try:                                       # avisa se der erro ao acessar o site do jornal.
            response = requests.get(self.url)      # baixa o html do site do jornal.
            soup = BeautifulSoup(response.text, "html.parser")  # interpreta o html usando o beautifulsoup.
            titulos = soup.find_all("h3")          # h3 é a tag dos titulos das manchetes.
            for i, titulo in enumerate(titulos[:limite], start=1):    # exibe as manchetes a partir da primeira.
                print(f"{i}. {titulo.get_text(strip=True)}")    # removendo espaços em branco (get_text(strip=True)).
        except Exception as e:
            print(f"Erro ao acessar {self.nome}: {e}")   # retorna erro se o site estiver fora do ar, ou alteração na estrutura do site.

                                                     # Programa principal
if __name__ == "__main__":
                                                     # Criando objetos para cada jornal
    bbc = Raspador("BBC", "https://www.bbc.com/portuguese")
    estadao = Raspador("Estadão", "https://www.estadao.com.br/")

                                                     # Chamando o método para coletar manchetes
    bbc.coletar_manchetes()
    estadao.coletar_manchetes()





