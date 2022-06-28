# -*- coding:UTF-8 -*-
class No:
    def __init__ (self,dado, prioridade):
        self.dado = dado
        self.prioridade = prioridade
        self.prox = None
class Filaprioridade:
    def __init__(self,capacidade = 10):
        self.inificoDaFila = None
        self.capacidade = capacidade
        self.qtdElementosFila = 0
        print(f"Criada EDD fila com capacidade {capacidade}")
    def is_empty(self):
        pass
    def is_full(self):
        pass
    def add(self,novo):
        pass
    def remove(self):
        pass
    def list_items(self):
        pass
