from django.shortcuts import render
from django.http import HttpResponse
import psycopg2 
import pandas as pd
import csv

# Create your views here.
def main(request):
    file=open('static/immo_CSV.csv', 'rb')
    if  file ==None:
        html="<p>Immo_csv non présent!<p><a href=\"../\">Lien vers load_csv</a>"
    else:
        
        html=read_immo()
        
           
    return HttpResponse(html)


def read_immo():
    conn = psycopg2.connect("dbname=test user=postgres password=jaune2000")
    cur = conn.cursor()
    data=pd.read_csv('static/immo_CSV.csv',delimiter=";")
    print("DAAAAAAAAATA")
    print(data.shape)
    print(data.columns)
    print(type(data))
    data['prix_tva_reduite'] = data['prix_tva_reduite'].fillna(0)
    print(data)
    print(data['prix_tva_reduite'])
    #data.to_sql("immoTable",conn)
    #cur.execute("DROP * FROM immo WHERE balcony=True")
    #db_table_nm="immo"
    csv_name = "static/immo_CSV.csv"
    qry = "TRUNCATE immo;"
    cur.execute(qry)
    #path ='D:/Bureau/Formation/brief14/bien_immo/static/immo_CSV.csv'

    with open(csv_name , 'r') as f:
    # Notice that we don't need the `csv` module.
        next(f) # Skip the header row.
        cur.copy_from(f, 'immo', sep=';',null='')
    conn.commit()
    #path ='static/immo_CSV.csv'
    #qry = "COPY immo(Id, id_lot,nb_piece,typologie,prix_tva_reduite,prix_tva_normale,\"prix_HT\",\"prix_m2_HT\",\"prix_m2_TTC\",orientation,exterieur,balcony,garden,parking,ville,departement,date_fin_programme,adresse_entiere,date_extraction) FROM '"+path+"' DELIMITER ';' CSV HEADER;"
    #cur.execute(qry)
    sql= pd.read_sql_query("SELECT * FROM immo WHERE balcony = False ",conn)
    print(sql)
    return "<p>"+str(sql)+"<p><p><a href=\"../\">Lien vers load_csv</a>" 
#read_immo()