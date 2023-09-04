from modulos.modulo1 import cliente
from modulos.modulo2 import llamado_modulo2

from modulos.registro import main

#persona1 = cliente("Kevin", "ayala", "kevin.test@test.com")
#print(persona1)


#persona2 = cliente ("Lautaro", "Bazzola", "Lautaro.test@test.com")
#print(persona2)

persona1 = cliente(main())
print(persona1)
llamado_modulo2()