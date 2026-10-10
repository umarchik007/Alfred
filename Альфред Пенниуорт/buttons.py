from telebot.types import *

def starting_buttons():
    kb = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

    developments = KeyboardButton('Развития')
    tasks = KeyboardButton('Задачи')
    motivation = KeyboardButton('Мотивация')
    others = KeyboardButton('Другое')
    help = KeyboardButton('Помощь')

    kb.add(developments, tasks, motivation, others, help)
    return kb

def development_buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    new_one = KeyboardButton('Новая сфера')
    my_spheres = KeyboardButton('Мои сферы')
    back = KeyboardButton('Назад')

    kb.add(new_one, my_spheres, back)
    return kb

def back_button():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    back = KeyboardButton('Назад')

    kb.add(back)
    return kb

def yes_no_buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    yes = KeyboardButton('Да')
    no = KeyboardButton('Нет')

    kb.add(yes, no)
    return kb

def all_stats_of_development_buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    name = KeyboardButton('Название')
    max_level = KeyboardButton('Максимальный уровень')
    final_goal = KeyboardButton('Конечная цель')
    reason = KeyboardButton('Причина')
    back = KeyboardButton('Назад')
    delete = KeyboardButton('Удалить')

    kb.add(name, max_level, final_goal, reason, back, delete)
    return kb

def all_user_developments_numbers(n):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)
    ostatok = n % 5
    j = 0
    if n - ostatok > 0:
        for i in range(int((n-ostatok)/5)):
            q = KeyboardButton(f'{j+1}')
            w = KeyboardButton(f'{j+2}')
            e = KeyboardButton(f'{j+3}')
            r = KeyboardButton(f'{j+4}')
            t = KeyboardButton(f'{j+5}')
            kb.add(q, w, e, r, t)
            j += 5

    if ostatok == 1:
        q = KeyboardButton(f'{n}')
        kb.add(q)
    elif ostatok == 2:
        q = KeyboardButton(f'{n-1}')
        w = KeyboardButton(f'{n}')
        kb.add(q, w)
    elif ostatok == 3:
        q = KeyboardButton(f'{n-2}')
        w = KeyboardButton(f'{n-1}')
        e = KeyboardButton(f'{n}')
        kb.add(q, w, e)
    elif ostatok == 4:
        q = KeyboardButton(f'{n-3}')
        w = KeyboardButton(f'{n-2}')
        e = KeyboardButton(f'{n-1}')
        r = KeyboardButton(f'{n}')
        kb.add(q, w, e, r)
    back = KeyboardButton('Назад')
    kb.add(back)
    return kb

def exact_development_features():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    more_info = KeyboardButton('Подробности улучшений')
    level_up = KeyboardButton('Улучшить')
    change = KeyboardButton('Изменить')
    back = KeyboardButton('Назад')
    delete = KeyboardButton('Удалить')

    kb.add(more_info)
    kb.add(level_up, change, back, delete)
    return kb

def motivation_buttons(tg_id):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)


    my_motivations = KeyboardButton('Личные')
    random_motivation = KeyboardButton('Рандом')
    back = KeyboardButton('Назад')
    if tg_id == 7445671893:
        timed = KeyboardButton('Временные')
        kb.add(timed)
    kb.add(my_motivations, random_motivation, back)
    return kb

def user_motivations_buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    new_one = KeyboardButton('Новый')
    olds = KeyboardButton('Существующие')
    back = KeyboardButton('Назад')

    kb.add(new_one, olds, back)
    return kb

def choosing_status_of_motivation_buttons():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)

    local = KeyboardButton('Локальный')
    global_ = KeyboardButton('Глобальный')
    back = KeyboardButton('Назад')

    kb.add(local, global_, back)
    return kb