# Recipe Management System

## Development Overview

**Recipe Management System** a web based recipe manager totally built using AI (opencode and agents) accept for this file (the developer's notes). It makes use of flask (the python web framework) Jinja2 tempalte engine and sqlite3 for persistence.

Please follow [Recipe Management System README](/README.md) for installation and technical documentation.

## Development Notes

- the main project is a [flask](https://flask.palletsprojects.com/) web based [python](https://www.python.org/) application all in the directory `recipe_manager`
- uses `poetry` for dependency management ([poetry](https://python-poetry.org/))
- uses an [sqlite3](https://docs.python.org/3/library/sqlite3.html) database
- built using [opencode](https://opencode.ai/) via prompts
- developed and tested on [debian linux](https://www.debian.org/)
- **IMPORTANT** this repo is built on top of [OpenAgentsControl repo](https://github.com/darrenhinde/OpenAgentsControl) !!!
    - **why** ? configured and optimized opencode agents _out-of-the-box_
    - removed the initial `.git` directory from origianl repo for simplification !!
- ⚠⚠ **CHECK** `documentation/*.gif` for screencasts (screen recordings) ⚠⚠ 😲
    - uses `git lfs` to track `gif` screencasts

### Would have been better

- a cleaner directory structure which adheres to python and flask apps conventions
- use an ORM such as peewee, pony or sqlalchemy instead of raw sql
- adding cleaner and incremental git commits
- use a frontend framework such as react/svelte... instead of server-side rendering
- enhance website layout/colors using better CSS/sass and well defined color schemes
    - probably night mode !!
- add test scripts (for all flask endpoints)
    - add test builds to `.github/workflows` (using tags)

## TODOs

- [ ] add docker/podman compose
- [ ] add valid github actions via workflows (if possible) or CI/CD deployment files

## Project Overview

recipe-ms **Documentation** at [Recipe Management System README](/README.md)
