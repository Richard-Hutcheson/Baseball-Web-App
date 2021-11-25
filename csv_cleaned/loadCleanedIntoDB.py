import pymysql as sql
from csi3335fall2021 import user
import os


def main():
    con = sql.connect(user=user['username'], password=user['password'], host=user['host'], db=user['host'])

    with con:
        cur = con.cursor()

        files = os.listDir()

        for file in files:
            if file.find(".csv") != -1:



if __name__ == "__main__":
    main()