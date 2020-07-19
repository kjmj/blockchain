class Blockchain:
    def __init__(self):
        self.chain = []
        self.currentTransactions = []

    def newBlock(self):
        # creates a new block and adds it to the chain
        pass

    def newTransaction(self):
        # creates a new transaction and adds it to the list of transactions
        pass

    @staticmethod
    def hash(block):
        # hashes a block
        pass

    @property
    def lastBlock(self):
        # return the last block in the chain
        pass

    def newTransaction(self, sender, recipient, amount):
        """
        create a new transaction, which will go into the next mined block

        :param str sender: address of the sender
        :param str recipient: address of the recipient
        :param str amount: the amount for this transaction
        :return int: the index of the block that will hold this transaction
        """
        self.currentTransactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

        return self.lastBlock['index'] + 1
