import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    def popola_dd_biblioteca(self):
        lista_biblioteche = self._model.get_biblioteche()
        self._view.dd_biblioteca.options.clear()
        for bib in lista_biblioteca:
            self._view.dd_biblioteca.options.append(ft.dropdown.Option(bib))

    def popola_dd_genere(self):
        lista_generi = self._model.get_generi()
        self._view.dd_genere.options.clear()
        for gen in lista_generi:
            self._view.dd_genere.options.appen(ft.dropdown.Option(gen))

    # TODO

    # CALLBACKS DROPDOWN
    #e.control.value rappresenta il valore scelto nella dropdown(dropdown = e.control)
    def biblio_selezionata(self,e):
        self.biblioteca_selezionata = e.control.value

    def gen_selezionato(self,e):
        self.genere_selezionato = e.control.value
    # TODO


    # AZIONE: MOSTRA LIBRI
    def mostra_libri(self,e):
        lista = self._model.get_libri_filtrati(self.biblioteca_selezionata, self.genere_selezionato)

        self._view.lista_libri.controls.clear()

        if not lista:
            self._view.show_alert("Nessun libro trovato.")
            self._view.update()
            return
        for libro in lista:
            self._view.lista_libri.controls.append(ft.Text(libro.__str__()))
        self._view.update()
    # TODO
