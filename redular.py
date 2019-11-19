import os
import os.path
import re

# operator and state data
states = {}
operators = {
    'Airtel': [9900, 9980, 9845, 9880],
    'VF': [9886, 9986, 9964],
    'BSNL': [9480, 9481, 9482],
    'Idea': [9844, 9489],
}


def read_file(filename):
    if not os.path.isfile(filename):
        return []
    fr = open(filename)
    result = fr.readlines()
    fr.close()
    result = [i.strip() for i in result]
    return result


def process_states(states_data):
    states = {}
    for line in states_data:
        state_data = re.split(r"\s+", line)
        states[state_data[0]] = state_data[1]
    return states


def get_states():
    states = read_file('states')
    states = process_states(states)
    return states


def get_operator_and_state(number):
    operator = None
    state = None

    matched = re.search(r"^\d{4}\d{2}\d{4}$", str(number))
    if not matched:
        return operator, state

    opr_no = matched.group(1)
    state_no = matched.group(2)

    for operator in operators:
        if opr_no in operators[operator]:
            operator = opr_no
            break

    # reads states file from current folder
    states = get_states()
    state = states.get(state_no)

    return operator, state


def generate_state_operator_numbers():
    all_operators = list(operators.values())
    all_operators = [opr for operator in all_operators for opr in operator]
    states = get_states()

    all_operator_numbers = []
    for operator in all_operators:
        for state in states:
            all_operator_numbers.append(str(operator) + str(state))

    return all_operator_numbers


def convert_to_str(data):
    data = str(data)
    if len(data) == 1:
        data = '0' + data
    return data


def create_file(filename, dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    fw = open(dirname + "\\" + filename, 'w')
    return fw
