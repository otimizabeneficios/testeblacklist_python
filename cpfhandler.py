import re

from django.core.validators import EMPTY_VALUES


class CpfHandler:

    @staticmethod
    def validarCpf(cpf):
        if cpf in EMPTY_VALUES:
            return u''
        if not str(cpf).isdigit():
            cpf = re.sub("[-\.]", "", cpf)

        valido = True

        try:
            int(cpf)
        except ValueError:
            valido = False
        if(len(str(cpf))!= 11):
            valido = False

        return valido

    def converterCpf(cpf):
        return '{}.{}.{}-{}'.format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:]) + '\n'

    @staticmethod
    def checarBlacklist(cpf):
        blacklist_file = open("blacklist.txt", "r")

        bloq = False

        for linha in blacklist_file:
            if(cpf == linha):
                bloq = True

        blacklist_file.close()
        return bloq