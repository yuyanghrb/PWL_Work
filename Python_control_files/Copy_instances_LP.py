import os
import shutil
from glob import glob

# cwd = os.getcwd()
cwd = '/lustre/scratch/yangyu/PWL/QCP_Batch'

dst_dir = '/lustre/scratch/yangyu/SCQP/Instances/LP_files/'

Step_BPs = [10]
Timelimit = [60]
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
                os.chdir('LP_files')
                files = glob('QCP_*')
                for src in files:
                    var_string = str(var_size)
                    if len(var_string) == 3:
                        var_string = '0'+var_string
                    
                    count_string = src.split('_')[-1]
                    if len(count_string) == 4:
                        count_string = '0'+count_string

                    target = 'SCQP_'+var_string+'_'+ count_string
                    dst = dst_dir+target
                    shutil.copy(src,dst)
                    print(target + ' Done!')
            except:
                continue
            