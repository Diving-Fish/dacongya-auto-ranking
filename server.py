from quart import Quart
from collections import defaultdict
import os
import time

app = Quart(__name__)

@app.route('/data', methods=['GET'])
async def get_data():
    d = defaultdict(lambda: [])
    with open("ranking_data.txt", encoding='utf-8') as f:
        lines = f.read()
    for line in lines.split('\n'):
        arr = line.strip().split(' ')
        if len(arr) != 10:
            continue
        for i in range(2, 10, 2):
            d[arr[i]].append(arr[i+1])
    return d

@app.route('/time', methods=['GET'])
async def get_time():
    return {"ts": os.stat("ranking_data.txt").st_mtime}

app.run(host="0.0.0.0", port=8105)