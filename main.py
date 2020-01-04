import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *


PROJECT_NAME = ''
HOMEPAGE = ''
NO_OF_THREADS = 8
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
queue = Queue()
DOMAIN_NAME = get_domian_name(HOMEPAGE)
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)


def create_workers():
    for _ in range(NO_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon
        t.start()

def work():
    while True:
        url = queue.get()
        Spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()

def create_job():
    for link in file_to_set(QUEUE_FILE):
        queue.put(link)
    queue.join()
    crawl()


def crawl():
    queued_links = file_to_set(QUEUE_FILE)
    if len(queued_links) > 0:
        create_job()


create_workers()
crawl()