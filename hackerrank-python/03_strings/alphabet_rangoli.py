def print_rangoli(size):
    
    width = 4 * size - 3    
    alphabets = [chr(97+j) for j in range(size)]

    for i in range(size-1):#Top
        left = alphabets[size-1:size-i-1:-1]        
        right = alphabets[size-i-1:size]
    
        top ='-'.join(left+right)
        print((top).center(width,'-'))
    
    for i in range(size):#middle and bottom    
        left = alphabets[size-1:i:-1]
        right = alphabets[i:size]
         
    
        bottom ='-'.join(left+right)
        print((bottom).center(width,'-'))
    
   

