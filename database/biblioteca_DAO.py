from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        pass

    # Funzione incaricata di creare la lista di nomi delle biblioteche dal database con SQL
    def read_biblioteche_from_db(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            print("Connection to database established")

            query ="SELECT nome FROM biblioteca"
            cursor = cnx.cursor(dictionary=True)
            cursor.execute(query)

            nomi_biblioteche= []
            for row in cursor:
                nomi_biblioteche.append(row["nome"]) #aggiungo il nome della biblioteca alla lista dei nomi delle biblioteche

            nomi_biblioteche.append("No filtro") #aggiungo opzione no filtro di default nella casella dell'interfaccia

            cursor.close()
            cnx.close()
            print("Biblioteche lette correttamente")
            return nomi_biblioteche

