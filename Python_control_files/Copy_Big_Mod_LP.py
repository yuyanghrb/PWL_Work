import os
import shutil
from glob import glob

cwd = '/lustre/scratch/yangyu/PWL/Generate_Big_LP_Mod'

LP_dst_dir = '/lustre/scratch/yangyu/SCQP/Instances/LP_files/'
Mod_dst_dir = '/lustre/scratch/yangyu/SCQP/Instances/Mod_files/'

VAR_NUM = [2000, 2500, 3000, 3500, 4000, 4500, 5000]

for var_size in VAR_NUM:
    os.chdir(cwd)
    var_str = 'var_2hr_' + str(var_size)
    os.chdir(var_str)

    # LP files:
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
            dst = LP_dst_dir+target
            shutil.copy(src,dst)
            print(target + ' Done!')

    except:
        print(str(var_size) + 'LP is wrong')
        continue
            
for var_size in VAR_NUM:
    os.chdir(cwd)
    var_str = 'var_2hr_' + str(var_size)
    os.chdir(var_str)

    # LP files:
    try: 
        os.chdir('Mod_files')
        files = glob('QCP_*')
        for src in files:
            var_string = str(var_size)
            if len(var_string) == 3:
                var_string = '0'+var_string
            
            count_string = src.split('_')[-1]
            if len(count_string) == 5:
                count_string = '0'+count_string

            target = 'SCQP_'+var_string+'_'+ count_string
            dst = Mod_dst_dir+target
            shutil.copy(src,dst)
            print(target + ' Done!')

    except:
        print(str(var_size) + 'Mod is wrong')
        continue
