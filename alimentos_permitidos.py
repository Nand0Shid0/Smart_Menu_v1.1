import sqlite3

alimentos_metabolicos = [
    "Avena", "Arroz", "Bolillo", "Tortilla", "Pan de caja", "Todas las frutas", "Todas las verduras",
    "Frijol", "Lenteja", "Haba", "Garbanzo", "Soya", "Alubia", "Alverjon", "Pollo", "Res", "Ternera",
    "Pescado", "Cerdo", "Clara de Huevo", "Jamon de Pavo", "Pechuga de Tavo", "Queso Panela", "Requeson", "Leche descremada", "Aceites y Grasas"
]

alimentos_catabolicos = [
    "Arroz", "Avena", "Tapioca", "Papa", "Camote", "Bolillo", "Tortilla", "Pan dulce", "Pan de caja",
    "Todas las frutas", "Todas las verduras", "Frijol", "Lenteja", "Haba", "Garbanzo", "Soya", "Alubia", "Alverjón",
    "Pollo", "Res", "Ternera", "Cerdo", "Huevo", "Pescado", "Mariscos", "Embutidos como jamón y salchichas de pavo", 
    "Todos los quesos", "Leche entera", "Descremada", "Semidescremada", "Aceites y grasas", "Azúcar", "Miel", "Mermeladas", "Cajeta", "Ate"
]

alimentos_gastrointestinales = [
    "Arroz", "Tapioca", "Pan tostado", "Papa", "Camote", "Manzana", "Pera", "Durazno", "Zanahoria", 
    "Chayote cocidos", "Pollo", "Jamón de Pavo", "Queso Panela", "Yogur", "Maíz", "Girasol", "Oliva", "Soya", "Canola", "Agua pura"
]

alimentos_cmd = [
    "Arroz", "Avena", "Bolillo", "Tortilla", "Pan de caja", "Sandía", "Melón", "Guayaba", "Jícama", "Ciruela roja",
    "Durazno", "Todas las verduras", "Frijol", "Lenteja", "Haba", "Garbanzo", "Soya", "Alubia", "Alverjón",
    "Pollo", "Pescado", "Res", "Clara de Huevo", "Queso Cottage y Requesón", "Jamón de Pechuga de Pavo", 
    "Pata de Res", "Queso Panela Cottage", "Leche Descremada y Yogurt Light", "Aceitunas", "Chía", "Linaza", 
    "Aguacate y Aceites de Oliva, Canola, Girasol y Soya", "Nuez", "Almendras", "Cacahuates", "Pepitas", "Avellanas", 
    "Piñones", "Pistaches", "Nuez de la India", "Agua pura"
]

alimentos_hpp = [
    "Arroz", "Avena", "Tapioca", "Bolillo", "Tortilla", "Pan de caja", "Pan dulce", "Papa", "Camote", "Todas las frutas", 
    "Todas las verduras", "Lenteja", "Haba", "Alverjón", "Frijol", "Garbanzo", 
    "Pollo", "Pescado", "Res", "Huevo", "Queso Panela, Requesón y Cottage", "Leche Entera, Descremada, Todo tipo de quesos y yogurt", 
    "Aceite de oliva, Canola, Girasol, Soya", "Crema", "Azúcar", "Miel", "Ate", "Agua pura"
]

alimentos_hieprca = [
    "Arroz", "Avena", "Tapioca", "Bolillo", "Tortilla", "Pan de caja", "Pan dulce", "Papa", "Camote", "Todas las frutas", 
    "Todas las verduras", "Lenteja", "Haba", "Alverjón", "Frijol", "Soya", "Res", "Pollo", "Pescado", "Mariscos", "Huevo", "Jamón de Pavo y todo tipo de quesos", 
    "Leche entera, descremada y yogurt", "Aceitunas, Chia, Linaza y Aguacate", "Aceites de Oliva, Canola, Girasol y Soya", "Nuez, Almendras, Cacahuates", 
    "Pepitas, Avellanas, Piñones, Pistaches, Nuez de la India", "Azúcar, Miel, Mermeladas, Cajeta", "Agua pura"
]

