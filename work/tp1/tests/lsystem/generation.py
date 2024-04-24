import pytest
from src.lsystem import generation



def test_der1():
    assert generation("F",  {'F':'FF-[-F+F+F]+[+F-F-F]'}, 2) == "FF-[-F+F+F]+[+F-F-F]FF-[-F+F+F]+[+F-F-F]-[-FF-[-F+F+F]+[+F-F-F]+FF-[-F+F+F]+[+F-F-F]+FF-[-F+F+F]+[+F-F-F]]+[+FF-[-F+F+F]+[+F-F-F]-FF-[-F+F+F]+[+F-F-F]-FF-[-F+F+F]+[+F-F-F]]"
    
def test_der2():
    assert generation("X", {'X':'F[+X][-X]FX','F':'FF'}, 3) == "FFFF[+FF[+F[+X][-X]FX][-F[+X][-X]FX]FFF[+X][-X]FX][-FF[+F[+X][-X]FX][-F[+X][-X]FX]FFF[+X][-X]FX]FFFFFF[+F[+X][-X]FX][-F[+X][-X]FX]FFF[+X][-X]FX"
    
    
 
