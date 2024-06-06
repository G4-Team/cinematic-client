from prompt_toolkit.styles import Style


class PageMaker:
    def __init__(self):
        self.dialogStyles = Style.from_dict(
            {
                "dialog": "bg:#333333",
                "dialog frame.label": "bg:#c3c3c3 #575757",
                "dialog.body": "bg:#c3c3c3 #575757",
                "dialog shadow": "bg:#232323",
            }
        )

    @staticmethod
    def drawLine(lineLength):
        line = "█" * lineLength + "\n"
        return line

    @staticmethod
    def drawEndedLine(lineLength):
        line = "██" + " " * (lineLength - 4) + "██\n"
        return line

    @staticmethod
    def drawSpaces(spaceCount):
        line = " " * spaceCount
        return line

    def drawLineWithParameters(self, lineLength, *args):
        totalEmptySpaces = lineLength - 4
        for arg in args:
            totalEmptySpaces -= len(arg)
        eachSpace = totalEmptySpaces // (len(args) + 1)
        remainingSpaces = totalEmptySpaces - eachSpace * (len(args) + 1)
        line = "██"
        for arg in args:
            if remainingSpaces > 0:
                line += self.drawSpaces(eachSpace + 1)
                remainingSpaces -= 1
            else:
                line += self.drawSpaces(eachSpace)
            line += arg
        line += self.drawSpaces(eachSpace)
        line += "██\n"
        return line

    def drawLineWithParametersStartAt(self, lineLength, start, *args):
        remainingSpace = lineLength - 4 - start
        line = "██"
        line += self.drawSpaces(start)
        for arg in args:
            line += arg
            line += " "
            remainingSpace -= len(arg) + 1
        line += self.drawSpaces(remainingSpace)
        line += "██\n"
        return line
