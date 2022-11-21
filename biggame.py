from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
import pymssql

@app.route('/backend', methods=['GET'])
def backend():
  global tabella_selezionata
  citta_negozio = request.args['citta_shop']
  via_negozio = request.args['via_shop']
  conn = pymssql.connect(server = '213.140.22.237\SQLEXPRESS',user = 'tolentino.mirko',password = 'xxx123##',database = 'tolentino.mirko')
  query = f"Select * from Shops inner join Location on Shops.id_shops = Location.id_shops inner join Games on Location.id_games = Games.id_games WHERE Shops.indirizzo_shop = '{via_negozio}' and Shops.citta_negozio = '{citta_negozio}'"
  tab_giochi_quantita = f"Select Shop."
  df = pd.read_sql(query,conn)
  
  return jsonify()


@app.route('/backend/addgames', methods=['GET'])
def addgames():
  nome_gioco = request.args['nome_game']
  studio_gioco = request.args['studio_game']
  prezzo_prezzo = request.args['prezzo_game']
  quantita_gioco = request.args['quantita_game']
  
  
  return




if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)