import bot
import configparser
import json

def main():

    config = configparser.ConfigParser()
    with open('config.json','r') as f:
        config = json.load(f)
    username = config['DEFAULT']["USERNAME"]
    password = config['DEFAULT']["PASSWORD"]
    client = bot.FluzzBot(username,password).start()
    client.handle_forever()


if __name__ == "__main__":
    main()


