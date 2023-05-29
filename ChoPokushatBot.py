import random
import requests
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler, CallbackContext

# Обработчики команд
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Привет! Я могу помочь тебе подобрать рецепт на завтрак, обед или ужин. Введи /breakfast, /lunch или /dinner для получения рецепта.")

def get_recipe_url(meal_type):
    # Получаем URL случайного рецепта выбранного типа приема пищи
    url = f'https://eda.ru/recepty/{meal_type}/sluchajnyj-recept'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    recipe_url = soup.find('a', {'class': 'horizontal-tile__image'}).get('href')
    return recipe_url

def get_recipe_info(recipe_url):
    # Получаем информацию о рецепте по его URL
    response = requests.get(recipe_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.find('h1', {'class': 'recipe__name'}).text.strip()
    ingredients = []
    for ingredient in soup.find_all('span', {'class': 'ingredient__text'}):
        ingredients.append(ingredient.text.strip())
    instructions = []
    for instruction in soup.find_all('div', {'class': 'instruction__description'}):
        instructions.append(instruction.text.strip())
    image_url = soup.find('div', {'class': 'recipe__cover'}).find('img').get('src')
    return title, ingredients, instructions, image_url

def get_random_recipe(meal_type):
    # Получаем случайный рецепт выбранного типа приема пищи
    recipe_url = get_recipe_url(meal_type)
    recipe_info = get_recipe_info(recipe_url)
    return recipe_info

def breakfast(update, context):
    recipe_info = get_random_recipe('zavtrak')
    context.bot.send_photo(chat_id=update.message.chat_id, photo=recipe_info[3], caption=f"{recipe_info[0]}\n\nИнгредиенты:\n{', '.join(recipe_info[1])}\n\nШаги приготовления:\n{', '.join(recipe_info[2])}")

def lunch(update, context):
    recipe_info = get_random_recipe('obed')
    context.bot.send_photo(chat_id=update.message.chat_id, photo=recipe_info[3], caption=f"{recipe_info[0]}\n\nИнгредиенты:\n{', '.join(recipe_info[1])}\n\nШаги приготовления:\n{', '.join(recipe_info[2])}")
def dinner(update, context):
    recipe_info = get_random_recipe('uzhin')
context.bot.send_photo(chat_id=update.message.chat_id, photo=recipe_info[3], caption=f"{recipe_info[0]}\n\nИнгредиенты:\n{', '.join(recipe_info[1])}\n\nШаги приготовления:\n{', '.join(recipe_info[2])}")

def unknown_command(update, context):
context.bot.send_message(chat_id=update.message.chat_id, text="Извините, я не понимаю эту команду. Пожалуйста, введите /breakfast, /lunch или /dinner для получения рецепта.")

def main():
# Инициализируем бота и добавляем обработчики команд
updater = Updater(token='5993160127:AAHPIkBwDFAx0QRvYcgSd1wo-EvdU7-2v-g', use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('breakfast', breakfast))
dispatcher.add_handler(CommandHandler('lunch', lunch))
dispatcher.add_handler(CommandHandler('dinner', dinner))
dispatcher.add_handler(CommandHandler('unknown', unknown_command))
pdater.start_polling()
updater.idle()
if name == 'main':
main()






