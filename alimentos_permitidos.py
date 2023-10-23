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

def mostrar_enfermedades_alimentos_permitidos(alimentos):
    
    frutas = {"Frutas": [
        "Todas las frutas",
        "Manzana",
        "Pera",
        "Durazno",
        "Sandía",
        "Melón",
        "Guayaba",
        "Jícama",
        "Ciruela roja"
    ]}

    verduras = {
        "Verduras": [
            "Todas las verduras",
            "Zanahoria",
            "Chayote cocidos"
        ]}

    alimentos_animal = {
        "Alimentos de origen animal": [
            "Pollo",
            "Res",
            "Ternera",
            "Pescado",
            "Cerdo",
            "Clara de Huevo",
            "Jamón de Pavo",
            "Pechuga de Pavo",
            "Queso Panela",
            "Requeson",
            "Leche descremada"
        ]}

    cereales = {
        "Granos y cereales": [
            "Avena",
            "Arroz",
            "Bolillo",
            "Tortilla",
            "Pan de caja",
            "Tapioca",
            "Papa",
            "Camote",
            "Pan dulce",
            "Tostada",
            "Maíz"
        ]}

    lacteos = {
        "Lacteos": [
            "Leche entera",
            "Semidescremada",
            "Queso Cottage",
            "Yogur"
        ]}

    grupos_alimentos = [frutas, verduras, alimentos_animal, cereales, lacteos]

    salida = {
        "Frutas": [],
        "Verduras": [],
        "Alimentos de origen animal": [],
        "Granos y cereales": [],
        "Lacteos": []

    }

    for grupo in grupos_alimentos:
        for key, value in grupo.items():
            for alimento in alimentos:
                if alimento in value:
                    salida[key].append(alimento)
                    continue
                else:
                    continue

    return salida


enfermedades_seleccionadas = input("Ingrese las enfermedades seleccionadas (separadas por comas): ")
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
    menu = mostrar_enfermedades_alimentos_permitidos(lista_alimentos)
    for key, value in menu.items():
        print("\n"+key)
        for item in value:
            print(f"\t- {item}")
else:
    print("No se encontraron alimentos permitidos para las enfermedades seleccionadas.")
