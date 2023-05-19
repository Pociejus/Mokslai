from operator import attrgetter
from statistics import mean, median

#  pirma uzduotis

# tekstas1 = "Authorities in New Zealand are still trying to determine how many people died in a blaze that tore through a hostel in the capital Wellington overnight, killing at least six.Fire crews were called to Loafers Lodge hostel in the city center just after midnight local time and found the top floor of the four-story building well alight, according to a statement from Fire and Emergency New Zealand.As firefighters fought the blaze, 52 people were evacuated but it’s unclear how many people were inside at the time. Late Monday, Urban Search and Rescue Squad members were still determining whether the building was safe to search."
# print(tekstas1) # paprastas tekstas
# splitintas_listas = tekstas1.split(".") # splitinam ties tasku, verciam i lista
# print(splitintas_listas) # splitintas tekstas
# sauktukas = "! "
# garsiai = sauktukas.join(splitintas_listas) # idedam sauktuka tarp listo elemtu
# print(garsiai) # tekstas su sauktukais vietoj tasko

#  pirmo antras???--

# tekstas1 = "Authorities in New Zealand are still trying to determine how many people died in a blaze that tore through a hostel in the capital Wellington overnight, killing at least six.Fire crews were called to Loafers Lodge hostel in the city center just after midnight local time and found the top floor of the four-story building well alight, according to a statement from Fire and Emergency New Zealand.As firefighters fought the blaze, 52 people were evacuated but it’s unclear how many people were inside at the time. Late Monday, Urban Search and Rescue Squad members were still determining whether the building was safe to search."
# print(tekstas1) # paprastas tekstas
# splitintas_listas = tekstas1.split(".") # splitinam ties tasku, verciam i lista
# print(splitintas_listas) # splitintas tekstas
# mapas = map(lambda x: x + "! ", splitintas_listas)
# garsiai = "".join(mapas)
# print(garsiai)

#  antra -------------------------------------------------------------------------------

# rangel = list(range(0, 51))
# padaugintas10 = map(lambda x: x * 10, rangel)
# print(list(padaugintas10))
# dalinasi7 = filter(lambda x: x % 7 == 0 and x != 0, rangel)
# dalinas7_list = list(dalinasi7)
# print(dalinas7_list)
#
# pakeltas2 = map(lambda x: x ** 2,  rangel)
# pakeltas2_use = list(pakeltas2)
# pakeltaslist = [x for x in pakeltas2_use if x != 0]
# pakeltasbenulio = list(pakeltaslist)
# pakeltas_sum = sum(pakeltasbenulio)
# pakeltas_max = max(pakeltasbenulio)
# pakeltas_min = min(pakeltasbenulio)
# pakeltas_mean = mean(pakeltasbenulio)
# pakeltas_median = median(pakeltasbenulio)
# atbulai = pakeltas2_use[::-1]                        ## arba galima su atbulai.sort(reverse=True)
                                                       ## arba naujas = sorted(atbulai) tada nepakeis toliau kode
# print(pakeltas2_use)
# print(pakeltasbenulio)
# print("SUMA",pakeltas_sum)
# print("MAX",pakeltas_max)
# print("MIN", pakeltas_min)
# print("Vidurkis", pakeltas_mean)
# print("Mediana", pakeltas_median)

# print("Atbulai",atbulai)

#  3 uzd --------------------------------------------------

# sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8,"Vakaras"]
# skaiciu_sarasas = []
# zodziu_sarasas = []
# bulynuTrue_sarasas = []

# for x in sarasas:
#     if type(x) is int or type(x) is float:
#         skaiciu_sarasas.append(x)
#     elif type(x) is str:
#         zodziu_sarasas.append(x)
#     elif type(x) is bool and x is True:
#         bulynuTrue_sarasas.append(x)

# suma = sum(skaiciu_sarasas)
# print(suma)
# sakinys = " ".join(zodziu_sarasas) # idedam sauktuka tarp listo elemtu
# print(sakinys)
# suma_teisingu = sum(bulynuTrue_sarasas)
# print(suma_teisingu)

####### bandymas nr 3.2 -----------------------------------------


# sarasas = [2.5, 2, "Labas", True, 5, 7, 8, 2.8, "Vakaras"]
# skaiciufiltras = filter(lambda x: type(x) is int or type(x) is float, sarasas) #isfiltruojam skaicius
# skaiciu_sarasas = list(skaiciufiltras)                                         #verciam i lista
#
# zodziufiltras = filter(lambda x: type(x) is str, sarasas)
# zodziu_sarasas = list(zodziufiltras)
#
# truefiltras = filter(lambda x: type(x) is bool, sarasas)
# bulynuTrue_sarasas = list(truefiltras)
#
# suma = sum(skaiciu_sarasas)
# print("skaiciu suma", suma)
# sakinys = " ".join(zodziu_sarasas)                                              # idedam tarpa tarp eiluciu
# print(sakinys)
# suma_teisingu = sum(bulynuTrue_sarasas)
# print("boolyn reiksmiu", suma_teisingu)



### 4 uzd --------------------

# class Zmogus:
#     def __init__(self,vardas, amzius):
#         self.vardas = vardas
#         self.amzius = amzius
#
#     def __repr__(self):
#         return f"{self.vardas}- {self.amzius};"
#
# zmogus1 = Zmogus("Petras", 17)
# zmogus2 = Zmogus("Antanas", 25)
# zmogus3 = Zmogus("kritijonas", 49)
# zmogus_list = [zmogus1, zmogus2, zmogus3]
#
#

# surusiuota_amziu = sorted(zmogus_list, key=attrgetter('amzius'))
# surusiuota_varda = sorted(zmogus_list, key=attrgetter('grazina'))
# print(surusiuota_amziu)
# print(surusiuota_varda)
