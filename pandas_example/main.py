import pymysql
import pandas


cameron = pandas.DataFrame(pandas.read_csv('cameron.csv', header=0))


cameron.info()
