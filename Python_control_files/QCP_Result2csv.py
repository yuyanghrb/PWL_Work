import os
from glob import glob

cwd = os.getcwd()

os.chdir('Results_Summary')

BRN_Files = glob('BRN_*')
QCP_Files = glob('QCP_*')

Result_list = [['Type', 'Step', 'Time limit', 'Var Size', 'Instance', 'Time', 'Obj', 'Status', 'Opt_Count']]

counter = 1

for qcp_file in QCP_Files:

    print(counter)
    counter += 1

    rtype = 'QCP'
    filenames =  qcp_file.split('_')

    rstep = int(filenames[2])
    Time_limit = int(filenames[4])
    Var_size = int(filenames[6].split('.')[0])

    try:
        line_index = 1
        with open(qcp_file) as file:
            for line in file:
                items = line.split(' ')
                items = list(filter(None, items))
                rtime = float(items[1])
                robj = float(items[0])
                rstatus = int(items[3])
                
                ropt = 1
                if rtime >= 0.97*Time_limit:
                    ropt = 0

                Result_list.append([rtype, rstep, Time_limit, Var_size,
                                    line_index, rtime, robj, rstatus, ropt ])
                line_index = line_index +1
    except:
        continue

import csv

def list2csv(listname, csvname):    
    with open(csvname,  "w") as f:
        writer = csv.writer(f)
        writer.writerows(listname)
    return 1

os.chdir(cwd)
list2csv(Result_list, 'QCP_Result.csv')
