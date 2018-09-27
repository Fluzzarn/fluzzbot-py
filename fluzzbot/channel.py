import markov
import logging
import json
import os
from threading import Timer

class Channel(object):
    is_on_cooldown = False
    channel_name = ""
    cooldown_time = 5
    char_limit = 300
    


    log = logging.getLogger(__name__)

    def __init__(self,name):
        self.channel_name = name

    def init_markov(self):
        self.markov_model = markov.MarkovContainer(self.channel_name)

    def see_if_on_cooldown(self):
        return self.is_on_cooldown

    def update_model_with_message(self,message):
        self.markov_model.add_message_to_corpus(message)


    def generate_markov(self):
        markov_string = self.markov_model.generate_markov_sentence_with_char_limit(self.char_limit)

        self.log.info('Generated markov for channel ' + self.channel_name)
        self.is_on_cooldown = True
        self.cooldown_timer = Timer(5,self.reset_cooldown)
        self.cooldown_timer.start()
        return markov_string


    def reset_cooldown(self):
        self.log.info(self.channel_name + ' is no longer on cooldown')
        self.is_on_cooldown = False