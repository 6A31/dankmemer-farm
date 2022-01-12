import requests
import time
import random
from multiprocessing import Process
#Imports

#########################################

channel_id = 'Your channel id for mining here'
id = 'the id the bots will send the money to'

#########################################



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
    tokenlist = token.read().split("\n") #Creates a list with all the Tokens form the file
except:
    print("No file with tokens detected. Please place a file in the same directory as the script called 'tokens.txt'")

def sendmessage(token):
    message = "pls beg"
    messagedig = "pls dig"
    messagefish = "pls fish"
    messagehunt = "pls hunt"
    message2 = f"random text to bypass the bot protection AAA {random.randint(19999,199999992323324324)}" #Sends a string with random numbers to trick dankmemer's macro detection
    pay = f"pls share max <@{id}>"
    headers = {'Authorization': token}
    i = 0

    while True:
        try:
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': messagehunt})
            time.sleep(5)
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': message})
            time.sleep(5)
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': messagefish})
            time.sleep(5)         
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': messagedig})
            time.sleep(5)
            time.sleep(random.randint(1,6))

            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': message2  })
            time.sleep(25 + random.randint(1,5))
            i += 1
            if i > 2:
                res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': pay})
                i = 0

            if res.status_code == 429:
                print("Ratelimit detected....")
        except:
            pass
            print(f"Failed on token: {token}")
            print("If the script is not working, feel free to contact me on discord, https://discord.gg/kjsdxkbtjw")


#Start script
if __name__=='__main__':
    for token in tokenlist:
        p1 = Process(target=sendmessage, args=(token,))
        p1.start()

    
    
