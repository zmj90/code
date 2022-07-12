"""

"""
class MyRangeIterator:
    def __init__(self,end):
        self.number = -1
        self.end = end

    def __next__(self):
        if  self.number == self.end-1:
            raise StopIteration()
        self.number += 1
        return self.number

class MyRange:
    def __init__(self,stop):
        self.stop = stop

    def __iter__(self):
        return MyRangeIterator(self.stop)

# for number in MyRange(5):
#     print(number)# 0 1 2 3 4
obj = MyRange(5)
iterator = obj.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item) # 0 1 2 3 4
    except StopIteration:
        break