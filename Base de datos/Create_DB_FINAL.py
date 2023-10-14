import sqlite3
import os
from csv import reader

def fun_obtener_id_grupo(cursor):
    for row in cursor:
        return row[0]
    
db_name = "Alimentozz.db"
var_conexion = sqlite3.connect(db_name)
var_cursor = var_conexion.cursor()
alimentos_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Alimentos")

var_cursor.execute('''
    CREATE TABLE IF NOT EXISTS Grupo_alimentos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Nombre_grupo TEXT NOT NULL
    )
''')

var_cursor.execute('''
    CREATE TABLE IF NOT EXISTS Alimentos (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ID_Grupo INTEGER, 
        Alimento TEXT NOT NULL,
        Peso_neto VARCHAR(60) DEFAULT 'NA',
        Peso_bruto_redondeado VARCHAR(8) DEFAULT 'NA',
        Energia VARCHAR(8) DEFAULT 'NA',
        Proteina VARCHAR(8) DEFAULT 'NA',
        Lípidos VARCHAR(8) DEFAULT 'NA',
        Hidratos_de_carbono VARCHAR(8) DEFAULT 'NA',
        Fibra VARCHAR(8) DEFAULT 'NA',
        Vitamina_A VARCHAR(8) DEFAULT 'NA',
        Acido_Ascórbico VARCHAR(8) DEFAULT 'NA',
        Acido_Fólico VARCHAR(8) DEFAULT 'NA',
        Hierro_NO_HEM VARCHAR(8) DEFAULT 'NA',
        Calcio VARCHAR(60) DEFAULT 'NA',
        Hierro VARCHAR (8) DEFAULT 'NA',        
        Potasio VARCHAR(8) DEFAULT 'NA',
        Fósforo VARCHAR(8) DEFAULT 'NA',
        Azúcar_por_equivalente VARCHAR(8) DEFAULT 'NA',
        AG_Saturados VARCHAR(8) DEFAULT 'NA',
        Azúcares_por_equivalente VARCHAR(8) DEFAULT 'NA',
        AG_Monoinsaturados VARCHAR(8) DEFAULT 'NA',
        AG_Poliinsatuirados VARCHAR(8) DEFAULT 'NA',
        Colesterol VARCHAR(8) DEFAULT 'NA',
        Sodio VARCHAR(8) DEFAULT 'NA',
        Selenio VARCHAR(8) DEFAULT 'NA',
        Indica_glicémico VARCHAR(8) DEFAULT 'NA',
        Carga_glicémica VARCHAR(8) DEFAULT 'NA',
        FOREIGN KEY (ID_Grupo) REFERENCES Grupo_alimentos(ID)
    )
''')


var_Nombres_csv=['VERDURAS', 'FRUTAS', 'CEREALES SIN GRASA','LEGUMINOSAS',
                   'A.O.A MUY BAJOS EN GRASA', 'LECHE DESCREMADA', 'ACEITES Y GRASAS', 
                   'ACEITES Y GRASAS CON PROTEINAS', 'AZUCARES SIN GRASA',
                   'A.O.A.BAJO EN GRASA',
                   'A.O.A.MODERADOS EN GRASA','LECHE ENTERA'
                   ]

var_insert_verduras = f"""
INSERT OR IGNORE INTO  Alimentos (ID_Grupo, Alimento, Peso_neto, Energia,
                     Proteina, Lípidos,Hidratos_de_carbono, Fibra, 
                     Vitamina_A, Acido_Ascórbico, Acido_Fólico, 
                     Hierro_NO_HEM, Potasio) 
                     VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);
"""

