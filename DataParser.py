import json
class DataParser:
    def __init__(self, line, sequence_order):
        score, values = line.split(':', 1)
        self.score = score
        self.json_str = values
        self.key = (int(score), sequence_order)

    # Sorting. Highest score first. If same score then most recently first
    def __lt__(self, other):
        return self.key < other.key

    def get(self, queries):
        try:
            json_props = json.loads(self.json_str)
        except:
            json_props = None
        if json_props == None: 
            raise Exception('invalid json format No JSON object could be decoded THIS IS NOT JSON')
        ret = {}
        for query in queries:
            if query == 'score':
                ret[query] = self.score
            else: ret[query] = json_props[query]
        return ret
