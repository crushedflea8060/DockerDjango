source ../myenv/bin/activate

gunicorn -b 0.0.0.0:80 blog_project.wsgi