var_insert_frutas = f"""
INSERT OR IGNORE INTO  Alimentos (ID_Grupo, Alimento, Peso_bruto_redondeado,Peso_neto,Energia,
                    Proteina,Lípidos,Hidratos_de_carbono,Fibra,
                    Vitamina_A,Acido_Ascórbico,Acido_Fólico,
                    Hierro_NO_HEM,Potasio,Azúcar_por_equivalente)
                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);
"""
var_insert_cereales_sin_grasa = f"""
INSERT OR IGNORE INTO  Alimentos (ID_Grupo,Alimento,Peso_neto,Energia,Proteina, 
                                Lípidos,Hidratos_de_carbono,Fibra,Acido_Fólico, 
                                Calcio,Hierro,Sodio,Azúcar_por_equivalente)
                                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);
"""
var_insetar_leguminosas = f"""
INSERT OR IGNORE INTO  Alimentos (ID_Grupo,Alimento,Peso_neto,Energia,Proteina,Lípidos,
                        Hidratos_de_carbono,Fibra,Hierro_NO_HEM,Selenio, 
                        Sodio,Fósforo,Potasio,Azúcar_por_equivalente)
                        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?);
"""
var_insetar_A_O_A = f"""
INSERT OR IGNORE INTO  Alimentos (ID_Grupo,Alimento,Peso_neto,Energia,Proteina,Lípidos,
                  Hidratos_de_carbono,Colesterol,Vitamina_A,Calcio,
                  Hierro,Sodio,Selenio)
                  VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);
"""
var_insetar_Leche_Descremada = f"""
INSERT OR IGNORE INTO  Alimentos (ID_Grupo,Alimento,Peso_neto,Energia,Proteina,Lípidos, 
                            Hidratos_de_carbono,Colesterol,Vitamina_A,Calcio,Sodio)
                            VALUES(?,?,?,?,?,?,?,?,?,?,?);
"""
var_insetar_Aceites_y_Grasas = f"""
INSERT OR IGNORE INTO  Alimentos (ID_Grupo,Alimento,Peso_neto,Energia,Proteina,Lípidos,Hidratos_de_carbono, 
                            AG_Saturados,AG_Monoinsaturados,AG_Poliinsatuirados,Colesterol,Sodio)
                            VALUES(?,?,?,?,?,?,?,?,?,?,?,?);
"""
var_insetar_A_y_G_con_proteina = f"""
INSERT OR IGNORE INTO  Alimentos (ID_Grupo,Alimento,Peso_neto,Energia,Proteina,Lípidos,Hidratos_de_carbono, 
                               AG_Saturados,AG_Monoinsaturados,AG_Poliinsatuirados,Colesterol,Sodio)
                               VALUES(?,?,?,?,?,?,?,?,?,?,?,?);
"""
var_insetar_Azucares_sin_grasa = f"""
INSERT OR IGNORE INTO  Alimentos (ID_Grupo,Alimento,Peso_neto,Energia,Proteina,Lípidos,Hidratos_de_carbono, 
                               Sodio,Azúcares_por_equivalente,Indica_glicémico,Carga_glicémica)
                               VALUES(?,?,?,?,?,?,?,?,?,?,?);
"""
var_insetar_A_O_A_Bajo_En_Grasa = f"""
INSERT OR IGNORE INTO  Alimentos (ID_Grupo, Alimento, Peso_neto, Energia, Proteina, Lípidos, Hidratos_de_carbono,
                                Colesterol, Vitamina_A, Calcio, Hierro, Sodio, Selenio)
                                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);

"""
var_insetar_A_O_A_Moderados = f"""
INSERT OR IGNORE INTO  Alimentos (ID_Grupo,Alimento,Peso_neto,Energia,Proteina,Lípidos,Hidratos_de_carbono,
                                Colesterol ,Vitamina_A,Calcio,Hierro,Sodio,Selenio)
                               VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);
"""

var_insetar_Leche_Entera = f"""
INSERT OR IGNORE INTO  Alimentos (ID_Grupo,Alimento,Peso_neto,Energia,Proteina,Lípidos,
                            Hidratos_de_carbono,Colesterol ,Vitamina_A,Calcio,Sodio)
                            VALUES(?,?,?,?,?,?,?,?,?,?,?);
"""

dic_Insertar_datos = {'VERDURAS':var_insert_verduras,
                            'FRUTAS':var_insert_frutas,
                            'CEREALES SIN GRASA':var_insert_cereales_sin_grasa,
                            'LEGUMINOSAS':var_insetar_leguminosas,
                            'A.O.A MUY BAJOS EN GRASA':var_insetar_A_O_A,
                            'LECHE DESCREMADA':var_insetar_Leche_Descremada,
                            'ACEITES Y GRASAS':var_insetar_Aceites_y_Grasas,
                            'ACEITES Y GRASAS CON PROTEINAS':var_insetar_A_y_G_con_proteina,
                            'AZUCARES SIN GRASA':var_insetar_Azucares_sin_grasa,
                            'A.O.A.BAJO EN GRASA':var_insetar_A_O_A_Bajo_En_Grasa,
                            'A.O.A.MODERADOS EN GRASA':var_insetar_A_O_A_Moderados,
                            'LECHE ENTERA':var_insetar_Leche_Entera}

for grupo in var_Nombres_csv:
    var_cursor.execute(f"INSERT OR IGNORE INTO Grupo_alimentos(Nombre_grupo) VALUES ('{grupo}');")
    var_conexion.commit()
print("Nombres de alimentos guardados!!")

for insertar in var_Nombres_csv:
        #Contador
        count = 0
        # abrir archivo
        with open(os.path.join(alimentos_directory, f"{insertar}.csv"), "r") as my_file:
            #obtenemos el id del grupo de alimentos
            var_cursor.execute(f"SELECT ID FROM Grupo_alimentos WHERE Nombre_grupo='{insertar}'")
            var_id_grupo = fun_obtener_id_grupo(var_cursor)
            #pasar las filas del archivo para leerlas
            file_reader = reader(my_file)
            # recorremos las filas
            for i in file_reader:
                i.insert(0,var_id_grupo)
                var_cursor.executemany(dic_Insertar_datos[insertar],[i])
                var_conexion.commit()
        print(f"Los alimentos de: {str(insertar)} se guardaron con exito!!")
        print("Base de datos completa!!")
var_conexion.close()