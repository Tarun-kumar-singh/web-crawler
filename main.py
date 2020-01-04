import threading
from queue import Queue
from spider import Spider
from domain import *
from general import *


PROJECT_NAME = ''
HOMEPAGE = ''
DOMAIN_NAME = get_domian_name(HOMEPAGE)
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)
