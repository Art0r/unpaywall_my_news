from bs4 import BeautifulSoup
import requests

url = str(input("Url da notícia:\n")) 

# text_div[0] sendo o attr interno que deve ser procurado na tag
# e text_div[1] o valor ao qual deve ser encontrado
# para a div (ou outra tag) que incopora todo o texto da reportagem
text_div = ()

# text_paragraphs[0] sendo o attr interno que deve ser procurado na tag
# e text_paragraphs[1] o valor ao qual deve ser encontrado
# para a tag que incopora o texto do parágrafo correspondente
text_paragraphs = ()

# title[0] sendo o attr interno que dev ser procurado na tag
# e title[1] o valor ao qual deve ser encontrado para a tag
# qye incorpora o texto do titulo correspondente
title = ()

# para cada fonte, text_div e text_paragraphs terão valores específicos
if 'uol.com.br' in url:
    text_div = ("data-metric-area", "texto-noticia")
    text_paragraphs = ("class", "bullet")
    title = ("div", "title-content")

if 'estadao.com.br' in url:
    text_div = ("id", "content")
    text_paragraphs = ("data-component-name", "paragraph")
    title = ("class", "headline")

if 'globo.com' in url:
    text_div = ("class", "protected-content")
    text_paragraphs = ("data-block-type", "unstyled")
    title = ("itemprop", "headline")


res = requests.get(url)

soup = BeautifulSoup(res.content.decode(), "html.parser")

# encontrando a div (ou outra tag) que incorpora todo o texto da reportagem
news = soup.find(lambda tag: False if tag.get(text_div[0]) is None else text_div[1] in tag.get(text_div[0]))

# encontrando todos os parágrafos que estão dentro da div do texto
elements = news.find_all(lambda tag: False if tag.get(text_paragraphs[0]) is None else text_paragraphs[1] in tag.get(text_paragraphs[0]))

# encontrando o titulo da matéria
title_text = soup.find(lambda tag: False if tag.get(title[0]) is None else title[1] in tag.get(title[0])).text

# juntando o texto de todos os parágrafos
text_list = [el.text for el in elements]
text = '\n'.join(text_list)

print(title_text)
print(text)
