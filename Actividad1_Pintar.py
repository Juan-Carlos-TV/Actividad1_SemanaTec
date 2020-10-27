#A008267629 Juan Carlos Triana Vela
#A00827858 Enrique Jose Garcia
from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()                                   #Pen up (levanta el lapiz)
    goto(start.x, start.y)                 #Ubica a Start como punto de partida
    down()                                 #Pen down (baja el lapiz)
    goto(end.x, end.y)                     #Traza hasta el punto end

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)                 #Ubica Start como punto de partida
    down()
    begin_fill()                           #Comienza el llenado

    for count in range(4):                 #Se ejecuta el ciclo 4 veces al ser una figura de 4 lados
        forward(end.x - start.x)           #Avanza de end.x a start.x
        left(90)                           #Gira 90° (360°/4) a la izquierda

    end_fill()

def circle(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)             #Toma como punto de partida a Start
    down()
    
    arc = 0.01745*(end.x - start.x)    #Calcula el arco para un ángulo de 1 grado, recordando que Arc = rad * r
                                       #Donde r = end.x - start.x
    begin_fill()                       #Empieza el llenado
    
    for count in range(360):           #Se ejecutará el ciclo 360 veces por ser 360 segmentos de 1 grado
        forward(arc)                   #Se desplaza la longitud de un arco
        left(1)                        #Gira un grado a la izquierda
        
    end_fill()                         #Termina el llenado

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)         #Convierte a start en punto de partida
    down()
    
    begin_fill()                   #Comienza el llenado de la figura
    for count in range(4):         #Ejecuta el ciclo 4 veces al ser una figura de 4 lados
        if (count % 2) == 0 :      
            forward (end.x - start.x)  #Si el contador es par, se trata una linea horizontal
        else:
            forward (end.y - start.y)  #Si el contador es impar, se trata de una linea vertical
            
        left(90) #Para cualquiera de los casos, gira 90° (360°/4 lados) a la izquierda
            
    end_fill()                    #Termina de llenar
    
def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)         #Convierte a start en punto de partida
    down()
    
    begin_fill()                   #Comienza el llenado de la figura
    for count in range(3):         #Ejecuta el ciclo 3 veces al ser una figura de 3 lados
        forward(end.x - start.x)   #Cada lado medirá la diferencia entre el X de end y de start
        left(120)                  #Gira 120° (360°/3 Lados) a la izquierda
    end_fill()                     #Termina de llenar

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']         #Extaer el punto de partida de state

    if start is None:                 
        state['start'] = vector(x, y)  #Si start es nulo, se le asigna el valor del punto clickeado
    else:
        shape = state['shape']         #Si start posee un valor se asigna a shape la función de la figura
        end = vector(x, y)             #Se lee el punto end
        shape(start, end)              #Se ejecuta la función de shape
        state['start'] = None          #Se asigna un valor nulo a start

def store(key, value):
    "Store value in state at key."
    state[key] = value                 #Guarda un valor dentro de state en base a una key

state = {'start': None, 'shape': line} #Inicializa state
setup(420, 420, 370, 0)                #Establece el tamaño de la ventana (420 x 420) y su posición
onscreenclick(tap)                     #Para leer los clicks en la pantalla se usará tap
listen()
#Onkey asigna un evento/función a un caracter específico
#Se usa lambda debido a que onkey requiere una función que no tenga parametros
onkey(undo, 'u')                                #Asigna el comando undo a u
onkey(lambda: color('black'), 'K')              #Asigna el color negro a la "K"
onkey(lambda: color('white'), 'W')              #Asigna el color blanco a "W"
onkey(lambda: color('green'), 'G')              #Asigna el color verde a "G"
onkey(lambda: color('blue'), 'B')               #Asigna el color azul a "B"
onkey(lambda: color('red'), 'R')                #Asigna el color red a "R
onkey(lambda: color('violet'), 'V')             #Asigna el color violeta a la "V"
onkey(lambda: store('shape', line), 'l')        #Asigna la figura linea a "l"
onkey(lambda: store('shape', square), 's')      #Asigna la figura de cuadrado a "s"
onkey(lambda: store('shape', circle), 'c')      #Asigna la figura de círculo a "c"
onkey(lambda: store('shape', rectangle), 'r')   #Asigna la figura de rectangulo a "r"
onkey(lambda: store('shape', triangle), 't')    #Asigna la figura triagulo a "t"
done()                                          #Comienza el loop de eventos