TOKEN = 'MTA2NTgwODE3OTI4NTQ2NzE0Ng.GTh_F_.0LfaTiRXhYYJQjcJTxFyOPjD5jS2Py5hsVdCcE'

twitter_keys = {
        'consumer_key':        'GIy0W9gAlT0JZnkckaNM80irg',
        'consumer_secret':     '370tLYWMy3kWzAxaAzsRe6QifLsJ4WzI3h8uzP0x3rLljwCAco',
        'access_token_key':    '1257379940321935369-6hi0KkRd58HljWAFAyCAxDsx7sALdO',
        'access_token_secret': 'hd2rhiwCkDb0cBMj7bdoKrcooZ0wTqNSvq3AxqoQOeZXR'
    }

import discord
import tweepy
import random


#function to read a random line
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)


#discord setup
intents=discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

#discord confirmation 
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

#twitter setup
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)


#discord instructions
@client.event
async def on_message(message):
    if message.author == client.user:
        return
     #HelloCommand
    if message.content.startswith('Guess Hello'):
        await message.channel.send('Hello ! And welcome to los pollos hermanos my name is Gustavo but you can call me Gus ')

     #Help/Navigation Command
    if message.content.startswith("Gus Help") :
        await message.channel.send ("Use these specific commands and I will be at your service :  ")
        await message.channel.send ("'Gus Hello' will welcome you to my own restaurant! ")
        await message.channel.send ("'Gus Help' will send out all the commands you can use")
        await message.channel.send ("'Gus Tweet This' will allow you to tweet on twitter account @ChoseName from discord")
        await message.channel.send ("'Gus Give Me One Of Your Quotes' will give you one of my Breaking Bad Quotes")

     #Tweeting From Discord  
    if message.content.startswith("Gus Tweet This") :
      await message.channel.send("Tweet What ?")
      msg = await client.wait_for('message')
      response = (msg.content)
      api.update_status(response)
    
     #GusQuotes
    if message.content.startswith("Gus Give Me One Of Your Quotes") :     
        Quote = random_line('test.txt')
        await message.channel.send(Quote)
        api.update_status(Quote)

   # if message.content.startswith("Guess The Charachter") :
    #    await message.channel.send("OK let's start.Unfortunately,the choices are limited,I can guess one of the followings")
     #   await message.channel.send("Walter,Mike,Skyler,Walter JR,Hank,Gustavo and Marie")
      #  await message.channel.send("Is your charachter a male or female ?")
#
#       if message.content.startswith("male") :
#          await message.channel.send("its a boy")

#     if message.content.startswith("female") :
#        await message.channel.send("its a girl")

client.run(TOKEN)
