# heroes-replay

Heroes of might and magic 3 - is an old game > 20years old. This game has an interesting community (majori in East Europe). To this day this game is played by many, on custom maps. And There is a bunch of video replays of theirs games majority ir PVP games.

This project is a database of these games played by people.

### Todo:
- Backend
    - Database
    - Admin Panel (to add new matches)
    - ...
- Frontend


### run stuff:


```
export FLASK_DEBUG=1
export FLASK_ENV=dev
export FLASK_RUN_PORT=4432
export FLASK_RUN_HOST=0.0.0.0
export FLASK_APP=h3.app:create_app 

export FLASK_APP=h3backend.app:create_app 

flask run



----

flask db init

flask db migrate
flask db upgrade

```






https://heroes.thelazy.net/index.php/Hero_class



Something to look at: https://www.renpy.org/


 Todo:
1. Player page - UI
2. Opponent information (player + town + hero)
3. Hero + Town Images (???)
4. Fix filters by adding placeholder and move it to left drawer.
5. Mobile UI to fix
6. Add more videos