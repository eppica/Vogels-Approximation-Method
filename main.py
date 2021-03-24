from problems.generic_problem import *


result_matrix = []


def reset_result_matrix():
    column = []
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            column.append(None)
        result_matrix.append(column.copy())
        column.clear()


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
    origin_penalty = []
    destination_penalty = []
    column = []

    for i, line in enumerate(matrix):
        origin_penalty.append(difference_lower_costs(line.copy()))

    for j in range(0, len(matrix[0])):
        for k in range(0, len(matrix)):
            column.append(matrix[k][j])
        destination_penalty.append(difference_lower_costs(column))
        column.clear()

    if len(origin_penalty) == 1:
        return [origin_penalty, None]
    elif len(destination_penalty) == 1:
        return [destination_penalty, None]
    else:
        return [origin_penalty, destination_penalty]


def difference_lower_costs(iterable):
    iterable_remove_none = []
    for x in iterable:
        if x is not None:
            iterable_remove_none.append(x)
    try:
        best = min(iterable_remove_none)
        iterable_remove_none.remove(best)
    except ValueError:
        return None

    try:
        alternative = min(iterable_remove_none)
    except ValueError:
        return best

    return abs(alternative - best)


def get_column(index):
    column = []
    for j in range(0, len(matrix)):
        column.append(matrix[j][index])
    return column


def find_lower_cell(origin_penalty, destination_penalty):
    result = []

    max_difference_origin = max(origin_penalty)
    max_difference_destination = max(destination_penalty)

    if max_difference_origin < max_difference_destination:
        index_max_difference = destination_penalty.index(max_difference_destination)
        result.append(index_max_difference)
        column = get_column(index_max_difference)
        lower_cost_value = min(column)
        result.append(lower_cost_value)
        result.append(column.index(lower_cost_value))
    else:
        index_max_difference = origin_penalty.index(max_difference_origin)
        result.append(index_max_difference)
        line = matrix[index_max_difference]
        lower_cost_value = min(line)
        result.append(lower_cost_value)
        result.append(line.index(lower_cost_value))

    return result


def main():

    reset_result_matrix()

    if sum(need) > sum(availability):
        insert_artificial_origin()
    elif sum(need) < sum(availability):
        insert_artificial_destination()

    while sum(need) and sum(availability) != 0:
        origin_penalty, destination_penalty = calculate_penalties()

        index_max_difference, lower_cost_value, index_lower_cost_value = find_lower_cell(origin_penalty, destination_penalty)

        value_need = need[index_max_difference]
        value_availability = availability[index_lower_cost_value]

        if value_availability < value_need:
            result_matrix[index_lower_cost_value][index_max_difference] = lower_cost_value * value_availability
            matrix.pop(index_lower_cost_value)
            availability.pop(index_lower_cost_value)
            need[index_max_difference] -= value_availability
        else:
            result_matrix[index_lower_cost_value][index_max_difference] = lower_cost_value * value_need
            for i in range(0, len(matrix)):
                matrix[i].pop(index_max_difference)
            need.pop(index_max_difference)
            availability[index_lower_cost_value] -= value_need


main()
pass
