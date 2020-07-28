from time import time
import hashlib
import json
from uuid import uuid4
from flask import Flask, jsonify


class Blockchain:
    def __init__(self):
        self.chain = []
        self.currentTransactions = []

        self.newBlock(proof=100, previousHash=1)  # The genesis (first) block

    def newBlock(self, proof, previousHash=None):
        """
        Create a new block in this blockchain.

        :param int proof: The proof given by the proof of work algorithm.
        :param str previousHash: The hash of the previous block.
        :return dict: a new block.
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.currentTransactions,
            'proof': proof,
            'previousHash': previousHash or self.hash(self.lastBlock)
        }

        self.currentTransactions = []  # reset the list of current transactions
        self.chain.append(block)
        return block

    def newTransaction(self, sender, receipt, amount):
        """
        Create a new transaction and add it to the next mined block.

        :param str sender: Address of the sender.
        :param str receipt: Address of the receipt.
        :param amount: The amount for this transaction.
        :return int: The index of the block that will hold this transaction.
        """
        transaction = {
            'sender': sender,
            'receipt': receipt,
            'amount': amount
        }

        self.currentTransactions.append(transaction)
        return self.lastBlock['index'] + 1

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of a block.

        :param dict block: The block to hash.
        :return str: The SHA-256 hash of the given block.
        """
        blockString = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(blockString).hexdigest()

    @property
    def lastBlock(self):
        # return the last block in the chain
        return self.chain[-1]

    def newTransaction(self, sender, recipient, amount):
        """
        Create a new transaction, which will go into the next mined block.

        :param str sender: Address of the sender.
        :param str recipient: Address of the recipient.
        :param str amount: The amount for this transaction.
        :return int: The index of the block that will hold this transaction.
        """
        self.currentTransactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.lastBlock['index'] + 1

    def proofOfWork(self, lastProof):
        """
        Proof of work algorithm is as follows:
            - Find a number p' such that hash(pp') contains 4 leading zeros, where p is the previous p'
            - p is the previous proof, p' is the new proof

        :param lastProof: The previous proof.
        :return int: The number that satisfies the proof of work algorithm.
        """
        proof = 0
        while not self.validProof(lastProof, proof):
            proof += 1

        return proof

    @staticmethod
    def validProof(lastProof, proof):
        """
        Determines whether or not the proof is valid.

        :param int lastProof: The previous proof.
        :param int proof: The current proof.
        :return boolean: True if proof is correct, False otherwise
        """
        guess = f'{lastProof, proof}'.encode()
        guessHash = hashlib.sha256(guess).hexdigest()

        return guessHash[:4] == '0000'


app = Flask(__name__)
nodeID = str(uuid4()).replace('-', '')
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    return 'Make a new block'


@app.route('/transactions/new', methods=['POST'])
def newTransaction():
    return 'Add a new transaction'


@app.route('/chain', methods=['GET'])
def chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
