import sqlite3

def iniciarAssistant():
    Dientes =[
        #Zona 1
        (1,"Incisivo 11"),
        (1,"Incisivo 12"),
        (1,"Canino 13"),
        (1,"Premolar 14"),
        (1,"Premolar 15"),
        (1,"Molar 16"),
        (1,"Molar 17"),
        (1,"Molar 18"),
        #Zona 2
        (2,"Incisivo 21"),
        (2,"Incisivo 22"),
        (2,"Canino 23"),
        (2,"Premolar 24"),
        (2,"Premolar 25"),
        (2,"Molar 26"),
        (2,"Molar 27"),
        (2,"Molar 28"),
        #Zona 3
        (3,"Incisivo 31"),
        (3,"Incisivo 32"),
        (3,"Canino 33"),
        (3,"Premolar 34"),
        (3,"Premolar 35"),
        (3,"Molar 36"),
        (3,"Molar 37"),
        (3,"Molar 38"),
        #Zona 4
        (4,"Incisivo 41"),
        (4,"Incisivo 42"),
        (4,"Canino 43"),
        (4,"Premolar 44"),
        (4,"Premolar 45"),
        (4,"Molar 46"),
        (4,"Molar 47"),
        (4,"Molar 48"),
        ]
    connection = sqlite3.connect("datos.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS revision (id INTEGER PRIMARY KEY AUTOINCREMENT, name_patient INTEGER)")
    cursor.execute("CREATE TABLE IF NOT EXISTS revision_detalle (id INTEGER PRIMARY KEY AUTOINCREMENT, id_revision INTEGER, tooth INTEGER, valor VARCHAR(30))")
    
    cursor.execute("CREATE TABLE IF NOT EXISTS tooth (id INTEGER PRIMARY KEY AUTOINCREMENT, Zone INTEGER, name_tooth VARCHAR(30))")
    for zona,name_diente  in Dientes:
        cursor.execute("INSERT INTO tooth (Zone,name_tooth) VALUES (?,?)",(zona,name_diente))
    
    connection.commit()