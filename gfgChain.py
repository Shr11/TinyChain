# importing lib for features of a block in blockchain

# timestamp
import datetime 

# to calculate hash to add digital signature of a block
import hashlib

# to store data in a block
import json

# Flask->webapp & jsonify->display the blockchain
from flask import Flask,jsonify

class Blockchain:
    
    # func to create first block & set it's hash to 0
    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0') # default values 
        
    # func to add further blocks to the chain
    def create_block(self, proof , previous_hash):
        block = {'index':len(self.chain) + 1,
                 'timestamp':str(datetime.datetime.now()),
                 'proof':proof,
                 'previous_hash':previous_hash
                 }
        self.chain.append(block)
        return block
    
    