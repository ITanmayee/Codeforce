"""

Phoenix has collected n pieces of gold, and he wants to weigh them together so he can feel rich. The i-th piece of gold has weight wi. All weights are distinct. He will put his n pieces of gold on a weight scale, one piece at a time.

The scale has an unusual defect: if the total weight on it is exactly x, it will explode. Can he put all n gold pieces onto the scale in some order, without the scale exploding during the process? If so, help him find some possible order.
                                                            i
Formally, rearrange the array w so that for each i (1≤i≤n), ∑ wj≠x.
                                                            j=1

"""

def explodes(weights, avoid_weight):
    if len(weights) == 1 and weights[0] == avoid_weight:
        return "NO"
    total = 0
    
    for i in range(len(weights) - 1):
        if total + weights[i] == avoid_weight:
            weights[i], weights[i+1] = weights[i+1], weights[i]
        total += weights[i]
    
    if total + weights[-1] == avoid_weight:
        return "NO"
    print("YES")
    return ' '.join([str(i) for i in weights]) 
 
 
 
for _ in range(int(input())):
    gold_pieces, avoid_weight = map(int, input().split())
    weights = list(map(int, input().split()))
    print(explodes(weights, avoid_weight))
