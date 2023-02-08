# Blog API

  

## Description

  

This application allows you to create posts and interact with them, leave comments for authorized users and like specific posts.

  

## Built with

* Python

* DRF

* Docker

* PostgreSQL

  

## Getting Started

  

In order to use this app: clone this repository to your machine, in terminal go to project directory and run this commands:

### Start database and bot containers with:

```

docker compose up -d --build

```

### If you want to run project locally you can use commands listed below:

### Apply migration to the database:

```

python manage.py makemigrations
python manage.py migrate


```

### Run blog application with:

```

python manage.py runserver

```

### Now application is ready.

## Usage tips

An authorized user can create posts and can edit or delete them, in addition to him, admins also have the right to access these posts. Other authorized users can leave their own comments to any post, and the function of nested comments has also been developed. For each post, you can see information on how many users liked it and their username.
Users can register, but they need to specify: 
* Username
* Email
* Password(twice to confirm)
The password must contain at least 8 characters and one letter. Authorized users can change their own password.
Also created object level permissions using Django Guardian for admin site.
