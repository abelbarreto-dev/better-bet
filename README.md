# Better Bet

API to control bets, lost and winnings. So with that and a database,
you'll can control your bets better. Then you'll can filter and
compare previous bet profits for you. The only thing you need is
to create an account.

## Summary

1. Dependencies
   1. Python and Pip
   2. FastAPI
   3. Peewee
   4. Uvicorn
2. Models
   1. Login
   2. Single Bet
   3. Multi Bet
3. API Routes
   1. TODO
4. Project Structure
   1. TODO
5. Database Relationship
   1. TODO
6. FAQ

## Dependencies

Here you'll see the list of dependencies from this project.

1. Python and Pip [here](https://www.python.org/) and [here](https://pypi.org/project/pip/) language and package install resource
2. FastAPI [here](https://fastapi.tiangolo.com/lo/) used to build API Rest
3. Peewee [here](https://docs.peewee-orm.com/en/latest/index.html) used as a ORM
4. Uvicorn [here](https://www.uvicorn.org/) used as a server to access this API

> Note: you can install uvicorn searching for install it by
> pip from FastAPI website.

## Models

Bellow you can see our methods.

> class Login

```json
{
   "player_name": "string",
   "username": "string",
   "password": "string"
}
```

> class SingleBet

```json
{
   "id_login": 0,
   "home_team": "string", 
   "away_team": "string", 
   "team_bet": "string", 
   "odd": "1.00"
   "value_invest": "1.00"
   "profit": "1.00",
   "bet_status": "success"
}
```

> class MultiBet

```json
{
   "id_login": 0,
   "home_team": "string", 
   "away_team": "string", 
   "team_bet": "string", 
   "list_odds": [
      "1.00"
   ],
   "value_invest": "1.00"
   "profit": "1.00",
   "bet_status": "success"
}
```

## Project Structure

Here you can see the project tree for `source` and `tests` folders.
I used the structure of a `html` code. Each tag
means a package.

```html
<src>
   <api>
      <data>
         data.py
         __init__.py
      </data>
      <models>
         __init__.py
      </models>
      <repository>
         __init__.py
      </repository>
      <resource>
         __init__.py
      </resource>
      <routes>
         __init__.py
      </routes>
      __init__.py
   </api>
   <utils>
      __init__.py
   </utils>
   __init__.py
</src>
```

```html
<test>
   <api>
      <data>
         __init__.py
      </data>
      <models>
         __init__.py
      </models>
      <repository>
         __init__.py
      </repository>
      <resource>
         __init__.py
      </resource>
      <routes>
         __init__.py
      </routes>
      __init__.py
   </api>
   <mock>
      __init__.py
   </mock>
   __init__.py
</test>
```

## API Routes

### # [TODO](#)

## Database Relationship

### # [TODO](#)

## FAQ

### # [TODO](#)
