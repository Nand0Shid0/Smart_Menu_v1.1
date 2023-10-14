
class Base:

    def __init__(self, carbos, lipidos, prote, energia):
        self.energia = energia
        self.carbos =   round(energia*carbos/100/4,0)
        self.lipidos =  round(energia*lipidos/100/9,0)
        self.prote =    round((energia*prote/100)/4,0)
        self.suma_de_proteinas = 0
        self.suma_de_lipidos = 0
        self.suma_de_carbos = 0

    def calcular(self,leguminosas=None, leche_descremada=None, leche_semidescremada=None, leche_entera=None,
                 leche_azucar=None, verduras=None, muy_bajo_aporte=None, bajo_aporte=None, alto_aporte=None,
                 aceites_con_proteinas=None, azucares_sin_grasa=None, azucares_con_grasa=None):
        resultados = dict()
        resultados['cerales'] = self.cereals()
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
        for key in resultados:
            self.suma_de_proteinas += resultados[key][1]
        resultados['moderado_aporte'] = self.moderado_aporte()
        if muy_bajo_aporte:
            resultados['muy_bajo_aporte'] = self.muy_bajo_aporte(muy_bajo_aporte)
        if bajo_aporte:
            resultados['bajo_aporte'] = self.bajo_aporte(bajo_aporte)
        if alto_aporte:
            resultados['alto_aporte'] = self.alto_aporte(alto_aporte)
        for key in resultados:
            self.suma_de_lipidos += resultados[key][2]
        resultados['aceites_sin_proteinas'] = self.sin_proteinas()
        if aceites_con_proteinas:
            resultados['aceites_con_proteinas'] = self.con_proteinas(aceites_con_proteinas) 
        if azucares_sin_grasa:
            resultados['azucares_sin_grasa'] = self.azucares_sin_grasa(azucares_sin_grasa) 
        if azucares_con_grasa:
            resultados['azucares_con_grasa'] = self.azucares_con_grasa(azucares_con_grasa)
        for key in resultados:
            self.suma_de_carbos += resultados[key][3]
        resultados['frutas'] = self.frutas()
        for key, value in resultados.items():
            print(f'{key}: {value}')
        return resultados, self.prote, self.lipidos, self.carbos, self.energia
        
    
    def blueprint(self,quantity, pro, lip, car, ene):
        if quantity:
            quantity = round(quantity,0)
            proteinas = quantity * pro
            lipidos = quantity * lip
            carbohidratos = quantity * car
            energia = quantity * ene
            return [quantity, proteinas, lipidos, carbohidratos, energia]
        
    def cereals(self):
        rations_cereals = round(self.carbos/2/15, 0)
        proteinas_cereales = rations_cereals*2
        lipidos_cereales = rations_cereals*0
        carbo_cereales = rations_cereals*15
        energia = rations_cereals * 70
        return [rations_cereals,proteinas_cereales,lipidos_cereales,carbo_cereales, energia]

    #====================LEGUMINOSAS
    def leguminosas(self, quantity):
        return self.blueprint(quantity, 8,1,20,120)

    #====================LECHE
    def leche_descremada(self, quantity):
        return self.blueprint(quantity, 9,2,12,95)
    
    def leche_semidescremada(self, quantity):
        return self.blueprint(quantity, 9,4,12,110)

    def leche_entera(self, quantity):
        return self.blueprint(quantity, 9,8,12,150)
    
    def leche_azucar(self,quantity):
        return self.blueprint(quantity, 8,5,30,200)
    
    #======================VERDURAS
    def verduras(self, quantity):
        return self.blueprint(quantity, 2,0,4,25)

    #=========== ALIMENTOS DE ORIGEN ANIMAL
    def muy_bajo_aporte(self,quantity):
        return self.blueprint(quantity,7,1,0,40)

    def bajo_aporte(self,quantity):
        return self.blueprint(quantity,7,3,0,55)
    
    def moderado_aporte(self):
        quantity = round((self.prote - self.suma_de_proteinas)/7,0)
        return self.blueprint(quantity,7,5,0,75)

    def alto_aporte(self, quantity):
        return self.blueprint(quantity,7,8,0,100)


    #============ ACEITES Y GRASAS
    def sin_proteinas(self):
        quantity = round((self.lipidos - self.suma_de_lipidos)/5,0)
        return self.blueprint(quantity, 0,5,0,45)

    def con_proteinas(self,quantity):
        return self.blueprint(quantity, 3,5,3,70)

    #==============FRUTAS
    def frutas(self):
        quantity = round((self.carbos - self.suma_de_carbos)/15,0)
        return self.blueprint(quantity, 0,0,15,60)

    #==============AZUCARES
    def azucares_sin_grasa(self, quantity):
        return self.blueprint(quantity,0,0,10,40)
    
    def azucares_con_grasa(self, quantity):
        return self.blueprint(quantity, 0,5,10,58)

if __name__ == "__main__":
    base = Base(energia=1500, carbos=45, lipidos=30, prote=25)
    base.calcular(leguminosas=1, leche_descremada=2)