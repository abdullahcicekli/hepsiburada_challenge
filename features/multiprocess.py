from multiprocessing import Process
import os
def run(command):
    os.system(command)

if __name__ == '__main__':
    commands = ["behave senaryo1.feature","behave senaryo2.feature"]
    process=[]
    for i in commands:
        proc = Process(target=run,args=(i,))
        process.append(proc)
        proc.start()
    for p in process:
        p.join()
