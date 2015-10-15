# clone the project

git clone https://callicoder@bitbucket.org/somit/bagpiper.git

# use virtualenv
virtualenv venv
source venv/bin/activate

# install python dependencies
pip install -r requirements.txt

# install client side dependencies
npm install && bower install

# migrate database
python manage.py migrate

# run the app
python manage.py runserver

# Add some coupons
