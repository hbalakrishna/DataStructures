import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyspark
from pyspark import SparkContext
from pyspark.sql import SQLContext
from IPython.core.display import display, HTML
from IPython.core.magic import register_cell_magic, register_line_cell_magic, register_line_magic
from matplotlib import pyplot as plt
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler
from pyspark.sql.functions import array, col, count, mean, sum, udf, when
from pyspark.sql.types import DoubleType, IntegerType, StringType, Row
from pyspark.sql.functions import sum, col, udf
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from nba_utils import draw_3pt_piechart,plot_shot_chart