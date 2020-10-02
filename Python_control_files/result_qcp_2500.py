import os
import shutil

cwd = os.getcwd()

dst_dir = '/lustre/scratch/yangyu/PWL/Result_Summary/'

VAR_NUM = [2000, 2500, 3000, 3500, 4000, 4500, 5000]

for var_size in VAR_NUM:
    os.chdir(cwd)
    var_str = 'var_2hr_' + str(var_size)
    os.chdir(var_str)

    src = cwd + '/'+var_str + '/table.txt'
    dst_file = dst_dir+'Q_Big_'+str(var_size)+'.txt'
    try:
        shutil.copy(src,dst_file)
    except:
        continue

