# Myform Evaluator-app

- Status of [Travis CI build](https://travis-ci.com/ChatchapongC/myform): [![Build Status](https://travis-ci.com/ChatchapongC/myform.svg?branch=master)](https://travis-ci.com/ChatchapongC/myform)


**Table of contents**
- [Description](#description)
- [Team members](#team-members)
- [Documents](#documents)
- [Installation](#installing)
- [How to Run](#run-application)


## Description
**Myform** is the application that provides a customizable web-based evaluation form with data summarization and status reporting.  Event organizers can create a custom form for their event containing a list of entrants (contestants, projects, presentors, performers, etc) and a set of criteria that they are to be rated on. Criteria may also include guidance (help) on ratings.  There may optionally be space for entering comments.
The event organizers control who can view and submit an evaluation, and the time interval during which submission is allowed.  The organizers can elect to allow self-registration for open events.
The application authenticates each person who submits a form and ensures only one evaluation per person, although a person may revise and resubmit a prior submission, and evaluations may be submitted incrementally.  The application provides a status display for organizers that shows who has submitted an evaluation and whether its complete or not, but does not allow the organizer to view content of the evaluation. 
After the submittal period has ended, the application displays a summary of evaluations or scores, and provides access to comments.  It may limit who can view comments.
At some events the entrants/contestants are also allowed to submit evaluations. Students at KU can submit a senior project evaluation or vote at Exceed Camp even if they have a project entered in the competition.  The organizer can specify whether this is allowed and whether or not someone may evaluate his own project.


## Team members
Team members | GitHub  
-------------|--------
Jirawadee Sampusri| [**JirawadeeSampusri**](https://github.com/JirawadeeSampusri) 
Ingkharat Jangchud | [**ingkharatj**](https://github.com/ingkharatj) 
Chatchapong Chumpada | [**ChatchapongC**](https://github.com/ChatchapongC) 


## Project Documents
- **Iteration plan**: [Documentation](https://docs.google.com/document/d/1rDJOdz9LLVHhmFF3iuqE_Jmk5SodGcB1CdXmqaE_lXU/edit?ts=5da45a9b#bookmark=id.ubis0p7h5of7)
- **Task board**: [Trello](https://trello.com/b/3HD9FiRC)
- **Issue tracking**: [GitHub issue](https://github.com/ChatchapongC/myform/issues)
- **Code Review Script**: [Google Docs](https://docs.google.com/document/d/1LpJLmyLWiSoBRXpQJWmqK6wLSLc8UsPzZkV-UXFzBn0/edit?usp=sharing)
- **Code Review Checklist** [Google Docs](https://docs.google.com/document/d/1nFVZQUVCGOiv-FQsKDDub9sAaetvlcQYC9BdJfKn6cQ/edit?usp=sharing)

## Prerequisites
- **Python** (v.3.6 or newer) : [Download](https://www.python.org/downloads/)

- **Virtual Environment**
    ```shell script
    > pip install virtualenv
    ```

## Installing 
1. Clone the project from [Myform-evaluatorapp](https://github.com/ChatchapongC/myform) on **Terminal**.
    ```shell script
    # Clone with HTTPS
    > git clone https://github.com/ChatchapongC/myform.git
   
    # Clone with SSH
    > git clone git@github.com:ChatchapongC/myform.git
    ```
2. Change your current working directory into folder `myform` and create a new virtual environment.
    ```shell script
    > cd myform/
    > virtualenv env
    ```
3. Activate the virtual environment.
    ```shell script
    # For MacOS
    > source ./env/bin/activate

    # For Windows
    > .\env\Scripts\activate
    ```
4. Install dependencies from file `requirements.txt`.
    ```shell script
    (env) > pip install -r requirements.txt
   
    # to exit virualenv
    (env) > deactivate
    ```
5. Change a file name `.env.example` into `.env`.
     ```shell script
    # For windows
    (env) > rename .env.example .env
     
    # For MacOS
    (env) > mv .env.example .env
    ```


## Run Application
**Run the following commands to make migrations, apply migrate, add seed data and run server.**
1. Make migrations.
    ```shell script
    (env) > python manage.py makemigrations
    ```
2. Apply the migrations.
    ```shell script
    (env) > python manage.py migrate
    ```
3. Run server at [localhost:8000](http://localhost:8000)
    ```shell script
    (env) > python manage.py runserver
    ```
   
**If you want to login into admin site :**
```shell script
(env) > python manage.py createsuperuser
```
Then go to : [localhost:8000/admin](http://localhost:8000/admin) to visit Django admin site.
