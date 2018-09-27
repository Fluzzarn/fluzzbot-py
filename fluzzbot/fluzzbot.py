import bot
import configparser
import json
import os
import logging


def main():

    if not os.path.isdir('./markov'):
        os.mkdir('./markov')
    logging.basicConfig(level=os.environ.get("LOGLEVEL","INFO"))
    config = configparser.ConfigParser()
    with open('config.json','r') as f:
        config = json.load(f)
    username = config['DEFAULT']["USERNAME"]
    password = config['DEFAULT']["PASSWORD"]
    channels = config['DEFAULT']["CHANNELS"]
    client = bot.FluzzBot(username,password).add_channels_to_join(channels).start()
    client.handle_forever()


if __name__ == "__main__":
    main()


