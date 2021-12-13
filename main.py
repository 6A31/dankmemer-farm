import requests
import time
import random
from multiprocessing import Process


try:
    token = open("tokens.txt", "r")
    tokenlist = token.read().split("\n")
except:
    print("No file with tokens detected. Please place a file in the same directory as the script called 'tokens.txt'")
try:
    f = open("proxies.txt", "r")
    proxielist = f.read().split("\n")
except:
    print("No file with proxies detected. Please place a file in the same directory as the script called 'proxies.txt'")
channel_id = input("Enter channel id here >>> ")
id = input("Enter your user-id here. All coins will be tranfered to this id every 4 minutes >>> ")
def convertproxy(proxy):
    prox = f"http://{proxy}"
    proxies={"http": 0}
    proxies["http"] = prox
    return proxies

def sendmessage(token):
    message = f"pls beg"
    message2 = f"random text to bypass the bot protection AAA {random.randint(19999,199999992323324324)}"
    pay = f"pls share max <@{id}>"
    collect = "pls daily"
    headers = {'Authorization': token}
    while True:
        try:
            i = random.randint(0, len(proxielist))
            p = convertproxy(proxielist[i])
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



if __name__=='__main__':
    for token in tokenlist:
        p1 = Process(target=sendmessage, args=(token,))
        p1.start()

    
    
