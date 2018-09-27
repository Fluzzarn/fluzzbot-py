from python_twitch_irc import TwitchIrc
import markov
import logging



class FluzzBot(TwitchIrc):
    joined_channels = ["fluzzbot"]
    markov_models = {}
    log = logging.getLogger(__name__)

    def add_channels_to_join(self,channels):
        self.joined_channels += channels
        return self

    def init_markov(self,channel):
        self.markov_models[channel] = markov.MarkovContainer(channel)


    def on_connect(self):
        for channel in self.joined_channels:
            self.log.info("JOINing " + channel)
            self.init_markov(channel)
            self.join('#' + channel)
    
    def on_message(self,timestamp,tags,channel,user,message):
        self.log.info("Received message " + message + " from " + user + " in channel " + channel)
        self.message(channel,self.markov_models[channel[1:]].generate_markov_sentence_with_char_limit(200))