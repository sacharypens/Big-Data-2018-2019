import psutil

PROCNAME = 'firefox'

for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        proc.kill()
