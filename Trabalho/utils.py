#!/usr/bin/env python
# -*- coding: utf-8 -*-
class CalculadoraMedidas:
    def calculaIMC(self,peso,altura):
        return peso/altura**2
    
    def statusIMC(self,imc):
        if(imc < 18.5):
            return 'Abaixo do peso'
        elif(imc >= 18.5 and imc <= 25):
            return 'Normal'
        elif(imc > 25 and imc <= 30):
            return 'Acima do peso'
        elif(imc > 30 and imc <= 35):
            return 'Obesidade'
        else:
            return 'Obesidade severa'

class cores:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'