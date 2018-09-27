import markovify
import logging
import json
import os

class MarkovContainer(object):

    log = logging.getLogger(__name__)
    markov_order = 3
    user_channel = ""

    def __init__(self, channel):
        self.user_channel = channel
        self.log.info('Loading markov corpus for ' + channel)
        self.load_model_from_disk(channel)

    def load_model_from_disk(self,channel):
        if os.path.isfile("./markov/" + channel + ".json"):
            with open("./markov/" + channel + ".json",'r') as outfile:
                text = outfile.read()
                self.markov_model = markovify.Text.from_json(text)
        else:
            if os.path.isfile("./markov/" + channel + ".txt"):
                with open("./markov/" + channel + ".txt",'r',encoding="utf-8") as f:
                    text = f.read()
                    print(text)
                    self.markov_model = markovify.NewlineText(text,state_size=self.markov_order)
                    model_json = self.markov_model.to_json()
                    with open("./markov/" + channel + ".json",'w') as outfile:
                        outfile.write(model_json)
            else:
                file = open("./markov/" + channel + ".txt",'w+')
                self.markov_model = markovify.Text("",state_size=self.markov_order)

        self.log.info('Done loading markov corpus for ' + channel)

        

    def add_message_to_corpus(self,message):
        new_model = markovify.Text(message,state_size=self.markov_order)
        model_union = markovify.combine([self.markov_model,new_model],[1,1])
        self.markov_model = model_union
        model_json = self.markov_model.to_json()
        with open("./markov/" + self.user_channel + ".json",'w') as outfile:
            outfile.write(model_json)

    def generate_markov_sentence(self):
        return self.markov_model.make_sentence()

    def generate_markov_sentence_with_char_limit(self,length):
        return self.markov_model.make_short_sentence(length)

