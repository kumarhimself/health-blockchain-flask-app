import hashlib
from block import Block

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        genesis_last_hash = generate_hash("Genesis Block - Hash Last")
        genesis_hash = generate_hash("Genesis Block - Current Hash")

        genesis = Block("0", "genesis", genesis_hash, genesis_last_hash)
        self.chain = [genesis]

    def append_block(self, search_key, data):
        previous_hash = self.chain[-1].current_hash
        current_hash = generate_hash(data)

        self.chain.append(Block(search_key, data, previous_hash, current_hash))

    def search(self, search_key):
        for i in range(len(self.chain)):
            if (self.chain[i].read_key() == search_key):
                return self.chain[i].read_data()

        return None

    def __str__(self):
        return ", ".join([self.chain[i].read_data() for i in range(len(self.chain))])
