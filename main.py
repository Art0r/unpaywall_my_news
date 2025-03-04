from bs4 import BeautifulSoup
import requests

url = "https://www.uol.com.br/esporte/colunas/milly-lacombe/2025/03/03/todo-o-deboche-contido-na-celebracao-a-anora.htm" 

res = requests.get(url)

soup = BeautifulSoup(res.content.decode(), "html.parser")

news = soup.find(lambda tag: tag.get('data-metric-area') == 'texto-noticia')
elements = news.find_all(lambda tag: False if tag.get("class") is None else 'bullet' in tag.get("class"))

text_list = [el.text for el in elements]
text = '\n'.join(text_list)

print(text)
