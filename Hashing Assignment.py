class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):
        hashvalue = self.hashfunction(key,len(self.slots))

        if self.slots[hashvalue] == None:
            self,slots[hashvalue] = key
            self.slots[hashvalue] = data

        else:
            nextslot = self.rehash(hashvalue,len(self.slots))
            while self.slots[nextslot] != None and \
                             self.slots[nextslot] != key:
                nextslot = self.rehash(nextslot,len(self.slots))

            if self.slots[nextslot] == None:
                self.slots[nextslot]= key
                self.data[nextslot]=data

            else:
                self.data[nextslot] = data

    def hashfunction(self,key,size):
        return key%size

    def rehash(selfself,oldhash,size):
        return (oldhash+1)%size

    def binarySearch(alist, item):
        first = 0
        last = len(alist)-1
        found = False

        while first <=last and not found:
            midpoint = (first + last)//2
            if alist[midpoint] == item:
                found = True

            else:
                if item < alist[midpoint]:
                    last = midpoint-1
                else:
                    first = midpoint+1

        return found

S = HashTable()
S[54]="cat"
S[26]="dog"
S[93]="Lion"
S[17]="tiger"
S[31]="cow"
S[44]="goat"
S[55] ="pig"

print(binarySearch(S), "cow")



