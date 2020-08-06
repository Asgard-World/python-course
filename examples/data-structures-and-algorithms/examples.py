

# ----- 1.1) Unpacking a Sequence into Separate Variables ----- #

# 1.
details = ['Ferrari', 89, 60, (10, 5, 2020)]

company, price, shares, date = details
print(date)

company, price, shares, (day, month, year) = details
print(day, month, year)

# 2.
# Note: Unpacking work with any object that happens to be iterable, not just tuples and lists.
python = 'Python'
p, y, t, h, o, n = python
print(p, y, t, h, o, n)

# 3.
# Sometimes you want to discard some values when unpacking (we don't need that values in that
# values in that point in code). You can use a "throwaway variable" name for these values.
# Make sure the variable isn't already picked => _ seems to be a good choice.
details = ['Ferrari', 89, 60, (10, 5, 2020)]

_, price, shares, _ = details
print(price, shares)

_, _, shares, (_, _, year) = details
print(year)

# NOT recomanded:
print(_)  # it works, but it's very confusing. What did the interpreter print here ?


# ----- 1.2) Unpacking Elements from Iterable of Arbitrary Length ----- #

# Sometimes you need to unpack N elements from an iterable, but the iterable my be longer than
# N elements => raise ValueError. Python "star expressions" can help us to address this problem.

# 1.
t = (10, 20)
try:
    a, b, c = t  # => will raise ValueError exception -> not enough values to unpack (expected 3, got 2)
except ValueError as e:
    print(e)


# 2.
# Suppose we have a list of Hamilton's lap durations at Silverstone and we want to discard the first
# record because the tires were not heated and the last one because the tires were in a bad situation.
def drop_first_last(f1_lap_times):
    first, *middle, last = f1_lap_times
    return sum(middle) / len(middle)


f1_lap_times = (1.78, 1.70, 1.6, 1.51, 1.32, 1.46, 1.75)
print(drop_first_last(f1_lap_times))


# 3.
# Suppose we have details about Formula 1 drivers that consist of a forename, surname, email and
# followed by a set of phone numbers.
record = ("Max", "Verstappen", 'max.verstappen@redbullracing.com', '773-555-1212', '847-555-1212')
forename, surname, email, *phone_numbers = record
print(phone_numbers)

# 4.
# The starred variable can also be the first.
record = ("Max", "Verstappen", "Netherlands", "Red Bull Racing Honda", 22, 34)
*driver_details, podiums = record
print(podiums)

# 5.
*trailing, current = [10, 4, 56, 23, 65, 44, 99]
print(trailing)
print(current)
