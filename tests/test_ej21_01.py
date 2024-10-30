import pytest 
from src.ej21_01 import comprobar_num, comprobar_edad

@pytest.mark.parametrize(
    "edad, salida",
    [
        (21,"Eres mayor de edad, puedes conducir."),
        (32,"Eres mayor de edad, puedes conducir."), 
        (11, "Eres menor de edad, no puedes conducir.")
    ]
)

def test_comprobar_edad(edad, salida):
    assert comprobar_edad(edad) == salida
    

@pytest.mark.parametrize(
    "num, retorno",
    [
        (["Hola","xd", "21"], 21),
        (["32"], 32), 
        (["11"], 11)
    ]
)

def test_comprobar_num(monkeypatch, num, retorno):
    entradas = iter(num)  # Crea un iterador de entradas
    monkeypatch.setattr('builtins.input', lambda _: next(entradas)) # el next lo que hace es q cambia a la prox variable
    assert comprobar_num("") == retorno