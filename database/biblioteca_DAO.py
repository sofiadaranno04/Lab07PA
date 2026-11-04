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

    def get_all_biblioteche(self):
        """recupera tutte le biblioteche presenti nel database e le restituisce come oggetti biblioteche DTO
        Returns:
            list[Biblioteca]: una lista di oggetti DTO 'Biblioteca' """
        #Passaggio 1 : Chiede una connesssione attiva al DB tramite la classe di connessione DBConnect
        cnx = DBConnect.get_connection()
        result = []
        #controllo di sicurezza : se la connessione al DB è fallita, ritorna la lista vuota
        if cnx is None:
            return result
        #Passaggio 2: Crea un cursore con dictionary= True
        #ciò permette di leggere ogni riga del DB come dizionario Python (es.{'id':1, 'nome':'Civica'}
        cursor = cnx.cursor(dictionary=True)

        #Passaggio 3: Scrive ed esegue la query SQL per estarre id e nome ordinati alfabeticamente
        query = "SELECT id, nome  FROM biblioteca ORDER BY nome"
        cursor.execute(query)

        #Passaggio 4: Cicla sui risultati restituiti del DB e per ciascuno crea un oggetto DTO ' Biblioteca'
        for row in cursor:
            #istanzia il DTO Biblioteca passando id e nome
            biblioteca_obj = Biblioteca(id=row['id'], nome=row['nome'])
            result.append(biblioteca_obj)
        #passaggio 5: Chiude semopre il cursore e la connessione per non sprecare risorse nel DB
        cursor.close()
        cnx.close()

        #passaggio 6: restituisce la lista di oggetti biblioteca al model
        return result

    # TODO
