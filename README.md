
# Personal Finance Discord Bot

![discord](https://img.shields.io/static/v1?label=&message=discord&color=blue) 
![sql](https://img.shields.io/static/v1?label=&message=sql&color=orange)
![python](https://img.shields.io/static/v1?label=&message=python&color=blue)

This bot is designed to help Discord users keep track of their personal finances directly on their Discord servers. The bot offers the ability to register financial transactions and generate charts to visualize financial data.




## Installation

1. Clone this repository on your local machine.
2. Create an application and bot on the **[Discord Developer Portal](https://discord.com/developers/applications)** and obtain the bot's token.
3. Add the Discord token as environment variables with the name `DISCORD_FINANCE_BOT_TOKEN`.
4. Invite the bot to the server where you want to use it.
5. Install necessary dependencies using the command

```bash
  pip install -r requirements.txt
```
    
## Deployment

To deploy this project run

```bash
  py main.py
```


## Usage

The bot has the following main features:

* Financial transaction registration: users can register their financial transactions using the !income and !expense commands. Each transaction includes a description, an amount.
* Charting: users can generate line charts to visualize their financial data using the !graph command. The user can extend the function with the following optional parameters:

  * -lm: displays data from the last month.
  * -in: displays only income data.
  * -ex: displays only expense data.

#### In addition, the bot includes the following additional commands:

* !balance: Shows the user's current balance.
* !help: Shows the list of available commands and provides additional information on how to use each command.
* !create: Registers a new user account on the bot.
* !delete: Deletes the user account from the bot and erases all associated data.

![App Screenshot](https://i.postimg.cc/nzybCpWv/Screenshot-2023-02-16-231033.png)

## Contributing

Contributions are always welcome! If you would like to help improve this project, please create an issue or pull request on GitHub. If you have any questions or suggestions, you can contact me.


## License

This project is available under the [MIT](https://choosealicense.com/licenses/mit/) license.

