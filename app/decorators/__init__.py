import logging
import time
from config import PATH_TO_LOGGER
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s' ,level=logging.INFO, filename=PATH_TO_LOGGER,filemode="a")
#время плюс три 
# параметр "a" , записывает в уже созданный файл и не перезаписывает его , "w" - перезаписывает файл