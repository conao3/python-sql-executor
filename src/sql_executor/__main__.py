import argparse
import contextlib
import sys
import time

import sqlalchemy as sa

@contextlib.contextmanager
def timewatch():
    start = time.time()
    yield
    end = time.time()
    m, s = divmod(end - start, 60)
    h, m = divmod(m, 60)
    print(f'Time: {h:02.0f}:{m:02.0f}:{s:05.02f}')


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
                with timewatch():
                    print(f'SQL: {sql.splitlines()[0]}')
                    res = conn.execute(sa.text(sql))
                    print(f'Rows affected: {res.rowcount}')

                print()

            except Exception as e:
                if 'empty query' in str(e):
                    continue  # ignore empty queries error

                raise
