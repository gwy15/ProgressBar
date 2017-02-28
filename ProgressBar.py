import math
class ProgressBar:
    global charset
    charset = "▏▎▍▌▋▊▉█"

    def __init__(self, maxLength, maxCount, printCount=True, printPercentage=False):
        self.maxLength = maxLength
        self.maxCount = maxCount
        self.currentCount = 0
        self.printCount = printCount
        self.printPercentage = printPercentage

    def update(self, currentCount, maxCount=None):
        self.currentCount = currentCount
        if maxCount:
            self.maxCount = maxCount
        self._print()
    
    def _print(self):
        percentage = float(self.currentCount)/float(self.maxCount)
        percentage = max(0., percentage)
        percentage = min(1., percentage)
        length = float(self.maxLength)*percentage
        intPart = math.floor(length)
        restPart = length-intPart

        string =  charset[-1]*intPart # print main part
        if restPart > 0.01:
            string += charset[math.floor(restPart*len(charset))] # print rest part
        string += '  ' * (self.maxLength - len(string)) # fill with blank
        string += charset[0] # print boarder

        if self.printPercentage:
            string += "%2.1f%% "%(percentage*100.,)
        if self.printCount:
            countStr = str(self.currentCount)+'/'+str(self.maxCount)
            if self.printPercentage:
                countStr = ' (%s)'%countStr
            string += countStr
        string = '\r ' + string + '\r'
        print(string, end='')

if __name__ == '__main__':
    bar = ProgressBar(50, 500, printPercentage=True)
    import time
    for i in range(501):
        bar.update(i)
        time.sleep(0.05)
    print()