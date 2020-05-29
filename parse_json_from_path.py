from DataParser import DataParser
import heapq
import json

def parse_all_lines(all_lines):
    for i, line in enumerate(all_lines):
        if line == '': continue
        line_instance = DataParser(line, i)
        yield line_instance

def get_highest_n_element(all_lines, count):
    heap = []
    for line_instance in parse_all_lines(all_lines):
        heapq.heappush(heap, line_instance)
        if len(heap) > count:
            heapq.heappop(heap)
    heap.sort(reverse=True)
    return heap

def parse_JSON_from_path(file_path, count):
    all_lines_file = open(file_path, 'r')
    top_n_element = get_highest_n_element(all_lines_file, count)
    all_lines_file.close()
    queries = ["score", "id"]
    output = [data.get(queries) for data in top_n_element]
    return output
