import sqlite3

connection = sqlite3.connect('all_data.db')

sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS development_first(tg_id INTEGER, name TEXT, own_level INTEGER, max_level INTEGER, final_goal TEXT, reason TEXT);')

sql.execute('CREATE TABLE IF NOT EXISTS actions_to_level_up_development(tg_id INTEGER, name_of_development TEXT, action TEXT, level INTEGER);')

sql.execute('CREATE TABLE IF NOT EXISTS motivations(tg_id INTEGER, motivational_text TEXT, status TEXT);')


def adding_new_development_to_db(tg_id, name, own_level, max_level, final_goal, reason):
    connection = sqlite3.connect('all_data.db')
    sql = connection.cursor()

    sql.execute('INSERT INTO development_first(tg_id, name, own_level, max_level, final_goal, reason) VALUES (?, ?, ?, ?, ?, ?);', (tg_id, name, own_level, max_level, final_goal, reason))

    connection.commit()

def getting_all_developments_by_tg_id(tg_id):
    connection = sqlite3.connect('all_data.db')
    sql = connection.cursor()

    user_developments = sql.execute('SELECT * FROM development_first WHERE tg_id=?;', (tg_id,)).fetchall()

    return user_developments

def adding_action_to_level_up(tg_id, name, action, level):
    connection = sqlite3.connect('all_data.db')
    sql = connection.cursor()

    sql.execute('UPDATE development_first SET own_level=? WHERE tg_id=? AND name=?;', (level, tg_id, name))
    sql.execute('INSERT INTO actions_to_level_up_development(tg_id, name_of_development, action, level) VALUES (?, ?, ?, ?);', (tg_id, name, action, level))

    connection.commit()

def adding_motivational_text_to_db(tg_id, motivational_text, status):
    connection = sqlite3.connect('all_data.db')
    sql = connection.cursor()

    sql.execute('INSERT INTO motivations(tg_id, motivational_text, status) VALUES (?, ?, ?);', (tg_id, motivational_text, status))
    connection.commit()

def getting_actions_to_level_up_development(tg_id, name):
    connection = sqlite3.connect('all_data.db')
    sql = connection.cursor()

    users_actions_to_level_up_development = sql.execute('SELECT * FROM actions_to_level_up_development WHERE tg_id=? and name_of_development=?;', (tg_id, name)).fetchall()

    return users_actions_to_level_up_development

def deleting_exact_development(tg_id, name):
    connection = sqlite3.connect('all_data.db')
    sql = connection.cursor()

    sql.execute('DELETE FROM actions_to_level_up_development WHERE tg_id=? AND name_of_development=?', (tg_id, name))
    sql.execute('DELETE FROM development_first WHERE tg_id=? AND name=?', (tg_id, name))
    connection.commit()
