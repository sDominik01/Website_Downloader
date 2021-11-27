#Importálások
import ctypes
import json, requests
from bs4 import BeautifulSoup

#Ha nem rendszergazda jogosultsággal indul a program akkor elindít magánat egy új cmd-t.
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
#Kiírja az össze parancsot. 
def help():
    print("Parancsok: \n help - Parancsok listázása \n webclone - Honlapok klónozása")

#Kapcsolódás
def hit_it(url):
    """
    ########
    """
    try:
        r = requests.get(url)
    except:
        print('Error 2: Sikertelen kapcsolódás')
        initializer()
    return r
# Összes <a> link lekérése
def get_a(soup, url):
    """
    Összes <a> link
    """
    a_tags = soup.find_all('a')
    print(len(a_tags), "<a> TAGS")
    for _ in a_tags:
        try:
            if _['href'].startswith('/'):
                # links on the input_url
                print(url+_['href'])
            else:
                # external links
                print(_['href'])
        except:
            print("Error 5: hyperlink nem található.")
#Össze <link> lekérése
def get_link(soup):
    """
   Összes <link>
    """
    link_tags = soup.find_all('link')
    print(len(link_tags), "<link> TAGS")
    for _ in link_tags:
        try:
            if _['rel'][0] == 'stylesheet':
                print(_['href'])
        except:
            print("Error 4: css nem található.")

#Összes szkirpt lekérése
def get_script(soup):
    """
    Összes <script>
    """
    script_tags = soup.find_all('script')
    print(len(script_tags), "<script> TAGS")
    for _ in script_tags:
        try:
            print(_['src'])
        except:
            print("Error 3: js nem található")
#Interface megejelenése.
def interface(soup, url):
    """
    Menü
    """
    wrong_choice_count = 0
    while(True):
        choice = input("""\nNyomd meg 1-5. Majd nyomj egy entert.
                        1. Összes hyperlinks mutatása.
                        2. Összes css fájl mutatása.
                        3. Összes javascript fájl mutatása.
                        4. Új url megadása.
                        5. Kilépés. 
                        """)
        if choice == "1":
            get_a(soup, url)
        elif choice == "2":    
            get_link(soup)
        elif choice == "3":
            get_script(soup)
        elif choice == "4":    
            initializer()
        elif choice == "5":    
            exit()
        else:
            wrong_choice_count += 1
            print("\Rossz választás..")
            if wrong_choice_count > 3:
                exit()
#Kapcsolódás az urlhez, majd az interface megnyitása.
def initializer():
    """
    Add meg az url-t a menü megnyitásához.
    """
    entered_url = input('\nWebsite url: ').strip()

    if not entered_url.startswith('http'):
        input_url = 'https://' + entered_url
    else:
        input_url = entered_url

    print('Kapcsolódás: ' + input_url)

    if input_url.count('.') < 4:
        r = hit_it(input_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        interface(soup, input_url)
    
    else:
        print('Error 1: Hibás URL')
        initializer()



        

    

