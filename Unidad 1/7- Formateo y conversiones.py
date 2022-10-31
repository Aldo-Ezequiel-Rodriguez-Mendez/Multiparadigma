import datetime 

print("-----------MENU------------- \n" +
      " 1. Imprimir YYYY/MM/DD \n" +
      " 2. Imprimir  MM/DD/YYYY \n" + 
      "----------------------------")

opcionElegida = input("Ingrese la opcion a elegir: ")
fechaActual = datetime.date.today()

def darFormato():
    if opcionElegida == "1":
        print("\n La fecha actual con formato YYYY/MM/DD es " + fechaActual.strftime("%Y-%m-%d"))
    else:
        print("\n La fecha actual con formato MM/DD/YYYY es " + fechaActual.strftime("%m-%d-%Y"))

darFormato()



