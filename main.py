# Add milliseconds to datetime in Python

from datetime import datetime, timedelta

d = '2023-11-24 09:30:00.000123'

# 👇️ Convert a string to a datetime object
dt = datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f')

print(dt)  # 👉️ 2023-11-24 09:30:00.000123

result = dt + timedelta(milliseconds=300)
print(result)  # 👉️ 2023-11-24 09:30:00.300123