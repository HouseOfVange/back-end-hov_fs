# House of Vange dot com : Back-end Layer

This is the back end for the future houseofvange.com. It has models and routes for Piece, Comment, Guestbook Entry, and the Price Point.

## One-Time Setup
1. Install Homebrew `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
2. Install Postgres `brew install postgresql@14`
3. Run `createdb hov_db`
4. Create virtual environment `python3 -m venv venv`
5. Activate venv `source venv/bin/activate`
6. Install dependencies `pip install -r requirements.txt`
7. Create a `.env` file based on `env.axample` in the project root. Run `cp .env.example .env`

## Local Run
To run this backend locally (after one time set up) follow these steps:
1. Start Postgres (if not already running) 
`sudo brew services start postgresql@14`
    - If Postgres fails to start, remove the stale lock file and restart:
      `rm /usr/local/var/postgresql@14/postmaster.pid` then `brew services restart postgresql@14`
2. Activate venv
`source venv/bin/activate`
3. Run migrations
`flask db upgrade`
4. Start Flask
`flask run --port 1414`  
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>


# Old things copied from previous project...
This scaffold includes the following:

## `app/__init__.py`

This file configures the app. It's where:

We expect developers to modify this file by:

- Replacing the database connection string
- Importing all models
- Registering all blueprints

Note that `create_app` also uses CORS. There is no extra action needed to be done with CORS.

## `app/routes.py`

We expect endpoints to be defined here.

The file already imports:

- `Blueprint`
- `request`
- `jsonify`
- `make_response`
- `db`

Feel free to alter these import statements.

This file also has a comment to define a Blueprint. Feel free to delete it.

## `app/models` Directory

This project already includes `app/models/board.py` and `app/models/card.py`, to anticipate the models `Board` and `Card`.

Both files already import `db`, for convenience!

## `requirements.txt`

This file lists the dependencies we anticipate are needed for the project.

## `Procfile`

This file already has the contents needed for a Heroku deployment.

If the `create_app` function in `app/__init__.py` is renamed or moved, the contents of this file need to change. Otherwise, we don't anticipate this file to change.
