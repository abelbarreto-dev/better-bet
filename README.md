# Better Bet

API to control bets, lost and winnings. So with that and a database,
you'll can control your bets better. Then you'll can filter and
compare previous bet profits for you. The only thing you need is
to create an account.

## Summary

1. [Dependencies](#dependencies)
   1. Python and Pip
   2. FastAPI
   3. Peewee
2. [How To Run](#how-to-run)
3. [How To Test](#how-to-test)
   1. Run Specific Tests
   2. Run All Tests
4. [Models](#models)
   1. [Login](#login)
   2. [Single Bet](#singlebet)
   3. [Multi Bet](#multibet)
5. [Models of Body](#models-of-body)
   1. [BetPatchBody](#betpatchbody)
   2. [DateFromToBody](#datefromtobody)
   3. [DateFilterBody](#datefilterbody)
6. [Project Structure](#project-structure)
   1. [Source Package](#source-package)
   2. [Test Package](#test-package)
7. [API Routes](#api-routes)
8. [Database Relationship](#database-relationship)
9. [FAQ](#faq)

## Dependencies

Here you'll see the list of dependencies from this project.

1. Python and Pip [here](https://www.python.org/) and [here](https://pypi.org/project/pip/) language and package install resource
2. FastAPI [here](https://fastapi.tiangolo.com/lo/) used to build API Rest
3. Peewee [here](https://docs.peewee-orm.com/en/latest/index.html) used as a ORM
4. Uvicorn [here](https://www.uvicorn.org/) used as a server to access this API

> Note: you can install uvicorn searching for install it by
> pip from FastAPI website.

## How To Run?

Before you run this project, you need to check if all [dependencies](#dependencies)
are installed and access [FAQ](#faq) to set the file `settings.json` and
`.env` configurations.

To run this project, after you have made what was described here, you need to run the following
command:

```commandline
uvicorn main:app --reload
```

## How To Test?

To run unit tests here you need to check what is described at [How to Run](#how-to-run) topic. After
you have two options:

1. Access the package [test](test/api) then you have two options:
   1. [controller](test/api/controller) the endpoints tests
   2. [repository](test/api/repository) the persistence tests
2. Run the following command in [root dir](/) for run all tests:
   1. ```commandline
      pytest
      ```

## Models

Bellow you can see our methods.

### Login

```json
{
   "player_name": "string",
   "username": "string",
   "password": "string"
}
```

### SingleBet

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

### MultiBet

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

Bodies to use as a custom JSON to make API operations.

### BetPatchBody

```json
{
   "id": 0,
   "bet_status": "string",
}
```

### DateFromToBody

```json
{
   "login_id": 0,
   "date_from": "2023-05-24",
   "date_to": null
}
```

### DateFilterBody

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

### Source Package

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
      create_tables.py
      exceptions.py
      types_utils.py
   </utils>
   __init__.py
</src>
```

### Test Package

```html
<test>
   <api>
      <controller>
         __init__.py
         test_login_controller.py
         test_single_bet_controller.py
         test_multi_bet_controller.py
      </controller>
      <repository>
         __init__.py
      </repository>
      __init__.py
   </api>
   __init__.py
   conftest.py
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
    "get_filter_single": "/get/bet/single",
    "get_filter_multi": "/get/bet/multi",
    "get_profits_single": "/bet/single/profits",
    "get_profits_multi": "/bet/multi/profits",
    "get_lost_single": "/bet/single/lost",
    "get_lost_multi": "/bet/multi/lost",
    "get_all_profits": "/bet/profits/{id_login}/all",
    "get_all_lost": "/bet/lost/{id_login}/all",
    "post_compound_interest": "/compound-interest"
}
```

So we can see the name and the link to each endpoint at this API.

## Database Relationship

The main class of this project is named `Login`. So we have others 2 (two) database
entities, `SingleBet` and `MultiBet`. Both are independent, but both is linked to `Login`.

```commandline
                        [ Login ]
                     ___/       \___                        Login <> SingleBet
                 ___/               \___                    Login <> MultiBet
             ___/                       \___
            /                               \
      SingleBet                           MultiBet
```

## FAQ

At this point, we select common questions to answer.

<details>
   <summary>
      How to create a file <code>settings.json</code>?
   </summary>
   <p>
      Note: it must be at project's root directory.
   </p>
   <p>
      After, paste the following text:
      <code>
         {"database": "staging"}
      </code>
   </p>
</details>

<details>
   <summary>
      How to set the file <code>.env</code>?
   </summary>
   <p>
      At root directory, you will find the file <code>.env.example</code>. Copy
      it and rename to <code>.env</code>, so open and sets the information required
      there.
   </p>
   <ul>
      <li><code>DATABASE_HOST</code></li>
      <li><code>DATABASE_PORT</code></li>
      <li><code>DATABASE_NAME</code></li>
      <li><code>DATABASE_USER</code></li>
      <li><code>DATABASE_PASSWD</code></li>
   </ul>
   <p>You need to fill these variables.</p>
</details>

<details>
   <summary>
      How the module <code>set_config.py</code> works?
   </summary>
   <p>
      This module has functions to use as a switch between databases as part
      of this file to change the database between <code>staging</code>,
      <code>production</code> and <code>testing</code>.
   </p>
</details>

<details>
   <summary>
      What's the field <code>potential_earnings</code>?
   </summary>
   <p>
      This field represents the earnings without the <code>operator_fee</code>.
   </p>
</details>

<details>
   <summary>
      What's the field <code>total_amount</code>?
   </summary>
   <p>
      This field represents the real earning after apply the <code>operator_fee</code>.
   </p>
</details>

<details>
   <summary>
      What's the field <code>profit</code>?
   </summary>
   <p>
      This field represents the profit of operation or the <code>value_invest * odd</code>
   </p>
</details>

[Back to Start](#better-bet)
