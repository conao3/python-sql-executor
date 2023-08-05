import argparse
import sqlalchemy as sa


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='DB URL like postgresql://{username}:{password}@{host}:{port}/{database}', required=True)

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    engine = sa.create_engine(args.url)
    with engine.connect() as conn:
        result = conn.execute(sa.text('SELECT 1'))
        print(result.fetchone())
