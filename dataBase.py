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
    cursor.execute("CREATE TABLE IF NOT EXISTS revision (id_revision INTEGER PRIMARY KEY, name_patient VARCHAR(250))")
    cursor.execute("CREATE TABLE IF NOT EXISTS revision_detalle (id_revision_detalle INTEGER PRIMARY KEY AUTOINCREMENT, id_revision INTEGER, id_tooth INTEGER, valor VARCHAR(30))")
    
    cursor.execute("CREATE TABLE IF NOT EXISTS tooth (id_tooth INTEGER PRIMARY KEY AUTOINCREMENT, Zone INTEGER, name_tooth VARCHAR(30))")
    for zona,name_diente  in Dientes:
        cursor.execute("INSERT INTO tooth (Zone,name_tooth) VALUES (?,?)",(zona,name_diente))
    
    connection.commit()
    cursor.close()
    connection.close()
    
def GetRevision(revisonid):
    connection = sqlite3.connect("datos.db")
    cursor = connection.cursor()
    valor = cursor.execute("SELECT Sum(valor) as valor  FROM revision_detalle WHERE id_revision = ?",(revisonid,),).fetchone()
    cursor.close()
    connection.close()
    return valor

def GetIdRevisionConsecutivo():
    connection = sqlite3.connect("datos.db")
    cursor = connection.cursor()
    valor = cursor.execute("Select IFNULL(max(id_revision)+1,1) as id_revision from revision ").fetchone()
    cursor.close()
    connection.close()
    
    return valor

def GuardarRevision(id_revision,name_patient):
    connection = sqlite3.connect("datos.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO revision (id_revision,name_patient) VALUES (?,?)",(id_revision,name_patient))
    connection.commit()
    cursor.close()
    connection.close()
    
def ConsultarTooth():
    connection = sqlite3.connect("datos.db")
    cursor = connection.cursor()
    tooths = cursor.execute("Select id_tooth,name_tooth from tooth ").fetchall()
    connection.close()
    return tooths

def GuardarDetalleRevision(id_revision,id_tooth,valor):
    connection = sqlite3.connect("datos.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO revision_detalle (id_revision,id_tooth,valor) VALUES (?,?,CASE ? WHEN 'sano' THEN 10 WHEN 'disminuido' THEN 20 WHEN 'gingivitis' THEN 30 WHEN 'Periodontitis' THEN 40 WHEN 'ausente' THEN 0 ELSE 0 END)",(id_revision,id_tooth,valor))
    connection.commit()
    cursor.close()
    connection.close()
    
def ConsultaRegistros():
    connection = sqlite3.connect("datos.db")
    cursor = connection.cursor()
    cant_revision = cursor.execute("Select Count(*) as count from revision ").fetchone()
    connection.close()
    cursor.close()
    
    return cant_revision
    