building_blocks = {
        1: "one", 
        2: "two", 
        3: "three", 
        4: "four", 
        5: "five", 
        6: "six", 
        7: "seven", 
        8: "eight", 
        9: "nine", 
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
        100: "hundred",
        }

def count(start, stop):
    assert 0 < start < 1000
    assert start < stop <= 1000
    i = start 
    num_letters = 0
    while i <= stop: 
        number_string = spell_number(i)
        print(number_string)
        num_letters += len(number_string.replace(" ", ""))
        i += 1
    return num_letters


def spell_number(i):
    if i == 0:
        return ""
    elif i <= 20:
        return building_blocks[i]
    elif i < 100:
        tens = (i // 10)
        ans = building_blocks[tens * 10]
        ones = i - tens * 10
        return ans + " " + spell_number(ones)
    elif i < 1000:
        hundreds = (i // 100)
        ans = spell_number(hundreds) + " hundred"
        if i % 100 != 0:
            ans += " and " + spell_number(i - hundreds * 100)
        return ans
    else: 
        return "one thousand"


if __name__ == "__main__":
    num_letters = count(1, 1000)
    print("Total letters: %d" % num_letters)
