Prediction of genders of english names based on US Social Security data. The gender probability of each name is computed based on the number of male and female babies that were given this name between 1880 and 2017. 

The full data can be found at https://www.ssa.gov/oact/babynames/limits.html

# Description

The main function returns the probability for a given english name to be a male name. There are optional arguments start_year (default 1880) and end_year (default 2018) to use a specific period of time for calculation. For instance, for gender prediction of babyboomers, the period can be set to 1946-1965.

# Installation
```
$ pip install
```

Basic Usage
```python
>>> from NameGenderPredictor import predict_gender
>>> name='john'
>>> print(predict_gender(name))
0.9957852975260119
>>> print(predict_gender(name,start_year=1950,end_year=2010)
0.9962062922197198
```
