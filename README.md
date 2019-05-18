# python-app-server

sudo wget https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm
sudo yum -y localinstall mysql57-community-release-el7-11.noarch.rpm
sudo yum -y install mysql
sudo yum -y install python3
sudo yum -y install git
sudo yum install python3-pip
git clone https://github.com/sshariqrizvi15/python-app-server.git
sudo pip3 install -r python-app-server/requirements.txt
nohup python3 /home/ec2-user/python-app-server/app/app.py > output.txt 2>&1  </dev/null &
