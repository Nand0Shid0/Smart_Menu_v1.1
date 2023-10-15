import manager
from Filtro_alimentos import *

class Table(manager.Base):
#Esta clase hereda de la clase base
    
    def __init__(self, carbos, lipidos, prote, energia, multiplicador):
        """Al llamar a la clase debemos recibir las raciones a cubrir durtante todo el dia de carbohidratos, lipidos y porteinas. Ademas de las kcalorias a consumir

        Args:
            carbos (_type_): raciones totales del dia de carbohidratos
            lipidos (_type_): raciones totales del dia de lipidos
            prote (_type_): raciones totales del dia de proteinas
            energia (_type_): las kilo calorias a consumir durante el dia
            multiplicador (_type_): Este dato es determinado para cada comida del dia y en base a este se calcularan las raciones para la comida
        """
        self.energia =  round(energia*multiplicador,0)
        self.prote =    round(prote*multiplicador,0)
        self.lipidos =  round(lipidos*multiplicador,0)
        self.carbos =   round(carbos*multiplicador,0)

    def calcular(self, cereales=None, moderado_aporte=None, leguminosas=None, leche_descremada=None, leche_semidescremada=None, leche_entera=None, leche_azucar=None, verduras=None, muy_bajo_aporte=None, bajo_aporte=None, alto_aporte=None, aceites_con_proteinas=None, azucares_sin_grasa=None, azucares_con_grasa=None, aceites_sin_proteinas=None, frutas=None):
        """Metodo para en base a los grupos a limenticios que le des te dara las raciones de cada grupo


        Returns:
            - diccionario de raciones
            - raciones de proteinas a consumir
            - raciones de lipidos a consumir
            - raciones de carbohidratos a consumir
            - energia consumida en esa comida
        """
        resultados = dict()
        if cereales:
            resultados['cerales'] = self.cereals(cereales)
        if leguminosas:
            resultados['leguminosas'] = self.leguminosas(leguminosas)
        if leche_descremada:
            resultados['leche_descremada'] = self.leche_descremada(leche_descremada)
        if leche_semidescremada:
            resultados['leche_semidescremada'] = self.leche_semidescremada(leche_semidescremada)
        if leche_entera:
            resultados['leche_entera'] = self.leche_entera(leche_entera) 
        if leche_azucar:
            resultados['leche_azucar'] = self.leche_azucar(leche_azucar)
        if verduras:
            resultados['verduras'] = self.verduras(verduras)
        if moderado_aporte:
            resultados['moderado_aporte'] = self.moderado_aporte(moderado_aporte)
        if muy_bajo_aporte:
            resultados['muy_bajo_aporte'] = self.muy_bajo_aporte(muy_bajo_aporte)
        if bajo_aporte:
            resultados['bajo_aporte'] = self.bajo_aporte(bajo_aporte)
        if alto_aporte:
            resultados['alto_aporte'] = self.alto_aporte(alto_aporte)
        if aceites_sin_proteinas:
            resultados['aceites_sin_proteinas'] = self.sin_proteinas(aceites_sin_proteinas)
        if aceites_con_proteinas:
            resultados['aceites_con_proteinas'] = self.con_proteinas(aceites_con_proteinas) 
        if azucares_sin_grasa:
            resultados['azucares_sin_grasa'] = self.azucares_sin_grasa(azucares_sin_grasa) 
        if azucares_con_grasa:
            resultados['azucares_con_grasa'] = self.azucares_con_grasa(azucares_con_grasa)
        if frutas:
            resultados['frutas'] = self.frutas(frutas)
        return resultados, self.prote, self.lipidos, self.carbos, self.energia


        """
           Estos metodos los sobreescribimos de la clase padre debio a que en esta estos cuatro grupos los calcula automaticamente y aqui no debe ser asi
        """
    def cereals(self, quantity):
        return self.blueprint(quantity,2,0,15,70)
    
    def moderado_aporte(self, quantity):
        return self.blueprint(quantity,7,5,0,75)
    
    def sin_proteinas(self, quantity):
        return self.blueprint(quantity,7,5,0,75)
    
    def frutas(self, quantity):
        return self.blueprint(quantity, 0,0,15,60)


