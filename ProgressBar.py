import math
import time
class ProgressBar:
    global charset
    charset = "▏▎▍▌▋▊▉█"

    def __init__(self, maxLength, maxCount, printCount=True, printPercentage=False, printTime=False):
        self.maxLength = maxLength
        self.maxCount = maxCount
        self.currentCount = 0
        self.printCount = printCount
        self.printPercentage = printPercentage
        self.printTime = printTime
        self.startTime = time.time()

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

        if self.printTime:
            secondsSpent = math.floor(time.time() - self.startTime)
            if secondsSpent < 3600:
                timeStr = time.strftime('%M:%S', time.gmtime(secondsSpent))
            elif secondsSpent < 3600*24:
                timeStr = time.strftime('%H:M:%S', time.gmtime(secondsSpent))
            else:
                days = secondsSpent // (3600*24)
                seconds = secondsSpent % (3600*24)
                timeStr = int(days) + time.strftime('days %H:M:%S', time.gmtime(seconds))
            string = timeStr + ' ' + string
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
    bar = ProgressBar(50, 500, printPercentage=True, printTime=True)
    import time
    for i in range(501):
        bar.update(i)
        time.sleep(0.01)
    print()
