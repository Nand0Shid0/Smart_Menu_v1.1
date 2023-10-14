def fun_geb(edad,peso,sexo,actividad):
    '''
    Este metodo se encarga de calcular el geb
    '''
    result = 0
    if sexo == 'Mujer':
        if edad == 0:
            result = (11.02 * peso) + 679
        elif edad == 1:
            result = (10.92 * peso) + 677
        elif edad == 2:
            result = (10.98 * peso) + 520
    elif sexo == 'Hombre':
        if edad == 0:
            result = (13.37 * peso) + 747
        elif edad == 1:
            result = (13.08 * peso) + 693
        elif edad == 3:
            result = (14.21 * peso) + 429
    result = result + (result*actividad) + (result*0.1)
    return round(result,3)

    

def fun_imc(peso,altura):
    '''
    Metodo para el calculo del imc
    '''
    estatura = altura/100
    estatura = estatura ** 2

    result = peso / estatura
    result = round(result,3)

    return result


def fun_distribucion(var_get,var_carbo, var_proteinas, var_lipido):
    '''
    Distribucion del GET mediante el porcentaje ingresado
    '''
    var_carbo_consumir = var_get * var_carbo
    var_lipid_consumir = var_get * var_lipido
    var_prote_consumir = var_get * var_proteinas

    print(f'get: {var_get}\ncarbohidratos: {var_carbo_consumir}\nproteinas: {var_prote_consumir}\nlipidos: {var_lipid_consumir}\ntotal: {var_lipid_consumir+var_prote_consumir+var_carbo_consumir}')


def fun_gramos(var_proteinas,var_lipidos,var_carbo):
    ''''
    Calcula los gramos a consumir
    '''
    var_gr_proteinas = (var_proteinas * 1) / 4
    var_gr_lipidos = (var_lipidos * 1) / 9
    var_gr_carbo = (var_carbo * 1) / 4
    print(f'proteinas {var_gr_proteinas}g\nlipidos {var_gr_lipidos}g\nhidratos de carbono {var_gr_carbo}g')

    
def fun_raciones_cereales(var_gr_carbo):
    '''
    calcula las raciones del grupo de carbohidratos
    '''
    var_mitad_carbo = var_gr_carbo / 2
    var_raciones_equivalentes_cerales = var_mitad_carbo / 15
    var_raciones_equivalentes_cerales = round(var_raciones_equivalentes_cerales)
    var_proteinas_carbo = 2 * var_raciones_equivalentes_cerales
    var_lipidos_carbo = 0 * var_raciones_equivalentes_cerales
    var_carbo_carbo = 15 * var_raciones_equivalentes_cerales
    var_kilocalorias = 70 * var_raciones_equivalentes_cerales


def fun_raciones_leguminosas(var_raciones):
    var_proteinas_racion = 8 * var_raciones
    var_lipidos_racion = 1 * var_raciones
    var_carbo_racion = 20 * var_raciones
    var_kilocalorias = 120 * var_raciones


def fun_raciones_leche(var_raciones):
    var_proteinas_racion = 9 * var_raciones
    var_lipidos_racion = 2 * var_raciones
    var_carbo_racion = 12 * var_raciones
    var_kilocalorias = 95 * var_raciones


def fun_racoines_verduras(var_raciones):
    var_proteinas_racion = 2 *var_raciones
    var_lipidos_racion = 0 * var_raciones
    var_carbo_racion = 4 * var_raciones
    var_kilocalorias = 25 * var_raciones


def fun_raciones_aoa(var_proteina_total,var1,var2,var3,var4):
    #Alimentos de origen animal(AOA)
    var_proteina = var_proteina_total - (var1 + var2 + var3 + var4)
    var_raciones_equivalentes = var_proteina / 7
    var_proteinas_racion = 7 * var_raciones_equivalentes
    var_lipidos_racion = 5 * var_raciones_equivalentes
    var_carbo_racion = 0 * var_raciones_equivalentes
    var_kilocalorias = 75 * var_raciones_equivalentes


def fun_raciones_aceites(var_lipidos_total,var1,var2,var3,var4,var5):
    pass



fun_distribucion(2700,0.6,0.15,0.25)
fun_gramos(405.0,675.0,1620.0)
