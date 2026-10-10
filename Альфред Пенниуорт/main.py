import telebot
from telebot import types
from telebot.types import *
import buttons
import databse

bot = telebot.TeleBot('7538042011:AAE7jZYUjdugSZA0PSvNY5X9SoVbluvBfPw')

@bot.message_handler(commands=['start'])
def starting_def(message):
    user_id = message.from_user.id

    bot.send_photo(user_id, 'AgACAgIAAxkBAANVZ6ZkccNY2uMGMtAMjh96qpC3TTMAAjzpMRtNkDFJB7kaT_Az70QBAAMCAAN5AAM2BA', 'Приветствую тебя!\n\nЯ — Альфред Пенниуорт, бот, который может помочь упростить задачи в разных сферах жизни и улучшить твою жизнь!', reply_markup=buttons.starting_buttons())

#     bot.register_next_step_handler(message, hz)
# def hz(message):
#     user_id = message.from_user.idё
#     print(message.photo[-1].file_id)

@bot.message_handler(content_types=['text'])
def texts_def(message):
    user_id = message.from_user.id

    if message.text == 'Развития':
        bot.send_message(user_id, 'Выберите действие:', reply_markup=buttons.development_buttons())
        bot.register_next_step_handler(message, development_def)
    elif message.text == 'Задачи':
        bot.send_message(user_id, 'Выберите действие:', reply_markup=buttons.development_buttons())
    elif message.text == 'Мотивация':
        bot.send_message(user_id, 'Выберите действие:', reply_markup=buttons.motivation_buttons(user_id))
        bot.register_next_step_handler(message, motivation_def)
    elif message.text == 'Другое':
        bot.send_message(user_id, 'Ещё основных функций нет, откуда другие')
    elif message.text == 'Помощь':
        bot.send_message(user_id, 'Спасибо за помощь!')
    else:
        bot.send_message(user_id, 'Нажмите на одну из кнопок')
        bot.register_next_step_handler(message, texts_def)


def tasks_def(message):
    pass


def development_def(message):
    user_id = message.from_user.id

    if message.text == 'Новая сфера':
        bot.send_message(user_id, 'Как хотите назвать новую сферу развития?', reply_markup=buttons.back_button())
        bot.register_next_step_handler(message, new_development_def)
    elif message.text == 'Мои сферы':
        user_developments = databse.getting_all_developments_by_tg_id(user_id)
        if len(user_developments) != 0:
            n = 0
            text = ''
            for i in user_developments:
                n += 1
                text += f'{n}. {i[1]}({i[2]}/{i[3]})\n'
            bot.send_message(user_id, f'{text}', reply_markup=buttons.all_user_developments_numbers(n))
            bot.register_next_step_handler(message, users_one_development)
        else:
            bot.send_message(user_id, 'У вас пока нет сфер развития!')
            bot.register_next_step_handler(message, development_def)
    elif message.text == 'Назад':
        bot.send_photo(user_id, 'AgACAgIAAxkBAANVZ6ZkccNY2uMGMtAMjh96qpC3TTMAAjzpMRtNkDFJB7kaT_Az70QBAAMCAAN5AAM2BA', 'Приветствую тебя!\n\nЯ — Альфред Пенниуорт, бот, который может помочь упростить задачи в разных сферах жизни и улучшить твою жизнь!', reply_markup=buttons.starting_buttons())
        bot.register_next_step_handler(message, texts_def)
    else:
        bot.send_message(user_id, 'Нажмите на одну из кнопок')
        bot.register_next_step_handler(message, development_def)

