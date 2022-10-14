cd ..
rm -rf IP-TRACKER
apt update  && apt upgrade -y
clear
apt install python3
git clone https://github.com/EthicalHackingLK/IP-TRACKER.git
cd IP-TRACKER
python3 main.py
