from ast import For
from calendar import c
import psycopg2
from simple_salesforce import Salesforce
import requests
import pandas as pd
import numpy as np
import csv
from io import StringIO
import remplazarCaracteres
import caracteres_remplazar
import os 
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

for i in report_df.index:
    try:
        print(report_df["Nombre del cliente"][i])
        report_df["Nombre del cliente"][i] = ''.join( x for x in report_df["Nombre del cliente"][i] if x in characters)
    except:
        report_df["Nombre del cliente"][i] = 'Sin Asignar'
        
result= caracteres_remplazar.remplazarCaracteress(report_df)
# result.to_csv('facebook.csv', index=False, encoding='utf-8', header=None) #DESCARGA CSV SI QUIERES
print(result)