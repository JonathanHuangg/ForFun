import random


months = [
    "January, 31",
    "February, 28",
    "March, 31",
    "April, 30",
    "May, 31",
    "June, 30",
    "July, 31",
    "August, 31",
    "September, 30", 
    "October, 31",
    "November, 30",
    "December, 31"
]

monthsHash = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6, 
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

def generateString(num):
    inputs = [

    ]
    # Generates input strings
    for _ in range(0, num):
        indexMonth = random.randrange(0, len(months))
        month = months[indexMonth].split(",")[0]
        day = random.randint(1, int(months[indexMonth].split(",")[1][1:]))
        year = int(random.normalvariate(2024, 3))
        time = str(random.randint(0, 24)) + ":" + str(random.randint(0, 60))

        if int(time.split(":")[0]) < 10:
            time = "0" + time.split(":")[0] + ":" + time.split(":")[1]
        if int(time.split(":")[1]) < 10:
            time = time.split(":")[0] + ":" + "0" + time.split(":")[1]
        inputs.append(month + " " + str(day) + ", " + str(year) + "; " + time)
    
    return inputs

# August 17, 2028; 22:01
def sort(inputs):

    date = sorted(inputs, key = lambda year: 
                  (year.split(";")[0][-4:], 
                   monthsHash[year.split(":")[0].split(" ")[0]], 
                   year.split(",")[0][-2:], 
                   year.split(";")[1].split(":")[0][1:],
                   year.split(";")[1].split(":")[1]
                   ))
    return date

def parse(inputs):
    for input in inputs:
        print(input)

def main():
    inputs = generateString(100)
    parse(sort(inputs))

main()


