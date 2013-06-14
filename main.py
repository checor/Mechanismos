#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  mecanismos_2.py
#  
#  Copyright 2012 Los Mexmen <mexmen@checor-PC>
#  
#  Liscense: WTFPL

import Tkinter, pygame
import matplotlib.pyplot as plt
from math import *

class plot:
  def __init__(self, ang , a2, v2, a3, v3, vp1, vp2, vp3, ap1, ap2, ap3):
		
		plt.plot(ang , a2, color='b', label = 'Acel. barra 2', marker='o')
		plt.plot(ang, v2, color = 'b', linestyle='--', label = 'Vel. barra 2', marker='s')
		plt.plot(ang, a3, color = 'r', label = 'Acel. barra 3', marker='o' )
		plt.plot(ang, v3, color = 'r', linestyle='--', label = 'Vel. barra 3', marker='s')
		plt.title('Velocidades y aceleraciones')
		plt.xlabel('Angulo a2 en grados')
		plt.ylabel('Grados/s')

		
		plt.legend()
		plt.show()
		
		plt.plot(ang, vp1, color='c', label = 'Vel. pto 1', marker='o')
		plt.plot(ang, vp1, color='m', label = 'Vel. pto 2', marker='o')
		plt.plot(ang, vp1, color='k', label = 'Vel. pto 3', marker='o')
		
		plt.plot(ang, ap1, color='c', label = 'Acel. pto 1', linestyle = '--', marker='s')
		plt.plot(ang, ap2, color='m', label = 'Acel. pto 2', linestyle = '--',  marker='s')
		plt.plot(ang, ap3, color='k', label = 'Acel. pto 3', linestyle = '--',  marker='s')
		plt.title('Velocidades y aceleraciones de los puntos')
		plt.xlabel('Angulo a2 en grados')
		plt.ylabel('unidades/s')
		
		plt.legend()
		plt.show()
		
class animacion:
	def __init__(self, tetha1, tetha2, tetha3, vel_1, vel_2, acel_1, acel_2, a1, a2, a3, a4, p2x, p2y, est):
		size = self.width, self.height = 640, 480 
		black = (0, 0, 0)
		green = (0, 100, 0)
		blue = (0, 0, 255)
		background = (200, 200, 200)
		purple = (120, 76, 177)
		screen = pygame.display.set_mode(size)
		pygame.display.set_caption("Animacion - Presione ESC para salir") 
		pygame.font.init() 
		font = pygame.font.Font(None, 30) 
		clock = pygame.time.Clock()
		i=0
		offx,offy = 50,50
		zoom = float(1)
		while True:
			screen.fill(background)
			if i>=len(tetha1)-1:
				i=0
			#print i, tetha1[i], tetha2[i], tetha3[i]
			teclado = pygame.key.get_pressed()
			
			if (teclado[pygame.K_ESCAPE]): 
				break
			elif (teclado[pygame.K_UP]):
				if(zoom>=1):
					zoom+=1
				else:
					zoom = zoom*10
			elif (teclado[pygame.K_DOWN]):
				if(zoom>1):
					zoom = zoom - 1
				else:
					zoom = zoom / 10
			elif (teclado[pygame.K_w]):
				offy += 10
			elif (teclado[pygame.K_s]):
				offy += -10
			elif (teclado[pygame.K_d]):
				offx += 10
			elif (teclado[pygame.K_a]):
				offx += -10
			for event in pygame.event.get(): 
				if event.type == pygame.QUIT:
					exit()
			
			#Lo que en verdad hace por frame

			fx, fy = self.vector(screen, blue, offx, offy, tetha1[i], a1*zoom)
			#pygame.draw.circle(screen, green, (offx, self.height - offy), int(a1*zoom/20) )
			j = i
			if est == 1:
				while(j>=0):
					pto2 = (int(p2x[j]*zoom+offx) , int( self.height - p2y[j]*zoom -offy ) )
					pygame.draw.circle(screen, purple, pto2, int((a1*zoom/20)/5))
					j = j -1
			
			#Circulo de la estela
			pto2 = (int(p2x[i]*zoom+offx) , int( self.height - p2y[i]*zoom -offy ) )
			pygame.draw.circle(screen, green, pto2, int(a1*zoom/20))
			
			fxa, fya = self.vector(screen, blue, fx, fy, tetha2[i], a2*zoom)
			fx, fy = self.vector(screen, blue, fxa, fya, tetha3[i], a3*zoom)
			#self.vector(screen, blue, fx, fy, 180, a4*zoom)
			
			pygame.draw.circle(screen, green, (offx, self.height - offy), int(a1*zoom/20) )
			pygame.draw.circle(screen, green, (int(offx+a4*zoom), self.height - offy), int(a1*zoom/20) )
			
			texto1="v2 = " + str(round(vel_1[i], 6)) + " v3 = " + str(round(vel_2[i],6))
			texto2="a2 = " + str(round(acel_1[i], 6)) + " a3 = " + str(round(acel_2[i],6))
			self.printos(screen, texto1, 0,0, green, font)
			self.printos(screen, texto2, 0,40, green, font)
			
			pygame.display.flip() #Habra que cambiar esto para la estela
			clock.tick(30)
			i+=1
			
	def printos(self, surface, text, x, y, color, font):
		text_in_lines = text.split('\n')
		for line in text_in_lines:
			new = font.render(line, 1, color)
			surface.blit(new, (x, y))
			y += new.get_height()

	def vector(self, screen, color, x, y, ang, largo):
		y = self.height - y
		w, z = x + largo*cos(radians(360-ang)), y + largo*sin(radians(360-ang))
		x, y, w, z = int(x), int(y), int(w), int(z)
		pygame.draw.line(screen, color, (x, y), (w, z))
		return w, self.height-z

