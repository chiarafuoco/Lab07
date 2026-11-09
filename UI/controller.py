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
    def popola_dropdown_biblioteca(self): #aggiungo alla dropdown gli elementi presenti nella lista creata all'interno della funzione get_biblioteche richiamandola

        for biblioteca in self._model.get_biblioteche():
            self._view.filtro_biblioteca.options.append(ft.dropdown.Option(biblioteca))


    def popola_dropdown_generi(self): #aggiungo alla dropdown gli elementi presenti nella lista creata all'interno della funzione get_generi richiamandola
        for genere in self._model.get_generi():
            self._view.filtro_generi.options.append(ft.dropdown.Option(genere))

    # CALLBACKS DROPDOWN
    def pulisci_lista(self):
        self._view.lista_libri.controls = [] #ogni volta che cambio il filtraggio o rischiaccio il mostra libri mi viene pulita la listview

    # AZIONE: MOSTRA LIBRI
    def handler_btn(self): #bottone da richiamare nella view per mostrare a video i passaggi scelti della dropdown
        lista_libri = self._model.get_libri_filtrati(self._view.filtro_biblioteca.value, self._view.filtro_generi.value)
        for el in lista_libri:
            self._view.lista_libri.controls.append(ft.Text(value=el))
