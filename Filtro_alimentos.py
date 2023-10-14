import sqlite3

def get_proteina(grupo_alimentos, limite):
    print("Proteina\n")
    sql = "SELECT Alimento, Proteina, Energia FROM Alimentos WHERE ID_Grupo=" + grupo_alimentos
    var_cursor.execute(sql)
    rows = var_cursor.fetchall()
    Output(rows, limite)
    print("\n")

def get_lipidos (grupo_alimentos, limite):
    print("Lipidos\n")
    sql = "SELECT Alimento, Lípidos, Energia FROM Alimentos WHERE ID_Grupo=" + grupo_alimentos
    var_cursor.execute(sql)
    rows = var_cursor.fetchall()
    Output(rows, limite)
    print("\n")

def get_carbohidratos(grupo_alimentos, limite):
    print("Carbohidratos\n")
    sql = "SELECT Alimento, Hidratos_de_carbono, Energia FROM Alimentos WHERE ID_Grupo=" + grupo_alimentos
    var_cursor.execute(sql)
    rows = var_cursor.fetchall()
    Output(rows, limite)
    print("\n")

def get_energia(grupo_alimentos):
    print("Energia\n")
    sql = "SELECT Alimento, Energia FROM Alimentos WHERE ID_Grupo=" + grupo_alimentos
    var_cursor.execute(sql)
    rows = var_cursor.fetchall()
    Output(rows)
    print("\n")


def Output(rows, limite):
    for row in rows:
        filtro(row, limite)

def filtro(row, limite):
    #Elementos mayores a 5gr de cada tipo Proteina, Lipidos y Carbos por ejemplo seran tomados en cuenta
    if row[1] > limite:
        print(row)

db_name = "Alimentozz.db"
var_conexion = sqlite3.connect(db_name)
var_cursor = var_conexion.cursor()