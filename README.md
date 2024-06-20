# Django

Projet GDS Orano

# Mise en marche :

env/Scripts/activate

pip install --no-cache-dir -r requirements.txt

python .\manage.py runserver 0.0.0.0:8000

# Faire des migrations :

- python manage.py makemigrations
- python manage.py migrate

# Apache restart :

sudo service apache2 restart

# Convertir SCSS en CSS :

sass --watch public/pages/scss:public/pages/css

# Faire un fichier de requirements :

pip freeze > requirements.txt