if __name__ == '__main__':
    """
    Aqui usamos la clase Base para obtener las raciones a cubrir durante el dia
    """
    print("========== MENU A CUBRIR ==========")
    distribucion = manager.Base(energia=1800, carbos=45, lipidos=30, prote=25)
    resultado_distribucion, prote, lipi, carbo, ene = distribucion.calcular(leguminosas=1, leche_descremada=2)
    """for key, value in resultado_distribucion.items():
            print(f'{key}: {value}')"""
    print(f"""
          TOTAL
            proteinas:      {prote}
            lipidos:        {lipi}
            carbohidratos:  {carbo}
            energia:        {ene}
""")

    print("========= DESAYUNO ============")
    """
    En base a los resultados anteriores mandamos las raciones a cubrir creando un objeto desayuno que es una instacia de la clase Table, donde el utimo argumento de multiplicador es 0.3 debido a que asi lo marca la tabla donde nos basamos.
    """
    desayuno = Table(carbo, lipi, prote, ene, 0.3)
    resultado_des, prote_des, lipi_des, carbo_des, ene_des = desayuno.calcular(cereales=1, verduras=2, moderado_aporte=2, aceites_sin_proteinas=3)
    print(f"""
          COMIDA    
            proteinas:      {prote_des}
            lipidos:        {lipi_des}
            carbohidratos:  {carbo_des}
            energia:        {ene_des}
""")
    
    
    print("========= COLACION MATUTINA ============")
    """
    En base a los resultados anteriores mandamos las raciones a cubrir creando un objeto desayuno que es una instacia de la clase Table, donde el utimo argumento de multiplicador es 0.3 debido a que asi lo marca la tabla donde nos basamos.
    """
    colacion1 = Table(carbo, lipi, prote, ene, 0.3)
    resultado_col1, prote_col1, lipi_col1, carbo_col1, ene_col1 = colacion1.calcular(aceites_con_proteinas=4)
    print(f"""
          COLACION MATUTINA    
            proteinas:      {prote_col1}
            lipidos:        {lipi_col1}
            carbohidratos:  {carbo_col1}
            energia:        {ene_col1}
""")
    print("========= COMIDA ============")
    comida = Table(carbo, lipi, prote, ene, 0.35)
    resultado_comida, prote_comida, lipi_comida, carbo_comida, ene_comida = comida.calcular(verduras=2, moderado_aporte=4, aceites_sin_proteinas=4)
    print(f"""
          COMIDA    
            proteinas:      {prote_comida}
            lipidos:        {lipi_comida}
            carbohidratos:  {carbo_comida}
            energia:        {ene_comida}
""")
    
    print("========= COLACION VESPERTINA ============")
    """
    En base a los resultados anteriores mandamos las raciones a cubrir creando un objeto desayuno que es una instacia de la clase Table, donde el utimo argumento de multiplicador es 0.3 debido a que asi lo marca la tabla donde nos basamos.
    """
    colacion2 = Table(carbo, lipi, prote, ene, 0.15)
    resultado_col2, prote_col2, lipi_col2, carbo_col2, ene_col2 = colacion2.calcular(aceites_con_proteinas=4)
    print(f"""
          COLACION MATUTINA    
            proteinas:      {prote_col2}
            lipidos:        {lipi_col2}
            carbohidratos:  {carbo_col2}
            energia:        {ene_col2}
""")

    print("========= CENA ============")
    cena = Table(carbo, lipi, prote, ene, 0.20)
    resultado_cena, prote_cena, lipi_cena, carbo_cena, ene_cena = cena.calcular(verduras=2, moderado_aporte=3, aceites_sin_proteinas=3)
    print(f"""
          COMIDA    
            proteinas:      {prote_cena}
            lipidos:        {lipi_cena}
            carbohidratos:  {carbo_cena}
            energia:        {ene_cena}
""")
