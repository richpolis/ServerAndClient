#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime


class Imei(object):
    sql = ""
    tabla = "tabla_"
    alerta = ""
    fecha = {"year": "", "month": "", "day": ""}
    tiempo = {"hour": "", "minute": "", "second": ""}
    latitud = ""
    longitud = 0.0
    velocidad = 0.0
    curso = ""
    otro = ""
    gsm_data = ""
    comandos_entrada = ""

    def set_data(self, data):
        # desfragmentar el mensaje
        lista1 = data.split("#")
        lista = lista1[1].strip().split(",")
        self.comandos_entrada = data
        for index in range(8):
            if index == 0:
                # IMEI
                self.tabla = self.tabla + "" + lista[index];
                print "IMEI: " + lista[index];
            elif index == 1:
                # Alerta
                self.alerta = lista[index];
                print "Alerta: " + lista[index];
            elif index == 2:
                self.gsm_data = lista[index];
                print "GSM data: " + lista[index];
            elif index > 2:
                datos = lista[index].strip().split(":")
                datos[1] = datos[1].strip()
                print datos[0] + ": " + datos[1]
                if datos[0] == "DATE":
                    s_fecha = datos[1]
                    #  s_fecha = "" + s_fecha[4:6] + "-" + s_fecha[2:4] + "-" + s_fecha[:2]
                    #  self.fecha = datetime.datetime.strptime(s_fecha , '%d-%m-%y').date()
                    self.fecha["year"] = "20" + s_fecha[:2]
                    self.fecha["month"] = s_fecha[2:4]
                    self.fecha["day"] = s_fecha[4:6]
                elif datos[0] == "TIME":
                    s_tiempo = datos[1]
                    self.tiempo["hour"] = s_tiempo[:2]
                    self.tiempo["minute"] = s_tiempo[2:4]
                    self.tiempo["second"] = s_tiempo[4:6]
                elif datos[0] == "LAT":
                    self.latitud = float(datos[1][:-1])
                elif datos[0] == "LOT":
                    self.longitud = float(datos[1][:-1]) - float(datos[1][:-1]) - float(datos[1][:-1])
                    letra = datos[-1]
                elif datos[0] == "Speed":
                    self.velocidad = datos[1]
                elif datos[0] == "CURSE":
                    self.curso = datos[1]
                elif datos[0] == "OTHER":
                    self.otro = datos[1]

    def get_query_insert(self):
        sql = "INSERT INTO " + self.tabla + "(Alerta, Fecha_Envio, Hora_Envio, Latitud , Longitud, Velocidad, " \
                                            "Comandos_entrada, fecha_servidor, hora_servidor) " \
                                            "VALUES (%s, %s ,%s , %s, %s, %s, %s, %s, %s )"
        return sql

    def get_args_insert(self):
        return (self.alerta, self.get_s_fecha(), self.get_s_tiempo(), self.latitud,
                self.longitud, self.velocidad, self.comandos_entrada,
                self.get_server_fecha(), self.get_server_tiempo())
                
    def get_query_insert_with_args(self):
        sql = self.get_query_insert();
        args = self.get_args_insert();
        return sql % args

    def get_s_fecha(self):
        #  s_fecha = "20" + self.fecha["year"] + "-" + self.fecha["month"] + "-" + self.fecha["day"]
        t = datetime.datetime(int(self.fecha["year"]), int(self.fecha["month"]), int(self.fecha["day"]), 0, 0)
        # return t.strftime('%Y-%m-%d')
        return t

    def get_s_tiempo(self):
        #  s_tiempo = "" + self.tiempo["hour"] + ":" + self.tiempo["minute"] + ":" + self.tiempo["second"]
        t = datetime.time(int(self.tiempo["hour"]), int(self.tiempo["minute"]), int(self.tiempo["second"]))
        # return t.strftime('%H:%M:%S')
        return t

    def get_server_fecha(self):
        hoy = datetime.datetime.now()
        # return hoy.strftime('%Y-%m-%d')
        return hoy

    def get_server_tiempo(self):
        hoy = datetime.datetime.now()
        # return hoy.strftime('%H:%M:%S')
        return hoy
