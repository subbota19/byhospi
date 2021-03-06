import pandas
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://zhenya:zhenya@localhost/byhospi")


def add_number_phone():
    pd = pandas.read_csv(
        "/home/zhenya/PycharmProjects/django/byhospi/scrapy_byhospi/number.csv"
    )
    pd.to_sql("hospital_number", engine, if_exists="append", index=False)


def add_hospital():
    pd = pandas.read_csv(
        "/home/zhenya/PycharmProjects/django/byhospi/scrapy_byhospi/hospital.csv"
    )
    pd.to_sql("hospital_hospital", engine, if_exists="append", index=False)
