from modulos.modulo1 import cliente
from modulos.modulo2 import llamado_modulo2


persona1 = cliente("Kevin", "ayala", "kevin.test@test.com", "22")
print(persona1)


persona2 = cliente ("Lautaro", "Bazzola", "Lautaro.test@test.com","26")
print(persona2)

persona3 = cliente ("Agustin", "Di'pilato", "Agustin.puto@test.com", "40")
print(persona3)


llamado_modulo2()