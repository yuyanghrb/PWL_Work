import os
from subprocess import call
import fileinput
from tempfile import NamedTemporaryFile

cwd = os.getcwd()
source_dir = os.path.join(cwd, 'qcp_code')


Step_BPs = [10,20,30,40]
Timelimit = [60, 120, 300, 600, 900, 1800]
VAR_NUM = [400, 500, 600, 700, 800, 900, 1000, 
          1200, 1400, 1600, 1800, 2000]


for step in Step_BPs:
    os.chdir(cwd)
    step_folder = 'Step_BP'+str(step)
    call(['mkdir', step_folder])

    for time in Timelimit:
        os.chdir(os.path.join(cwd, step_folder))
        time_folder = 'Time_'+str(time)
        call(['mkdir', time_folder])
        
        for var_size in VAR_NUM:
            os.chdir(os.path.join(cwd, step_folder, time_folder))
            var_str = 'var_' + str(var_size)
            call(['cp', '-a', source_dir, var_str])
            os.chdir(var_str)
                    
            file_name = 'Funcs_Vars_MIQCP.h'            
            with open(file_name, 'r') as file:
                filedata = file.read()
                new_step = 'MAX_STEPS=' + str(step)
                new_time = 'CPX_Tlimit=' + str(time)
                new_var = 'NUM_VAR = ' + str(var_size)
                filedata = filedata.replace('MAX_STEPS=30', new_step)
                filedata = filedata.replace('CPX_Tlimit=7200', new_time)
                filedata = filedata.replace('NUM_VAR=2500', new_var)     
            with open(file_name, 'w') as file:
                file.write(filedata)
                                
            file_name = 'job_source.sh'
            with open(file_name, 'r') as file:
                filedata = file.read()
                new_job_name = 'Q_s'+str(step/10)+'_t'+str(time/60)+'_v' + str(var_size/100)
                filedata = filedata.replace('QCP_baron4', new_job_name)
            with open(file_name, 'w') as file:
                file.write(filedata)
	
            call(['qsub','job_source.sh'])
