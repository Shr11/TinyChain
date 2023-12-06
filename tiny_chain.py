import hashlib as hasher
import datetime as date

class Block:
    def __init__(self, index , timestamp , data, previous_hash): # self is used to update the state of  instance of Block
        self.index = index                 # self.property for self(instance) = parameter name
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = hash_block()
        
    def hash_block(self): # self is used to read the state of instance of class Block
        sha = hasher.sha256() 
        sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash))
        return sha.hexdigest()
    
def create_genesis_block(): # first block with arbitrary data & previous_hash values
        # manually constructing & adding a block to chain
        # with index 0 & arbitrary provous_hash
        return Block(0,date.datetime.now() , "Genesis Block", 0)
    
def next_block(last_block):
        this_index = last_block.index + 1
        this_timestamp = date.datetime.now() 
        this_data = "Hey! I'm block " + str(this_index)
        this_hash = last_block.hash
        return Block(this_index , this_timestamp, this_data , this_hash )
    
# Now to create the blockchain or python list with 1st element as the genesis block

blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# how many blocks to add to the chain after genesis block
no_of_blocks_to_add = 20

# adding those blocks to the chain
for i in range(0, no_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        # announce
        print("Block #{} has been adde to the tinychain!".format(block_to_add.index(previous_block)))
        print("Hash: {}\n".format(block_to_add.hash))
    