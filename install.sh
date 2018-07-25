tar -xvzf socialvibe.tar.gz
cd django-wedding-website
source Paytm/bin/activate
cd paytm-django/payments/
sudo apt install python-pip
pip install -r requirements.txt
pip install django-widget-tweaks
cd ../../
python manage.py migrate
python manage.py runserver
