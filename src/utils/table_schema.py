from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    DoubleType,
)

happiness_data_schema = StructType(
    [
        StructField("Country", StringType(), True),
        StructField("Region", StringType(), True),
        StructField("Happiness Rank", IntegerType(), True),
        StructField("Happiness Score", DoubleType(), True),
        StructField("Standard Error", DoubleType(), True),
        StructField("Economy (GDP per Capita)", DoubleType(), True),
        StructField("Family", DoubleType(), True),
        StructField("Health (Life Expectancy)", DoubleType(), True),
        StructField("Freedom", DoubleType(), True),
        StructField("Trust (Government Corruption)", DoubleType(), True),
        StructField("Generosity", DoubleType(), True),
        StructField("Dystopia Residual", DoubleType(), True),
    ]
)

json_schema = StructType(
    [
        StructField("cookTime", StringType(), True),
        StructField("datePublished", StringType(), True),
        StructField("description", StringType(), True),
        StructField("image", StringType(), True),
        StructField("ingredients", StringType(), True),
        StructField("name", StringType(), True),
        StructField("prepTime", StringType(), True),
        StructField("recipeYield", StringType(), True),
        StructField("url", StringType(), True),
    ]
)
