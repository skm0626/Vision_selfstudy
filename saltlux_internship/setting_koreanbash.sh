apt-get install locales
apt-get install language-pack-ko
apt-get install language-pack-ko-base
echo "export LANGUAGE=ko_KR.UTF-8" >> ~/.bashrc
echo "export LANG=ko_KR.UTF-8" >> ~/.bashrc
source ~/.bashrc
locale-gen ko_KR ko_KR.UTF-8
update-locale LANG=ko_KR.UTF-8
dpkg-reconfigure locales
#echo "LANG=ko_KR.UTF-8" >>  /etc/environment
#echo "LANG=ko_KR.EUC-KR" >> /etc/environment
#echo "LANGUAGE=ko_KR:ko:en_GB:en" >> /etc/environment
#echo "LANGUAGE=ko_KR:ko:en_GB:en" >> /etc/default/locale
#echo "LANG=ko_KR.EUC-KR" >> /etc/default/locale
#echo "LANG=ko_KR.UTF-8" >>  /etc/default/locale
#echo "LANG=ko_KR.UTF-8" >>  /etc/profile

