from problems.generic_problem import *

def insert_artificial_origin():
    origin.append('dummy')
    line = []
    for i in range(0, len(destination)):
        line.append(999)
    matrix.append(line)
    availability.append(sum(need)-sum(availability))


def insert_artificial_destination():
    destination.append('dummy')
    for line in matrix:
        line.append(999)
    need.append(sum(availability)-sum(need))


def calculate_penalties():
    column = []

    for i, line in enumerate(matrix):
        origin_penalty.append(difference_lower_costs(line.copy()))

    for j in range(0, len(matrix[0])):
        for k in range(0, len(matrix)):
            column.append(matrix[k][j])
        destination_penalty.append(difference_lower_costs(column))
        column.clear()


def difference_lower_costs(iterable):
    first_min = min(iterable)
    iterable.remove(min(iterable))
    second_min = min(iterable)
    return second_min - first_min


def main():
    if sum(need) > sum(availability):
        insert_artificial_origin()
    elif sum(need) < sum(availability):
        insert_artificial_destination()

    calculate_penalties()

    pass


main()