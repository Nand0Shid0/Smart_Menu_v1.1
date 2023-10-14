array_enfermedades_catabolicas = ["cancer","sida","quemaduras","sepsis","neurológicas"]
array_nfermedades_metabolicas = ['sobrepeso','obesidad','hipertensión','sindrome de Cushing','hipotiroidismo']
array_alimentos_catabolicas = ['alimento 1','alimento 2','alimento 3','alimento 4','alimento 5']
array_alimentos_metabolicas = ['alimento 1','alimento 2','alimento 3','alimento 6','alimento 7']
array_grupo_enfermedades = [array_enfermedades_catabolicas,array_nfermedades_metabolicas]
array_alimetons_disponibles = [array_alimentos_catabolicas,array_alimentos_metabolicas]
array_enfermedades_seleccionadas = ['sida','sobrepeso']
array_alimentos = []
array_menu = []
var_carbo = 0.0



for enferdedad in array_enfermedades_seleccionadas:
    for grupo in range(0,len(array_grupo_enfermedades)):
        if enferdedad in array_grupo_enfermedades[grupo]:
            array_alimentos += array_alimetons_disponibles[grupo]


dict_repeticiones = dict(zip(array_alimentos,map(lambda x: array_alimentos.count(x),array_alimentos)))


for key in dict_repeticiones.keys():
    if dict_repeticiones[key] == len(array_enfermedades_seleccionadas):
        array_menu.append(key)

    
print(array_menu)


