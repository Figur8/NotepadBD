import requests
from bs4 import BeautifulSoup
import json

class NotepadBD:
#Certamente vou passar um parâmetro para demonstrar a chave da conversa
#   def __init__():
#      captureData()
    def __init__(self):
        self.url = "http://dontpad.com/tiotio"

    def captureData(self):
        #TODO - validar pro json não dar erro
        page = requests.get("http://dontpad.com/tiotio")
        soup = BeautifulSoup(page.content, 'html.parser')
        data = json.loads(soup.find('textarea', id='text').get_text())
        print(data)
       #data["user_name"] = "meulogin2"
        #text ="text=" + json.dumps(data)
        #requests.post(self.url, text)
    
    #Tentar fazer preencher o text área com python (post não funciona)
    def post_notepad():
        url = "http://dontpad.com/tiotio"
        texto = "text='{'user_name': 'meulogin', 'user_password': 'minhasenha123'}'"
        postando = requests.post(url, texto)

note = NotepadBD()
note.captureData()
