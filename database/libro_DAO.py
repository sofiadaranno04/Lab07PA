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
    def get_generi(self)-> list[str]:

        """Recupera tutti i generi distinti (senza duplicati)dei libri presenti nel DB
        Returns:
            list[str]: lista di stringhe contenente i nomi dei generi"""
        cnx = DBConnect.get_connection()

        if cnx is None:
            raise ConnectionError("Impossibile connetersi al database.")
        cursor = cnx.cursor()

        try:
            query = """
                    SELECT DISTINCT genere
                    FROM libro
                    WHERE genere IS NOT NULL
                    ORDER BY genere ASC
                """
        #query sql per estrarre generi unici (distinct), escludendo i valori NULl

            cursor.execute(query)
            lista_generi =[]

            for row in cursor:
            #estrae la stringa del genere del dizzionario e la aggiunge alla lista
                lista_generi.append(row[0])
            return lista_generi

        finally:
            cursor.close()
            cnx.close()

def get_libro_filtrati(self, biblioteca=str|None, genere=str | None)->list[Libro]:
        """Recupera i libri filtrati per biblioteca e/op per genere.
        Args:
            id_biblioteca (int/str, optional): ID della biblioteca da filtrare (None se nessun filtro )
            genere (str, optional): nome del genere da filtrare (None se nessun genere )

            returns:
            list[libro]:lista di oggetti DTO 'LIbro'"""
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            raise ConnectionError("Impossibile connetersi al database.")
        cursor = cnx.cursor(dictionary=True)

        try:
            query = """
                SELECT 1.*
                FROM libro 1, biblioteca b
                WHERE b.id=1.id_biblioteca
                    AND b.nome = COALESCE(%s, b.nome) AND 1.genere = COALESCE(%s, 1.genere)
            """
            cursor.execute(query,(biblioteca,genere))
            lista_libri_filtrata = []

            for row in cursor:
                lista_libri_filtrata.append(Libro(**row))

            return lista_libri_filtrata
        finally:
            cursor.close()
            cnx.close()

        #SOPEGAZIONE QUERY SQL CON COALESCE:
        #LA FUNZIONE COALESCE(%s, colonna) restituisce il primo valore NON NULL tra i due argomenti.
        #-CASO 1: L'utente seleziona un filtro (es. id_biblioteca = 2)
        #COALESCE(2, id_biblioteca) restuisce 2 --> la clausola diventa: WHERE id_biblioteca=2
        #-CASO 2: L'utente sceglie "Nessun filtro" (passiamo None / NULL a %s)
        #COALESCE (NULL, id_biblioteca) restituisce id_biblioteca --> la clausola diventa: WHERE id_biblioteca = id_biblioteca(condizione SEMPRE VERA!)
        query = """
          """



    # TODO
