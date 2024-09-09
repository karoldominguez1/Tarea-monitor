##TAREA 1 INFO 2

class Reporte:
    def __init__(self, zona, hora, frec1, presion, sp, temp, frec2):
        self.__zona =zona
        self.__hora = hora
        self.__frec1= frec1
        self.__presion= presion
        self.__sp= sp
        self.__temp= temp
        self.__frec2= frec2

    def get_zona(self):
        return self.__zona
    
    def get_hora(self):
        return self.__hora
    
    def get_frec1(self):
        return self.__frec1
    
    def get_presion(self):
        return self.__presion
    
    def get_sp(self):
        return self.__sp
    
    def get_temp(self):
        return self.__temp
    
    def get_frec2(self):
        return self.__frec2
    
    def __str__(self):
        return (f'''
            Zona de uso del equipo:{self.__zona} 
            Hora del reporte:{self.__hora}
            Frecuencia cardiaca:{self.__frec1}
            Presión arterial:{self.__presion}
            Temperatura corporal:{self.__temp}
            Frecuencia respiratoría:{self.__frec2}''')

def leerarchivo (reportes) :
    lista=[]
    with open (reportes, 'r') as file:

        for i in file:
            todos= i.strip().split('|')
            zonauso= todos [0]
            hora= todos [1]

            datosrecolec= todos[2].split('^')
            frec11= datosrecolec [0]
            presion= datosrecolec[1]
            tempo= datosrecolec[2]
            frec22= datosrecolec [3]

            objeto1= Reporte (zonauso, hora, datosrecolec,frec11, tempo, frec22)
            reportes.append (objeto1)

    return reportes 

  

        

            
