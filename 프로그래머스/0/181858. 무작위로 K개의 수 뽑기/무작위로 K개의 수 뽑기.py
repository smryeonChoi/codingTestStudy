def solution(arr,k) :
    X = []
    for i in arr :
        if i not in X :
            X.append(i)
    if len(X) > k :
        X = X[:k]
    else : 
        for i in range(k-len(X)) :
            X.append(-1)
    return X