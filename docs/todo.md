Implement Logging Decorator Function as given below
https://towardsdatascience.com/python-decorators-for-data-science-6913f717669a


Implement Timing Decorator Function to get runtime 
https://towardsdatascience.com/python-decorators-for-data-science-6913f717669a

Use Dataclass 
https://zetcode.com/python/dataclass/

Feature to turn off logging


logs directory, should it be pushed as part of deployment?
Configurable logging


#### What are advantages and disadvantages of using zip as python application?


### How to avoid path conflict in python? like when we give relative path of config file, or logs directory, This fails when environment changes. 

By using Absolute Path:
```python
import os

# get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# use the absolute path to the config file
config_file_path = os.path.join(script_dir, 'config.ini')

# use the absolute path to the log directory
log_dir_path = os.path.join(script_dir, 'logs')

```

Or by using Environment Variable

```python
import os

# get the absolute path to the directory containing the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# use the absolute path to the config file
config_file_path = os.path.join(script_dir, 'config.ini')

# use the absolute path to the log directory
log_dir_path = os.path.join(script_dir, 'logs')

```


How to redirect entire output of spark-submit to a file
https://stackoverflow.com/questions/46429962/how-to-redirect-entire-output-of-spark-submit-to-a-file