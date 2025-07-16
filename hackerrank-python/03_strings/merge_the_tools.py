def merge_the_tools(string, k):
    #spliting rhe string in equal parts
    #string_length = len(string)
    split = [string[i:i+k] for i in range(0,len(string),k)]
    #print(len(split))
    #split_length = len(split)
    
    for part in split:
        result =""
        for char in part:
            if char not in result:
                result += char
                #print(result)
        print(result)
        
    
    

