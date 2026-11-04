from database.DB_connect import DBConnect
from model.libro_DTO import Libro

"""
    LIBRO DAO
    Gestisce le operazioni di accesso al database relative ai libri (Effettua le Query).
"""

class LibroDAO:
    def __init__(self):
        """
        costruttore della classe LibroDAO.
        Inizializza l'ogetto DAO responsabile dell'accesso ai dati dei libri.
        """
        pass
    def get_all_generi(self):
        """Recupera tutti i generi distinti (senza duplicati)dei libri presenti nel DB
        Returns:
            list[str]: lista di stringhe conetente i nomi dei generi"""
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result
        cursor = cnx.cursor(dictionary=True)
        #query sql per estrarre generi unici (distinct), escludendo i valori NULl
        query = "SELECT DISTINCT genere FROM libro WHERE genere IS NOT NULL ORDER BY genere"
        cursor.execute(query)

        for row in cursor:
            #estrae la stringa del genere del dizzionario e la aggiunge alla lista
            result.append(row['genere'])
        cursor.close()
        cnx.close()
        return result

    def get_libro_filtrati(self, id_biblioteca=None, genere=None):
        """Recupera i libri filtrati per biblioteca e/op per genere.
        Args:
            id_biblioteca (int/str, optional): ID della biblioteca da filtrare (None se nessun filtro )
            genere (str, optional): nome del genere da filtrare (None se nessun genere )

            returns:
            list[libro]:lista di oggetti DTO 'LIbro'"""
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            return result
        cursor = cnx.cursor(dictionary=True)

        #SOPEGAZIONE QUERY SQL CON COALESCE:
        #LA FUNZIONE COALESCE(%s, colonna) restituisce il primo valore NON NULL tra i due argomenti.
        #-CASO 1: L'utente seleziona un filtro (es. id_biblioteca = 2)
        #COALESCE(2, id_biblioteca) restuisce 2 --> la clausola diventa: WHERE id_biblioteca=2
        #-CASO 2: L'utente sceglie "Nessun filtro" (passiamo None / NULL a %s)
        #COALESCE (NULL, id_biblioteca) restituisce id_biblioteca --> la clausola diventa: WHERE id_biblioteca = id_biblioteca(condizione SEMPRE VERA!)
        query = """
          """



    # TODO
