import json

class DataParser:
    def __init__(self, line, sequence_order):
        score, values = line.split(':', 1)
        self.key = (int(score), sequence_order)
        try:
            self.json_props = json.loads(values)
        except:
            self.json_props = None
        if self.json_props != None:
            self.json_props['score'] = int(score)
            self.json_props['sequence_order'] = sequence_order

    # If the parsed data is not a json string or id is not presence in the json string, the data is not valid
    @property
    def is_valid(self):
        return self.json_props != None and 'id' in self.json_props

    # Sorting. Highest score first. If same score then most recently first
    def __lt__(self, other):
        return self.key > other.key

    def __repr__(self):
        return 'None' if self.json_props == None else str(self.json_props['score']) + ' ' + str(self.json_props['sequence_order'])

    def get(self, queries):
        ret = {query: self.json_props[query] for query in queries}
        return json.dumps(ret)

print(__name__)
