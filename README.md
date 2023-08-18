# python-sql-executor
Execute SQL from stdin.

## Install
```
poetry install
```

## Usage
```
usage: sql-executor [-h] --url URL

options:
  -h, --help  show this help message and exit
  --url URL   DB URL like postgresql://{username}:{password}@{host}:{port}/{database}
```

## Example
```
cat sample1.sql | poetry run sql-executor --url postgresql://{username}:{password}@{host}:{port}/{database}
```
