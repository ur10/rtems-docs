import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '1.0'
release = '4.11.99'

project = "RTEMS CPU Supplement Documentation"

latex_documents = [
	('index', 'cpu-supplement.tex', u'RTEMS CPU Supplement Documentation', u'RTEMS Documentation Project', 'manual'),
]
