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
3. Models of Body
4. Project Structure
5. API Routes
6. Database Relationship
   1. TODO
7. FAQ

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

## Models of Body

> class BetPatchBody

```json
{
   "id": 0,
   "bet_status": "string",
   "finish_datetime": "2023-05-24 22:53:28.293153",
   "operator_fee": "1.00",
   "total_amount": "1.00",
   "profit": "1.00"
}
```

> class DateFromToBody

```json
{
   "login_id": 0,
   "date_from": "2023-05-24",
   "date_to": null
}
```

> class DateFilterBody

```json
{
   "login_id": 0,
   "date_from": null,
   "date_to": null
}
```

## Project Structure

Here you can see the project tree for `source` and `tests` folders.
I used the structure of a `html` code. Each tag
means a package.

```html
<src>
   <api>
      <app>
         __init__.py
         app.py
      </app>
      <application>
         __init__.py
         application.py
      </application>
      <controller>
         __init__.py
         controller.py
      </controller>
      <data>
         __init__.py
         data_model.py
      </data>
      <models>
         __init__.py
         api_models.py
         request_body.py
      </models>
      <repository>
         __init__.py
      </repository>
      <routes>
         __init__.py
         routes.py
      </routes>
      __init__.py
   </api>
   <utils>
      __init__.py
      bet_status.py
      checker.py
      connection.py
      exceptions.py
   </utils>
   __init__.py
</src>
```

```html
<test>
   <api>
      <controller>
         __init__.py
      </controller>
      <repository>
         __init__.py
      </repository>
      __init__.py
   </api>
   <mock>
      __init__.py
   </mock>
   __init__.py
</test>
```

## API Routes

Here I present our routes for this API. It will be in `JSON` format.

```json
{
    "post_login": "/login",
    "post_login_auth": "/login/auth",
    "post_single_bet": "/bet/single",
    "post_multi_bet": "/bet/multi",
    "patch_single_bet": "/bet/single",
    "patch_multi_bet": "/bet/multi",
    "get_filter_single": "/bet/single",
    "get_filter_multi": "/bet/multi",
    "get_profits_single": "/bet/single/profits",
    "get_profits_multi": "/bet/multi/profits",
    "get_lost_single": "/bet/single/lost",
    "get_lost_multi": "/bet/multi/lost",
    "get_all_profits": "/bet/profits/all",
    "get_all_lost": "/bet/lost/all",
    "post_compound_interest": "/compound-interest"
}
```

So we can see the name and the link to each endpoint at this API.

## Database Relationship

### # [TODO](#)

## FAQ

### # [TODO](#)
