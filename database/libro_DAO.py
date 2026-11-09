from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        pass

    def read_generi_from_db(self):
        cnx = DBConnect.get_connection() #creo la connessione con il database
        if cnx is not None: #mi assicuro che avvenga la connessione con il database
            print("Connection to database established")


            query = "SELECT genere FROM libro" #seleziono i generi
            cursor = cnx.cursor(dictionary=True) #creo un cursore e definisco il database con un dizionario
            cursor.execute(query)

            lista_generi = [] #creo la lista generi e controllo se il genere non è già presente, in tal caso lo aggiungo
            for row in cursor:
                if row["genere"] not in lista_generi:
                    lista_generi.append(row["genere"])

            lista_generi.append("No filtro") #aggiungo il no filtro che mi servirà quando andrò a vedere nella dropbox le diverse azioni, lo metto di default come parametro

            cursor.close()
            cnx.close()
            print("Generi letti correttamente")
            return lista_generi

    def read_libri_from_database(self, biblioteca, genere):
        cnx = DBConnect.get_connection() #creo la connessione con il database
        if cnx is not None:
            print("Connection to database established") #mi assicuro che avvenga la connessione con il database
            if biblioteca != "No filtro" and genere != "No filtro": #se entrambi hanno delle opzioni messe dall'utente != dal no filtro
                query = f"SELECT titolo FROM libro AS l, biblioteca AS b WHERE l.genere='{genere}' AND l.id_biblioteca = b.id AND b.nome ='{biblioteca}' " #utilizzo il join per unire le tabelle
            elif biblioteca == "No filtro" and genere != "No filtro": #bibliotrche senza filtri, genere invece richiesto specifico
                query = f"SELECT titolo FROM libro AS l, biblioteca AS b WHERE l.genere='{genere}'"
            elif biblioteca != "No filtro" and genere == "No filtro": #biblioteca scelta dall'utente, genere senza filtro dunque mi stampa TUTTI i libri di quella determinata biblioteca
                query = f"SELECT titolo FROM libro AS l, biblioteca AS b WHERE l.id_biblioteca = b.id AND b.nome ='{biblioteca}' "
            else:
                query = f"SELECT DISTINCT titolo FROM libro" #seleziono i titoli non ripetuti grazie a distinct

            cursor = cnx.cursor(dictionary=True) #creo un cursore e definisco il database con un dizionario
            cursor.execute(query)

            lista_libri = []

            for row in cursor:
                lista_libri.append(row["titolo"]) #aggiungo il titolo alla lista dei libri



            cursor.close()
            cnx.close()
            print("Libri trovati correttamente")

            return lista_libri

