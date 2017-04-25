
def histgram(s):
    d = dict()
    for c in s :
        if c not in d :
            d[c] = 1
        else :
            d[c] += 1
    return (d)

print(histgram([2, 2, 4, 6, 7, 5, 4, 2]))    

def total(intitial, *numbers, **params):
    count = intitial
    print(count)
    for num in numbers:
        count += num
    for key in params:
        count += params[key]
    return count    
print(total(10, 1, 2, 3, vegetables = 50, fruits = 100))

def diff(L):
    return max(L) - min(L)

lst = [2,555,-45,784,-44]
print(diff(lst))
