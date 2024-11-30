import numpy as np
import pandas as pd
from utilsTwitterCovid import *

import logging
logger = logging.getLogger('ftpuploader')

from urllib.request import Request, urlopen 


link ="https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv"

#job=False
#while not job:

req = Request(link)
req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0')
content = urlopen(req)
dataCovid = pd.read_csv(content)
caption,figureName = plotCovidFigure(dataCovid)

#for i in range(10):
#    try:
#        publishFigure(caption,figureName)
#    except Exception as e: # work on python 3.x
#        logger.error('Failed to upload to ftp: '+ str(e))