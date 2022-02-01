
# dankmemer-farm

Simple script to farm Dankmemer coins with multiple accounts at once.

**Requires:** `Discord Tokens` | `requests` module

## Disclaimer
I don't take responsibility if you get banned from a server or if your Tokens get locked

You can run this script with 15 accounts at once before getting rate limited.

**All accounts need access to the channel ID you provide. Make sure all accounts are in the server and have send message permission**

## Usage
This script was build for [Python 3.9](https://www.python.org/downloads/release/python-390/)

```
py main.py
```

How to use.
------------
**1.** Create a folder.

**2.** Place the python file in the folder.

**3.** Place a text file (`tokens.txt`) with discord Tokens in the folder.
**Call the file "tokens.txt"**. If you change the name, the script won't find your Tokens.

**4.** Open the script and change the following variables.

`channel_id` -> Set this to the ID of the channel you want to farm in.

`id` -> Set this to your user ID. The bots will send their money to this account.

**All your Tokens need access to the channel, so make sure they are joined, and have send message permission.**

**5.** Run the script with `python3 main.py`

**6. Profit**

## Support
Dm me on Discord or join my [server](https://daddyissue.org)

You can open an issue on Github as well

## FAQ
> **Do i need multiple accounts?**

No, you can run this with as many accounts as you like. Note that Discord will rate limit you if you send too many API requests.

> **The file closes after i open it**

You have to run the file via the command prompt / terminal. if you don't know how to do that ask for help in [my discord server](https://daddyissue.org)

> **All the commands are saying they failed**

Make sure your tokens are valid and that all accounts have permisson to send messages in the channel you supplied.

> **How do i get channel id's and user id's**

You can enable developer settings in Discord like this: `settings -> advanced -> developer settings` then rightclick a channel or user and click `copy id`

> **How do i get my Discord token**

I can't explain this here, but **google it**
