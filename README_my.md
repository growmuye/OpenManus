https://repo.anaconda.com/archive/Anaconda3-2022.05-Linux-x86_64.sh
export PATH="/root/anaconda3/bin":$PATH
source /root/anaconda3/bin/activate
source ~/.bashrc

conda create --name my-manus python=3.12

conda activate my-manus

pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/