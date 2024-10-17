# Python Discord Rich Presence Monitor
import os
import time

import psutil
import pypresence
from dotenv import load_dotenv

load_dotenv()
rpc_conn = pypresence.Presence(os.getenv('APPID'))
data = None
start = None

rpc_conn.connect()

while True:
    found = False
    for proc in psutil.process_iter(['name']):
        if 'sublime' in proc.info['name'].lower():
            found = True
            if start is None:
                start = time.time()
            data = {"start": start}

    if not found:
        data = None
        start = None

    if data:
        rpc_conn.update(**data)
    else:
        rpc_conn.clear()

    time.sleep(15)
