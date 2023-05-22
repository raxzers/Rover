#TECSpace
#Proyecto Rover
#Codigo para mover motores

#Primero se importan las librerias
#Se elige RPI.GPIO y no GPIO Zero ya que puede ser utilizada con facilidad para los otros modulos
#y no requieere conocer todos los metodos para cada clase

import RPI.GPIO as GPIO
from time import sleep

#Se declara el modo, donde existe BOARD y BCM
#BOARD = Numeros de los pins segun la tarjeta
#BCM Broadcom = utiliza los pines segun su numero GPIO
GPIO.setmode(GPIO.BOARD)
#Se quitan las advertencias, solo porque dicen que son molestas
GPIO.setwarning(False)

#Definimos una clase para los motores
class Motor():
    def __init__(self,Enable,Backward,Forward):
        self.Enable = Enable
        self.Forward = Forward
        self.Backward = Backward
        #Se declaran esos pines como salidas
        GPIO.setup(self.Enable, GPIO.OUT)
        GPIO.setup(self.Forward, GPIO.OUT)
        GPIO.setup(self.Backward, GPIO.OUT)
        #Se define la frecuencia de los pulsos, que determina la velocidad del motor
        #pwm es Pulse Width Modulation
        self.pwm = GPIO.PWM(self.Enable,100) #Maximo
        self.pwm.star(0) #Condicion inicial
        
    #Metodo para ir hacia adelante
    def avanzar(self, v = 50, t = 0):
        GPIO.output(self.Forward,GPIO.HIGH)
        GPIO.output(self.Backward,GPIO.LOW)
        self.pwm.ChangeDutyCycle(v)
        sleep(t)
    
    #Metodo para ir hacia atras
    def retroceder(self, v = 50, t = 0):
        GPIO.output(self.Backward,GPIO.HIGH)
        GPIO.output(self.Forward,GPIO.LOW)
        self.pwm.ChangeDutyCycle(v)
        sleep(t)
    
    #Metodo para parar
    def parar(self, t = 0):
        self.pwm.ChangeDutyCycle(0)
        sleep(t)
        
#Codigo Principal 
motor_der = Motor(2,3,4)
motor_izq = Motor(5,6,7)

#Un loop que se repite siempre
while True:
    motor_der.avanzar(100, 2)
    motor_izq.avanzar(100, 2)
