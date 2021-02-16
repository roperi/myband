# myband

This repo is entirely based on https://github.com/bhrutledge/jahhills.com . My
version is very simple in comparison and lacks tons of functionalities. So go and check his if you want to see 
this project in its full glory. 


## Getting Started

Clone repo `git clone git:github.com:roperi/myband`

Change to the created folder `cd myband`

Install requirements with `pip install -r requirements.txt`

Enable development mode with `export DEBUG=True` from command line

Edit your settings `hth/settings.py` 

Start Django server with `python manage.py runserver` 

Open your browser and navigate to `http://127.0.0.1:8000/`

To edit content go to `http://127.0.0.1:8000/admin` but first create superuser 
with `python manage.py createsuperuser`

## Production infrastructure

- Domain registered on [Namecheap](https://www.namecheap.com/) (w/ DNS and email forwarding)
- Media hosted on [Cloudinary](https://cloudinary.com/)

## Todo 
- Settings file
- Environment variables management
- Deployment instructions
