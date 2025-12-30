# sql-executor

A simple command-line tool for executing SQL statements from stdin against PostgreSQL databases.

## Features

- Execute multiple SQL statements from standard input
- Displays execution time for each statement
- Reports affected row counts
- Automatically commits transactions on completion

## Requirements

- Python 3.11+
- PostgreSQL database

## Installation

```bash
pip install sql-executor
```

Or install from source using Poetry:

```bash
git clone https://github.com/conao3/python-sql-executor.git
cd python-sql-executor
poetry install
```

## Usage

```
sql-executor --url <database-url>
```

### Options

| Option | Description |
|--------|-------------|
| `--url` | Database connection URL (required) |
| `-h, --help` | Show help message |

### Database URL Format

```
postgresql://<username>:<password>@<host>:<port>/<database>
```

## Examples

Execute SQL from a file:

```bash
cat queries.sql | sql-executor --url postgresql://user:pass@localhost:5432/mydb
```

Execute inline SQL:

```bash
echo "SELECT * FROM users; UPDATE users SET active = true;" | sql-executor --url postgresql://user:pass@localhost:5432/mydb
```

### Sample Output

```
SQL: SELECT * FROM users;
Rows affected: 10
Time: 00:00:00.05

SQL: UPDATE users SET active = true;
Rows affected: 10
Time: 00:00:00.02
```

## License

Apache-2.0
