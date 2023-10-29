# auto-reservation

## setup

### install pacakges

```sh
  $ cp .env.local .env
  $ poetry install
```

## start

```sh
  $ poetry shell
  $ export $(cat .env | xargs) 2>/dev/null
  $ python3 ./src/gmail_auto.py
```
