Prediction of genders of english names based on US Social Security data. The gender probability of each name is computed based on the number of male and female babies that were given this name between 1880 and 2017. 

The full data can be found at https://www.ssa.gov/oact/babynames/limits.html

# Description

The main function returns the probability for a given english name to be a male name. There are optional arguments start_year (default 1880) and end_year (default 2018) to use a specific period of time for calculation. For instance, for gender prediction of babyboomers, the period can be set to 1946-1965. If the name is absent from the database, `None` is returned. 

# Installation
Requires package sqlite3. The code was only tested with Python 3.7.
```
$ pip install NameGenderPredictor
```

# Basic Usage
```python
>>> from NameGenderPredictor import predict_gender
>>> print(predict_gender('john'))
0.9957852975260119
>>> print(predict_gender('Avi'))
0.8783253379851723
>>> print(predict_gender('chris'))
0.8632186721917374
>>> print(predict_gender('chris'),start_year=2000,end_year=2010)
0.9833235466823254
>>> print(predict_gender('chris'),start_year=1950,end_year=1965)
0.8111958317448215
```
