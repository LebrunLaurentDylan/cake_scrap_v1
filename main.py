from bs4 import BeautifulSoup
import requests

# lecture des données html en ligne pour le test IRL
url = "https://codeavecjonathan.com/res/site_recette/recette.html"

# lecture des données html sur local pour le dev
'''f = open("recette.html", "r")
html_content = f.read()
f.close()'''

response = requests.get(url)
response.encoding = "utf-8"
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

titre_h1 = soup.find("h1")  # class_="description"
text_titre = titre_h1.text
description_paragraphe = soup.find("p", class_="description")
description = description_paragraphe.text
div_info = soup.find("div", class_="info")
img_info = div_info.find("img")
print("\ntitre de la page html:", text_titre)
print("\ndescription:", description)
print("\nle src de l'image est :", img_info["src"])

table_info = soup.find("table", class_="info")
table_info_tr = table_info.find_all("tr")
table_info_headers = table_info_tr[0].find_all("th")
table_info_datas = table_info_tr[1].find_all("td")
print("\nInformations:\n")
for i in range(len(table_info_headers)):
    print("   ", table_info_headers[i].text, ":", table_info_datas[i].text)

ingredient_list = soup.find("div", class_="ingredients")
ingredients = ingredient_list.find_all("p")
print("\nIngrédients:\n")
for i in ingredients:
    print("   ",i.text)

# <table class="preparation">
# <tr><td><p class="numero">1</p></td><td class="preparation_etape">Faire fondre le chocolat avec le beurre</td></tr>
cooking_steps = soup.find("table", class_="preparation")
steps = cooking_steps.find_all("td", class_="preparation_etape")

print("\nEtapes de Préparation:\n")
for i in range(len(steps)):
    print("   ", i+1, " - ", steps[i].text)


"""list_div_centre = soup.find_all("div", class_="centre")
if list_div_centre and len(list_div_centre) >= 2:
    paragraphe_description = list_div_centre[1].find("p", class_="description")
print("titre de la page html:", text_titre)
if paragraphe_description:
    print("description:", paragraphe_description.text)"""



