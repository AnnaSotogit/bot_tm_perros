import discord
from discord.ext import commands
from model import get_class
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix= '|', intents=intents)

@bot.event
async def on_ready():
    print(f'Holaaa!! Nos hemos logueado con la cuenta con el nombre de {bot.user}')

@bot.command()
async def descripcion(ctx):
    await ctx.send("Este proyecto consiste en un bot de Discord que utiliza un modelo de clasificación de imágenes creado en Teachable Machine. El bot permite a los usuarios subir una imagen de un perro y recibe, como respuesta, el porcentaje de probabilidad de que la raza de la mascota en la imagen sea Beagle, Poodle o Pug El modelo fue entrenado con ejemplos de estas tres razas para reconocerlas y diferenciar entre ellas. Esto se desarrolló en Visual Studio Code, donde se integró el modelo de Teachable Machine para su uso en Discord. Al recibir una imagen, el bot procesa la foto, ejecuta la clasificación y responde en el canal de Discord con los porcentajes correspondientes a cada raza.")

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("ups! aun no has subido ninguna foto")

bot.run('...')