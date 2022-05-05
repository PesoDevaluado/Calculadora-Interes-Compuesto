while True:

    print("Bienvenido a la Calculadora de Interes Compuesto V4...")
    print("Por favor no usar comas", "," ,"sino puntos", ".","dentro de la calculadora...")
    print("------------------------------------------------------------------")

    InversionInicial = int(input("Inversion Inicial: "))
    print("------------------------------------------------------------------")
    PlazoInversion = int(input("Plazo de Inversion en Dias: "))
    print("------------------------------------------------------------------")
    Interes = float(input("% de Interes Anual de la Inversion: "))
    print("------------------------------------------------------------------")
    Meses = int(input("Cantidad de meses de calculo: "))
    print("------------------------------------------------------------------")
    RestoMensual = int(input("Dinero que va a separar de sus ganancias para vivir: "))
    print("------------------------------------------------------------------")
    ImpuestoGanancias = input("Impuesto a las Ganancias S/N: ")
    print("------------------------------------------------------------------")

    Contador = 0
    ImpuestoGanancias3 = 3/100

    for i in range(Meses):
        InteresMensual = (((Interes/100)*PlazoInversion)/365)
        GananciaY = (InversionInicial*InteresMensual)*ImpuestoGanancias3
        Contador = Contador + 1 
        if ImpuestoGanancias == "N":
            GananciaX = InversionInicial + (InversionInicial * InteresMensual) - RestoMensual
            print("Mes #"+str(Contador),"Tuviste una ganancia de: "+"{:.2f}".format(GananciaX))
        else:
            GananciaX = InversionInicial + ((InversionInicial * InteresMensual)-GananciaY) - RestoMensual
            print("Mes #"+str(Contador),"Tuviste una ganancia de: "+"{:.2f}".format(GananciaX), "/ Imp Ganancias: "+"{:.2f}".format(GananciaY))
        InversionInicial = GananciaX
        
        

    Repetir = input("Desea hacer otro Calculo? S/N: ")

    if Repetir == "N":
        break
    else:
        print("Se Reinicia Calculadora...")

