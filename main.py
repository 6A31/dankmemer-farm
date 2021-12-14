import requests
import time
import random
from multiprocessing import Process
#Imports

#########################################

channel_id = 'Your channel id here'
id = 'Your user id here'

#########################################

try:
    token = open("tokens.txt", "r")
    tokenlist = token.read().split("\n") #Creates a list with all the Tokens form the file
except:
    print("No file with tokens detected. Please place a file in the same directory as the script called 'tokens.txt'")

try:
    f = open("proxies.txt", "r")
    proxielist = f.read().split("\n") #Creates a list with all the proxies from the file
except:
    print("No file with proxies detected. Please place a file in the same directory as the script called 'proxies.txt'")


def convertproxy(proxy): #Turns a proxy into the correct format and dict. for the request module to use.
    prox = f"http://{proxy}"
    proxies={"http": 0}
    proxies["http"] = prox
    return proxies

def sendmessage(token):
    message = f"pls beg"
    message2 = f"random text to bypass the bot protection AAA {random.randint(19999,199999992323324324)}" #Sends a string with random numbers to trick dankmemer's macro detection
    pay = f"pls share max <@{id}>"
    collect = "pls daily" #Plan on adding. Autocollect daily, monthly
    headers = {'Authorization': token}
    while True:
        try:
            i = random.randint(0, len(proxielist))
            p = convertproxy(proxielist[i]) #Chooses a random proxy for every Farm-Sell cycle.
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, proxies=p, json={'content': message})
            print(res)
            time.sleep(20 + random.randint(2,5))
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, proxies=p, json={'content': message2  })
            print(res)
            time.sleep(25 + random.randint(0,10))
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, proxies=p, json={'content': message})
            print(res)
            time.sleep(20 + random.randint(2,5))
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, proxies=p, json={'content': message2  })
            print(res)
            time.sleep(25 + random.randint(0,10))
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, proxies=p, json={'content': message})
            print(res)
            time.sleep(20 + random.randint(2,5))
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, proxies=p, json={'content': message2  })
            print(res)
            time.sleep(25 + random.randint(0,10))
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, proxies=p, json={'content': message})
            print(res)
            time.sleep(20 + random.randint(2,5))
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, proxies=p, json={'content': message2  })
            print(res)
            time.sleep(25 + random.randint(0,10))
            res = requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, proxies=p, json={'content': pay  })
            print(res)
            if res.status_code == 429:
                print("Ratelimit detected....")
        except:
            pass
            print(f"Failed on token: {token}")


#Start script
if __name__=='__main__':
    for token in tokenlist:
        p1 = Process(target=sendmessage, args=(token,))
        p1.start()

    
    