def new_development_def(message):
    user_id = message.from_user.id

    all_developments_names_from_data = databse.getting_all_developments_by_tg_id(user_id)
    n = 0
    for i in range(len(all_developments_names_from_data)):
        if message.text == all_developments_names_from_data[i][1]:
            n += 1
            bot.send_message(user_id, 'Развитие с таким именем уже существует!')
            bot.send_message(user_id, 'Назовите как-то по другому!')
            bot.register_next_step_handler(message, new_development_def)
    if n == 0:
        if message.text == 'Назад':
            bot.send_message(user_id, 'Выберите действие:', reply_markup=buttons.development_buttons())
            bot.register_next_step_handler(message, development_def)
        else:
            name = message.text
            bot.send_message(user_id, 'Каким будет максимальный уровень в этой сфере?')
            bot.register_next_step_handler(message, max_level_of_development_def, name)

def max_level_of_development_def(message, name):
    user_id = message.from_user.id

    if message.text == 'Назад':
        bot.send_message(user_id, 'Как хотите назвать новую сферу развития?', reply_markup=buttons.back_button())
        bot.register_next_step_handler(message, new_development_def)
    else:
        try:
            max_level = int(message.text)
            try:
                if max_level > 0:
                    bot.send_message(user_id, 'Какова ваша конечная цель?')
                    bot.register_next_step_handler(message, final_goal_of_development_def, name, max_level)
            except:
                bot.send_message(user_id, 'Минимальный уровень "1"')
                bot.register_next_step_handler(message, max_level_of_development_def, name)
        except:
            bot.send_message(user_id, 'Введите число')
            bot.register_next_step_handler(message, max_level_of_development_def, name)

def final_goal_of_development_def(message, name, max_level):
    user_id = message.from_user.id

    if message.text == 'Назад':
        bot.send_message(user_id, 'Каким будет максимальный уровень в этой сфере?')
        bot.register_next_step_handler(message, max_level_of_development_def, name)
    else:
        final_goal = message.text
        bot.send_message(user_id, 'Назовите причину, почему вы хотите развиться в этой сфере?')
        bot.register_next_step_handler(message, reason_of_development_def, name, max_level, final_goal)

def reason_of_development_def(message, name, max_level, final_goal):
    user_id = message.from_user.id

    if message.text == 'Назад':
        bot.send_message(user_id, 'Какова ваша конечная цель?')
        bot.register_next_step_handler(message, final_goal_of_development_def, name, max_level)
    else:
        reason = message.text
        bot.send_message(user_id, f'Название: {name}\nМаксимальный уровень: {max_level}\nКонечная цель: {final_goal}\nПричина: {reason}\n\nПравильная ли информация?', reply_markup=buttons.yes_no_buttons())
        bot.register_next_step_handler(message, saving_new_development_def, name, max_level, final_goal, reason)

def saving_new_development_def(message, name, max_level, final_goal, reason):
    user_id = message.from_user.id

    if message.text == 'Да':
        databse.adding_new_development_to_db(user_id, name, 0, max_level, final_goal, reason)
        bot.send_message(user_id, 'Сохранено!')
        bot.send_message(user_id, 'Выберите действие:', reply_markup=buttons.development_buttons())
        bot.register_next_step_handler(message, development_def)
    elif message.text == 'Нет':
        bot.send_message(user_id, 'Какая информация не правильная?', reply_markup=buttons.all_stats_of_development_buttons())
        bot.register_next_step_handler(message, editing_new_development_def, name, max_level, final_goal, reason)

