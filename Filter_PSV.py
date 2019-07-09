from datetime import datetime
import numpy as np
import os
import re
from pathlib import Path


path_to_file = Path('/Users/mistral/Downloads/2018_06/')
move_to = Path('/Users/mistral/Downloads/unused_psv/') #directory by this name must exist in path
files = os.listdir(path_to_file)

starttime = datetime.strptime('08:00','%H:%M').time()
endtime = datetime.strptime('17:00','%H:%M').time()

#parse time from files
hms = [re.findall(r'\-([0-9]{2}\.[0-9]{2}\.[0-9]{2})\-', file)[0] for file in files]
times = [datetime.strptime(x, '%H.%M.%S').time() for x in hms]
psv_times = np.column_stack((times, files))

ignore_psv = [row for row in psv_times if (row[0]>starttime and row[0]<endtime)]

for row in ignore_psv:
    os.rename(os.path.join(path_to_file, row[1]), os.path.join(move_to, row[1]))
