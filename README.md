# hubspot-test

Prototype Python experiments to play with the Hubspot APIs.

## Usage

### Setup

- Requires `Python` ( version listed in `Pipfile` )
- Requires `GNU Make` and `pipenv`
- 
- Ensure you have a `.env` file which specifies the following variables:
  - API_KEY
  - APP_NAME
  - APP_ID
  - CLIENT_ID
  - CLIENT_SECRET
  - OAUTH_URL


### Building the project

```shell
make install
```

### Running the project

```shell
make run
```