from sys import argv

script_name, hours_work, rate_hour, premium = argv

print(int(hours_work) * int(rate_hour) + int(premium))