def editing_new_development_def(message, name, max_level, final_goal, reason):
    user_id = message.from_user.id

    if message.text == 'Название':
        bot.send_message(user_id, 'Какое название хотите дать?', reply_markup=buttons.back_button())
        bot.register_next_step_handler(message, changing_name_of_development, name, max_level, final_goal, reason)
    elif message.text == 'Максимальный уровень':
        bot.send_message(user_id, 'Какой максимальный уровень хотите поставить?', reply_markup=buttons.back_button())
        bot.register_next_step_handler(message, changing_max_level_of_development, name, max_level, final_goal, reason)
    elif message.text == 'Конечная цель':
        bot.send_message(user_id, 'Какую конечную цель хотите поставить?', reply_markup=buttons.back_button())
        bot.register_next_step_handler(message, changing_final_goal_of_development, name, max_level, final_goal, reason)
    elif message.text == 'Причина':
        bot.send_message(user_id, 'На какую причину хотите поменять?', reply_markup=buttons.back_button())
        bot.register_next_step_handler(message, changing_reason_of_development, name, max_level, final_goal, reason)
    elif message.text == 'Назад':
        bot.send_message(user_id, f'Название: {name}\nМаксимальный уровень: {max_level}\nКонечная цель: {final_goal}\nПричина: {reason}\n\nПравильная ли информация?', reply_markup=buttons.yes_no_buttons())
        bot.register_next_step_handler(message, saving_new_development_def, name, max_level, final_goal, reason)
    elif message.text == 'Удалить':
        bot.send_message(user_id, 'Удалено!')
        bot.send_message(user_id, 'Выберите действие:', reply_markup=buttons.development_buttons())
        bot.register_next_step_handler(message, development_def)
    else:
        bot.send_message(user_id, 'Нажмите на одну из кнопок!')
        bot.register_next_step_handler(message, editing_new_development_def, name, max_level, final_goal, reason)

def changing_name_of_development(message, name, max_level, final_goal, reason):
    user_id = message.from_user.id
    if message.text == 'Назад':
        bot.send_message(user_id, 'Какая информация не правильная?', reply_markup=buttons.all_stats_of_development_buttons())
        bot.register_next_step_handler(message, editing_new_development_def, name, max_level, final_goal, reason)
    else:
        name = message.text
        bot.send_message(user_id, f'Название: {name}\nМаксимальный уровень: {max_level}\nКонечная цель: {final_goal}\nПричина: {reason}\n\nПравильная ли информация?', reply_markup=buttons.yes_no_buttons())
        bot.register_next_step_handler(message, saving_new_development_def, name, max_level, final_goal, reason)

def changing_max_level_of_development(message, name, max_level, final_goal, reason):
    user_id = message.from_user.id
    if message.text == 'Назад':
        bot.send_message(user_id, 'Какая информация не правильная?', reply_markup=buttons.all_stats_of_development_buttons())
        bot.register_next_step_handler(message, editing_new_development_def, name, max_level, final_goal, reason)
    else:
        max_level = message.text
        bot.send_message(user_id, f'Название: {name}\nМаксимальный уровень: {max_level}\nКонечная цель: {final_goal}\nПричина: {reason}\n\nПравильная ли информация?', reply_markup=buttons.yes_no_buttons())
        bot.register_next_step_handler(message, saving_new_development_def, name, max_level, final_goal, reason)

def changing_final_goal_of_development(message, name, max_level, final_goal, reason):
    user_id = message.from_user.id
    if message.text == 'Назад':
        bot.send_message(user_id, 'Какая информация не правильная?', reply_markup=buttons.all_stats_of_development_buttons())
        bot.register_next_step_handler(message, editing_new_development_def, name, max_level, final_goal, reason)
    else:
        final_goal = message.text
        bot.send_message(user_id, f'Название: {name}\nМаксимальный уровень: {max_level}\nКонечная цель: {final_goal}\nПричина: {reason}\n\nПравильная ли информация?', reply_markup=buttons.yes_no_buttons())
        bot.register_next_step_handler(message, saving_new_development_def, name, max_level, final_goal, reason)

def changing_reason_of_development(message, name, max_level, final_goal, reason):
    user_id = message.from_user.id
    if message.text == 'Назад':
        bot.send_message(user_id, 'Какая информация не правильная?', reply_markup=buttons.all_stats_of_development_buttons())
        bot.register_next_step_handler(message, editing_new_development_def, name, max_level, final_goal, reason)
    else:
        reason = message.text
        bot.send_message(user_id, f'Название: {name}\nМаксимальный уровень: {max_level}\nКонечная цель: {final_goal}\nПричина: {reason}\n\nПравильная ли информация?', reply_markup=buttons.yes_no_buttons())
        bot.register_next_step_handler(message, saving_new_development_def, name, max_level, final_goal, reason)

