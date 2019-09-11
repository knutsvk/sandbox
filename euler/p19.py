months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if __name__ == "__main__":
    count = 0
    year = 1901
    day = 1 # 1901 started on a Tuesday
    while year <= 2000:
        # Think about leap year
        if year % 100 != 0 and year % 4 == 0 or year % 100 == 0 and year % 400 == 0:
            months[1] = 29
        else: 
            months[1] = 28
        for month in months:
            day = (day + month) % 7
            if day == 6: 
                count += 1
        year += 1
    print(count)
