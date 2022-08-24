# hacker-discordbot
## discord bot with hacking vibes with all basics commands and `CTF flag` verification system
# PREVIEW
![alt text](https://github.com/MahdiAw/hacker-discordbot/blob/main/verification.PNG)
![alt text](https://github.com/MahdiAw/hacker-discordbot/blob/main/preview.png)
# configuration 

## Database 
export postgres database connection url to your env
```
export DATABASE_URL=postgres://{user}:{password}@{hostname}:{port}/{database-name}
```
## TOKEN
```
export DISCORD_TOKEN="discord bot token"
```
## Constants `utils/const.py`
after the server creation, make **verify** channel,create **verified**  and **unverified** role
replace the variables in the const.py file 

```
GUILDS = ("you server id".)
VERIFICATION_ROOM_ID = ...
VERIFIED_ROLE_ID = ...
UNVERIFIED_ROLE_ID = ...
```

