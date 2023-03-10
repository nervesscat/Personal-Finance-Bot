from functions import Functions
import discord
import os

class DiscordMain:
    def run(token):
        func = Functions()
        client = discord.Client(intents=discord.Intents.default())

        @client.event
        async def on_message(message):

            user = message.author.id

            msg = message.content.split(' ')

            if message.author == client.user:
                return


            elif message.content.startswith('!create'):

                await message.channel.send('Create a new account\nPlease select a currency')

                # Create a menu with the currencies
                embed = discord.Embed(title="Currencies", description="Select a currency", color=0x00ff00)

                embed.add_field(name="1", value="EUR", inline=False)
                embed.add_field(name="2", value="USD", inline=False)
                embed.add_field(name="3", value="Pound", inline=False)
                embed.add_field(name="4", value="LPS", inline=False)
                await message.channel.send(embed=embed)

                # Wait for the user to select a currency
                msg = await client.wait_for('message', check=lambda message: message.author == message.author)

                # If the user selects a currency, create the account
                if msg.content == '1':
                    dbMessage = func.createUser(message.author.id, 'EUR')
                    await message.channel.send(dbMessage)
                elif msg.content == '2':
                    dbMessage = func.createUser(message.author.id, 'USD')
                    await message.channel.send(dbMessage)
                elif msg.content == '3':
                    dbMessage = func.createUser(message.author.id, 'Pound')
                    await message.channel.send(dbMessage)
                elif msg.content == '4':
                    dbMessage = func.createUser(message.author.id, 'LPS')
                    await message.channel.send(dbMessage)

            elif message.content.startswith('!income'):

                income = msg[1]

                if len(msg) > 2:
                    description = msg[2]
                else:
                    description = ''

                dbMessage = func.addIncome(user, income, description)

                await message.channel.send(dbMessage)  
            

            elif message.content.startswith('!expense'):

                expense = msg[1]

                if len(msg) > 2:
                    description = msg[2]
                else:
                    description = ''

                dbMessage = func.addExpense(user, expense, description)

                await message.channel.send(dbMessage)


            elif message.content.startswith('!balance'):

                dbMessage = func.getBalance(user)

                if dbMessage == "User doesn't exist" :
                    await message.channel.send(dbMessage)
                    return

                embed = discord.Embed(title="Balance", description="Shows the total balance", color=0x00ff00)

                embed.add_field(name="Total Balance", value=dbMessage, inline=False)

                await message.channel.send(embed=embed)


            elif message.content.startswith('!graph'):

                if len(msg) > 1:
                    graphType = msg[1]
                else:
                    graphType = '-bal'

                dbMessage = func.getGraph(user, graphType)

                if dbMessage == "User doesn't exist" :
                    await message.channel.send(dbMessage)
                elif dbMessage == 'Graph created':
                    await message.channel.send(file=discord.File('plot.png'))


            elif message.content.startswith('!delete'):

                await message.channel.send('Are you sure you want to delete your account? (y/n)')
                msg = await client.wait_for('message', check=lambda message: message.author == message.author)
                if msg.content == 'y':
                    dbMessage = func.deleteUser(message.author.id)
                    await message.channel.send(dbMessage)
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

                embed.add_field(name="!graph", value="Get a graph of your incomes, expenses (Use the word -in, -ex, -ba for print only one graph or -lm to print only the last month)", inline=False)

                embed.add_field(name="!help", value="Get a list of commands", inline=False)

                await message.channel.send(embed=embed)

        client.run(token)
