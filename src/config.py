import os
from dotenv import load_dotenv

d_name = os.path.d_name(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(d_name, "..", ".env"))
except File