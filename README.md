# 530_2026_09_emp
Employee performance review for 530 9/2026

## Install and run (on the compsci server)
1. `git clone https://github.com/krispepper/530_2026_09_emp.git`
2. `cd 530_2026_09_emp`
3. `python3 -m venv .venv`
4. `source .venv/bin/activate`
5. `pip install -r requirements.txt`
6. `cp .env.sample .env` then edit `.env` if needed (PORT, DB_USER, DB_NAME)
7. `python3 app.py`
8. Open `http://localhost:<PORT>/` (VS Code Remote-SSH forwards the port)

The shared UAT copy is in `/home/groupprojects/fall2026_530_emp/530_2026_09_emp`. There: `cd` into it, `git pull origin main`, then start at step 4.

## Run the unit tests
From the `530_2026_09_emp` folder with the venv active: `pytest -v`

## Project structure (MVC)
- `app.py` - starts the app and registers the blueprints (the only file to run)
- `models/` - database access and rules (`db.py`, `employee.py`, `review_period.py`); all SQL lives here
- `routes/` - Flask blueprints, one per feature (`login_routes.py`, `period_routes.py`)
- `templates/`, `static/` - HTML pages and CSS/JS
- `sql/` - scripts to create/change tables between sprints
- `tests/` - pytest unit tests

## Contributions

Everyone worked collarboratively on the project as we all took designated roles in order to complete application. If one person was unsure of how to do something, we switched between tasks in order to work efficiently and fairly. After Branson created the table, Maaz started working on the code and both Branson and Cynthia worked on the readme file . This allowed the group members to maintain structure and flow throughout the work environment. Throughout the process, we decided it was best that Maaz became group leader since his knowledge of code was much stronger than the rest of us and can guide us throughout the assignment. 