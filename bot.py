import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
import db
import logging

logging.basicConfig(#filename="sample.log",
                    level=logging.INFO,
                    #filemode='w',
                    format='%(asctime)s - %(levelname)s - %(message)s',)

API_TOKEN = str(os.environ.get('BOT_TOKEN'))

storage = MemoryStorage()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


class State(StatesGroup):
    add_players = State()
    set_characters = State()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer_sticker(r'CAACAgIAAxkBAAEFkCpi-gSytYxF_YgXZT5CCnqz218lEQACzBkAAl4F0UvjaucGIq3RAykE')
    await message.answer("Вводи имена игроков по одному в сообщении!\n_Когда закончишь жми_ *Далее*!", parse_mode='Markdown')
    await State.add_players.set()
    await state.update_data(players=list())

@dp.message_handler(state=State.add_players, regexp='Далее')
async def add_track(message: types.Message, state: FSMContext):
    data = await state.get_data()
    players = data['players']
    if len(players) == 0:
        await message.answer("Никто не добавлен ((\n_Ещё раз_", parse_mode='Markdown')
        await state.finish()
        await send_welcome(message, state)
    else:
        await message.answer("Теперь добавь персонажей!\n\nЭто могут быть те, кто сейчас в комнате, ваши знакомые и родственники.\nЯ могу дополнить список знаменитостями\n\n _Присылай фото и имя в одном сообщении чтобы добавить своего персонажа_", parse_mode='Markdown')
        await State.set_characters.set()

@dp.message_handler(state=State.add_players)
async def add_player(message: types.Message, state: FSMContext):
    data = await state.get_data()
    players = data['players']
    players.append(message.text)
    await state.update_data(players=players)
    await message.answer('Добавлен')




if __name__ == '__main__':
    print("Starting")
    executor.start_polling(dp, skip_updates=True)
    