class Block:
    def __init__(self, data, previous_hash, current_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.current_hash = current_hash

    def read_data(self):
        return self.data


