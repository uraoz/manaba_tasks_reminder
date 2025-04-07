import os
import time
import json
from datetime import datetime
import pyotp
from dotenv import load_dotenv
import logging
import re
load_dotenv()
TOTP_TOKEN = os.getenv('TOTP_TOKEN')
totp = pyotp.TOTP(TOTP_TOKEN)
totp_code = totp.now()
print(totp_code)