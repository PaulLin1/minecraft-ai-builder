from javascript import require, On
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')

BOT_USERNAME = 'python'

settings = {
  'host': '127.0.0.1',
  'port': 53858,
  'username': BOT_USERNAME
}

bot = mineflayer.createBot(settings)
bot.loadPlugin(pathfinder.pathfinder)
print("Started mineflayer")

@On(bot, 'spawn')
def handle(*args):
    print("I spawned 👋")
    movements = pathfinder.Movements(bot)


    # bot.chat('Hi, you said ' + bot.username)
    bot.chat('Hi, you said ')
    player = bot.players[bot.username].entity


    if player:
        offset = 2
        lookVector = player.yawToVec(1.0)
        
        spawnPosition = player.position.offset(lookVector.x * offset, 0, lookVector.z * offset)
        
        bot.entity.position.set(spawnPosition.x, spawnPosition.y, spawnPosition.z)
        bot.lookAt(player.position)

    @On(bot, 'chat')
    def handleMsg(this, sender, message, *args):
        print("Got message", sender, message)
        if sender and (sender != BOT_USERNAME):
            bot.chat('Hi, you said ' + message)
            if 'come' in message:
                player = bot.players[sender]
                print("Target", player)
                target = player.entity
                if not target:
                    bot.chat("I don't see you !")
                    return

                pos = target.position
                bot.pathfinder.setMovements(movements)
                bot.pathfinder.setGoal(pathfinder.goals.GoalNear(pos.x, pos.y, pos.z, 1))

@On(bot, "end")
def handle(*args):
    print("Bot ended!", args)