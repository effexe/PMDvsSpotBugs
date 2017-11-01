import time
import os

def test():
    times = []
    for i in range(10):
        start_time = time.time()
        os.system("$HOME/spotbugs-4.0.0-SNAPSHOT/bin/spotbugs -textui -jvmArgs '-Duser.language=en' itext7-barcodes-7.0.5-SNAPSHOT.jar itext7-font-asian-7.0.5-SNAPSHOT.jar itext7-forms-7.0.5-SNAPSHOT.jar itext7-hyph-7.0.5-SNAPSHOT.jar itext7-io-7.0.5-SNAPSHOT.jar itext7-kernel-7.0.5-SNAPSHOT.jar itext7-layout-7.0.5-SNAPSHOT.jar itext7-pdfa-7.0.5-SNAPSHOT.jar itext7-pdftest-7.0.5-SNAPSHOT.jar itext7-sign-7.0.5-SNAPSHOT.jar")
        times.append(time.time()-start_time)

    average = 0
    for index in range(len(times)):
        average = average + times[index]

    print(average / 10)

if __name__ == '__main__':
    test()