def users_one_development(message):
    user_id = message.from_user.id
    if message.text == 'Назад':
        bot.send_message(user_id, 'Выберите действие:', reply_markup=buttons.development_buttons())
        bot.register_next_step_handler(message, development_def)
    else:
        try:
            n = int(message.text)
            user_developments = databse.getting_all_developments_by_tg_id(user_id)
            e = user_developments[n-1]
            bot.send_message(user_id, f'Название: {e[1]}\nУровень: {e[2]}/{e[3]}\nКонечная цель: {e[4]}\nПричина: {e[5]}', reply_markup=buttons.exact_development_features())
            bot.register_next_step_handler(message, exact_development_changing, e)
        except:
            bot.send_message(user_id, 'Введите число')

def exact_development_changing(message, e):
    user_id = message.from_user.id

    if message.text == 'Улучшить':
        bot.send_message(user_id, 'Что вы сделали, что-бы улучшить эту сферу?',reply_markup=buttons.back_button())
        bot.register_next_step_handler(message, level_up_exact_development, e)
    elif message.text == 'Подробности улучшений':
        podrobnosti = databse.getting_actions_to_level_up_development(user_id, e[1])
        text = f'Подробности сферы \'{e[1]}\':\n\n'
        if len(podrobnosti) == 0:
            text += 'Вы ещё не улучшали эту сферу!'
        else:
            for i in podrobnosti:
                text += f'{podrobnosti[0][3]}: {podrobnosti[0][2]}\n'
        bot.send_message(user_id, f'{text}')
        bot.register_next_step_handler(message, exact_development_changing, e)
    elif message.text == 'Изменить':
        bot.send_message(user_id, 'Какую информацию хотите изменить?', reply_markup=buttons.all_stats_of_development_buttons())
        bot.register_next_step_handler(message, editing_development_def, e)
    elif message.text == 'Назад':
        user_developments = databse.getting_all_developments_by_tg_id(user_id)
        n = 0
        text = ''
        for i in user_developments:
            n += 1
            text += f'{n}. {i[1]}({i[2]}/{i[3]})\n'
        bot.send_message(user_id, f'{text}', reply_markup=buttons.all_user_developments_numbers(n))
        bot.register_next_step_handler(message, users_one_development)
    elif message.text == 'Удалить':
        databse.deleting_exact_development(user_id, e[1])
        bot.send_message(user_id, 'Удалено!')
        bot.send_message(user_id, 'Выберите действие:', reply_markup=buttons.development_buttons())
        bot.register_next_step_handler(message, development_def)

def level_up_exact_development(message, e):
    user_id = message.from_user.id

    if message.text == 'Назад':
        bot.send_message(user_id, f'Название: {e[1]}\nУровень: {e[2]}/{e[3]}\nКонечная цель: {e[4]}\nПричина: {e[5]}', reply_markup=buttons.exact_development_features())
        bot.register_next_step_handler(message, exact_development_changing, e)
    else:
        databse.adding_action_to_level_up(user_id, e[1], message.text, int(e[2])+1)
        bot.send_message(user_id, 'Улучшено!')
        user_developments = databse.getting_all_developments_by_tg_id(user_id)
        n = 0
        text = ''
        for i in user_developments:
            n += 1
            text += f'{n}. {i[1]}({i[2]}/{i[3]})\n'
        bot.send_message(user_id, f'{text}', reply_markup=buttons.all_user_developments_numbers(n))
        bot.register_next_step_handler(message, users_one_development)

def motivation_def(message):
    user_id = message.from_user.id

    if message.text == 'Личные':
        bot.send_message(user_id, 'Выберите действие:', reply_markup=buttons.user_motivations_buttons())
        bot.register_next_step_handler(message, users_motivations)
    elif message.text == 'Рандом':
        pass
    elif message.text == 'Назад':
        bot.send_photo(user_id, 'AgACAgIAAxkBAANVZ6ZkccNY2uMGMtAMjh96qpC3TTMAAjzpMRtNkDFJB7kaT_Az70QBAAMCAAN5AAM2BA', 'Приветствую тебя!\n\nЯ — Альфред Пенниуорт, бот, который может помочь упростить задачи в разных сферах жизни и улучшить твою жизнь!', reply_markup=buttons.starting_buttons())
        bot.register_next_step_handler(message, texts_def)
    elif message.text == 'Временные' and user_id == 7445671893:
        pass

