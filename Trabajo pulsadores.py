from machine import Pin as pin
import utime
from utime import sleep as pausa, sleep_ms as pausam, sleep_us as pausau
boton1=pin(27,pin.IN,pin.PULL_UP)
boton2=pin(26,pin.IN,pin.PULL_UP)
boton3=pin(25,pin.IN,pin.PULL_UP)
boton4=pin(33,pin.IN,pin.PULL_UP)

velocidadmas=pin(19,pin.IN,pin.PULL_UP)
velocidadmen=pin(21,pin.IN,pin.PULL_UP)

leda=pin(2,pin.OUT)
ledb=pin(4,pin.OUT)
ledc=pin(16,pin.OUT)
ledd=pin(17,pin.OUT)
lede=pin(5,pin.OUT)
ledf=pin(18,pin.OUT)
ledg=pin(19,pin.OUT)
ledh=pin(21,pin.OUT)
vel=0.5
utime.sleep(vel)

forma1=[leda,ledb,ledc,ledd,lede,ledf,ledg,ledh]
forma2=[leda,ledc,lede,ledg,ledb,ledd,ledf,ledh]
forma3=[ledd,lede,ledc,ledf,ledb,ledg,leda,ledh]
forma4=[ledd,ledc,ledb,leda,lede,ledf,ledg,ledh]
forma5=[ledb,leda,ledg,ledh,ledd,ledc,lede,ledf]
def secuencia1():
    for i in forma1:
        for j in range (2):
            i.value(not i.value())
            pausam(80)
            
def secuencia2():
    for i in reversed(forma1):
        for j in range (2):
            i.value(not i.value())
            pausam(80)

def secuencia3():
    for i in forma2:
        for j in range (2):
            i.value(not i.value())
            pausam(250)
            
def secuencia4():
    for i in reversed(forma2):
        for j in range (2):
            i.value(not i.value())
            pausam(250)

def secuencia5():
    for i in forma3:
        for j in range (2):
            i.value(not i.value())
            pausam(250)

def secuencia6():
    for i in reversed(forma3):
        for j in range (2):
            i.value(not i.value())
            pausam(250)

def secuencia7():
    for i in forma4:
        for j in range (2):
            i.value(not i.value())
            pausam(250)

def secuencia8():
    for i in reversed(forma4):
        for j in range (2):
            i.value(not i.value())
            pausam(250)

def secuencia9():
    for i in forma5:
        for j in range (2):
            i.value(not i.value())
            pausam(250)
          
def secuencia10():
    for i in reversed(forma5):
        for j in range (2):
            i.value(not i.value())
            pausam(250)
            
while(True):
    if(boton1.value()==0):
        secuencia1()
    
    elif(boton2.value()==0):
        secuencia2()
    
    elif(boton3.value()==0):
        secuencia3()

    elif(boton4.value()==0):
        secuencia4()
    

    
    else:
        if(boton1.value() and boton2.value()==0 and boton3.value() and boton4.value()==1):
            secuencia5()
        
        elif(boton1.value() and boton3.value()==0 and boton2.value() and boton4.value()==1):
            secuencia6()
     
        elif(boton1.value() and boton4.value()==0 and boton2.value() and boton3.value()==1):
            secuencia7()
        
        elif(boton2.value() and boton3.value()==0 and boton1.value() and boton4.value()==1):
            secuencia8()
    
        elif(boton2.value() and boton4.value()==0 and boton1.value() and boton3.value()==1):
            secuencia9()
    
        elif(boton3.value() and boton4.value()==0 and boton1.value() and boton2.value()==1):
            secuencia10()
            


        
        
#     else:
 #       if(boton3.value()==0):
  #          abrir()

#    if not velocidadmas.value():
 #       vel=vel+0.02
#    utime.sleep(0.3)