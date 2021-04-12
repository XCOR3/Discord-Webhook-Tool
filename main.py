import json
from os import system
from time import sleep
from colorama import Fore,Style,init
from Commands.check_webhook import webhook_checker
from Commands.spam_webhook import webhook_spammer

init()


Options_Menu = '''

        cw - For Check one Webhook 

        sw - For Spam an Webhook

'''

def retornar_ao_menu():
        print("\n")
        return_to_main_menu_2 = str(input(" Return to main menu ? y/n \n"))
        if return_to_main_menu_2 == 'y' or return_to_main_menu_2 == 'Y':
            main()
        else:
            pass
    
def main ():
    try:
        system("cls")
        print(Options_Menu)
        op = str(input(" > "))
        if op == 'cw':
            system("cls")
            webhook = str(input("Insere Uma webhook : "))
            print(webhook_checker(webhook))
            retornar_ao_menu()
        if op == 'sw':
            system("cls")
            webhook = str(input("Insere Uma webhook : "))
            print()
            spam_quantity = int(input("Insere a quantidade de mensagens que queres spamar : "))
            webhook_spammer(webhook,spam_quantity)
            retornar_ao_menu()
    except:
        print(Fore.RED,"Algo deu errado .",Style.RESET_ALL)
        retornar_ao_menu()

main()