import argparse
import sys

import sqlalchemy as sa


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='DB URL like postgresql://{username}:{password}@{host}:{port}/{database}', required=True)

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    engine = sa.create_engine(args.url)
    with engine.connect() as conn:
        for sql_ in sys.stdin.read().split(";"):
            sql = sql_.strip() + ";"

            try:
                res = conn.execute(sa.text(sql))
                print(f'SQL: {sql.splitlines()[0]}')
                print(f'Rows affected: {res.rowcount}')
                print()

            except Exception as e:
                if 'empty query' in str(e):
                    continue  # ignore empty queries error

                raise