def users_motivations(message):
    user_id = message.from_user.id

    if message.text == 'Новый':
        bot.send_message(user_id, 'Напишите новое мотивационную надпись:', reply_markup=buttons.back_button())
        bot.register_next_step_handler(message, users_new_motivation)
    elif message.text == 'Существующие':
        pass
    elif message.text == 'Назад':
        bot.send_message(user_id, 'Выберите действие:', reply_markup=buttons.motivation_buttons())
        bot.register_next_step_handler(message, motivation_def)

def users_new_motivation(message):
    user_id = message.from_user.id

    if message.text == 'Назад':
        bot.send_message(user_id, 'Выберите действие:', reply_markup=buttons.user_motivations_buttons())
        bot.register_next_step_handler(message, users_motivations)
    else:
        motivation = message.text
        bot.send_message(user_id, 'Выберите статус:', reply_markup=buttons.choosing_status_of_motivation_buttons())
        bot.register_next_step_handler(message, choosing_status_of_motivation_def, motivation)

def choosing_status_of_motivation_def(message, motivation):
    user_id = message.from_user.id

    if message.text == 'Назад':
        bot.send_message(user_id, 'Напишите новое мотивационную надпись:', reply_markup=buttons.back_button())
        bot.register_next_step_handler(message, users_new_motivation)
    elif message.text == 'Локальный':
        databse.adding_motivational_text_to_db(user_id, motivation, message.text)
        bot.send_message(user_id, 'Сохранено!')
        bot.send_message(user_id, 'Выберите действие:', reply_markup=buttons.motivation_buttons())
        bot.register_next_step_handler(message, motivation_def)
    elif message.text == 'Глобальный':
        bot.send_message(7445671893, 'Подтвердите мотивационную надпись пользователя')
        databse.adding_motivational_text_to_db(user_id, motivation, 'Временный')
        bot.send_message(user_id, 'Ждем разрешение у админа')
        bot.send_message(user_id, 'Выберите действие:', reply_markup=buttons.motivation_buttons())
        bot.register_next_step_handler(message, motivation_def)

def editing_development_def(message, e):
    user_id = message.from_user.id

    if message.text == 'Название':
        bot.send_message(user_id, 'Какое название хотите дать?', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, changing_name_of_development, e[3], e[4], e[5])
    elif message.text == 'Максимальный уровень':
        bot.send_message(user_id, 'Какой максимальный уровень хотите поставить?', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, changing_max_level_of_development, e[1], e[4], e[5])
    elif message.text == 'Конечная цель':
        bot.send_message(user_id, 'Какую конечную цель хотите поставить?', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, changing_final_goal_of_development, e[1], e[3], e[5])
    elif message.text == 'Причина':
        bot.send_message(user_id, 'На какую причину хотите поменять?', reply_markup=ReplyKeyboardRemove())
        bot.register_next_step_handler(message, changing_reason_of_development, e[1], e[3], e[4])
    elif message.text == 'Назад':
        bot.send_message(user_id, f'Название: {e[1]}\nУровень: {e[2]}/{e[3]}\nКонечная цель: {e[4]}\nПричина: {e[5]}', reply_markup=buttons.exact_development_features())
        bot.register_next_step_handler(message, exact_development_changing, e)
    elif message.text == 'Удалить':
        databse.deleting_exact_development(user_id, e[1])
        bot.send_message(user_id, 'Удалено!')
        bot.send_message(user_id, 'Выберите действие:', reply_markup=buttons.development_buttons())
        bot.register_next_step_handler(message, development_def)
    else:
        pass
































bot.polling(non_stop=True)