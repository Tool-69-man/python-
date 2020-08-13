import os
import time
source =[ r"需备份文件txt", r"X:\简明python电子书\需备份文件" ]
target_dir = r"X:\简明python电子书\ "
target = target_dir + "备份后文件" + ".txt"
my_command = "cmd  '%s' %s" % (target, " ".join(source))
if os.system(my_command) == 0:
    print('Successful', target)
else:
    print('FAILED')