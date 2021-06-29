import discord_webhook
from discord_webhook import DiscordEmbed, DiscordWebhook
import string
import random
import time
import requests
import colorama
import json
from colorama import *

colorama.init()

print(f'''{Fore.RED} _  _  _____  _____  ____  ___  ____    __    ____  ____  ____  ____    _    _  ____  ____  _   _  _____  _____  _  _    ___  ____   __    __  __  __  __  ____  ____
( \( )(  _  )(  _  )(  _ \/ __)(  _ \  /__\  (_  _)(  _ \( ___)(  _ \  ( \/\/ )( ___)(  _ \( )_( )(  _  )(  _  )( )/ )  / __)(  _ \ /__\  (  \/  )(  \/  )( ___)(  _ /
 )  (  )(_)(  )(_)(  ) _ <\__ \ )   / /(__)\  _)(_  )(_) ))__)  )   /   )    (  )__)  ) _ < ) _ (  )(_)(  )(_)(  )  (   \__ \ )___//(__)\  )    (  )    (  )__)  )   /
(_)\_)(_____)(_____)(____/(___/(_)\_)(__)(__)(____)(____/(____)(_)\_)  (__/\__)(____)(____/(_) (_)(_____)(_____)(_)\_)  (___/(__) (__)(__)(_/\/\_)(_/\/\_)(____)(_)\_)
                                                                                                                       
                                                                                                                       Created by hellonoobs and massy
                                                                                                                       If it stops spamming press enter!{Style.RESET_ALL}
''')

def sbammah():
    webhook = input(Fore.YELLOW + "[>] Enter The Webhook Link: ")
    message = input(Fore.GREEN + "[>] Enter The Message: ")    
    delay = float(input(Fore.MAGENTA + "[>] Enter The Delay (EX: 0.1): "))
    print(Fore.BLUE + 'Starting to send messages')

    while True:

        print(Fore.CYAN + "Sending -> " + message)
        print(Fore.RESET + " ")
        try:
            time.sleep(delay)
            _data = requests.post(webhook, json={'content': message})

            if _data.status_code == 204:
                print(Fore.CYAN + "Sent -> " + message) 
        except:
            print("Something Happend! | Probably Broken Webhook -> " + webhook)
            time.sleep(5)
            exit()

x = 5
while x == 5:
    sbammah()
