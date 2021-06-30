import os
import psycopg2

class appService(object): 

    def get_responses():
        conn = psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require')
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
