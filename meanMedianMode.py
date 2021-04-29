import csv
from collections import Counter

with open("C:/Users/sravy/White Hat Jr/Project 104- Mean, Median, Mode/SOCR-HeightWeight.csv", newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)
new_data = []

for i in range(len(file_data)):
    num = file_data[i][2]
    new_data.append(float(num))

total_weight = 0
total_number_of_people = len(new_data)

for x in new_data:
    total_weight += x

def mean_calc(sum_of_values, total_number):
    mean = sum_of_values / total_number
    print(f"The mean is: {mean: f}")

new_data.sort()
def median_calc(total_number):
    if(total_number % 2 == 0):
        median1 = float(new_data[total_number//2])
        median2 = float(new_data[total_number//2 - 1])
        median = (median1 + median2)/2
        print(f"The median is: {median: f}")
    else:
        median = new_data[total_number//2]
        print(f"The median is: {median: f}")

def mode_calc():
    data = Counter(new_data)
    range_data = {
                    "75-85": 0,
                    "85-95": 0,
                    "95-105": 0,
                    "105-115": 0,
                    "115-125": 0,
                    "125-135": 0,
                    "135-145": 0,
                    "145-155": 0,
                    "155-165": 0,
                    "165-175": 0
                }
    for weight, occurence in data.items():
        if 75 < float(weight) < 85:
            range_data["75-85"] += occurence
        elif 85 < float(weight) < 95:
            range_data["85-95"] += occurence
        elif 95 < float(weight) < 105:
            range_data["95-105"] += occurence
        elif 105 < float(weight) < 115:
            range_data["105-115"] += occurence
        elif 115 < float(weight) < 125:
            range_data["115-125"] += occurence
        elif 125 < float(weight) < 135:
            range_data["125-135"] += occurence
        elif 135 < float(weight) < 145:
            range_data["135-145"] += occurence
        elif 145 < float(weight) < 155:
            range_data["145-155"] += occurence
        elif 155 < float(weight) < 165:
            range_data["155-165"] += occurence
        elif 165 < float(weight) < 175:
            range_data["165-175"] += occurence

    mode_range, mode_occurence = 0, 0
    for range, occurence in range_data.items():
        if occurence > mode_occurence:
            mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence
    
    mode = float((mode_range[0] + mode_range[1]) / 2)
    print(f"The mode is: {mode: f}")

mean_calc(total_weight, total_number_of_people)
median_calc(total_number_of_people)
mode_calc()