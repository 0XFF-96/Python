sudo apt-get -y install apache2 mysql-server php5 php5-mysql php-pear php5-gd
sudo mv dvwasql/ /var/www/html/
sudo service mysql start
sudo service apache2 start
