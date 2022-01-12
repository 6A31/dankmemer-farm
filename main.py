import requests
import time
import random
from multiprocessing import Process
#Imports

#########################################

channel_id = '818808200475443233'
id = '557904328225062935'

#########################################


if channel_id == 'The id to farm in': 
    print("Make sure to specify a channel id. If you don't know how to obtain channel id's use Google.")
    time.sleep(5)
    quit()
if channel_id == 'your id for receiving money':
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

print("Starting...")

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
    message2 = f"random text to bypass the bot protection AAA {random.randint(1, 99999) * random.randint(1, 9999) + random.randint(1,99999)}" #Sends a string with random numbers to trick dankmemer's macro detection
    pay = f"pls share max <@{id}>"
    headers = {'Authorization': token}
    i = 0

    while True:
        try:
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': messagehunt})
            print("Hunt successfully")
            time.sleep(5)
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': message})
            print("beg successfully")
            time.sleep(5)
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': messagefish})
            print("fish successfully")
            time.sleep(5)         
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': messagedig})
            print("dig successfully")
            time.sleep(5)
            time.sleep(random.randint(1,6))

            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': message2})
            print("Bypassed message send successfully")
            time.sleep(25 + random.randint(1,5))
            i += 1
            if i > 2:
                res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': pay})
                print("payout successfull")
                i = 0

        except:
            print(f"Failed on token: {token}")
            print("If the script is not working at all, feel free to contact me on discord, https://discord.gg/kjsdxkbtjw")
            pass


#Start script
if __name__=='__main__':
    print("Starting threads...")
    for token in tokenlist:
        p1 = Process(target=sendmessage, args=(token,))
        p1.start()

    
    
