def lexical(s, n): 
  
    for i in range(n - 1, -1, -1): 
        if s[i] != 'z': 
            k = ord(s[i]) 
            s[i] = chr(k + 1) 
            return ''.join(s) 
        s[i] = 'a'
  

S = input()
T = input()
n = len(S) 
q = S
S = list(S)
word = lexical(S, n) 

if word != T and q!=T:
    print(word) 
else: 
    print(-1)