from database.DB_connect import DBConnect
from model.biblioteca_DTO import Biblioteca

"""
    Biblioteca DAO
    Gestisce le operazioni di accesso al database relative alle biblioteche (Effettua le Query).
"""

class BibliotecaDAO:
    def __init__(self):
        """inizializza la classe DAO per le biblioteche."""
        pass

    def get_nomi_biblioteche(self):
        """recupera tutte le biblioteche presenti nel database e le restituisce come oggetti biblioteche DTO
        Returns:
            list[Biblioteca]: una lista di oggetti DTO 'Biblioteca' """
        #Passaggio 1 : Chiede una connesssione attiva al DB tramite la classe di connessione DBConnect
        cnx = DBConnect.get_connection()

        #controllo di sicurezza : se la connessione al DB è fallita, ritorna la lista vuota
        if cnx is None:
            raise ConnectionError("Impossibile connettersi al database.")

        cursor = cnx.cursor()

        try:
            query = """
                    SELECT DISTINT nome
                    FROM biblioteca
                    WHERE nome IS NOT NULL
                    ORDER BY nome ASC
                """
            cursor.execute(query)

            lista_biblioteche = []

        #Passaggio 4: Cicla sui risultati restituiti del DB e per ciascuno crea un oggetto DTO ' Biblioteca'
            for row in cursor:
            #istanzia il DTO Biblioteca passando id e nome
                lista_biblioteche.append(row[0])
            return lista_biblioteche

            #result.append(biblioteca_obj)
        #passaggio 5: Chiude semopre il cursore e la connessione per non sprecare risorse nel DB

        finally:
            cursor.close()
            cnx.close()

    # TODO
