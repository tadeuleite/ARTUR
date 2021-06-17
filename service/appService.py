import os
import psycopg2

class appService(object): 

    def get_responses():
        conn = psycopg2.connect('postgres://gtmzrjxctpfbwf:656cb219cfe588e047b012f19241c8431c223c27cf6e148a077f1ca63ccff875@ec2-34-230-115-172.compute-1.amazonaws.com:5432/dfcbi0ip98i74n', sslmode='require')
        cur = conn.cursor()
        responses = []
        try:
             cur.execute('select txt_response from "QnA".response')
             responses = cur.fetchall()
        except:
            teste = 'Não foi possível conectar ao banco'
        finally:
            cur.close()
            conn.close()
        return responses
