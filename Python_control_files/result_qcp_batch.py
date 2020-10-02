import os
import shutil
from glob import glob

cwd = os.getcwd()
dst_dir = '/lustre/scratch/yangyu/PWL/Result_Summary/'

Step_BPs = [10,20,30,40]
Timelimit = [60, 120, 300, 600, 900, 1800]
VAR_NUM = [400, 500, 600, 700, 800, 900, 1000, 
          1200, 1400, 1600, 1800, 2000]


for step in Step_BPs:
    os.chdir(cwd)
    step_folder = 'Step_BP'+str(step)

    for time in Timelimit:
        os.chdir(os.path.join(cwd, step_folder))
        time_folder = 'Time_'+str(time)
        
        for var_size in VAR_NUM:
            os.chdir(os.path.join(cwd, step_folder, time_folder))
            var_str = 'var_' + str(var_size)
            os.chdir(var_str)

            try:
                src = glob('Summary_*')[0]
#                print(src)
                target = 'QCP_Step_'+str(step)+'_Time_'+str(time)+'_Var_'+str(var_size)+'.txt'
#                print(target)
                dst = dst_dir+target
                shutil.copy(src,dst)
                print(target + ' Done!')
            except:
                continue
            