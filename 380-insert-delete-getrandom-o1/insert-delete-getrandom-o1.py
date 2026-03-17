class RandomizedSet:

    def __init__(self):
        self.Map={}
        self.list=[]

    def insert(self, val: int) -> bool:
        res = val not in self.Map
        if res:
            self.Map[val]=len(self.list)
            self.list.append(val)

        return res

    def remove(self, val: int) -> bool:
        res= val in self.Map
        if res:
            ind=self.Map[val]
            lval=self.list[-1]
            self.list[ind]=lval
            self.list.pop()
            self.Map[lval]=ind
            del self.Map[val]
        return res
        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()