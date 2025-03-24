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
        
        bits64 = len(bits448)
        
        # Faz o padding de 1 e 0 até o 448
        bits448 += "1"
        
        while len(bits448) < 448:
            bits448 += "0"
        
        # Transforma o tamanho em bits
        bits64 = format(bits64, '08b')
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
            W.append(self.bits512[i:(i+32)])
        
        i = 0
        while len(W) < 64:
            print(i)
            w0 = W[i]
            w1 = W[i+1]
            w9 = W[i+9]
            w14 = W[i+14]
            
            rot1 = self.rotacionar(w1, [7, 18, 3])
            rot2 = self.rotacionar(w14, [17, 19, 3])
            
            new_w1 = ""
            new_w14 = ""
            for j in range(0, 32):
                if (rot1[0][j] == "1") or (rot1[1][j] == "1") or (rot1[2][j] == "1"):
                    new_b1 = "1"
                else:
                    new_b1 = "0"
                
                if (rot2[0][j] == "1") or (rot2[1][j] == "1") or (rot2[2][j] == "1"):
                    new_b2 = "1"
                else:
                    new_b2 = "0"
                
                new_w1 += new_b1
                new_w14 += new_b2
            
            new_w = ""
            for j in range(0, 32):
                if (w0[j] == "1") or (new_w1[j] == "1") or (w9[j] == "1") or (new_w14[j] == "1"):
                    new_b = "1"
                else:
                    new_b = "0"
                
                new_w += new_b
            W.append(new_w)
            i += 1
        print(W)
        
        
                
    
    def rotacionar(self, bits, rotates = []):
        rots = []
        for r in rotates:
            rots.append(bits[len(bits) - r:] + bits[:-r])
        
        return rots
        
            
    
            
            
            
        
            
