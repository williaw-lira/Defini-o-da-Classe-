class ContaBancaria:
    def __init__(self, numero, titular, saldo = 0):
        """ Construtor Que cria os atributos Conta Bancaria
        :param numero:
        :param titular:
        :param saldo:
        """
        
        self.numero = numero
        self.titular = titular
        self.saldo = saldo