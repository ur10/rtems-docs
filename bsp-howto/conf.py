import sys, os
sys.path.append(os.path.abspath('../common/'))

from conf import *

version = '4.11.99'
release = '4.11.99'

project = "RTEMS BSP and Device Driver Development Guide"

latex_documents = [
	('index', 'bsp-howto.tex', u'RTEMS BSP and Device Driver Development Guide', u'RTEMS Documentation Project', 'manual'),
]
