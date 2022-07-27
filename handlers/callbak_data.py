from aiogram import types
from misc import dp, bot
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from .sqlit import update_country,cheak_traf,reg_user,cheak_chat_id,get_country
import random

reg_user(0)

content_chat = -1001523112454


text_stop = """Аяяй я смотрю, кто-то решил
пошалить 😏

Сначала смотри видос, а потом нажимай))👌"""

markup = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='СПРИНТ💸', callback_data='pognali')
markup.add(bat_a)

markup_2 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='🔥Дальше🔥', callback_data='next')
markup_2.add(bat_a)

markup_3 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='🔥Начинаем🔥', callback_data='go_start')
markup_3.add(bat_a)

markup_4 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='😎оп оп😎', callback_data='go_go')
markup_4.add(bat_a)

markup_5 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='🔥 Едем дальше 🔥', callback_data='train_go')
markup_5.add(bat_a)

markup_6 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Готово✅', callback_data='ready')
markup_6.add(bat_a)


markup_test = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='А', callback_data='a')
bat_b = types.InlineKeyboardButton(text='Б', callback_data='b')
bat_v = types.InlineKeyboardButton(text='В', callback_data='v')
markup_test.add(bat_a,bat_b,bat_v)

markup_open_test = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Тест', callback_data='open_test')
markup_open_test.add(bat_a)


#КЛАВИАТУРЫ ДЛЯ ВТОРОГО ПРОГРЕВА
markup_finish = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Гоо', callback_data='finish_go')
markup_finish.add(bat_a)


markup2_go = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Давай', callback_data='2_go')
markup2_go.add(bat_a)

markup_go_12_1 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Гоо🚀', callback_data='go_12_1')
markup_go_12_1.add(bat_a)

markup_go_12_2 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='ДАВАЙ', callback_data='go_12_2')
markup_go_12_2.add(bat_a)

markup_go_12_3 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='А как?', callback_data='go_12_3')
markup_go_12_3.add(bat_a)

markup_go_12_4 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_12_4')
markup_go_12_4.add(bat_a)

markup_go_12_44 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Дальше 🚀', callback_data='go_12_44')
markup_go_12_44.add(bat_a)

markup_go_12_5 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='КАК?', callback_data='go_12_5')
markup_go_12_5.add(bat_a)

markup_go_18_1 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Гоо🚀', callback_data='go_18_1')
markup_go_18_1.add(bat_a)

markup_go_18_2 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='ДАВАЙ', callback_data='go_18_2')
markup_go_18_2.add(bat_a)

markup_go_18_3 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='А как?', callback_data='go_18_3')
markup_go_18_3.add(bat_a)

markup_go_18_4 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_18_4')
markup_go_18_4.add(bat_a)

markup_go_18_44 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Дальше 🚀', callback_data='go_18_44')
markup_go_18_44.add(bat_a)

markup_go_18_5 = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='КАК?', callback_data='go_18_5')
markup_go_18_5.add(bat_a)

markup3_go = types.InlineKeyboardMarkup()
bat_a20 = types.InlineKeyboardButton(text='20', callback_data='s_20')
bat_a50 = types.InlineKeyboardButton(text='50', callback_data='s_50')
bat_a100 = types.InlineKeyboardButton(text='100', callback_data='s_100')
markup3_go.add(bat_a20,bat_a50,bat_a100)

markup_summa20 = types.InlineKeyboardMarkup()
bat_summa20 = types.InlineKeyboardButton(text='Сумма', callback_data='summa_20')
markup_summa20.add(bat_summa20)

markup_summa50 = types.InlineKeyboardMarkup()
bat_summa50 = types.InlineKeyboardButton(text='Сумма', callback_data='summa_50')
markup_summa50.add(bat_summa50)

markup_summa100 = types.InlineKeyboardMarkup()
bat_summa100 = types.InlineKeyboardButton(text='Сумма', callback_data='summa_100')
markup_summa100.add(bat_summa100)

