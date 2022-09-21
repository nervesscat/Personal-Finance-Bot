from functions import Functions
import discord
import os

DISCORD_TOKEN = os.environ.get('DISCORD_FINANCE_BOT_TOKEN')

func = Functions()
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_message(message):

    user = message.author.id

    if message.author == client.user:
        return


    elif message.content.startswith('!create'):

        await message.channel.send('Create a new account')

        dbMessage = func.createUser(message.author.id)
        
        await message.channel.send(dbMessage)


    elif message.content.startswith('!income'):

        msg = message.content.split(' ')

        income = msg[1]

        description = msg[2]

        dbMessage = func.addIncome(user, income, description)

        func.updateBalance(user, float(income), 0)  

        await message.channel.send(dbMessage)  
    

    elif message.content.startswith('!expense'):
        
        msg = message.content.split(' ')

        expense = msg[1]
        description = msg[2]

        dbMessage = func.addExpense(user, expense, description)

        func.updateBalance(user, 0, float(expense))

        await message.channel.send(dbMessage)


    elif message.content.startswith('!balance'):

        func.getBalance(user)

        await message.channel.send(dbMessage)


    elif message.content.startswith('!graph'):

        dbMessage = func.getGraph(user)

        await message.channel.send(file=discord.File('plot.png'))


    elif message.content.startswith('!delete'):

        await message.channel.send('Are you sure you want to delete your account? (y/n)')
        msg = await client.wait_for('message', check=lambda message: message.author == message.author)
        if msg.content == 'y':
            func.deleteUser(message.author.id)
            await message.channel.send('Account deleted')
        else:
            await message.channel.send('Account not deleted')


    elif message.content.startswith('!help'):

        #Create an embed message

        embed = discord.Embed(title="Help", description="List of commands", color=0x00ff00)

        embed.add_field(name="!create", value="Create a new account", inline=False)

        embed.add_field(name="!delete", value="Delete an account", inline=False)

        embed.add_field(name="!income", value="Add an income", inline=False)

        embed.add_field(name="!expense", value="Add an expense", inline=False)

        embed.add_field(name="!balance", value="Get your balance", inline=False)

        embed.add_field(name="!graph", value="Get a graph of your expenses", inline=False)

        embed.add_field(name="!help", value="Get a list of commands", inline=False)

        await message.channel.send(embed=embed)

client.run(DISCORD_TOKEN)