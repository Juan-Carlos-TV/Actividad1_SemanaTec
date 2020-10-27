#A008267629 Juan Carlos Triana Vela
#A00827858 Enrique Jose Garcia
from turtle import *
from freegames import vector

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

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
    end_fill                       #Termina de llenar

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('violet'), 'V')             #Asigna el color violeta a la "V"
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()