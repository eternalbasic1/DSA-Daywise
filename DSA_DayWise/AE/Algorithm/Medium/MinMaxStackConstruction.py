#O(1) time and O(n) space {space i think it is correct please Crosscheck}
class MinMaxStack:
    def __init__(self):
        self.MinMax = []
        self.stack = []
    def peek(self):
        return self.stack[len(self.stack)-1]
    def pop(self):
        self.MinMax.pop()
        return self.stack.pop()
    def push(self,value):
        if len(self.MinMax) == 0:
            self.stack.append(value)
            self.MinMax.append([value,value])
        else:
            self.stack.append(value)
            a = self.MinMax[len(self.MinMax)-1][0] if value > self.MinMax[len(self.MinMax)-1][0] else value
            b = self.MinMax[len(self.MinMax)-1][1] if value < self.MinMax[len(self.MinMax)-1][1] else value
            self.MinMax.append([a,b])
    def FullMinMaxDisplay(self):
        return self.MinMax
    def getMin(self):
        return self.MinMax[len(self.MinMax)-1][0]
    def getMax(self):
        return self.MinMax[len(self.MinMax)-1][1]

if __name__ == "__main__":
    MinMax = MinMaxStack()
    arr = [5,7,2]
    for i in arr:
        MinMax.push(i)
    print(MinMax.FullMinMaxDisplay())
    print(MinMax.getMin())
    print(MinMax.getMax())