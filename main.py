# Build - pyinstaller --onefile -w main.py  
import os
import json
import time

from discordMain import DiscordMain

def run():
    # Print a log message in log.txt
    log = open('log.txt', 'a')
    log.write('Program started at ' + time.strftime('%d/%m/%Y %H:%M:%S') + '\n')

    jsonFile = open('config.json')
    config = json.load(jsonFile)

    # Load environment variables
    envVar = config['env_var']
    DISCORD_TOKEN = os.environ.get(envVar)

    # Try to connect the bot to discord
    try:
        DiscordMain.run(DISCORD_TOKEN)
    except Exception as e:
        print(e)
        print('Failed to connect')
        log.write('Failed to connect at ' + time.strftime('%d/%m/%Y %H:%M:%S') + ':\n' + e + '\n')
        # Check if the token is valid
        if e == 'Improper token has been passed.':
            print('Try to change the token')
        # Check if is a connection error
        elif e == 'Cannot connect to host':
            print('Connection error, trying again in 20 seconds')
            # Wait 10 seconds and try again
            time.sleep(20)
            run()
        # Check if is a timeout error
        elif e == 'Read timed out.':
            print('Timeout error')
        # Check if is a invalid token error
        elif e == '401: Unauthorized':
            print('Invalid token')

    except KeyboardInterrupt:
        print('Program stopped by user')
        jsonFile.close()
        log.close()

if __name__ == '__main__':
    run()




