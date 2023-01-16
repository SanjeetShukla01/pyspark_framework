# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------
# Created By  :     'Sanjeet Shukla'
# Created Date:     16/01/23 1:07 am
# File:             test_happiness_index_data_job.py
# -----------------------------------------------------------------------

import unittest

from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, IntegerType
from src.utils import spark_utils, table_schema


class TestHappinessJob(unittest.TestCase):

    utils = spark_utils.SparkUtils()
    spark = utils.get_spark_session("aa_data_job")

    # Using hardcoded file path as config directory is inside src and relative path of data is different.
    # TODO: To move the config directory outside src.

    file_path = "../data/source_data/happiness_index_data"
    file_format = "csv"
    csv_schema = table_schema.happiness_data_schema

    def test_read_data_csv(self, path: str = file_path, file_format: str = file_format,
                           schema: StructType = csv_schema):
        actual_df = self.utils.read_data(self.spark, path, file_format, schema)
        expected_df = self.spark.read.csv(path, header=True)
        assert actual_df.count() == expected_df.count()

    def test_csv_data_schema(self,  schema=csv_schema, path=file_path, file_format=file_format):
        actual_df = self.utils.read_data(self.spark, path, file_format, schema)
        assert actual_df.schema == schema

    def test_compare_data_csv(self, path=file_path, file_format=file_format, schema=csv_schema):
        actual_df = self.utils.read_data(self.spark, path, file_format, schema).filter(col("Happiness Rank") <= 2)
        data = [("Switzerland", "Western Europe", 1, 7.587, 0.03411, 1.39651, 1.34951, 0.94143, 0.66557, 0.41978,
                 0.29678, 2.51738),
                ("Iceland", "Western Europe", 2, 7.561, 0.04884, 1.30232, 1.40223, 0.94784, 0.62877, 0.14145,
                 0.4363, 2.70201)]
        expected_df = self.spark.createDataFrame(data, schema)
        assert sorted(actual_df.collect()) == sorted(expected_df.collect())

    def test_dataframe(self):
        data1 = [(171, 76), (151, 96)]
        data2 = [(172, 75), (95, 234)]
        schema = StructType([StructField("a", IntegerType(), True),
                             StructField("b", IntegerType(), True)])
        df1 = self.spark.createDataFrame(data1, schema)
        df2 = self.spark.createDataFrame(data1, schema)
        assert sorted(df1.collect()) == sorted(df2.collect())


if __name__ == '__main__':
    unittest.main()
