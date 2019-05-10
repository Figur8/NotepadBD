import requests
from bs4 import BeautifulSoup
import json
import os


class NotepadBD:
#Certamente vou passar um parâmetro para demonstrar a chave da conversa
    

    def __init__(self, nameBD):
        self.url = "http://dontpad.com/" + nameBD 
        print("DB's name: ",self.url)
        self.texto = "text='{'user_name': 'meulogin', 'user_password': 'minhasenha123'}'"
        self.nameBD = nameBD

    def captureData(self):
        #TODO - validar pro json não dar erro
        #ERROR - if notepad page is blank, the json.loads() will make a error.
        page = requests.get("http://dontpad.com/tiotio")
        soup = BeautifulSoup(page.content, 'html.parser')
        data = json.loads(soup.find('textarea', id='text').get_text())
        print(data)
       #data["user_name"] = "meulogin2"
        #text ="text=" + json.dumps(data)
        #requests.post(self.url, text)
    
    #Tentar fazer preencher o text área com python (post não funciona)
    
    def post_notepad(self):
        db = {"user_name": "meulogin", "user_password": "minhasenha123"}
        url = "http://dontpad.com/tiotio"
        print(self.url)
        data = {"text":json.dumps(db)}
        postando = requests.post(url=url, data=data)
        #comando = "curl -X POST -d "+ data +" "+str(self.url)
        #print(comando)
        #os.system(comando)
        #ERROR - the method bellow will clean notepad page

#Execution
teste = str(input())
note = NotepadBD(teste)
note.post_notepad()
