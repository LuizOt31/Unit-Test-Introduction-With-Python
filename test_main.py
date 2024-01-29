import calculadora
import primo
from manipulador_string import ManipuladorStrings

def test_soma():
    a, b = 2,2
    esperado = 4
    assert calculadora.somar(a, b) == esperado

def test_soma_erro():
    a, b = 2, 2
    esperado = 5
    assert calculadora.somar(a, b) == esperado

def test_sub():
    a, b = 1, 1
    esperado = 0
    assert calculadora.subtrair(a, b) == esperado

def test_sub_erro():
    a, b = 2, 1
    esperado = 8
    assert calculadora.subtrair(a, b) == esperado



def test_primo():
    a = 5
    esperado = True
    assert primo.Eh_primo(a) == esperado

def test_primo_erro():
    a = 10
    esperado = True
    assert primo.Eh_primo(a) == esperado



def test_inverter():
    manipulador = ManipuladorStrings()
    assert manipulador.inverter("python") == "nohtyp"
    
def test_inverter_erro():
    manipulador = ManipuladorStrings()
    assert manipulador.inverter("python") == "piton"


# assert calculadora.somar(1, 1) == 2
# assert calculadora.subtrair(1, 1) == 0
# assert calculadora.multiplicar(1,1) == 1
# assert calculadora.dividir(2,2) == 1