import discord
from discord.ext import commands
from model import get_class
from os import remove

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć! Jestem botem, {bot.user}!')

@bot.command()
async def image(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("Aby ta komenda zadziałała prawidłowo, należy do niej załączyć obrazk (obrazki)")

    for attachment in ctx.message.attachments:
        filename = attachment.filename

        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            await attachment.save(filename)
            await ctx.send(f"Plik {filename} jest przetwarzany")
            result = get_class(filename)
            await ctx.send(f"Wykryta klasa: {result[0]}, pewność: {round(result[1]*100)}%")
            remove(filename)
        else:
            await ctx.send(f"Plik {filename} nie jest w odpowiednim formacie i nie zostanie przetworzony")

bot.run("MTMzMzg0NTYzMDgzMzAwMDUzOQ.GsDTgE.dWD8u7yBdSM9-gIHrQ0wo9rkdsnSakwRMOugO0")