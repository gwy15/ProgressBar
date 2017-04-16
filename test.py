from __init__ import *

if __name__ == '__main__':
    bar = ProgressBar(500, 50, printPercentage=True, printTime=True)
    import time
    for i in range(501):
        bar.update(i)
        time.sleep(0.01)

    del bar
    bar = ProgressBar(500, 40)
    @growBar(bar, 2)
    def fun(a):
        time.sleep(0.01)
    
    for i in range(250):
        fun(2)