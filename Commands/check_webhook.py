import requests
from colorama import Fore,Style,init

init()

class webhook_checker():
    def __init__(self,webhook):
        try:
            self.webhook = webhook
            validation = requests.get(self.webhook)
            print(validation.status_code)
            if validation.status_code == 200 :
                color = Fore.GREEN
                status = 'valida'
            elif validation.status_code == 404 :
                color = Fore.RED
                status = 'offline'
            else :
                color = Fore.RED
                status = 'Unrecognizable' 
            print("Webhook Status :",color,f"{status}",Style.RESET_ALL)
        except:
            print(Fore.RED,"unexpected error",Style.RESET_ALL)
                
    
        
        
        