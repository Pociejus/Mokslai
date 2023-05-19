# class Namas:
#     def __init__(self, plotas, verte):
#         self.plotas = plotas
#         self.__verte = verte
#
#     def set_verte(self,nauja):
#         if str(nauja).isdigit():
#             self.__verte = nauja
#         else:
#             print("verte turi būti skaičius")
#
#     def get_verte(self):
#         return self.__verte
#
# namas1 = Namas(14, 25)
# print(namas1.get_verte())
#
# namas1.set_verte(45)
# print(namas1.get_verte())
#
# namas1.set_verte("edfef")
# print(namas1.get_verte())



 # antra versija -----------------------------------

class Namas:
    def __init__(self, plotas, verte):
        self.plotas = plotas
        self.__verte = verte

    @property
    def verte(self):
        return self.__verte

    @verte.setter
    def verte(self,nauja):
        if str(nauja).isdigit():
            self.__verte = nauja
        else:
            print("verte turi būti skaičius")



namas1 = Namas(14, 25)
print(namas1.verte)

namas1.verte = 45
print(namas1.verte)

namas1.verte = "edfef"
print(namas1.verte)