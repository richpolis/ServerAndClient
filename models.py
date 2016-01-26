#!/usr/bin/python
# -*- coding: utf-8 -*-

from db import MysqlManager
import datetime

class Imei(MysqlManager):
	sql = ""
	tabla = "tabla_"
	alerta = ""
	fecha = {"year":"","month": "","day": ""}
	tiempo = {"hour":"","minute":"","second":""}
	latitud = ""
	longitud = ""
	velocidad = ""
	curso = ""
	otro = ""
	
	def set_data(self, lista):
		for index in range(10):
			if index == 0:
				# IMEI
				self.tabla = self.tabla + "" + lista[index];
				print "IMEI: " + lista[index];
			elif index == 1:
				# Alerta
				self.alerta = lista[index];
				print "Alerta: " + lista[index];
			elif index >= 2:
				datos = lista[index].strip().split(":")
				datos[1] = datos[1].strip()
				print datos[0] + ": " + datos[1]
				if datos[0] == "DATE":
					s_fecha = datos[1]
					#  s_fecha = "" + s_fecha[4:6] + "-" + s_fecha[2:4] + "-" + s_fecha[:2]
					#  self.fecha = datetime.datetime.strptime(s_fecha , '%d-%m-%y').date()
					self.fecha["year"]  = s_fecha[:2]
					self.fecha["month"] = s_fecha[2:4]
					self.fecha["day"] = s_fecha[4:6]
				elif datos[0] == "TIME":
					s_tiempo = datos[1]
					self.tiempo["hour"] = s_tiempo[:2]
					self.tiempo["minute"] = s_tiempo[2:4]
					self.tiempo["second"] = s_tiempo[4:6]
				elif datos[0] == "LAT":
					self.latitud = datos[1]
				elif datos[0] == "LOG":
					self.longitud = datos[1]
				elif datos[0] == "Speed":
					self.velocidad = datos[1]
				elif datos[0] == "CURSE":
					self.curso = datos[1]
				elif datos[0] == "OTHER":
					self.otro = datos[1]
	
	def get_query_insert(self):
		