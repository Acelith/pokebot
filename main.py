from telebot import *
from credentials import bot_credentials
import json
import pokebase 
from pokebase import cache
cache.API_CACHE

# Inizializzazione del bot 
pokebot = telebot.TeleBot(bot_credentials["token"])

@pokebot.message_handler(commands=['start'])
def send_welcome(message):
    pokebot.reply_to(
        message, "Avvio in corso ... bibubububbip ... scrivi /help per gli aiuti ai comandi")


@pokebot.message_handler(commands=['help'])
def help(message):
    markup = types.InlineKeyboardMarkup()
    button_img = types.InlineKeyboardButton(
        text='/poke - Per cercare un pokemon', callback_data="/poke ")
    markup.add(button_img)
    button_src = types.InlineKeyboardButton(
        text='/rdmpoke - Per cercare un pokemon random', callback_data="/rdmpoke ")
    markup.add(button_src)
    pokebot.send_message(
        message.chat.id, "Di segutio i comandi", reply_markup=markup)


@pokebot.message_handler(commands=['poke'])
def img(message):
    json_result = pixivCrawler.illust_ranking('day')
    len_illust = len(json_result.illusts)
    illustN = random.randint(0, len_illust)
    pokebot.reply_to(message, json_result.illusts[illustN].image_urls.medium)


@pokebot.message_handler(commands=['rdmpoke'])
def src(message):
    sent_msg = pokebot.send_message(
        message.chat.id, "Cerco un pokemon random ...")
    sent_msg = pokebot.send_message(getPokemon())


def getPokemon(p_pokemon = None):
    if p_pokemon == None:
        pokemon = pokebase.pokemon("pickachu")
    else:
        pokemon = pokebase.pokemon(p_pokemon)
    return pokemon.natural_gift_type.name

pokebot.infinity_polling()

