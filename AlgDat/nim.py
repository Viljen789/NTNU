def take_pieces(n):
    return (n-1)%8 if (n-1)%8>0 else 1
    
print(take_pieces(9))