import os
from dotenv import load_dotenv

load_dotenv()
 
class Config(): 
    ENVIROMENT_VARIABLE = os.getenv('RAILWAY_STATIC_URL')
