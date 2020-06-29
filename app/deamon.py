from os import waitpid
from time import sleep
from cron import Cronjobs

cronjob = Cronjobs()


def child_done():
    waitpid(-1, 0)
    print('child exited')


while True:
    sleep(300)
    print('start cron')
    cronjob.start(child_done)
