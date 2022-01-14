import csv
csv_data = []
age = []
sex = []
bmi = []
children = []
smoker = []
location = []
cost = []
with open("C:\Programming\Python\python-portfolio-project-starter-files\python-portfolio-project-starter-files\insurance.csv") as insurance_file:
    insurance_file_dict = csv.DictReader(insurance_file)
    for row in insurance_file_dict:
        csv_data.append(row)
        age.append(row["age"])
        sex.append(row["sex"])
        bmi.append(row["bmi"])
        children.append(row["children"])
        smoker.append(row["smoker"])
        location.append(row["region"])
        cost.append(row["charges"])
    for key, value in insurance_file_dict:
        csv_data[key] = value

# Average Age:

age = [float(num) for num in age]
def average_age(age):
    average_age = 0
    for num in age:
        average_age += num
    average_age = average_age / len(age)
    return round(average_age)
print(f"Average Age: {average_age(age)}")

# Number of Males and Females:

def no_of_m_and_f(sex):
    number_of_gender = {"Males": 0,
                        "Females": 0}
    count_m, count_f = 0, 0
    for gen in sex:
        if gen == "male":
            count_m += 1
            number_of_gender["Males"] = count_m
        elif gen == "female":
            count_f += 1
            number_of_gender["Females"] = count_f
    return number_of_gender
print(f"Number of Males and Females: {no_of_m_and_f(sex)}")

# Average BMI:

bmi = [float(num) for num in bmi]
def average_bmi(bmi):
    average_bmi = 0
    for num in bmi:
        average_bmi += num
    average_bmi = average_bmi / len(bmi)
    return round(average_bmi, 2)
print(f"Average BMI: {average_bmi(bmi)}")

# Average number of children:

children = [int(num) for num in children]
def average_number_children(children):
    average_number_children = 0
    for num in children:
        average_number_children += num
    average_number_children = average_number_children / len(children)
    return round(average_number_children)
print(f"Average number of children: {average_number_children(children)}")

# Number of Smokers and Non-smokers:

def no_of_s_and_ns(smoker):
    Number_of_Smokers_and_Non_smokers = {"Smokers": 0,
                                        "Non-smokers": 0}
    count_s, count_ns = 0, 0
    for num in smoker:
        if num == "yes":
            count_s += 1
            Number_of_Smokers_and_Non_smokers["Smokers"] = count_s
        elif num == "no":
            count_ns += 1
            Number_of_Smokers_and_Non_smokers["Non-smokers"] = count_ns
    return Number_of_Smokers_and_Non_smokers
print(f"Number_of_Smokers_and_Non_smokers: {no_of_s_and_ns(smoker)}")

# Location count:

def no_of_location(location):
    count_of_location = {}
    count_ne,count_nw,count_se,count_sw = 0,0,0,0
    for area in location:
        if area not in count_of_location.keys() and area == "northeast":
            count_ne = 1
            count_of_location[area] = count_ne
        elif area in count_of_location.keys() and area == "northeast":
            count_ne += 1
            count_of_location[area] = count_ne
        if area not in count_of_location.keys() and area == "northwest":
            count_nw = 1
            count_of_location[area] = count_nw
        elif area in count_of_location.keys() and area == "northwest":
            count_nw += 1
            count_of_location[area] = count_nw
        if area not in count_of_location.keys() and area == "southeast":
            count_se = 1
            count_of_location[area] = count_se
        elif area in count_of_location.keys() and area == "southeast":
            count_se += 1
            count_of_location[area] = count_se
        if area not in count_of_location.keys() and area == "southwest":
            count_sw = 1
            count_of_location[area] = count_sw
        elif area in count_of_location.keys() and area == "southwest":
            count_sw += 1
            count_of_location[area] = count_sw
    return count_of_location
print(f"Location count: {no_of_location(location)}")

# Average Insurance Cost:

cost = [float(num) for num in cost]
def average_insurance_cost(cost):
    average_insurance_cost = 0
    for num in cost:
        average_insurance_cost += num
    average_insurance_cost = average_insurance_cost / len(cost)
    return round(average_insurance_cost, 3)
print(f"Average Insurance Cost: ${average_insurance_cost(cost)}")

# Smoker Insurance Cost:

smoker_cost = []
def avg_smoker_cost(csv_data):
    for num in csv_data:
        if num["smoker"] == "yes":
            smoker_cost.append(num["charges"])
    return smoker_cost
smoker_cost = avg_smoker_cost(csv_data)
#print(smoker_cost)
smoker_cost = [float(num) for num in smoker_cost]
avg_smoker_insurance_cost = 0
for num in smoker_cost:
    avg_smoker_insurance_cost += num
avg_smoker_insurance_cost = round(avg_smoker_insurance_cost / len(smoker_cost), 3)
print(f"Average insurance cost for smoker: ${avg_smoker_insurance_cost}")

# Non-smoker Insurance Cost:

non_smoker_cost = []
def avg_non_smoker_cost(csv_data):
    for num in csv_data:
        if num["smoker"] == "no":
            non_smoker_cost.append(num["charges"])
    return non_smoker_cost
non_smoker_cost = avg_non_smoker_cost(csv_data)
#print(non_smoker_cost)
non_smoker_cost = [float(num) for num in non_smoker_cost]
avg_non_smoker_insurance_cost = 0
for num in non_smoker_cost:
    avg_non_smoker_insurance_cost += num
avg_non_smoker_insurance_cost = round(avg_non_smoker_insurance_cost / len(non_smoker_cost), 3)
print(f"Average insurance cost for non-smoker: ${avg_non_smoker_insurance_cost}")

