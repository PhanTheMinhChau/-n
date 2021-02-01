from subprocess import run
from threading import Thread


def gocr():
    
    def func1():
        run('python crawl.py', shell=False)
        
    def func2():
        run('python run.py', shell=False)
        
    
    Thread(target = func1).start()
    Thread(target = func2).start()