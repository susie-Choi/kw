class CuckooHashing:
    def __init__(self, size):
        self.M = size
        self.h = [[None, None] for x in range(size)]  # h-table
        self.d = [[None, None] for x in range(size)]  # d-table

    def hash(self, key):        # h-hash function, h(key)
        return key % self.M      
    
    def hash2(self, key):       # d-hash function, d(key)
        return (key*key % 17) *11 % self.M  
    
    def put(self, key, data): # item (key,data) 삽입위한 method 
        #### 구현하시오.
        i = self.hash(key)
        print("i= ", i)
        if self.h[i][0] == key:
            self.h[i] = [key, data]
        elif self.d[self.hash2(key)][0] == key:
            self.d[self.hash2(key)] = [key, data]
        else:
            tmp = self.h[i]
            self.h[i] = [key, data]
            while True:
                if tmp[0] is None:
                    print("h-table : [", i, "] ", self.h[i])
                    break
                else:
                    j = self.hash2(tmp[0])
                    tmp2 = self.d[j]
                    self.d[j] = tmp
                    print(tmp, " : h[", i, "]", self.h[i], " : h[", i, "]")
                    if tmp2[0] is None:
                        print("d-table : [", self.hash2(tmp[0]), "] ", tmp)
                        break
                    else:
                        i = self.hash(tmp2[0])
                        tmp = self.h[i]
                        self.h[i] = tmp2
                        print(tmp2, " : d[", j, "]", self.d[j], " : d[", j, "]")
                                 
    def get(self, key): # key 값에 해당하는 value 값을 return 
        #### 구현하시오.
        if self.h[self.hash(key)][0] == key:
            return self.h[self.hash(key)][1]
        elif self.d[self.hash2(key)][0] == key:
            return self.d[self.hash2(key)][1]
        else:
            return None

    def delete(self, key): # key를 가지는 item 삭제 
        #### 구현하시오.
        if self.h[self.hash(key)][0] == key:
            self.h[self.hash(key)] = [None, None]
        elif self.d[self.hash2(key)][0] == key:
            self.d[self.hash2(key)] = [None, None]
        else:
            return None

    def print_table(self):
        print('********* Print Tables ************')
        print('h-table:')
            #### h-table 출력 : 구현하시오
        for i in range(self.M):
            print(i, end="\t")
        print()
        for i in self.h:
            print(i[0], end="\t")
        print('\nd-table:')
            #### d-table 출력 : 구현하시오
        for i in range(self.M):
            print(i, end="\t")
        print()
        for i in self.d:
            print(i[0], end="\t")

if __name__ == '__main__':
    t = CuckooHashing(13)
    t.put(25, 'grape')      # 25:  12,   0
    t.put(43, 'apple')      # 43:   4,   0
    t.put(13, 'banana')     # 13:   0,   7
    t.put(26, 'cherry')     # 26:   0,   0
    t.put(39, 'mango')      # 39:   0,  10
    t.put(71, 'lime')       # 71:   6,   8
    t.put(50, 'orange')     # 50:  11,  11
    t.put(64, 'watermelon') # 64:  12,   7
    print()
    print('--- Get data using keys:')
    print('key 50 data = ', t.get(50))
    print('key 64 data = ', t.get(64))
    print()
    t.print_table() 
    print()
    print('-----  after deleting key 50 : ---------------')
    t.delete(50)
    t.print_table()
    print()
    print('key 64 data = ', t.get(64))
    print('-----  after adding key 91 with data berry:---------------')
    t.put(91, 'berry')
    t.print_table()
    print()
    print('-----  after changing data with key 91 from berry to kiwi:---------------')
    t.put(91, 'kiwi')       # 91:  0,   9
    print('key 91 data = ', t.get(91))
    t.print_table()
    
