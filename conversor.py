# pip install sympy
import sympy as sy
import math as mt


class SHA256():
    
    bits512 = ""
    Hs = []
    
    def __init__(self, texto) -> None:
        # Transforma em ASCII
        ascii = bytearray(texto, encoding="utf-8")
        
        # Transforma o ASCII em bits
        bits448 = ""
        for a in ascii:
            bits448 += format(a, '08b')
        
        
        # Faz o padding de 1 e 0 até o 448
        bits448 += "1"
        
        while len(bits448) < 448:
            bits448 += "0"
        
        # Transforma o tamanho em bits
        bits64 = format(len(texto), '08b')
        print(len(texto))
        while len(bits64) < 64:
            bits64 = "0" + bits64
                
        self.bits512 = f"{bits448}{bits64}"
        self._inicializar_registrador()
    
    
    def _inicializar_registrador(self):
        num_primos = [2, 3, 5, 7, 11, 13, 17, 19]
        
        for n in num_primos:
            self.Hs.append("0x"+mt.sqrt(n).hex().split('.')[1][:8])
    
    
    def criptografar(self):
        W = []
        
        for i in range(0, 512, 32):
            W.append([self.bits512[i:(i+32)]])
        
        for w in W:
            print(w)
    
            
            
            
        
            
