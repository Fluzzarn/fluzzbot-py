from python_twitch_irc import TwitchIrc
import markov
import channel
import logging



class FluzzBot(TwitchIrc):
    joined_channels = ["fluzzbot"]
    channels = {}
    log = logging.getLogger(__name__)

    def add_channels_to_join(self,channels):
        self.joined_channels += channels
        return self

    def init_markov(self,channel):
        self.markov_models[channel] = markov.MarkovContainer(channel)


    def on_connect(self):
        for channel_to_join in self.joined_channels:
            self.log.info("JOINing " + channel_to_join)

            chan = channel.Channel(channel_to_join)
            self.channels[channel_to_join] = chan
            self.channels[channel_to_join].init_markov()
            self.join('#' + channel_to_join)
    
    def on_message(self,timestamp,tags,channel,user,message):
        self.log.info("Received message " + message + " from " + user + " in channel " + channel)

        stripped_channel = channel[1:]
        self.channels[stripped_channel].update_model_with_message(message)
        if not self.channels[stripped_channel].see_if_on_cooldown():
            self.message(channel,self.channels[stripped_channel].generate_markov())