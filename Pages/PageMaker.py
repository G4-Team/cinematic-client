class PageMaker:
    @staticmethod
    def drawLine(lineLength):
        for i in range(lineLength):
            print("#", end="")

    @staticmethod
    def drawEndedLine(lineLength):
        print("#", end="")
        for i in range(lineLength - 2):
            print("#", end="")
        print("#", end="")

    @staticmethod
    def drawSpaces(spaceCount):
        for i in range(spaceCount):
            print(' ', end = '')

    def drawLineWithParameters(self, lineLength, *args):
        totalEmptySpaces = lineLength - 2
        for arg in args:
            totalEmptySpaces -= len(arg)
        eachSpace = totalEmptySpaces // (len(args) + 1)
        remainingSpaces = totalEmptySpaces - eachSpace * (len(args) + 1)
        print('#', end = '')
        for arg in args:
            if remainingSpaces > 0:
                self.drawSpaces(eachSpace + 1)
                remainingSpaces -= 1
            else:
                self.drawSpaces(eachSpace)
            print(arg, end = '')
        self.drawSpaces(eachSpace)
        print('#', end = '')
