from skills import *
from gpt import *
from javascript import require, On
import math
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

class BuilderBot:
    def __init__(self):
        """
        Initializes a bot in minecraft
        """
        self.playerName = 'xj0hnx'
        self.bot = mineflayer.createBot(
            {
                'host': '127.0.0.1',
                'port': 53858,
                'username': 'python'
            }
        )
        print("Started mineflayer")

        self.setup_listeners()

    def setup_listeners(self):
        @On(self.bot, 'spawn')
        def handle_spawn(*args):
            """
            Spawns the bot
            """
            print("I spawned 👋")
            self.client = GPT()

            if self.playerName in self.bot.players:
                self.bot.chat('/tp @s ' + self.playerName)
            else:
                print(f"{self.playerName} is not online or the bot hasn't received their position yet.")

            @On(self.bot, 'chat')
            def on_chat(this, sender, message, *args):
                """
                Handles chats
                :param sender: The sender of the message
                :param message: The message that got sent
                """
                if sender and (sender != self.bot.username):
                    if 'build' in message:
                        bot = self.bot
                        response = self.client.send_to_llm(message)
                        print(response)
                        exec(response)
                    elif 'come' == message:
                        self.bot.chat('/tp @s ' + self.playerName)

            @On(self.bot, 'end')
            def on_end(*args):
                print("Bot ended!", args)