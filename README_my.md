https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
export PATH="/root/anaconda3/bin":$PATH
source /root/anaconda3/bin/activate
source ~/.bashrc

conda create --name my-manus python=3.12

conda activate my-manus

pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/


启动：python3 run_web.py

访问猎小易Manus：http://10.139.61.238:5172/

访问Supervisor：http://10.139.61.238:5173/
#启动
service supervisord start
#停止
service supervisord stop

$supervisorctl reread
 # 重启配置文件修改过的程序 
$supervisorctl update
 # 查看程序状态 
$supervisorctl status