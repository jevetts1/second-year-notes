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



def quicksort(ls):
    print(ls)
    if len(ls) <= 1:
        return ls
    p = ls[0]
    i = 1
    j = len(ls) - 1

    while True:
        while ls[i] > p and i < len(ls) - 1:
            i += 1
        
        while ls[j] < p and j > 1:
            j -= 1
        
        tmp = ls[i] 
        ls[i] = ls[j]
        ls[j] = tmp

        if i > j:
            break
    
    ls[0] = ls[j]
    ls[j] = p

    return quicksort(ls[:j-1]) + [p] + quicksort(ls[j:])


class Heap:
    arr = []

    def insert(self, node):
        self.arr.append(node)
        self.sift(len(self.arr) - 1, False)
    
    @classmethod
    def get_parent(cls, idx):
        return (idx - 1) // 2
    
    @classmethod
    def get_children(cls, idx):
        return 2 * idx + 1, 2 * idx + 2

    def sift(self, idx, down=True):
        if not down:
            while idx > 0:
                parent = Heap.get_parent(idx)
                if self.arr[parent] < self.arr[idx]:
                    tmp = self.arr[idx]
                    self.arr[idx] = self.arr[parent]
                    self.arr[parent] = tmp

                    idx = parent
                else:
                    break
        
        else:
            while 2 * idx + 2 <= len(self.arr) - 1:
                children = Heap.get_children(idx)
                if self.arr[children[0]] > self.arr[children[1]]:
                    larger = children[0]
                else:
                    larger = children[1]
                
                if self.arr[idx] < self.arr[larger]:
                    tmp = self.arr[idx]
                    self.arr[idx] = self.arr[larger]
                    self.arr[larger] = tmp
                    
                    idx = larger
                
                else:
                    break
    
    def get_max(self):
        root = self.arr[0]
        self.arr[0] = self.arr.pop()
        self.sift(0, True)
        return root

h = Heap()

h.insert(1)
h.insert(54)
h.insert(2)
h.insert(5)
h.insert(3)
h.insert(45)
h.insert(34)
h.insert(100)
print(h.arr)

while len(h.arr) > 1:
    h.get_max()
    print(h.arr)
