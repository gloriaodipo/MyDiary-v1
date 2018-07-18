# MyDiary-v1
[![Build Status](https://travis-ci.org/gloriaodipo/MyDiary-v1.svg?branch=develop)](https://travis-ci.org/gloriaodipo/MyDiary-v1) [![Coverage Status](https://coveralls.io/repos/github/gloriaodipo/MyDiary-v1/badge.svg?branch=develop)](https://coveralls.io/github/gloriaodipo/MyDiary-v1?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/f14b8d1aa3122f3b165c/maintainability)](https://codeclimate.com/github/gloriaodipo/MyDiary-v1/maintainability)

MyDiary is an online journal where users can pen down their thoughts and feelings.

## Features
- Users can create an account.
- Signed up users can log into their account.
- Users can get all diary entries.
- Users can get a specific diary entry.
- Users can add an entry
- Users can modify an entry.

## Prerequisites
- [Python3](https://www.python.org/) (A programming language)
- [Flask](http://flask.pocoo.org/) (A Python microframework)
- [Virtualenv](https://virtualenv.pypa.io/en/stable/) (Stores all dependencies used in the project)
- [Pivotal Tracker](www.pivotaltracker.com) (A project management tool)
- [Pytest](https://docs.pytest.org/en/latest/) (Tool for testing)

## Getting Started:

To start this app, please follow the instructions below:

On your terminal:

Install pip:

sudo apt-get install python-pip

Clone this repository:

git clone https://github.com/gloriaodipo/MyDiary-v1.git

Get into the root directory:

cd MyDiary-v1/

Install virtualenv:

pip install virtualenv

Create a virtual environment in the root directory:

virtualenv -name of virtualenv-
  
 Note: If you do not have python3 installed globally, please run this command when creating a virtual environment:
 
 virtualenv -p python3 -name of virtualenv-

Activate the virtualenv:

source name of virtualenv/bin/activate

Install the requirements of the project:

pip install -r requirements.txt

Create a file in the root directory called .env and add the two lines below

  export FLASK_APP="run.py"

  export SECRET="some random string"

Activate the env variables:

source .env

Run the application:

python run.py

To run tests:
pytest
