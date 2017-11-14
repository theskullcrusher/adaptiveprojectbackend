
sudo rm /etc/ndis/sites-enabled/default
sudo cp $PYTHONPATH/app_service/conf/app_service_nginx.conf /etc/nginx/sites-enabled/
pkill gunicorn
cd $PYTHONPATH/app_service/conf
echo $PWD
gunicorn -c gunicorn.py service_app:app
sudo service nginx restart


