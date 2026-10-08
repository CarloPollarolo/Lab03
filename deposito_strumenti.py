import csv
from operator import attrgetter

class Strumento:
    def __init__(self, id_strumento, tipo, marca, anno_acquisto, valore):
        self.__id_strumento = id_strumento
        self.__tipo = tipo
        self.__marca = marca
        self.__anno_acquisto = int(anno_acquisto)
        self.__valore = float(valore)
    @property
    def marca(self):
        return self.__marca
    @property
    def id_strumento(self):
        return self.__id_strumento

    def __str__(self):
        return f"{self.__id_strumento} - {self.__tipo} {self.__marca} ({self.__anno_acquisto}) - €{self.__valore:.2f}"

class Prestiti:
    def __init__(self,id_prestito,data,id_strumento,cognome_allievo):
        self.__id_prestito=id_prestito
        self.__data=data
        self.__id_strumento=id_strumento
        self.__cognome_allievo=cognome_allievo
    @property
    def id_strumento(self):
        return self.__id_strumento
    def __str__(self):
        return f"{self.__id_prestito}, {self.__data}, {self.__id_strumento}, {self.__cognome_allievo}"



class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome=nome
        self.__responsabile=responsabile
        self.strumenti={}
        self.prestiti={}
    @property
    def responsabile(self):
        return self.__responsabile
    @responsabile.setter
    def responsabile(self, responsabile):
        self.__responsabile=responsabile

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        # TODO
        try:
            with open(file_path,'r',newline='',encoding='utf-8') as f:
                r=csv.reader(f)

                for riga in r:
                    id_strumento=riga[0]
                    tipo=riga[1]
                    marca=riga[2]
                    anno=riga[3]
                    valore=riga[4]

                    s=Strumento(id_strumento,tipo,marca,anno,valore)
                    self.strumenti[id_strumento]=s

        except FileNotFoundError:
            print(f'file {file_path} non trovato')






    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        # TODO

        id_strumento="S"+str(len(self.strumenti)+1)
        s_nuovo=Strumento(id_strumento,tipo,marca,anno_acquisto,valore)
        self.strumenti[id_strumento]=s_nuovo

        return s_nuovo



    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        # TODO
        ordinati=sorted(self.strumenti.values(),key=attrgetter("marca"))
        return ordinati

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        if id_strumento not in self.strumenti:
            raise Exception('Strumento non trovato')

        for prestito_attivo in self.prestiti.values():
            if prestito_attivo.id_strumento==id_strumento:
                raise Exception('strumento già in prestito')

        id_prestito="P"+str(len(self.prestiti)+1)
        nuovo_p=Prestiti(id_prestito,data,id_strumento,cognome_allievo)
        self.prestiti[id_prestito]=nuovo_p

        return id_prestito

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        if id_prestito in self.prestiti:
            self.prestiti.pop(id_prestito)
        else:
            raise Exception('prestito non trovato')
