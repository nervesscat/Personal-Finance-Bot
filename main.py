from cmath import exp
from functions import Functions
import discord
import os

DISCORD_TOKEN = 'MTAwMTE0OTg3NTMwNTU5OTExOA.Gt6Hf9.VvBDg7SzDNbolj2obcjMq0LFQcMpXPhhgC-aJ4'
#DISCORD_TOKEN = os.environ.get('DISCORD_ING')

func = Functions()
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_message(message):

    if message.author == client.user:
        return


    elif message.content.startswith('!create'):

        await message.channel.send('Create a new account')

        dbMessage = func.createUser(message.author.id)
        
        await message.channel.send(dbMessage)


    elif message.content.startswith('!income'):

        msg = message.content.split(' ')

        user = message.author.id
        income = msg[1]

        description = msg[2]

        dbMessage = func.addIncome(user, income, description)

        func.updateBalance(user, float(income), 0)  

        await message.channel.send(dbMessage)  
    

    elif message.content.startswith('!expense'):
        
        msg = message.content.split(' ')

        user = message.author.id
        expense = msg[1]
        description = msg[2]

        dbMessage = func.addExpense(user, expense, description)

        func.updateBalance(user, 0, float(expense))

        await message.channel.send(dbMessage)

    elif message.content.startswith('!balance'):

        user = message.author.id

        dbMessage = func.getBalance(user)

        await message.channel.send(dbMessage)

    elif message.content.startswith('!history'):

        await message.channel.send('Function not available yet')

    elif message.content.startswith('!help'):

        await message.channel.send('!create - Create a new account\n!income [amount] [description] - Add income\n!expense [amount] [description] - Add expense\n!balance - Get your balance\n!history - Get your history')

    elif message.content.startswith('!delete'):

        await message.channel.send('Are you sure you want to delete your account? (y/n)')
        msg = await client.wait_for('message', check=lambda message: message.author == message.author)
        if msg.content == 'y':
            func.deleteUser(message.author.id)
            await message.channel.send('Account deleted')
        else:
            await message.channel.send('Account not deleted')

client.run(DISCORD_TOKEN)