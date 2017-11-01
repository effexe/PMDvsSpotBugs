import time
import os

def test():
    times = []
    for i in range(5):
        start_time = time.time()
        os.system("$HOME/spotbugs-4.0.0-SNAPSHOT/bin/spotbugs -textui -jvmArgs '-Duser.language=en' jEdit.jar MacOSX.jar QuickNotepad.jar")
        times.append(time.time()-start_time)

    average = 0
    for index in range(len(times)):
        average = average + times[index]

    print(average / 5)

if __name__ == '__main__':
    test()
