import requests
import time
import random
from multiprocessing import Process
#Imports

#########################################
           ###REPLACE THOSE###
    
channel_id = 'The id of your channel to farm in'
id = 'Your user id for receiving money'

           ###REPLACE THOSE###
#########################################

print("""
https://github.com/ScobraScope/dankmemer-farm/

This script is able to automatic farm dankmemer credits on multiple accounts
at once. It sends post requests to discords API and can run in the background.
Make sure to change the following variables in the python file before running it:

channel_id
id

If the script is not working at all, feel free to contact me on discord, https://discord.gg/kjsdxkbtjw

Made by 6A31 - https://github.com/scobrascope
GNU GENERAL PUBLIC LICENSE V3

Please follow the license at https://github.com/ScobraScope/dankmemer-farm/blob/main/LICENSE.md
""")

if channel_id == 'The id of your channel to farm in': #DON'T TOUCH THIS, THIS IS JUST A CHECK!
    print("Make sure to specify a channel id. If you don't know how to obtain channel id's use Google.")
    time.sleep(5)
    quit()
if channel_id == 'Your user id for receiving money': #DON'T TOUCH THIS, THIS IS JUST A CHECK!
    print("Please specify what user to send the money to. specify a user id above. If you don't know how to obtain user id's use Google")
    time.sleep(5)
    quit()


#███╗░░░███╗░█████╗░██████╗░███████╗
#████╗░████║██╔══██╗██╔══██╗██╔════╝
#██╔████╔██║███████║██║░░██║█████╗░░
#██║╚██╔╝██║██╔══██║██║░░██║██╔══╝░░
#██║░╚═╝░██║██║░░██║██████╔╝███████╗
#╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝


#██████╗░██╗░░░██╗
#██╔══██╗╚██╗░██╔╝
#██████╦╝░╚████╔╝░
#██╔══██╗░░╚██╔╝░░
#██████╦╝░░░██║░░░
#╚═════╝░░░░╚═╝░░░


#░█████╗░░█████╗░██████╗░░░███╗░░
#██╔═══╝░██╔══██╗╚════██╗░████║░░
#██████╗░███████║░█████╔╝██╔██║░░
#██╔══██╗██╔══██║░╚═══██╗╚═╝██║░░
#╚█████╔╝██║░░██║██████╔╝███████╗
#░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝


try:
    token = open("tokens.txt", "r")
    tokenlist = token.read().split("\n") #Creates a list with all the Tokens from the file
except:
    print("-" * 20)
    print("No file with tokens detected. Please place a file in the same directory as the script, called 'tokens.txt'")

def sendmessage(token):
    message = "pls beg"
    messagedig = "pls dig"
    messagefish = "pls fish"
    messagehunt = "pls hunt"
    message2 = f"random text to bypass the bot protection AAA {random.randint(1, 99999) * random.randint(1, 9999) + random.randint(1,99999)}" #Sends a string with random numbers to trick dankmemer's macro detection
    pay = f"pls share max <@{id}>"
    headers = {'Authorization': token}
    i = 0

    while True:
        try:
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': messagehunt})
            if res.status_code == 200:
                print("Hunted successfully")
            else:
                print(f"Failed to hunt. Errorcode {res}")
            time.sleep(5)
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': message})
            if res.status_code == 200:
                print("Begged successfully")
            else:
                print(f"Failed to beg. Errorcode {res}")
            time.sleep(5)
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': messagefish})
            if res.status_code == 200:
                print("Fished successfully")
            else:
                print(f"Failed to fish. Errorcode {res}")
            time.sleep(5)         
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': messagedig})
            if res.status_code == 200:
                print("Fished successfully")
            else:
                print(f"Failed to fish. Errorcode {res}")
            time.sleep(5)
            time.sleep(random.randint(1,6))

            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': message2})
            print("Bypassed message send successfully")
            time.sleep(25 + random.randint(1,5))
            i += 1
            if i > 2:
                res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': pay})
                if res.status_code == 200:
                    print("Payout successful")
                else:
                    print(f"Failed to pay. Errorcode {res}")
                i = 0

        except:
            print(f"Failed on token: {token}")
            print("If the script is not working at all, feel free to contact me on discord, https://discord.gg/kjsdxkbtjw")
            pass


#Start script
if __name__=='__main__':
    for token in tokenlist:
        p1 = Process(target=sendmessage, args=(token,))
        p1.start()

    
    
