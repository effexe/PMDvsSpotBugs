import time
import os

def test():
    times = []
    for i in range(10):
        start_time = time.time()
        os.system("$HOME/pmd-bin-5.8.1/bin/run.sh pmd -d jline3.zip -f text -R java-basic,java-imports,java-unusedcode")
        times.append(time.time()-start_time)

    average = 0
    for index in range(len(times)):
        average = average + times[index]

    print(average / 10)

if __name__ == '__main__':
    test()
