from cmath import exp
from functions import Functions
import discord
import os

DISCORD_TOKEN = os.environ.get('DISCORD_FINANCE_BOT_TOKEN')

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

    elif message.content.startswith('!graph'):

        user = message.author.id

        dbMessage = func.getGraph(user)

        await message.channel.send(file=discord.File('plot.png'))

    elif message.content.startswith('!help'):

        await message.channel.send('!create - Create a new account\n!income [amount] [description] - Add income\n!expense [amount] [description] - Add expense\n!balance - Get your balance\n!history - Get your history\n!graph - Get your graph')

    elif message.content.startswith('!delete'):

        await message.channel.send('Are you sure you want to delete your account? (y/n)')
        msg = await client.wait_for('message', check=lambda message: message.author == message.author)
        if msg.content == 'y':
            func.deleteUser(message.author.id)
            await message.channel.send('Account deleted')
        else:
            await message.channel.send('Account not deleted')

client.run(DISCORD_TOKEN)