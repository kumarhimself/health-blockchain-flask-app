# Data is the unique identifier (UID) that each person
# takes on.

class Block:
    def __init__(self, key, data, previous_hash, current_hash):
        self.key = key
        self.data = data
        self.previous_hash = previous_hash
        self.current_hash = current_hash

    def read_key(self):
        return self.key

    def read_data(self):
        return self.data


