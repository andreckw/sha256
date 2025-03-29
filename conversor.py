# pip install sympy
import sympy as sy
import math as mt


class SHA256():
    
    bits512 = ""
    Hs = []
    K = []
    
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
            w0 = W[i]
            w1 = W[i+1]
            w9 = W[i+9]
            w14 = W[i+14]
            
            rot1 = self.rotacionar_deslocar(w1, [7, 18], [3])
            rot2 = self.rotacionar_deslocar(w14, [17, 19], [10])

            
            new_w1 = ""
            new_w14 = ""
            for j in range(0, 32):
                if (rot1[0][j] == "1") ^ (rot1[1][j] == "1") ^ (rot1[2][j] == "1"):
                    new_b1 = "1"
                else:
                    new_b1 = "0"
                
                if (rot2[0][j] == "1") ^ (rot2[1][j] == "1") ^ (rot2[2][j] == "1"):
                    new_b2 = "1"
                else:
                    new_b2 = "0"
                
                new_w1 += new_b1
                new_w14 += new_b2
            
            new_w = int(w0, 2) + int(new_w1, 2) + int(w9, 2) + int(new_w14, 2)
            new_w = format(new_w, "08b")
            
            if (len(new_w) > 32):
                new_w = int(new_w, 2) % (2**32)
                new_w = format(new_w, "08b")
                
            while (len(new_w) < 32):
                new_w = "0" + new_w
            
            W.append(new_w)
            i += 1
        self._inicializar_k()
        print(self.K)
        
        
        
                
    
    def rotacionar_deslocar(self, bits, rotates = [], descolocacoes = []):
        retorno = []
        
        for r in rotates:
            retorno.append(bits[len(bits) - r:] + bits[:-r])
        
        for d in descolocacoes:
            retorno.append("0"*d + bits[:-d])
        
        return retorno
        
    def _inicializar_k(self):
        primos_64 = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
            59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131,
            137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223,
            227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311
        ]
        
        for p in primos_64:
            fracionaria = (p ** (1/3)) % 1
            bits = format(int(fracionaria * (2**32)), "08b")
            while (len(bits) < 32):
                bits = "0" + bits
            self.K.append(bits)


if __name__ == "__main__":
    sha = SHA256("porta")
    sha.criptografar()


