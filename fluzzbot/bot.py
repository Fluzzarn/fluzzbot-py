from python_twitch_irc import TwitchIrc
import logging



class FluzzBot(TwitchIrc):
    joined_channels = ["fluzzbot"]
    log = logging.getLogger(__name__)
    def add_channels_to_join(self,channels):
        self.joined_channels += channels
        return self

    def on_connect(self):
        for channel in self.joined_channels:
            self.log.info("JOINing " + channel)
            self.join('#' + channel)
    
    def on_message(self,timestamp,tags,channel,user,message):
        print(tags)
        self.message(channel,message)