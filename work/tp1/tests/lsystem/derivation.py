import pytest
from src.lsystem import derivation



def test_der1():
    assert derivation("FF-[-F+F+F]+[+F-F-F]",  {'F':'FF-[-F+F+F]+[+F-F-F]'}) == "FF-[-F+F+F]+[+F-F-F]FF-[-F+F+F]+[+F-F-F]-[-FF-[-F+F+F]+[+F-F-F]+FF-[-F+F+F]+[+F-F-F]+FF-[-F+F+F]+[+F-F-F]]+[+FF-[-F+F+F]+[+F-F-F]-FF-[-F+F+F]+[+F-F-F]-FF-[-F+F+F]+[+F-F-F]]"
    
def test_der2():
    assert derivation("F[+X][-X]FX", {'X':'F[+X][-X]FX','F':'FF'}) == "FF[+F[+X][-X]FX][-F[+X][-X]FX]FFF[+X][-X]FX"
    
    
 
