import sqlite3

connection = sqlite3.connect("ChatBot2.db",check_same_thread=False)
cursor = connection.cursor()

def user_id():
    cursor.execute("""CREATE TABLE IF NOT EXISTS users
                      (id TEXT PRIMARY KEY)""")
    connection.commit()
def init_db_chat():
    cursor.execute("""CREATE TABLE IF NOT EXISTS conversations
                      (message_id INTEGER PRIMARY KEY AUTOINCREMENT,user_id TEXT,role TEXT, content TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY (user_id) REFERENCES users(id))""")
    connection.commit()
def init_db_iamge():
    cursor.execute("""CREATE TABLE IF NOT EXISTS image
                      (image_id INTEGER PRIMARY KEY, user_id TEXT,role TEXT, content TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY (user_id) REFERENCES users(id))""")
    connection.commit()
def init_db_pay():
    cursor.execute("""CREATE TABLE IF NOT EXISTS pay
                      (msgcount INTEGER PRIMARY KEY AUTOINCREMENT,id TEXT ,paid INTEGER DEFAULT 0)""")
    connection.commit()    
def mpay(id):
    cursor.execute("INSERT INTO pay (id) VALUES (?)",(id,))
    connection.commit()



def save_user_id(user_id):
    #cursor.execute("DROP TABLE users")
    cursor.execute("SELECT * FROM users")
    f = cursor.fetchall()
    print(f)
    cursor.execute("INSERT OR IGNORE INTO users (id) Values (?)",(user_id,))
    connection.commit()

def save_message(user_id,role,content):
    #cursor.execute("DROP TABLE conversations")
    cursor.execute("INSERT INTO conversations (user_id,role,content) Values (?,?,?)",(user_id,role,content))
    connection.commit()
def save_iamge(user_id,role,content):
    #cursor.execute("DROP TABLE image")
    cursor.execute("INSERT INTO image (user_id,role,content) Values (?,?,?)",(user_id,role,content))
    connection.commit()
def deleting(user_id):
    import sqlite3

def deleting(user_id):
    cursor.execute("""
        DELETE FROM conversations
        WHERE message_id NOT IN (
            SELECT message_id FROM (
                SELECT message_id FROM conversations
                WHERE user_id = ?
                ORDER BY message_id DESC
                LIMIT 2
            )
        )
        AND user_id = ?;
    """, (user_id, user_id))

    connection.commit()


def get_pay(id):
    ouput = []
    cursor.execute("SELECT msgcount,paid FROM pay WHERE id=?",(id,))
    result = cursor.fetchall()
    for tuples in result:
        ouput.append({"Msgcount":tuples[0],"paid":tuples[1]})
    return ouput

def get_conversation(user_id):
    output = []
    cursor.execute("SELECT role,content FROM conversations WHERE user_id=?",(user_id,))
    result = cursor.fetchall()
    for row in result:
        output.append({"role":row[0],"content":[{"type":"text","text":row[1]}]})
        print(row)
    cursor.execute("SELECT role,content FROM image WHERE user_id=?",(user_id,))
    result = cursor.fetchall()
    for row in result:
        output.append({"role":row[0],"content":[{"type":"text","text":row[1]}]})
        print(row)
    return output