import discord

from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)



@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def Naber(ctx):
    await ctx.send(f'Sorduğun için teşekkürler {bot.user}, ve sana yardımcı olmaya hazırım!')



@bot.command()
async def plastik_el_isi(ctx):
    fikirler = [
        "Plastik şişelerin alt kısmını kesip boyayarak masa üstü düzenleyicisi olarak kullanabilirsin.Boyama, desen ekleme veya renkli bantlarla süsleyebilirsin.",
        "Şişeleri yatay veya dikey keserek mini saksılar oluşturabilirsin.Delikler açarak fazla suyun akmasını sağlamak bitkilerin sağlığı için iyi olur.",
        "Şeffaf şişelerin içine LED ışıklar koyarak veya delikler açarak ilginç aydınlatmalar yaratabilirsin.Şişenin dışını boyayarak veya iplerle sararak ekstra bir dokunuş katabilirsin.",
        "Dikey olarak kestiğin şişelere mutfak eşyalarını,gereçleri veya çeşitli eşyaları koyabilirsin."

    ]
    await ctx.send(f"Evde yapabileceğin plastik el işleri:\n- " + "\n- ".join(fikirler))


bot.run("token")
