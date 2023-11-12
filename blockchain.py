import hashlib
from block import Block

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        genesis_last_hash = generate_hash("Genesis Block - Hash Last")
        genesis_hash = generate_hash("Genesis Block - Current Hash")

        genesis = Block("genesis", genesis_hash, genesis_last_hash)
        self.chain = [genesis]

    def append_block(self, data):
        previous_hash = self.chain[-1].current_hash
        current_hash = generate_hash(data)

        self.chain.append(Block(data, previous_hash, current_hash))
