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
4. Database Relationship
   1. TODO
5. FAQ

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

## API Routes

### # [TODO](#)

## Database Relationship

### # [TODO](#)

## FAQ

### # [TODO](#)
