
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


valores = ['Aceites y Grasas', 'Pollo', 'Cerdo', 'Soya', 'Clara de Huevo', 'Leche descremada', 'Tortilla', 'Todas las verduras', 'Frijol', 'Todas las frutas', 'Lenteja', 'Avena',
           'Pechuga de Tavo', 'Alubia', 'Haba', 'Requeson', 'Alverjon', 'Pan de caja', 'Res', 'Garbanzo', 'Pescado', 'Jamon de Pavo', 'Bolillo', 'Ternera', 'Arroz', 'Queso Panela']

for grupo in grupos_alimentos:
    for key, value in grupo.items():
        for alimento in valores:
            if alimento in value:
                salida[key].append(alimento)
                continue
            else:
                continue

for key, value in salida.items():
    print("\n"+key)
    for item in value:
        print(f"\t** {item}")
