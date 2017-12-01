import time
import os
import psutil

def test():
    p = psutil.Popen(["$HOME/pmd-bin-5.8.1/bin/run.sh pmd -d itext7.zip -f text -R java-basic,java-imports,java-unusedcode"], shell=True)
    print(p)
    _ = p.memory_info_ex()
    print(_)
    print(_.vms / (1024.0 ** 2))
    print(p.memory_percent())
    
    
    """times = []
    for i in range(10):
        start_time = time.time()
        os.system()
        times.append(time.time()-start_time)

    average = 0
    for index in range(len(times)):
        average = average + times[index]

    print(average / 10)"""

if __name__ == '__main__':
    test()
