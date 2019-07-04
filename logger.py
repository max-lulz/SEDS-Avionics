import json
import time

import psutil
import requests

URL = "https://fathomless-thicket-66026.herokuapp.com/argo"
init_time = time.time()

while time.time() - init_time <= 60:
    data_pt = []
    req_time = time.time()
    while time.time() - req_time <= 10:
        cpu_usage = "CPU Usage: " + str(psutil.cpu_percent())
        ram_usage = sorted(psutil.process_iter(attrs=['name', 'memory_percent']), reverse=True,
                           key=lambda data_mem: data_mem.info['memory_percent'])

        data_to_send = [data.as_dict(attrs=['name', 'memory_percent']) for data in ram_usage[:9]]
        data_to_send.insert(0, cpu_usage)
        data_pt.append(data_to_send)

    data_pt.insert(0, "Team name : Argo")

    fin_data = json.dumps(data_pt)
    # print(fin_data)
    # pprint.pprint(data_pt)
    r = requests.post(url=URL, data=fin_data)
    print(r.status_code, r.reason)
