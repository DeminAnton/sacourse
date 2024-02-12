import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from asyncio import run


from queries.orm import create_tables, insert_data

if __name__ == "__main__":
    create_tables()
    run(insert_data())
    