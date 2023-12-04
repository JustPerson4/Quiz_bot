import sqlite3
from datetime import datetime

connection = sqlite3.connect('data.db')
sql = connection.cursor()

sql.execute('CREATE TABLE IF NOT EXISTS useres(id PRIMARIY KEY AUTOINCERMENT INTEGER,first_name TEXT,telegram_id INTEGER,phone_number TEXT,coin INTEGER,reg_data DATETIME);')

sql.execute('CREATE TABLE IF NOT EXISTS quastions (id PRIMARIY KEY AUTOINCERMENT INTEGER,qustion TEXT,correct_answer TEXT,options TEXT);')

sql.execute('CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMERY KEY AUTOINCERMENT,telegram_id INTEGER,correct_answer INTEGER,get_coins INTEGER,play_data DATETIME);')


def register_user(first_name,phone_number,telegram_id,coin=0):
    connection = sqlite3.connect("data.db")
    sql = connection.cursor()
    
    sql.execute('INSERT INTO useres (first_name,phone_number,telegram_id,reg_data) VALUES(?,?,?,?);', (first_name,phone_number,telegram_id,datetime.now()))
    
    connection.commit()
    connection.close()
    

    
def check_user(telegram_id):


    connection = sqlite3.connect("data.db")
    sql = connection.cursor()

    user = sql.execute("SELECT telegram_id FROM useres WHERE telegram_id = ?",(telegram_id,)).fetchone()




    if user:
        return True
    else:
        return False
    
def add_history(telegram_id,correct_answer,got_coins):
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()
    
    sql.execute('INSERT INTO useres (telegram_id,correct_answer,got_coins,play_date) VALUES (?,?,?,?)',(telegram_id,correct_answer,got_coins,datetime.now()))
    
    connection.commit()
    connection.close()
    
    
def get_history(telegram_id):
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()
    
    coin = sql.execute('SELECT correct_answer, got_coins,play_date FROM history WHERE telegram_id, = ?;',(telegram_id,))
    
    if coin:
        return coin.fetchall()
    
    else:
        return False
    
    
def add_qusation(quastions,correct_answer,options):
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()
    
    sql.execute('INSERT INTO quastions (quastions,correct_answer,options) VALUES (?,?,?)',(quastions,correct_answer,options))
    
    connection.commit()
    connection.close()
    
def delete_quastion(question):
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()
    
    sql.execute('DELETE FROM questions=?,', (question,))
    
    connection.commit()
    connection.close()
    
def update_quastion(new_question,question):
    connection = sqlite3.connect('data.db')
    sql = connection.cursor()
    
    sql.execute('UPDATE questions SET question=? WHERE question=?', (new_question,question))
    
    connection.commit()
    connection.close()


def insert_quiz_result(chat_id, correct_answers):
   
    connection = sqlite3.connect('data.db')     
    sql = connection.cursor()
    
   
    sql.execute('''CREATE TABLE IF NOT EXISTS quiz_results
                      (telegram_id INTEGER PRIMARY KEY, correct_answers INTEGER)''')
    

    sql.execute("INSERT INTO quiz_results (telegram_id, correct_answers) VALUES (?, ?)", (chat_id, correct_answers))
    
   
    connection.commit()
    
   
    connection.close()



def get_user_results(chat_id):
 
    connection = sqlite3.connect('quiz_results.db')
    
    sql = connection.cursor()
    
    
    cursor=sql.execute("SELECT correct_answers FROM quiz_results WHERE chat_id=?", (chat_id,))
    

    result = cursor.fetchone()
        
    if result:
        return result[0]
    else:
        return None





































