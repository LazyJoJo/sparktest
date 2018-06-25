# coding=utf-8
import time
from celery import Celery as cele
celery = cele('tasks',broker='redis://localhost:6379/0')

@celery.task
def sendmail(mail):
    print 'sending mail to %s...' %mail['to']
    time.sleep(2.0)
    print 'mail sent.'

