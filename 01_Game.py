test_cases = int(input())
 
def deletion(binary, pair) :
    pos = binary.index(pair)
    binary = list(binary)
    binary[pos], binary[pos + 1] = '', ''
    return ''.join(binary)
 
def distinct_pairs(binary) :    
    distinct_pairs = 0
    while ('01' in binary) or ('10' in binary) :
        if '01' in binary :
            binary = deletion(binary, '01')
        else :
            binary = deletion(binary, '10')
        distinct_pairs += 1
    return distinct_pairs
 
 
for i in range(test_cases) :
    binary = input()
    
    no_of_distinct_pairs = distinct_pairs(binary)
 
    if no_of_distinct_pairs % 2 != 0 :
        print("DA")
    else :
       print("NET")
 
