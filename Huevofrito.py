ingredientes= input("Tienes todos los ingredientes y los utensilios limpios? (si o no)")
if ingredientes== "no":
    print("Ir a la tienda a comprar o lavar lo necesario")
if ingredientes== "si" or ingredientes== "no": 
    print("Verificar el tipo de estufa")
estufa= input("La estufa es electrica o a gas? (Electrica o a gas)")
if estufa== "a gas":
    print("Verificar que tengas fosforos")
if estufa== "electrica" or estufa== "a gas":
    print("Encender")
    print("Colocar el sarten sobre la estufa")
    print("Agregar Aceite") 
caliente= input("Esta lo sufucientemente caliente? (si o no)")
if caliente== "no":
    print("Esperar unos minutos mas")
if caliente== "si" or caliente== "no":
    print("partir el huevo")
    print("agregarlo al sarten")
cocido= input("Está bien cocido?")
while cocido=="no":
    print("lo dejo cocer bien")
    cocido= input("Está bien cocido?")
if cocido== "si":
    print("Pasarlo al plato")
    print("agregarle sal y pimienta")
    print("Comerlo!!")
