def mergesort(ls):
    if len(ls) == 1:
        return ls

    mid = int(len(ls) / 2)
    return merge(mergesort(ls[:mid]), mergesort(ls[mid:]))

def merge(ls1, ls2):
    out = []
    while len(ls1) or len(ls2):
        if not len(ls1):
            out += ls2
            return out
        elif not len(ls2):
            out += ls1
            return out
        
        if ls1[0] < ls2[0]:
            out.append(ls1[0])
            ls1.pop(0)
        elif ls1[0] >= ls2[0]:
            out.append(ls2[0])
            ls2.pop(0)


print(mergesort([1,56,6,2,3,100,23,2,43,37,5]))