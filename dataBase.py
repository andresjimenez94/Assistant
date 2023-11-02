import sqlite3

def iniciarAssistant():
    connection = sqlite3.connect("datos.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS revision (id INTEGER PRIMARY KEY AUTOINCREMENT, name_patient INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS tooth (id INTEGER PRIMARY KEY AUTOINCREMENT, tooth INTEGER)")
    i=1
    while i<48:
        cursor.execute("INSERT INTO tooth (tooth) VALUES (?)",(i,))
        i=i+1
    cursor.execute("CREATE TABLE IF NOT EXISTS revision_detalle (id INTEGER PRIMARY KEY AUTOINCREMENT, id_revision INTEGER, tooth INTEGER, valor VARCHAR(30))")
    connection.commit()