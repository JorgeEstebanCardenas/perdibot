import discord
from keep_alive import keep_alive
import random

res=['perd','jugar','juego','terraria','jugamos','perdiste',
'perdimos','ah','game']



class MyClient(discord.Client):
    
   
    async def on_ready(self):
        await client.change_presence(activity=discord.Game('the game'))
        print('Logged on as', self.user)
    
    async def on_message(self, message):
        # don't respond to ourselves
      
        if message.author == self.user:
            return

        msg=message.content

        if any(word in msg.lower() for word in res):
            await message.channel.send('perdi')
        else:
            x=random.randrange(0,10)
            if x==1:
              await message.channel.send('perdi')

        
          
        
        


client = MyClient()


keep_alive()
client.run('ODA4NDcwNzkyNTA5MTk0Mjcx.GUCPYR.Ibt87s6_Fy64jwpUfS31GY4CcEpT6UigxfumTs')