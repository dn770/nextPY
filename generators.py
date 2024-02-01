def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    word_list = sentence.split()
    trans_gen = (words[w] for w in word_list)
    trans = []
    for word in trans_gen:
        trans.append(word)
    return " ".join(trans)


#print(translate("el gato esta en la casa"))

def is_prime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def first_prime_over(n):
    prime_generator = (num for num in range(n, 10 ** 100) if is_prime(num))
    return next(prime_generator)


#print(first_prime_over(100000))

def parse_ranges(ranges_string):
    slice_gen = (cup.split("-") for cup in ranges_string.split(","))
    ranges_gen = (n for i, j in slice_gen for n in range(int(i), int(j)+1))
    return ranges_gen


#print(list(parse_ranges("1-2,4-4,8-10")))
#print(list(parse_ranges("0-0,4-8,20-21,43-45")))


def get_fibo():
    num1 = 0
    num2 = 1
    next_number = 0

    while True:
        yield next_number
        num1 = num2
        num2 = next_number
        next_number = num1 + num2


#fibo_gen = get_fibo()
#for i in range(10):
#    print(next(fibo_gen))

def gen_secs():
    sec = 0
    while sec < 60:
        yield sec
        sec += 1

def gen_minutes():
    minute = 0
    while minute < 60:
        yield minute
        minute += 1

def gen_hours():
    hour = 0
    while hour < 24:
        yield hour
        hour += 1


def gen_time():
    hours_gen = gen_hours()
    for hour in hours_gen:
        mins_gen = gen_minutes()
        for minute in mins_gen:
            secs_gen = gen_secs()
            for second in secs_gen:
                yield f"{hour:02d}:{minute:02d}:{second:02d}"

def gen_years(start = 2023):
    while True:
        yield start
        start +=1

def gen_months():
    for month in range (1,13):
        yield month

def gen_days(month, year):
    for day in range(1, 32):
        yield day
        if day == 28 and month == 3 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            break
        if month == 3 and day == 29:
            break
        if day == 30 and month in [4, 6, 9, 11]:
            break


def gen_date():
    years_gen = gen_years()
    for year in years_gen:
        months_gen = gen_months()
        for month in months_gen:
            days_gen = gen_days(month, year)
            for day in days_gen:
                    yield f"{day:02d}/{month:02d}/{year:04d}"


def gen_data_time():
    date_gen = gen_date()
    for date in date_gen:
        time_gen = gen_time()
        for time in time_gen:
            yield f"{date} {time}"


date_time_gen = gen_data_time()
for i in range (10**10000):
    if  i % 1000000 == 0:
        print(next(date_time_gen))
    else:
        next(date_time_gen)