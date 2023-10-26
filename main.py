import config
from aiogram import Bot, types, Dispatcher, executor

bot = Bot(token=config.token)
dp = Dispatcher(bot)

# @dp.message_handler()
# async def echobot(message: types.Message):
#     await message.answer(message.text)

words = []
with open('math.txt') as input:
    for word in input:
        words.append(''.join(word.lower().strip()))


@dp.message_handler(commands=['start', 'help'])
async def statr(message: types.Message):
    await message.answer('HEllO!')


@dp.message_handler()
async def filter_message(message: types.Message):
    for word1 in message.text.lower().split():
        if word1 in words:
            await message.delete()


@dp.message_handler(content_types=['new_chat_members'])
async def new_chat(message: types.Message):
    await message.delete()
    await message.answer(f'welcome ' + message.from_user.full_name)


@dp.message_handler(content_types=['left_chat_member'])
async def left_chat(message: types.Message):
    await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp)
