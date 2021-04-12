import json
import random 
import requests
from time import sleep    
from colorama import Fore,Style,init
from dhooks import Webhook, Embed, File 

color_selection = [Fore.RED, Fore.BLUE, Fore.WHITE, Fore.GREEN, Fore.MAGENTA, Fore.YELLOW]

init()

class webhook_spammer():
    def __init__(self,webhook,spam_count):
        try:
            with open("cfgs/config.json") as cfgs :
                configs = json.load(cfgs)
                Title = configs['Title']
                Content_title = configs['Content_Title']
                Content = configs['Content']
                Footer = configs['Footer']
                
            self.webhook = webhook
            self.spam_count = spam_count
            print(f" webhook : {self.webhook} vezes : {self.spam_count} ")
            r = requests.get(self.webhook)
            if r.status_code != 200:
                print(Fore.RED,"Invalid webhook ",Style.RESET_ALL)
            else:
                hook = Webhook(self.webhook)
                for contador in range(0,self.spam_count) : 
                    request = requests.get(self.webhook)
                    if request.status_code == 200:
                        rand_color = random.choice(color_selection)
                        embed = Embed(title=f'{Title}',description='',color=0x690FC3,timestamp='now')
                        embed.add_field(f"{Content_title}",f"{Content}",inline=False)
                        embed.set_footer(text=f'{Footer}')
                        hook.send(embed=embed)
                        contador += 1
                        print(rand_color,f"Count : {contador}",Style.RESET_ALL)
                    else :
                        print(Fore.RED,"Webhook offline, provavelmente foi apagada .",Style.RESET_ALL)
                        break
                print(Fore.GREEN,f"Atack sucefully sent . Messages sended : {contador}",Style.RESET_ALL)
        except:
            print(Fore.RED,"Algo deu errado ",Style.RESET_ALL)