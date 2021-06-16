class Underscore:
    def map(self, iterable, callback):
        answer = []
        for i in range(len(iterable)):
            answer.append(iterable[i]**4)
        return answer
    def find(self, iterable, callback):
        for i in range(len(iterable)):
            if callback(iterable[i]) == True:
                return iterable[i]
        return False
            
    def reject(self, iterable, callback):
        answer = []
        for i in range(len(iterable)):
            if callback(iterable[i])== False:
                answer.append(iterable[i])
        return answer
    def filter(self, iterable, callback):
        answer = []
        for i in range(len(iterable)):
            if callback(iterable[i]) == True:
                answer.append(iterable[i])
        return answer
            

# you just created a library with 4 methods!
# let's create an instance of our class
_ = Underscore() # yes we are setting our instance to a variable that is an underscore
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(evens)
mapped = _.map([1,2,3,4,5], lambda x: x*4)
print(mapped)
find = _.find([1,2,3,3,1], lambda x: x>3)
print(find)
reject = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print(reject)
# should return [2, 4, 6] after you finish implementing the code above

