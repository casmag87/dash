import psycopg2
from config.settings import connection


def select_row(params):
    with connection as con:
        with con.cursor() as cur:
            query = """SELECT id, country_name, indicator_name, indicator_code, "year", value
                       FROM public.indicator_data
                       WHERE indicator_name = %s AND value IS NOT NULL;"""
              
            cur.execute(query, params)
            records = cur.fetchall()

    return records



