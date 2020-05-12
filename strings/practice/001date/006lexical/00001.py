def lexNext(s, n): 
  
    # Iterate from last character 
    for i in range(n - 1, -1, -1): 
  
        # If not 'z', increase by one 
        if s[i] != 'z': 
            k = ord(s[i]) 
            s[i] = chr(k + 1) 
            return ''.join(s) 
  
        # if 'z', change it to 'a' 
        s[i] = 'a'
  
# Driver Code 
if __name__ == "__main__": 
    S = input()
    T = input()
    n = len(S) 
    q = S
    S = list(S)
    res = lexNext(S, n) 
  
    # If not equal, print the 
    # resultant string 
    if res != T and q!=T:
        print(res) 
    else: 
        print(-1)