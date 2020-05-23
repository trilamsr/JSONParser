from pprint import pprint
from DataParser import DataParser
import sys

def parse_all_lines(all_lines):
    separate_lines = all_lines.split('\n')
    for i, line in enumerate(separate_lines):
        line_instance = DataParser(line, i)
        yield line_instance

def failed_validation(target_arr):
    requirement = lambda element: element.is_valid
    return not all(requirement(element) for element in target_arr)

def get_k_element(arr, k):
    ret = []
    for ele in arr:
        if k > 0:
            ret.append(ele)
            k-= 1
        if k <= 0: break
    return ret

def parse_JSON_from_path(file_path, count):
    file = open(file_path, 'r')
    all_lines = file.read()
    parsed_information = list(parse_all_lines(all_lines))
    file.close()
    parsed_information.sort()
    k_element = get_k_element(parsed_information, count)
    if failed_validation(k_element):
        raise Exception('invalid json format No JSON object could be decoded THIS IS NOT JSON')
    queries = ['score', 'id']
    output = [data.get(queries) for data in k_element]
    print(output)
    return output