class ventana:
	def __init__(self, papa):
		root.wm_title("Mecanismo de 4 barras")
		root.wm_geometry("500x300")
		
		#Validate command para que no acepte letras
		vcmd = (root.register(self.val), '%S')
		
		#Labels a1
		self.la1 = Tkinter.Label(papa, text="a1 =").grid(pady = 5)
		self.la2 = Tkinter.Label(papa, text="a2 =").grid(row = 1, column = 0, pady = 5)
		self.la3 = Tkinter.Label(papa, text="a3 =").grid(row = 2, column = 0, pady = 5)
		self.la4 = Tkinter.Label(papa, text="a4 =").grid(row = 3, column = 0, pady = 5)
		#Textbox a1
		self.ta1 = Tkinter.Entry(papa, width=7)#, validate="key", validatecommand=vcmd)
		self.ta1.grid(row = 0, column = 1, pady = 0, padx = 0, sticky="W")
		self.ta2 = Tkinter.Entry(papa, width=7)#, validate="key", validatecommand=vcmd)
		self.ta2.grid(row = 1, column = 1, pady = 0, padx = 0, sticky="W")
		self.ta3 = Tkinter.Entry(papa, width=7)#, validate="key", validatecommand=vcmd)
		self.ta3.grid(row = 2, column = 1, pady =0, padx = 0, sticky="W")
		self.ta4 = Tkinter.Entry(papa, width=7)#, validate="key", validatecommand=vcmd)
		self.ta4.grid(row = 3, column = 1, pady = 0, padx = 0, sticky="W")
		#Botones
		self.calc = Tkinter.Button(papa, text="Calcular", command = self.calc)
		self.calc.grid(row = 4, pady = 5, padx= 5)
		self.res = Tkinter.Button(papa, text="Borrar datos", command = self.reset)
		self.res.grid(row = 4, column = 1)
		#Palomitas
		
		self.graf = Tkinter.IntVar()
		self.checkgraf = Tkinter.Checkbutton(papa, text="Mostrar animacion", variable=self.graf, command=self.pa)
		self.checkgraf.select()
		self.checkgraf.grid()
		
		self.plot  = Tkinter.IntVar()
		self.plott = Tkinter.Checkbutton(papa, text= "Mostrar vel. / acel.", variable=self.plot)
		self.plott.select()
		self.plott.grid(row=5, column = 1)
		
		self.est = Tkinter.IntVar()
		self.estt = Tkinter.Checkbutton(papa,text= "Dibujar estela", variable=self.est)
		self.estt.select()
		self.estt.grid(row=6, column = 0, sticky = "W")
		
		self.la5 = Tkinter.Label(papa, text="").grid()
		self.la6 = Tkinter.Label(papa, text="Velocidad de a1").grid(sticky="W", pady=5) #8
		self.la7 = Tkinter.Label(papa, text="Aceleracion de a1").grid(sticky="W", pady=5)
		#Textboxs de velocidad y aceleracion
		self.ta5 = Tkinter.Entry(papa, width=7)#, validate="key", validatecommand=vcmd)
		self.ta5.grid(row = 8, column = 1, sticky = Tkinter.W)
		self.ta6 = Tkinter.Entry(papa, width=7)#, validate="key", validatecommand=vcmd)
		self.ta6.grid(row = 9, column = 1, sticky = Tkinter.W)
		
		#La ventana de info del texto
		#self.la8 = Tkinter.Label(papa, text = "Analisis de rotabilidad :", padx=15).grid(row=0, column=3)
		#self.texto = Tkinter.Text(papa,width=40, height=20)
		#self.texto.grid(row=1, column=2, columnspan=20, rowspan=20)
		pass
		
		#Para los puntos
		Tkinter.Label(papa, text="Posicion del punto en barra a2:").grid(row = 0, column = 4, pady = 5, columnspan=4)
		Tkinter.Label(papa, text="x: ").grid(row = 1, column = 4, pady = 0, sticky="W")
		self.ep1x = Tkinter.Entry(papa, width=7) #1x
		self.ep1x.grid(row = 1, column = 5, sticky = Tkinter.W)
		Tkinter.Label(papa, text="y: ").grid(row = 1, column = 6, pady = 1)
		self.ep1y = Tkinter.Entry(papa, width=7) #1y
		self.ep1y.grid(row = 1, column = 7, sticky = Tkinter.W)
		
		Tkinter.Label(papa, text="Posicion del punto en barra a3:").grid(row = 2, column = 4, pady = 5, columnspan=4)
		Tkinter.Label(papa, text="x: ").grid(row = 3, column = 4, pady = 0, sticky="W")
		self.ep2x = Tkinter.Entry(papa, width=7) #1x
		self.ep2x.grid(row = 3, column = 5, sticky = Tkinter.W)
		Tkinter.Label(papa, text="y: ").grid(row = 3, column = 6, pady = 1)
		self.ep2y = Tkinter.Entry(papa, width=7) #1y
		self.ep2y.grid(row = 3, column = 7, sticky = Tkinter.W)
		
		Tkinter.Label(papa, text="Posicion del punto en barra a4:").grid(row = 4, column = 4, pady = 5, columnspan=4)
		Tkinter.Label(papa, text="x: ").grid(row = 5, column = 4, pady = 0, sticky="W")
		self.ep3x = Tkinter.Entry(papa, width=7) #1x
		self.ep3x.grid(row = 5, column = 5, sticky = Tkinter.W)
		Tkinter.Label(papa, text="y: ").grid(row = 5, column = 6, pady = 1)
		self.ep3y = Tkinter.Entry(papa, width=7) #1y
		self.ep3y.grid(row = 5, column = 7, sticky = Tkinter.W)
	
	def pa(self):
		if self.graf.get() == 0:
					self.estt.deselect()
		
	def punto1(self, t1):
		t1 = radians(t1)
		vt1 = radians(self.v_phi1)
		at1 = radians(self.a_phi1)
		x = self.p1x
		y = self.p2y
		
		posx = x*cos(t1) + y*cos(t1)
		posy = x*sin(t1) + y*cos(t1)
		
		vi = -x*sin(t1)*vt1 - y*sin(t1)*vt1
		vj = x*cos(t1)*vt1 + y*cos(t1)*vt1
		
		ai = -x*cos(t1)*vt1**2 - x*sin(t1)*vt1 - y*cos(t1)*vt1**2 - y*sin(t1)*at1 
		aj = -x*sin(t1)*vt1**2 + x*cos(t1)*vt1 - y*sin(t1)*vt1**2 + y*cos(t1)*at1 
	
		v, a = sqrt(vi**2 + vj**2), sqrt(ai**2 + aj**2)
		
		return posx, posy, v, a
	
	def punto2(self, a1, i,j, vt2, at2):
		x = self.p2x
		y = self.p2y
		t1 = radians(i)
		t2 = radians(j)
		vt1 = radians(self.v_phi1)
		at1 = radians(self.a_phi1)
		vt2 = radians(vt2)
		at2 = radians(at2)
		
		posx = a1*cos(t1) + x*cos(t2) - y*sin(t2)
		posy = a1*sin(t1) + x*sin(t2) + y*cos(t2)
		
		vpi = -1*a1*sin(t1)*vt1 - x*sin(t2)*vt2-y*cos(t2)*vt2
		vpj = a1*cos(t1)*vt1 + x*cos(t2)*vt2-y*sin(t2)*vt2
		
		api = -1*a1*cos(t1)*vt1**2 - a1*sin(t1)*at1 - x*cos(t2)*vt2**2 - x*sin(t2)*at2 \
		+ y*sin(t2)*vt2**2 - y*cos(t2)*at2
		
		apj = -1*a1*sin(t1)*vt1**2 + a1*cos(t1)*at1 - x*sin(t2)*vt2**2 + x*cos(t2)*at2 \
		- y*cos(t2)*vt2**2 - y*sin(t2)*at2
		
		v = sqrt(vpi**2 + vpj**2)
		a = sqrt(api**2 + apj**2)
		print v
		#print posx, posy,
		#print " en angulo " + str(i)
		
		return posx, posy, v, a
	
	def punto3(self, a1, a2, t1, t2, t3, vt2, vt3, at2, at3):
		x = self.p3x
		y = self.p3y
		t1 = radians(t1)
		t2 = radians(t2)
		vt1 = radians(self.v_phi1)
		at1 = radians(self.a_phi1)
		vt2 = radians(vt2)
		at2 = radians(at2)
		t3 = radians(t3)
		vt3 = radians(vt3)
		at3 = radians(at3)
		
		posx = a1*cos(t1) + a2*cos(t2) + x*sin(t3) + y*sin(t3)
		posy = a1*sin(t1) + a2*sin(t2) - x*cos(t3) - y*sin(t3)	
		
		vi =-a1*sin(t1)*vt1 - a2*sin(t2)*vt2 + x*cos(t3)*vt3 + y*cos(t3)*vt3
		vj = a1*cos(t1)*vt1 -+a2*cos(t2)*vt2 + x*sin(t3)*vt3 + y*sin(t3)*vt3
		
		v = sqrt(vi**2 + vj**2)
		print v
		ai = -a1*cos(t1)*vt1**2 - a1*sin(t1)*at1 - a2*cos(t2)*vt2**2 - a2*sin(t2)*at2\
		-x*sin(t3)*vt3**2 + x*cos(t3)*at3 - y*sin(t3)*vt3**2 + y*cos(t3)*at3
		
		aj = -a1*sin(t1)*vt1**2 + a1*cos(t1)*at1 - a2*sin(t2)*vt2**2 + a2*sin(t2)*at2\
		+x*cos(t3)*vt3**2 + x*sin(t3)*at3 + y*cos(t3)*vt3**2 + y*sin(t3)*at3
		
		a = sqrt(ai**2 + aj**2)
		
		return posx, posy, v, a
				
	def val(self, i):
		dic = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, ".":0}
		return dic.has_key(i)	
		
	def printf(self, textito):
		print textito
		#self.texto.insert(Tkinter.END, textito + "\n")
	
	def grasshof(self, a1, a2, a3, a4):
		#TODO: Hacer que no imprima tanta paja
		dim = [a1,a2,a3,a4]
		orded = sorted(dim)
		l = orded[3]
		p = orded[2]
		q = orded[1]
		s = orded[0]
			
		self.printf("Analisis mediante ley de grasshof:")
		self.printf("l = " + str(l))
		self.printf("p = " + str(p))
		self.printf("q = " + str(q))
		self.printf("s = " + str(s))
		if l == (p+q+s):
			self.printf("Los datos de entrada corresponden a una estructura")
			return False
		elif l > (p+q+s):
			self.printf("Los datos corresponden a una cadena abierta")
			return False
		elif (l+s) > (p+q):
			self.printf("Mecanismo doble oscilatorio Clase II")
		elif (l+s) <= (p+q):
			self.printf("Mecanismo de clase I")
		return True
	
	def angulos(self, a1, a2, a3, a4):
		tetha2_0, tetha2_180, tetha4_0, tetha4_180 = [0,180,0,180]
		self.printf("\nAnalisis de rotabilidad:")
		if (a3 + a4) >= (a1 + a2):
			#Se cumple la primera condicion de rotabilidad de a2
			self.printf("Se cumple la primera condicion de rotabilidad de a2")	
			if abs(a1- a2) >= abs(a3 - a4):
				#a2 es un eslabon rotatorio (de 0 a 360)
				self.printf("Se cumple la segunda condicion de rotabilidad de a2")
				self.printf("a2 es un eslabon rotatorio (de 0º a 360º)")
				a2_rot = True
			else:
				a2_rot = False
				tetha2_0 = degrees( acos((a1 ** 2 + a2 ** 2 - (a4 - a3) ** 2 ) / (2*a1*a2) ))
				#a2 es oscilatorio de tetha2_0 a 180°
				self.printf("No se cumple la segunda condicion de rotabilidad de a2")
				self.printf("a2 es oscilatorio de " + str(tetha2_0) + " a 180º")
		else:
			a2_rot = False
			tetha2_180 = degrees( acos( (a1 ** 2 + a2 ** 2 - (a3 + a4) ** 2) / (2*a1*a2) ))
			#a2 va desde
			self.printf("No se cumple la primera condicion de rotabilidad de a2")
			if( abs(a1- a2) >= abs(a3 - a4) ):
				#a2 es un eslabon Oscilatorio (de 0 a tetha2_180)
				self.printf("Se cumple la segunda condicion de rotabildad")
				self.printf("a2 es un eslabon oscilatorio de 0 a " + str(tetha2_180) + "")	
			else:
				tetha2_0 = degrees( acos((a1 ** 2 + a2 ** 2 - (a4 - a3) ** 2 ) / (2*a1*a2) ))
				self.printf("No se cumple la segunda condicion de rotabilidad")
				self.printf( "a2 es un eslabon oscilatorio de " + str(tetha2_0) + " a " + str(tetha2_180) +"")	
				#a2 es oscilatorio de tetha2_0 a tetha2_180
	
		#Valores de tetha4
		self.printf("\nCalculando valores de a4")
		if (abs(a4 - a1)) >= (abs(a2- a3)):
			#Se cumple la primera condicion de rotabilidad de a4
			self.printf("Se cumple la primera condicion de rotabildad de a4")
			if (a2 + a3) >= (a1 + a4):
				#El eslabon a4 es rotatorio
				self.printf("Se cumple la segunda condicion de rotabilidad de a4")
				self.printf("El eslabon a4 es rotatorio (de 0º a 360º)")
				a4_rot = True
			else:
				a4_rot = False
				self.printf("No se cumple la segunda condicion de rotabilidad de a4")
				tetha4_0 = degrees( acos ( ((a2 + a3) ** 2 - a1 ** 2 - a4 **2 )/ (2*a1*a4) ) )
				#El esalbon a4 es oscilatorio desde tetha4_0 hasta 180
				self.printf("El eslabon a4 es scilatorio desde " + str(tetha4_0) + " hasta 180º")
		else:
			a4_rot = False
			#No se cumpla la primera condicion de rotabilidad
			self.printf("No se cumple la primera condicion de rotabilidad de a4")
			tetha4_180 = degrees( acos ( ((a2 - a3) ** 2 - a1 ** 2 - a4 **2 )/ (2*a1*a4) ) )
			if (a2 + a3) >= (a1 + a4):
				self.printf("Se cumple la segunda condicion de rotabildad de a4")
				#El eslabon a4 es oscilatorio desde 0 hasta tetha4_180
				self.printf("El eslabon a4 es oscilatorio desde 0º hasta " + str(tetha4_180) + "º")
			else:
				self.printf("No se cumple la segunda condicion de rotabildad de a4")
				tetha4_0 = degrees( acos ( ((a2 + a3) ** 2 - a1 ** 2 - a4 **2 )/ (2*a1*a4) ) )
				#El esalbon a4 es oscilatorio desde tetha4_0 hasta tetha4_180
				self.printf("El eslabon a4 es oscilatorio desde " + str(tetha4_0)+ " hasta " + str(tetha4_180) + "º")
		self.printf("")
	
		if a2_rot == True:
			if a4_rot == True:
				self.printf("El mecanismo es doble rotatorio")
			else:
				self.printf("El mecanismo es rotatorio en a2 y oscilatorio en a4\n")
				self.printf("En la segunda configuracion a4, oscila desde " + str((360-tetha4_180)) + "º hasta " + str((360-tetha4_0)) + "º")
		else:
			if a4_rot == True:
				self.printf("El mecanismo es ocilatorio en a2 y rotatorio en a4\n")
				self.printf("En la segunda configuracion a2, oscila desde " + str((360-tetha2_0)) + "º hasta " + str((360-tetha2_180)) + "º")
			else:
				self.printf("El mecanismo es doble oscilatorio\n")
				self.printf("En la segunda configuracion a4, oscila desde " + str((360-tetha4_0)) + "º hasta " + str((360-tetha4_180)) + "º")
				self.printf("En la segunda configuracion a2, oscila desde " + str((360-tetha2_0)) + "º hasta " + str((360-tetha2_180)) + "º")
		return tetha2_0, tetha2_180
		
	def posicion(self, val_control, a1, a2, a3, a4, g1, g2):
		i=0
		q = radians(val_control)
		phi1 = radians(g1)
		phi2 = radians(g2)
		while True:
			f1 = a1*cos(q) + a2*cos(phi1) + a3*cos(phi2) - a4
			f2 = a1*sin(q) + a2*sin(phi1) + a3*sin(phi2)
    
			dif1 = (f1*cos(phi2)+f2*sin(phi2))/(a2*sin((phi1-phi2)))
			dif2 = (f2*sin(phi1)+f1*cos(phi1))/(a3*sin((phi2-phi1)))

			phi1 += dif1
			phi2 += dif2
			i+=1
			if (-1e-15 <dif1< 1e-15 and -1e-15 <dif2< 1e-15) or i>100:
				a,b = degrees(phi1), degrees(phi2)
				return a, b

	def velocidad(self, phi1, phi2, phi3, a1, a2, a3):
		vc = radians(self.v_phi1)
		ac = radians(self.a_phi1)
		phi1 = radians(phi1)
		phi2 = radians(phi2)
		phi3 = radians(phi3)
		v_phi2 = (vc*a1/a2)*(sin(phi3-phi1)/sin(phi2-phi3))
		v_phi3 = (vc*a1/a3)*(sin(phi1-phi2)/sin(phi2-phi3))
		a_phi2 = (a1*ac*sin(phi3-phi1)-a1*vc**2*cos(phi1-phi3)-a2*v_phi2**2*cos(phi2-phi3)-a3*v_phi3**2)/(a2*sin(phi2-phi3))
		a_phi3 = (a1*ac*sin(phi1-phi2)+a1*vc**2*cos(phi1-phi2)+a2*v_phi2**2+a3*v_phi3**2*cos(phi3-phi2))/(a2*sin(phi2-phi3))
		return degrees(v_phi2), degrees(v_phi3), degrees(a_phi2), degrees(a_phi3)
		
	def calc(self):
		#Agregar velocidad y aceleracion
		a1= float(self.ta1.get())
		a2= float(self.ta2.get())
		a3= float(self.ta3.get())
		a4= float(self.ta4.get())
		self.v_phi1 = float(self.ta5.get())
		self.a_phi1 = float(self.ta6.get())
		#Lo nuevo de los calculos
		self.p1x = float(self.ep1x.get())
		self.piy = float(self.ep1y.get())
		self.p2x = float(self.ep2x.get())
		self.p2y = float(self.ep2y.get())
		self.p3x = float(self.ep3x.get())
		self.p3y = float(self.ep3y.get())
		if self.grasshof(a1, a2, a3, a4) == True:
			n1, n2 = self.angulos(a1, a2, a3, a4)
			n1, n2 = int(n1), int(n2)
			#if (a1)
			g1, g2 = 0, 360-90 #Checar esta madre. Tener un "banco" de posibles valores
			
			ang_q=[] #Lista de todas las posiciones a guardar en vectores
			ang_t1=[]
			ang_t2 = []
			vel_t1 = []
			vel_t2 = []
			acel_t1 = []
			acel_t2 = []
			#Estas que siguen son para los nuevos puntos
			vp1, vp3, vp2 = [], [], []
			ap1, ap3, ap2 = [], [], []
			pos_p2i = []
			pos_p2j = []
			
						
			i = n1
			while i<=n2: #De a1 a a2
				pos = self.posicion(i, a2, a3, a4, a1, g1, g2)
				g1, g2 = pos
				ang_q.append(i) #Tetha1
				ang_t1.append(g1) #Tetha2
				ang_t2.append(g2) #Teha3
				#print "Angulo " + str(i) + " " +  str(pos)
				v1, v2, ac1, ac2 = self.velocidad(i,g1,g2,a2,a3,a4)
				vel_t1.append(v1) #Velocidad tetha2
				vel_t2.append(v2) #Vel tetha3
				acel_t1.append(ac1) #
				acel_t2.append(ac2) #
				#Nuevas funciones de los puntos
				pos_p1x, pos_p1y, vel_p1, acel_p1 = self.punto1(i)
				vp1.append(vel_p1)
				ap1.append(acel_p1)#
				pos_p2x, pos_p2y, vel_p2, acel_p2 = self.punto2(a2, i, g1, v1, ac1)
				pos_p2i.append(pos_p2x)
				pos_p2j.append(pos_p2y)
				vp2.append(vel_p2)
				ap2.append(acel_p2)#
				pos_p3x, pos3y, vel_p3, acel_p3 = self.punto3(a2, a3, i, g1, g2, v1, v2, ac1, ac2)
				vp3.append(vel_p3)
				ap3.append(acel_p3)
				i+=1
			
			n1, n2 = 360-n2, 360-n1
			i=n1
			while i<=n2: #De a1 a a2
				pos = self.posicion(i, a2, a3, a4, a1, g1, g2)
				g1, g2 = pos
				ang_q.append(i)
				ang_t1.append(g1)
				ang_t2.append(g2)
				#print "Angulo " + str(i) + " " +  str(pos)
				v1, v2, ac1, ac2 = self.velocidad(i,g1,g2,a2,a3,a4)
				vel_t1.append(v1)
				vel_t2.append(v2)
				acel_t1.append(ac1)
				acel_t2.append(ac2)
				pos_p1x, pos_p1y, vel_p1, acel_p1 = self.punto1(i)
				vp1.append(vel_p1)
				ap1.append(acel_p1)#
				pos_p2x, pos_p2y, vel_p2, acel_p2 = self.punto2(a2, i, g1, v1, ac1)
				pos_p2i.append(pos_p2x)
				pos_p2j.append(pos_p2y)
				vp2.append(vel_p2)
				ap2.append(acel_p2)#
				pos_p3x, pos3y, vel_p3, acel_p3 = self.punto3(a2, a3, i, g1, g2, v1, v2, ac1, ac2)
				vp3.append(vel_p3)
				ap3.append(acel_p3)
				i+=1
			#Falta un if por lo de la palomita
			if self.graf.get() == 1:
				an = animacion(ang_q, ang_t1, ang_t2, vel_t1, vel_t2, acel_t1, acel_t2, a2, a3, a4 ,a1, pos_p2i, pos_p2j, self.est.get())
			if self.plot.get() == 1:
				pt = plot(ang_q, acel_t1, vel_t1, acel_t2, vel_t2, vp1, vp2, vp3, ap1, ap2, ap3)
		
	def reset(self):
		self.ta1.delete(0, Tkinter.END)
		self.ta2.delete(0, Tkinter.END)
		self.ta3.delete(0, Tkinter.END)
		self.ta4.delete(0, Tkinter.END)
		self.ta5.delete(0, Tkinter.END)
		self.ta6.delete(0, Tkinter.END)
		self.ep1x.delete(0, Tkinter.END)
		self.ep2x.delete(0, Tkinter.END)
		self.ep3x.delete(0, Tkinter.END)
		self.ep1y.delete(0, Tkinter.END)
		self.ep2y.delete(0, Tkinter.END)
		self.ep3y.delete(0, Tkinter.END)
		#self.texto.delete(0, Tkinter.END) Esta pendejada no jala, checar doc.
		pass
		
root = Tkinter.Tk()
v = ventana(root)
root.mainloop()