markup4_go = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Давай', callback_data='4_go')
markup4_go.add(bat_a)

markup5_go = types.InlineKeyboardMarkup()
bat_a = types.InlineKeyboardButton(text='Давай', callback_data='5_go')
markup5_go.add(bat_a)


class st(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()
    step4 = State()
    step5 = State()


@dp.callback_query_handler(lambda call: True, state='*')
async def answer_push_inline_button(call, state: FSMContext):
    if call.data == 'go_12':
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat,message_id=108,reply_markup=markup_go_12_1)
    if call.data == 'go_12_1':
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=109)
        await asyncio.sleep(4)
        await bot.send_message(chat_id=call.message.chat.id, text = """Некоторые смотрят на меня и думают: «блин, офигенно живёт. Ну вот же чел… оч повезло наверное. Возможно начал на мамины деньги»""")
        await asyncio.sleep(3)
        await bot.send_message(chat_id=call.message.chat.id, text = """- Рассказать правду, как я начал на мамины деньги?""",reply_markup=markup_go_12_2)
    if call.data == 'go_12_2':
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=110)
        await bot.send_message(chat_id=call.message.chat.id, text = """А вот них@@@яяя не на мамины! 😂""",reply_markup=markup_go_12_3)
    if call.data == 'go_12_3':
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=111,reply_markup=markup_go_12_4)
    if call.data == 'go_12_4':
        await bot.send_message(chat_id=call.message.chat.id, text="""Ну вот так и было. Еле работающий телефон, одежда с рынка (я конечно очень благодарен своим родным, что всегда был сыт и обут)
Но моим амбициям нужно было больше…

Внизу покажу реакцию с момента, когда я сделал первый большой подарок семье- 110.000₽. Взгляни, и продолжим про заработок, чтобы ты сделал(а) также.""")
        await asyncio.sleep(7)
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=113,reply_markup=markup_go_12_44)

    if call.data == 'go_12_44':
        await bot.send_message(chat_id=call.message.chat.id,text="""На дворе 2022 год. И да… начался он невесело… А что же будет дальше?

Не хочу вас пугать, но вот простой факт:""")
        await asyncio.sleep(3)
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=112,reply_markup=markup_go_12_5)
    if call.data == 'go_12_5':
        await bot.send_message(chat_id=call.message.chat.id, text="""Я нашёл простой способ, как без вложений в технику и рекламу, научиться зарабатывать от 400$. Причём получится даже, если у тебя нету никаких знаний и умений в интернет заработке! Справляются даже подростки-школьники🤯

Всё это благодаря уникальному механизму СПРИНТ""")
        await asyncio.sleep(4)
        await bot.send_message(chat_id=call.message.chat.id,text="""Предвижу твой вопрос, что за спринт, что надо делать, смогу ли я  зарабатывать?

Жми на кнопку👇 и я подробно расскажу и покажу""",reply_markup=markup)




    if call.data == 'go_18':
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=114,reply_markup=markup_go_18_1)
    if call.data == 'go_18_1':
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=116)
        await asyncio.sleep(4)
        await bot.send_message(chat_id=call.message.chat.id,
                               text="""Некоторые смотрят на меня и думают: «блин, офигенно живёт. Ну вот же чел… оч повезло наверное. Возможно начал на мамины деньги»""")
        await asyncio.sleep(3)
        await bot.send_message(chat_id=call.message.chat.id,
                               text="""- Рассказать правду, как я начал на мамины деньги?""",
                               reply_markup=markup_go_18_2)
    if call.data == 'go_18_2':
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=121)
        await bot.send_message(chat_id=call.message.chat.id, text="""А вот них@@@яяя не на мамины! 😂""",
                               reply_markup=markup_go_18_3)
    if call.data == 'go_18_3':
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=123,
                               reply_markup=markup_go_18_4)
    if call.data == 'go_18_4':
        await bot.send_message(chat_id=call.message.chat.id, text="""Ну вот так и было. Самый простой телефон, нету доходов, обычная  одежда( я очень благодарен своим родным, что всегда был сыт и обут). Но моим амбициям нужно было больше… 
Внизу покажу реакцию с момента, когда я сделал первый большой подарок семье- 110.000₽. Взгляни, и продолжим про заработок, чтобы ты сделал(а) также.""")
        await asyncio.sleep(7)
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=127,
                               reply_markup=markup_go_18_44)

    if call.data == 'go_18_44':
        await bot.send_message(chat_id=call.message.chat.id, text="""На дворе 2022 год. И да… начался он невесело… А что же будет дальше?

Не хочу вас пугать, но вот простой факт:""")
        await asyncio.sleep(3)
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=131,
                               reply_markup=markup_go_18_5)
    if call.data == 'go_18_5':
        await bot.send_message(chat_id=call.message.chat.id, text="""Я нашёл простой способ, как без вложений в технику и рекламу, научиться зарабатывать от 400$. Причём получится даже, если у тебя нету никаких знаний и умений в интернет заработке!
Люди уходят с найма и  делают здесь деньги.

Всё это благодаря уникальному механизму СПРИНТ""")
        await asyncio.sleep(6)
        await bot.send_message(chat_id=call.message.chat.id, text="""Предвижу твой вопрос, что за спринт, что надо делать, смогу ли я  зарабатывать?

Жми на кнопку👇 и я подробно расскажу и покажу""", reply_markup=markup)





    if call.data == 'pognali':
        await state.update_data(video1='stop')
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat,message_id=38,reply_markup=markup_2)
        await asyncio.sleep(21/2)  # 210 секунд
        await state.update_data(video1='start')


    if call.data == 'next':
        try:
            if ((await state.get_data())['video1']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat,caption= """Так делаю я, и каждый, кто ЕбаШит в спринте. Поэтому,если ты готов начать делать деньги в интернете жми 👇👇👇 ( уже не терпится начать разьёбчик)""",message_id=40,reply_markup=markup_3)


    if call.data == 'go_start':
        await state.update_data(video2='stop')
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat,message_id=43,reply_markup=markup_4)
        await asyncio.sleep(70)
        await state.update_data(video2='start')

    if call.data == 'go_go':
        try:
            if ((await state.get_data())['video2']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            await state.update_data(video3='stop')
            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=45,reply_markup=markup_open_test)
            await asyncio.sleep(75)
            await state.update_data(video3='start')

    if call.data == 'open_test':
        try:
            if ((await state.get_data())['video3']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            await bot.send_message(chat_id=call.message.chat.id, text="""Арбитраж трафика это?
А) Перевод человека из одного места в другое за определённый % от прибыли
Б) Продажа товаров в интернете 
В) Помощь новичку заработать в интернете""",reply_markup=markup_test)


    if call.data == 'b' or call.data == 'v': #НЕправильный ответ
        await bot.send_message(text="""Нет, это не арбитраж. Попробуй ещё раз""", chat_id=call.message.chat.id)


    if call.data == 'a':
        await bot.send_message(text="""Красава😎 Двигаемся дальше""", chat_id=call.message.chat.id)
        await asyncio.sleep(2)
        await state.update_data(video4='stop')

        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=54,reply_markup=markup_5)
        await asyncio.sleep(100)
        await state.update_data(video4='start')


    if call.data == 'train_go':
        try:
            if ((await state.get_data())['video4']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            await bot.send_message(text="""Сейчас создадим с тобой телеграм канал, который в дальнейшем пригодится для заработка 😎""", chat_id=call.message.chat.id)
            await asyncio.sleep(3)
            await state.update_data(video5='stop')
            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=76,reply_markup=markup_6)
            await asyncio.sleep(30)
            await state.update_data(video5='start')


    if call.data == 'ready':
        try:
            if ((await state.get_data())['video5']) == 'start':
                flag = True
            else:
                flag = False

        except:
            flag = True

        if flag == False:
            await call.message.answer(text_stop)

        else:
            await bot.send_message(text="""Молодец, ты почти дошёл до основного Спринта, а значит и до заработка денег😎""",chat_id=call.message.chat.id)
            await asyncio.sleep(3)
            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=106,caption="Мой телеграм👉 @VadimSprint")
            await asyncio.sleep(260)
            await bot.send_message(chat_id=call.message.chat.id, text = """Отзывы про Спринт(если хочешь,почитай😋)
👇👇👇👇👇
https://t.me/otzivisprint/23""")
            await asyncio.sleep(360)
            await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=101)
            await asyncio.sleep(7)
            await bot.send_message(chat_id=call.message.chat.id, text = """Мой тг👇
🚀 @VadimSprint 🚀""")
            update_country(id= call.message.chat.id, country = 'one')
            await asyncio.sleep(86400)
            await bot.send_message(chat_id=call.message.chat.id, text="""Хэй, привет! А давай посчитаем сколько ты можешь заработать в спринте💸?""",reply_markup = markup2_go)

    print(call.data)
    if call.data == '2_go':
        await bot.send_message(chat_id=call.message.chat.id, text="""Как думаешь, сколько ты готов загружать роликов в тик ток за день?""",reply_markup=markup3_go)

    if call.data == 's_20':
        await bot.send_message(chat_id=call.message.chat.id, text="""Окей, 20 роликов это примерно 500 трафика, один трафик это 0,5 руб. То есть получается сумма👇""",reply_markup=markup_summa20)

    if call.data == 'summa_20':
        await bot.send_message(chat_id=call.message.chat.id,text="""Это 250р. За день!Просто загрузив ролики в тт🤯. И кто тебе мешает загрузить в 2 раза больше роликов? Это ведь легко

Ноо это всего лишь предположие, ведь ролики могут залететь на много млн просмотров и будет в разы больше трафика🔥Такое кстати часто происходит""",reply_markup= markup_finish)

    if call.data == 's_50':
        await bot.send_message(chat_id=call.message.chat.id, text="""Окей, 50 роликов это примерно 1000 трафика, один трафик это 0,5 руб. То есть получается сумма👇""",reply_markup=markup_summa50)

    if call.data == 'summa_50':
        await bot.send_message(chat_id=call.message.chat.id, text="""Это 500 руб. За день! Просто загрузив ролики в тт🤯. И кто тебе мешает загрузить в 2 раза больше роликов? Это ведь легко

Ноо это всего лишь предположие, ведь ролики могут залететь на много млн просмотров и будет в разы больше трафика🔥Такое кстати часто происходит""",reply_markup=markup_finish)

    if call.data == 's_100':
        await bot.send_message(chat_id=call.message.chat.id, text="""Окей, 100 роликов это примерно 2000 трафика, один трафик это 0,5 руб. То есть получается сумма👇""",reply_markup=markup_summa100)

    if call.data == 'summa_100':
        await bot.send_message(chat_id=call.message.chat.id, text="""Это 1000 руб. За день! Просто загрузив ролики в тт🤯. И кто тебе мешает загрузить в 2 раза больше роликов? Это ведь легко

Ноо это всего лишь предположие, ведь ролики могут залететь на много млн просмотров и будет в разы больше трафика🔥Такое кстати часто происходит!""",reply_markup=markup_finish)

    await bot.answer_callback_query(callback_query_id=call.id)

    if call.data == 'finish_go':
        update_country(id=call.message.chat.id, country='two')
        await bot.copy_message(chat_id=call.message.chat.id, from_chat_id=content_chat, message_id=105)
        await asyncio.sleep(15)
        await bot.send_message(chat_id=call.message.chat.id, text= """@VadimSprint
Мой тг☝️. Погнали💸🚀""")






