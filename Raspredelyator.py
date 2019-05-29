import openpyxl
from openpyxl import Workbook
import sys


sys.setrecursionlimit(20000)

min_sd = 999
max_delta_up = 0.1
max_sd = 2.0


def copy_ammunition(amm):
    if type(amm) == type(dict()):
        amm_copy = dict()
    elif type(amm) == type([]):
        amm_copy = []
    for i in amm:
        if type(amm[i]) == type(dict()) or type(amm) == type([]):
            amm_copy[i] = copy_ammunition(amm[i])
        else:
            amm_copy[i] = amm[i]
    return amm_copy


def get_pers_by_num(num_pers):
    person = ""
    n_pers = 0
    for i in people.keys():
        if n_pers == num_pers:
            person = i
            break
        n_pers += 1
    return person


def get_smt_by_num(smt, num_pers):
    person = ""
    n_pers = 0
    for i in smt.keys():
        if n_pers == num_pers:
            person = i
            break
        n_pers += 1
    return person


def sd(ms):
    ssq = 0
    for i in ms.values():
        ssq += (i["weight"] - i["max_weight"])**2
    return ssq


def gen(num_pers):
    global peoples_ammunition, things_remaining
    flag_impossibility = False
    if num_pers == len(peoples_ammunition):
        possible_results.append(peoples_ammunition)
        flag_impossibility = True
    person = get_pers_by_num(num_pers)

    # Making buffers

    Buff_things_remainimg = things_remaining.copy()
    Buff_peoples_ammunitions = peoples_ammunition.copy()

    if not flag_impossibility:

        # This person
        for i in range(len(things_remaining)):
            thing = get_smt_by_num(things_remaining, i)
            #print(thing)
            if thing == '':
                break
            peoples_ammunition[person]["weight"] += things_remaining[thing]
            peoples_ammunition[person]["things"].append(thing)
            print(things_remaining)
            del things_remaining[thing]
            print(things_remaining)

            if sd(peoples_ammunition) < max_sd and peoples_ammunition[person]["weight"] < max_delta_up * peoples_ammunition[person]["max_weight"]:
                possible_results.append(peoples_ammunition)
                gen(num_pers)
            else:
                flag_impossibility = True
            print(peoples_ammunition, sd(peoples_ammunition))

            print(things_remaining == Buff_things_remainimg)
            things_remaining = Buff_things_remainimg
            peoples_ammunition = Buff_peoples_ammunitions






        # Next person
        person = get_pers_by_num(num_pers + 1)
        for i in range(len(things_remaining)):
            thing = get_smt_by_num(things_remaining, i)
            #print(thing)
            if thing == '':
                break
            peoples_ammunition[person]["weight"] += things_remaining[thing]
            peoples_ammunition[person]["things"].append(thing)
            print(things_remaining)
            del things_remaining[thing]
            print(things_remaining)
            if sd(peoples_ammunition) < max_sd and peoples_ammunition[person]["weight"] < max_delta_up * peoples_ammunition[person]["max_weight"]:
                possible_results.append(peoples_ammunition)
                gen(num_pers + 1)
            else:
                flag_impossibility = True
            print(sd(peoples_ammunition))
            gen(num_pers + 1)
            things_remaining = Buff_things_remainimg
            peoples_ammunition = Buff_peoples_ammunitions
    #print(peoples_ammunition)


def put(num_pers, ammunition, things_rem, num_recursion):
    global min_sd
    if sd(ammunition) < min_sd:
        min_sd = sd(ammunition)
        print(ammunition)
    if len(things_rem) == 0 and sd(ammunition) < max_sd:
        possible_results.append(peoples_ammunition)
    person = get_pers_by_num(num_pers)

    # This person:
    for i in range(len(things_rem)):
        thing = get_smt_by_num(things_rem, i)
        weight = things_rem[thing]
        # Putting
        things_rem_buff = copy_ammunition(things_rem)
        del things_rem_buff[thing]
        ammunition_buff = copy_ammunition(ammunition)
        ammunition_buff[person]["weight"] += weight
        ammunition_buff[person]["things"].append(thing)
        if ammunition_buff[person]["weight"] < (1 + max_delta_up) * ammunition[person]["max_weight"]:
            put(num_pers, copy_ammunition(ammunition_buff), copy_ammunition(things_rem_buff), num_recursion + 1)

        del ammunition_buff

    person = get_pers_by_num(num_pers + 1)
    # Next person
    if len(peoples_ammunition) >= num_pers + 2:
        for i in range(len(things_rem)):
            thing = get_smt_by_num(things_rem, i)
            weight = things_rem[thing]
            # Putting
            things_rem_buff = copy_ammunition(things_rem)
            del things_rem_buff[thing]
            ammunition_buff = copy_ammunition(ammunition)
            ammunition_buff[person]["weight"] += weight
            ammunition_buff[person]["things"].append(thing)

            if ammunition_buff[person]["weight"] < (1 + max_delta_up) * ammunition[person]["max_weight"]:
                put(num_pers + 1, copy_ammunition(ammunition_buff), copy_ammunition(things_rem_buff), num_recursion + 1)

            del ammunition_buff
    del things_rem
    del ammunition


def find_value(thing):
    while True:
        if thing is None:
            return 0
        try:
            return float(thing)
        except:
            if "*" in thing:
                thing = thing.split("*")
                return find_value(my_list[thing[0][1:]].value) * find_value(my_list[thing[1]].value)
            elif "/" in thing:
                thing = thing.split("/")
                return find_value(my_list[thing[0][1:]].value) / find_value(my_list[thing[1]].value)
            elif "SUM" in thing:
                last = thing.index(")")
                first = thing.index("(")
                st = thing[first+1:last].split(":")
                summ = 0
                cells_for_sum = my_list[st[0]:st[1]]
                for i in range(len(cells_for_sum)):
                    summ += find_value(cells_for_sum[i][0].value)
                return summ


people = dict()
things = dict()


book = openpyxl.load_workbook("C:\\Users\\Vova\\Downloads\\Slet(1).xlsx")

lists = book.sheetnames
my_list = book[lists[0]]


# Append things

cells_names_things_food = my_list["A1":"A20"]
cells_weights_things_food = my_list["B1":"B20"]

cells_names_things_equipment = my_list["A23":"A30"]
cells_weights_things_equipment = my_list["B23":"B30"]

for i in range(len(cells_names_things_food)):
    things[cells_names_things_food[i][0].value] = cells_weights_things_food[i][0].value


for i in range(len(cells_names_things_equipment)):
    things[cells_names_things_equipment[i][0].value] = cells_weights_things_equipment[i][0].value

#print(things)


# Append people

cells_names_people = my_list["E2":"E22"]
cells_names_people_weight = my_list["G2":"G22"]

for i in range(len(cells_names_people)):
    if cells_names_people[i][0].value is not None:
        stp = cells_names_people_weight[i][0].value
        stp = find_value(stp)
        people[cells_names_people[i][0].value] = stp


#print(people)

peoples_ammunition = people.copy()

for i in peoples_ammunition:
    peoples_ammunition[i] = {"max_weight" : peoples_ammunition[i]}
    peoples_ammunition[i]["weight"] = 0
    peoples_ammunition[i]["things"] = []


things_remaining = things.copy()

possible_results = []


put(0, peoples_ammunition.copy(), things_remaining.copy(), 0)


print(possible_results)
print(min_sd)

