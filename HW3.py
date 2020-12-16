class CuckooHashing: 
    def __init__(self, size): 
        self.M = size
        self.htable = [[None, None] for x in range(size+1)]  # h-table
        self.dtable = [[None, None] for x in range(size+1)]  # d-table

    def h(self, key):        # h-hash function, h(key)
        return key % self.M      
    
    def d(self, key):       # d-hash function, d(key)
        return (key*key % 17) *11 % self.M

    def find(self, i, key, data):
        if key == self.htable[i][0] and data == self.htable[i][1]:
            return 1
        else:
            return 0

    def __find(self, key):
        for i in range(self.M):
            if key == self.htable[i][0]:
                return 1
            else:
                return 0

    
    def put(self, key, data): # item (key,data) 삽입위한 method

        #[1]
        new_key = key
        new_data = data

        #[2]
        i = self.h(new_key)
        print("i= ",i)
        self.htable[i] = [new_key, new_data]
        print("h-table:[ ",i," ] ",self.htable[i])        
        
        while True:
            
            old_key = self.htable[i][0]
            old_data = self.htable[i][1]

            #[3]
            if self.htable[i][0] == None:
                self.htable[i] = [int(new_key), str(new_data)]
                return False

            else: #self.htable[i] != None            
                if self.find(i, old_key, old_data) == 1: #if old_key가 있었던 테이블이 htable이면
                    j = self.d(old_key)

                    print("[ ", self.htable[i][0]," , ", self.htable[i][1]," ] : h[ ", i," ] ", end='')
                    self.dtable[j] = self.htable[i]
                      
                    print([new_key, new_data], " : h[ ", i," ]")

                    old_key = self.dtable[j][0]
                    old_data = self.dtable[j][1]


                    break

                else: #if old_key가 있었던 테이블이 dtable이면
                    
                    new_i = self.h(old_key)
                    j = self.d(old_key)
                    
                    print("[ ", self.dtable[i][0]," , ", self.dtable[i][1]," ] : d[ ", j," ] ", end='')
                    self.htable[new_i] = self.dtable[j]
                   
                    print(self.dtable[j], " : d[ ", j," ]")

                    old_key = self.htable[new_i][0]
                    old_data = self.htable[new_i][1]

                    break

#                new_key =
#                new_data = 


#            print("d-table:[ ", ," ] ",self.dtable[])



    def get(self, key): # key 값에 해당하는 value 값을 return

        if self.__find(key) == 1:
            i = self.h(key)
            return self.htable[i][1]
        else:
            j = self.d(key)
            return self.dtable[j][1]


    def delete(self, key): # key를 가지는 item 삭제

        if self.__find(key) == 1:
            i = self.h(key)
            del self.htable[i]
        else:
            j = self.d(key)
            del self.dtable[j]
            
    def print_table(self):
        print('********* Print Tables ************')
        print('h-table:')
        for i in range(0, self.M):
            print(i,"  ",end ='')
        print()            
        for j in range(0, self.M):
            print(self.htable[i][0]," ",end ='')
        print()

        print('d-table:')
        for x in range(0, self.M):
            print(x,"  ",end ='')
        print()        
        for y in range(0, self.M):
            print(self.dtable[y][0]," ",end ='')
        print()


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
    
