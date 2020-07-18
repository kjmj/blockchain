class Blockchain:
    def __init__(self):
        self.chain = []
        self.currentTransactions = []

    # creates a new block and adds it to the chain
    def newBlock(self):
        pass

    # creates a new transaction and adds it to the list of transactions
    def newTransaction(self):
        pass

    # hashes a block
    @staticmethod
    def hash(block):
        pass

    # return the last block in the chain
    @property
    def lastBlock(self):
        pass
