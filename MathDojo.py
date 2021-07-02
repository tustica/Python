class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result+=num
        return self
    def subtract(self, num):
        self.result-=num
        return self

md = MathDojo()
print(md.result)
print(md.add(2).add(3).add(45).subtract(10).subtract(2).subtract(15).result)
