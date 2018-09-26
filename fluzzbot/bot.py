from python_twitch_irc import TwitchIrc



class FluzzBot(TwitchIrc):
    def on_connect(self):
        self.join('#fluzzbot')
    
    def on_message(self,timestamp,tags,channel,user,message):
        print(tags)
        self.message(channel,message)