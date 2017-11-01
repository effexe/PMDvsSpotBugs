import time
import os

def test():
    times = []
    for i in range(5):
        start_time = time.time()
        os.system("$HOME/spotbugs-4.0.0-SNAPSHOT/bin/spotbugs -textui -jvmArgs '-Duser.language=en' jline-3.5.2-SNAPSHOT-javadoc.jar jline-3.5.2-SNAPSHOT-sources.jar jline-3.5.2-SNAPSHOT.jar jline-builtins-3.5.2-SNAPSHOT-javadoc.jar jline-builtins-3.5.2-SNAPSHOT-sources.jar jline-builtins-3.5.2-SNAPSHOT.jar jline-demo-3.5.2-SNAPSHOT-javadoc.jar jline-demo-3.5.2-SNAPSHOT-sources.jar jline-demo-3.5.2-SNAPSHOT.jar jline-reader-3.5.2-SNAPSHOT-javadoc.jar jline-reader-3.5.2-SNAPSHOT-sources.jar jline-reader-3.5.2-SNAPSHOT.jar jline-remote-ssh-3.5.2-SNAPSHOT-javadoc.jar jline-remote-ssh-3.5.2-SNAPSHOT-sources.jar jline-remote-ssh-3.5.2-SNAPSHOT.jar jline-remote-telnet-3.5.2-SNAPSHOT-javadoc.jar jline-remote-telnet-3.5.2-SNAPSHOT-sources.jar jline-remote-telnet-3.5.2-SNAPSHOT.jar jline-style-3.5.2-SNAPSHOT-javadoc.jar jline-style-3.5.2-SNAPSHOT-sources.jar jline-style-3.5.2-SNAPSHOT.jar jline-terminal-3.5.2-SNAPSHOT-javadoc.jar jline-terminal-3.5.2-SNAPSHOT-sources.jar jline-terminal-3.5.2-SNAPSHOT.jar jline-terminal-jansi-3.5.2-SNAPSHOT-javadoc.jar jline-terminal-jansi-3.5.2-SNAPSHOT-sources.jar jline-terminal-jansi-3.5.2-SNAPSHOT.jar jline-terminal-jna-3.5.2-SNAPSHOT-javadoc.jar jline-terminal-jna-3.5.2-SNAPSHOT-sources.jar jline-terminal-jna-3.5.2-SNAPSHOT.jar")
        times.append(time.time()-start_time)

    average = 0
    for index in range(len(times)):
        average = average + times[index]

    print(average / 5)

if __name__ == '__main__':
    test()
