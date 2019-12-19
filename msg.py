# Louis Philippe B. Facun
# DogeClick Bot Channel from dogeclick.com
# Auto joiner (/join)

import asyncio
import logging
import re
import time
import os
import sys

logging.basicConfig(level=logging.ERROR)

from telethon import TelegramClient, sync, events
from telethon import functions, types
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.tl.functions.messages import GetHistoryRequest, GetBotCallbackAnswerRequest, ImportChatInviteRequest, AddChatUserRequest
from telethon.errors import SessionPasswordNeededError
from telethon.errors import FloodWaitError

from datetime import datetime
from colorama import Fore, init as color_ama
color_ama(autoreset=True)

os.system('cls' if os.name=='nt' else 'clear')

# Get your own values from my.telegram.org
api_id = 800812
api_hash = 'db55ad67a98df35667ca788b97f771f5'

''' DogeClick Bot Channel from dogeclick.com
Options:
1. Dogecoin_click_bot
2. Litecoin_click_bot
3. BCH_click_bot
4. Zcash_click_bot
5. Bitcoinclick_bot
# '''
channel_username = 'Dogecoin_click_bot'

def print_msg_time(message):
	print('[' + Fore.CYAN + f'{datetime.now().strftime("%H:%M:%S")}' + Fore.RESET + f'] {message}')

async def main():
	
                                
	# Check if phone number is not specified
	if len(sys.argv) < 2:
		print('Usage: python start.py phone_number')
		print('-> Input number in international format (example: +639162995600)\n')
		e = input('Press any key to exit...')
		exit(1)
		
	phone_number = sys.argv[1]
	
	if not os.path.exists("session"):
		os.mkdir("session")
   
	   
	# Connect to client
	client = TelegramClient('session/' + phone_number, api_id, api_hash)
	await client.start(phone_number)
	me = await client.get_me()
	
	print(f'Current account: {me.first_name}({me.username})\n')
	print_msg_time('Sending message...')
	print(f'\n')
	
	# Start command /bots
	await client.send_message(channel_username, '/bots')
	
	# Message the bot
	@client.on(events.NewMessage(chats=channel_username, incoming=True))
	async def join_start(event):
		message = event.raw_text
		if 'Forward a message to' in message:	
			channel_msg = event.message.reply_markup.rows[0].buttons[0].url # event.original_update.message.reply_markup.rows[0].buttons[1].url
			print_msg_time(f'URL @{channel_msg}')
			
			if '?' in channel_msg:
				cbot = re.search(r't.me\/(.*?)\?', channel_msg).group(1)
			elif '?' not in channel_msg:
				cbot = re.search(r't.me\/(.*?)', channel_msg).group(1)
			
			print_msg_time(f'Messaging @{cbot}...')
			#await client(SendMessageRequest(cbot, "/start"))
			#channel_msg = client.send_message(cbot, '/start')
			#channel_msg = (channel_username,
			#await client.send_message(cbot, '/start')
			await client.send_message(cbot, '/start')
			
			
			#await self.get_input_entity(entity)
			print_msg_time(f'Verifying...')
			#channel_entity=client.get_entity(channel_username)
			
			
			# Forward the bot message
			@client.on(events.NewMessage(chats=cbot, incoming=True))
			async def earned_amount(event):
				msg_id = event.message.id,
				await client.forward_messages(channel_username, msg_id, cbot)
	
	# Print earned amount
	@client.on(events.NewMessage(chats=channel_username, incoming=True))
	async def earned_amount(event):
		message = event.raw_text
		if 'You earned' in message:	
			print_msg_time(Fore.GREEN + event.raw_text + '\n' + Fore.RESET)
			
	# No more ads
	@client.on(events.NewMessage(chats=channel_username, incoming=True))
	async def no_ads(event):
		message = event.raw_text
		if 'no new ads available' in message:	
			print_msg_time(Fore.RED + 'Sorry, there are no new ads available\n' + Fore.RESET)
			e = input('Press any key to exit...')
			exit(1)
			
	await client.run_until_disconnected()
	
asyncio.get_event_loop().run_until_complete(main())