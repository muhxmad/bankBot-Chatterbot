from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Bot',storage_adapter='chatterbot.storage.SQLStorageAdapter',trainer='chatterbot.trainers.ListTrainer')
for file in os.listdir('data/'):
    convData = open('./data/' + file, 'r', encoding='latin-1').readlines()
    bot.set_trainer(ListTrainer)
    bot.train(convData)
