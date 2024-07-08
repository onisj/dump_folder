from itertools import groupby
from pprint import pprint

# Sample data
data = [
    ("a", "value a 1"),
    ("a", "value a 2"),
    ("b", "value b 1"),
    ("b", "value b 2"),
    ("c", "value c 1"),
    ("c", "value c 2")
]

# Sort data to ensure groupby works correctly
data.sort(key=lambda x: x[0])

# Group data by the first element of each tuple
grouped_data = groupby(data, key=lambda x: x[0])

# Print grouped data in a readable format
pprint([{'key': key, 'grouped_values': list(group)} for key, group in grouped_data])
