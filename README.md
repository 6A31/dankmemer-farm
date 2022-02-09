
# dankmemer-farm

Simple script to farm Dankmemer coins with multiple accounts at once.

**Requires:** `Discord Tokens` | `requests` module

## Disclaimer
I don't take responsibility if you get banned from a server or if your Tokens get locked

You can run this script with 15 accounts at once before getting rate limited.

**All accounts need access to the channel IDs you provide. Make sure all accounts are in the server and have send message permission**

## Usage
This script was build for [Python 3.9](https://www.python.org/downloads/release/python-390/)

### Windows
Double-click the .bat file

### MacOS / Linux
run the following command in the file's directory:
```
py main.py
```

How to use.
------------
**1.** Create a folder.

**2.** Place the python file in the folder.

**3.** Place a text file (`tokens.txt`) with discord Tokens in the folder, one per line.
**Call the file "tokens.txt"**. If you change the name, the script won't find your Tokens.

**4.** Place a text file (`channels.txt`) with channel IDs in the folder, one per line.
**Call the file "channels.txt"**. If you change the name, the script won't find your channels.

**5.** Open the script and change the following variables.

`backup_channel` -> Set this to the ID of the backup channel you want to farm in.

`id` -> Set this to your user ID. The bots will send their money to this account.

**All your Tokens need access to the channels you provide, so make sure they are joined, and have send message permission.**

**6. (WINDOWS ONLY)(OPTIONAL)** Place a .txt file in the same folder as everything else and copy/paste the code in start.bat to the txt file.

**7. (WINDOWS ONLY)(OPTIONAL)** Rename the file to `start.bat`

**8.** Run the script with `python main.py` or double click the .bat file if you're on windows.

**9. Profit**

**Note:** The way your tokens and channel IDs are placed is the way they will work. ie. TokenOne is on line one and ChannelOne is on line one, so TokenOne will send messages to ChannelOne. Also, if you only want... lets say two accounts in seperate channels, and the others in one channel all together, put the two tokens you want seperate on line one and two in `tokens.txt` as well as their respective channels on line one and two in `channels.txt` and the rest of the tokens the same way, except with no channels. Make sure to set the back up channel variable to the channel you want the rest of the accounts to run commands on.

## Support
Dm me on Discord or join my [server](https://daddyissue.org)

You can open an issue on Github as well

## FAQ
> **Do i need multiple accounts?**

No, you can run this with as many accounts as you like. Note that Discord will rate limit you if you send too many API requests.

> **The file closes after i open it**

You have to run the file via the command prompt / terminal. If you don't know how to do that, ask for help in [my discord server](https://daddyissue.org)

> **How do i download Python**

You can download the latest version of [Python3 here](https://www.python.org/downloads/)
After downloading, run the file, and make sure you click the checkbox `add to path` as it will help you out later.

> **Can i get banned**

Yes. You can always get banned. Blacklisted by dankmemer or banned by discord. It's very unlikely tho.

> **All the commands are saying they failed**

Make sure your tokens are valid and that all accounts have permission to send messages in the channel you supplied. If you still get errors, ask or help in [my discord server](https://daddyissue.org)

> **How do i get channel id's and user id's**

You can enable developer settings in Discord like this: `settings -> advanced -> developer settings` then right-click a channel or user and click `copy id`

> **How do i get my Discord token**

I can't explain this here, but **google it**

