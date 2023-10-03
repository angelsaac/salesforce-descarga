import psycopg2
from simple_salesforce import Salesforce
import requests
import pandas as pd
import numpy as np
from io import StringIO
import remplazarCaracteres
import caracteres_remplazar
from psycopg2.extensions import register_adapter, AsIs
import psycopg2.extras as extras
from datetime import date 
from datetime import timedelta 
from tkinter import *
from tkinter import messagebox as MessageBox


# loguearse en salesforece
sf = Salesforce(username='tuusuario@domain.com', 
password='123',
security_token='tutokendeseguridad')


# detalles del reporte de tareas
sf_org = 'https://tudomain.my.salesforce.com/'
report_id = 'id'
export_params = '?isdtp=p1&export=1&enc=UTF-8&xf=csv'
# descarga del reporte
sf_report_url = sf_org + report_id + export_params
response = requests.get(sf_report_url, headers=sf.headers, cookies={'sid': sf.session_id})
new_report = response.content.decode('utf-8')
report_tareas = pd.read_csv(StringIO(new_report)) #lectura del csv

# detalles del reporte de casos
report_id = 'id'
sf_report_url = sf_org + report_id + export_params
response = requests.get(sf_report_url, headers=sf.headers, cookies={'sid': sf.session_id})
new_report = response.content.decode('utf-8')
report_casos = pd.read_csv(StringIO(new_report)) #lectura del csv

# detalles del reporte de categorias
report_id = 'id'
sf_report_url = sf_org + report_id + export_params
response = requests.get(sf_report_url, headers=sf.headers, cookies={'sid': sf.session_id})
new_report = response.content.decode('utf-8')
report_categorias = pd.read_csv(StringIO(new_report)) #lectura del csv


characters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz- 0123456789ÁÉÍÓÚáéíóú"

#REPORTE DE TAREAS
for i in report_tareas.index:
    report_tareas["Nombre completo"][i] = ''.join( x for x in report_tareas["Nombre completo"][i] if x in characters)

for i in report_tareas.index:
    report_tareas["Asignado a: Nombre completo"][i] = ''.join( x for x in report_tareas["Asignado a: Nombre completo"][i] if x in characters)
result= caracteres_remplazar.remplazarCaracteress(report_tareas)

#REPORTE CASOS
for i in report_casos.index:
    report_casos["Nombre completo"][i] = ''.join( x for x in report_casos["Nombre completo"][i] if x in characters)
result= caracteres_remplazar.remplazarCaracteress(report_casos)

#REPORTE CATEGORIAS
for i in report_categorias.index:
    report_categorias["Nombre del cliente: Nombre completo"][i] = ''.join( x for x in report_categorias["Nombre del cliente: Nombre completo"][i] if x in characters)
result= caracteres_remplazar.remplazarCaracteress(report_categorias)


result_tareas= caracteres_remplazar.remplazarCaracteress(report_tareas)
result_casos= caracteres_remplazar.remplazarCaracteress(report_casos)
result_categorias= caracteres_remplazar.remplazarCaracteress(report_categorias)
# DESCARGAR CSV
# result_tareas.to_csv('tareas.csv', index=False, encoding='utf-8', header=None) #DESCARGA CSV SI QUIERES
# result_casos.to_csv('casos.csv', index=False, encoding='utf-8', header=None) #DESCARGA CSV SI QUIERES
# result_categorias.to_csv('categorias.csv', index=False, encoding='utf-8', header=None) #DESCARGA CSV SI QUIERES