enfermedades_alimentos_permitidos = {
    "Sobrepeso": alimentos_metabolicos,
    "Obesidad": alimentos_metabolicos,
    "Hipertension": alimentos_metabolicos,
    "Sindrome de Cushing": alimentos_metabolicos,
    "Hipotiridismo": alimentos_metabolicos,
    "SIDA": alimentos_catabolicos,
    "Quemaduras": alimentos_catabolicos,
    "Sepsis": alimentos_catabolicos,
    "Diverticulitis": alimentos_gastrointestinales,
    "Gastroparesia": alimentos_gastrointestinales,
    "Enfermedad de Crohn": alimentos_gastrointestinales,
    "Obstrucción": alimentos_gastrointestinales,
    "Estenosis del intestino": alimentos_gastrointestinales,
    "Colitis ulcerativa": alimentos_gastrointestinales,
    "Diarrea aguda": ["Arroz", "Pan tostado", "Manzana", "Plátano", "Yogur", "Agua pura"],
    "Diabetes mellitus": alimentos_cmd,
    "Hipotiroidismo": alimentos_cmd,
    "Enfermedad hepática obstructiva": alimentos_cmd,
    "ERC": alimentos_cmd,
    "Enfermedades cardiovasculares": alimentos_cmd,
    "Obesidad Mórbida": ["Todas las verduras", "Carne con grasa de res, cerdo, pollo, pescado", "Huevo entero", 
        "Jamón chicharrón", "Vísceras en general como hígado, sesos, pata, corazón, riñones", 
        "Todo tipo de quesos", "Aceites y Grasas", "Agua Pura", "Yogur Natural"],
    "Insuficiencia renal aguda": alimentos_hpp,
    "Enfermedad renal": alimentos_hpp,
    "Politraumatizados": alimentos_hieprca,
    "VIH": alimentos_hieprca,
    "Cancer": alimentos_hieprca,
    "Quemados": alimentos_hieprca,
    "Otra": []
}

def menu(search_name,deficiencia):
    database = "Alimentozz.db"
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    alimentos = []
    def caso2(id_gupo):
        try:
            cursor.execute(
                f"SELECT MIN({value}) FROM Alimentos WHERE ID_Grupo = ?", (id_gupo))
            min_value = cursor.fetchone()[0]

            cursor.execute(
                f"SELECT * FROM Alimentos WHERE {value} = ? AND ID_Grupo = ? ", (min_value,id_gupo))
            result = cursor.fetchone()

            if result:
                alimentos.append(result[2])
        except sqlite3.OperationalError:
            pass

    for value in deficiencia:
        for alimento in search_name:
            if alimento == "Todas las frutas":
                caso2("2")
            if alimento == "Todas las verduras":
                caso2("1")
            else:      
                try:
                    cursor.execute(
                        f"SELECT MIN({value}) FROM Alimentos WHERE Alimento LIKE ?", (alimento + '%',))
                    min_value = cursor.fetchone()[0]

                    cursor.execute(
                        f"SELECT * FROM Alimentos WHERE {value} = ? AND Alimento LIKE ?", (min_value, alimento + '%'))
                    result = cursor.fetchall()

                    if result:
                        for row in result:
                            alimentos.append(row[2])
                except sqlite3.OperationalError:
                    pass

    return list(set(alimentos))


#Entrada de datos al programa
enfermedades_seleccionadas = input("Ingrese las enfermedades seleccionadas (separadas por comas): ")
deficiencias = input("Ingrese las deficiencias seleccionadas (separadas por comas): ")
deficiencias_lista = deficiencias.split(',')

#################################################################################################
enfermedades_seleccionadas = [enfermedad.strip() for enfermedad in enfermedades_seleccionadas.split(',')]
alimentos_totales = []
for enfermedad in enfermedades_seleccionadas:
    alimentos_enfermedad = enfermedades_alimentos_permitidos.get(enfermedad)
    if alimentos_enfermedad:
        alimentos_totales.extend(alimentos_enfermedad)
alimentos_totales = list(set(alimentos_totales))
lista_alimentos = []
if alimentos_totales:
    print(f"Alimentos permitidos para las enfermedades seleccionadas:")
    for alimento in alimentos_totales:
        lista_alimentos.append(alimento)
    return_menu = menu(lista_alimentos,deficiencias_lista)
    #print(return_menu)
    print("Lista de los alimentos recomendados segun las decifiencias del paciente:")
    for alimento_menu in return_menu:
        print("\t-- "+alimento_menu)
    
else:
    print("No se encontraron alimentos permitidos para las enfermedades seleccionadas.")
