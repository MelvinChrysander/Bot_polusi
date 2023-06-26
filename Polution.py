import discord


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    
   
@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    
                
    if 'polusi' in message.content.lower():
        await message.channel.send('Pencemaran atau polusi adalah masuk atau dimasukkannya mahluk hidup, zat, energi dan/ atau komponen lain ke suatu tempat di alam yang bersifat merugikan.')
       
        await message.channel.send('Tekan "a" untuk mencari macam macam polusi')
        await message.channel.send('Tekan "b" untuk mencari cara mengurangi pencemaran')
    
    elif message.content.startswith('a'):
        await message.channel.send('Macam-Macam pencemaran air adalah air, tanah, dan udara.')
        
        await message.channel.send('Tekan "polusi" untuk mengetahui artinya')
        await message.channel.send('Tekan "b" untuk mencari cara mengurangi pencemaran')
        
    elif message.content.startswith('b'):
        await message.channel.send('Pencemaran Air:')
        await message.channel.send('Mengurangi penggunaan bahan kimia berbahaya seperti pestisida, pupuk, dan deterjen fosfat.')
        await message.channel.send('Menggunakan sistem pengolahan air yang efektif sebelum membuang limbah ke perairan.')
        await message.channel.send('Memastikan limbah industri dan domestik diproses dengan benar sebelum dibuang.')
        await message.channel.send('Pencemaran udara')
        await message.channel.send('Mengurangi penggunaan kendaraan pribadi dengan memilih transportasi publik, berjalan kaki, atau bersepeda.')
        await message.channel.send('Meningkatkan efisiensi energi dengan menggunakan peralatan listrik yang hemat energi.')
        await message.channel.send('Memastikan penggunaan bahan bakar yang bersih dan ramah lingkungan seperti gas alam atau energi terbarukan.')
        await message.channel.send('Pencemaran tanah')
        await message.channel.send('Mengelola limbah secara aman dan sesuai dengan peraturan yang berlaku.')
        await message.channel.send('Menggunakan bahan kimia dengan bijaksana, termasuk pengelolaan dan pembuangan yang tepat.')
        await message.channel.send('Menghindari penggunaan pupuk atau pestisida yang berlebihan di pertanian.')
        
        await message.channel.send('Tekan "polusi" untuk mengetahui artinya')
        await message.channel.send('Tekan "a" untuk mencari macam macam polusi')
        
        
client.run('Your token')   
   
   
   
   

