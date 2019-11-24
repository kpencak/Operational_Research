class Game:
    def __init__(self, player1, player2, previous, stacks1, stacks2, coins, turn, nextTurn):
        self.player1 = player1
        self.player2 = player2
        self.previous = previous
        self.stacks1 = stacks1
        self.stacks2 = stacks2
        self.coins = coins
        self.turn = turn
        self.nextTurn = nextTurn

    def __repr__(self):
        return "Player 1 {0}, Player 2 {1}".format(self.player1, self.player2)

    def nextTurn(self):
        if self.turn == "Player 1":
            return "Player 2"
        return "Player 1"


def coinsChoices(self, stack):
    result = []
    if self.coins[stack] == 0:
        return result

    if self.previous == 0 and self.coins[stack] >= 1:
        result.append(1)
        return result

    coinsToTake = 1
    while coinsToTake <= self.coins[stack] and coinsToTake <= self.previous * 2:
        result.append(coinsToTake)
        coinsToTake += 1

    return result


def subtrees(self):
    result = []
    numberOfStacks = self.coins.len()
    currentState = self.turn
    nextMove = self.nextTurn

    if currentState == "Player 1":
        possibleMoves = self.stacks1
    else:
        possibleMoves = self.stacks2

    isMoveMade = False
    for i in range(0, numberOfStacks):
        if possibleMoves[i] == True:
            continue

        possibleCoinChoices = self.coinsChoices[i]

        for coinsValue in possibleCoinChoices:
            newStack1 = self.stacks1.copy()
            newStack2 = self.stacks2.copy()
            newCoins = self.coins.copy()

            newCoins[i] -= coinsValue
            newPlayer1 = self.player1
            newPlayer2 = self.player2
            isMoveMade = True

            if currentState == "Player 1":
                newStack1[i] = True
                newPlayer1 += coinsValue
            else:
                newStack2[i] = True
                newPlayer2 += coinsValue

            result.append(Game(newPlayer1, newPlayer2, coinsValue, newStack1, newStack2, newCoins, nextMove, self))

    if not isMoveMade:
        gameOver = True
        for i in range(0, numberOfStacks):
            if self.coins != 0 and (self.stacks1[i] == False or self.stacks2[i] == False):
                gameOver = False
                break

        if not gameOver:
            result.append(Game(self.player1, self.player2, self.coins, newStack1, newStack2, newCoins))

    def makeTree(self):
        self.subtrees()
        for game in self.next:
            game.makeTree()


def minimaxTree(tree: Game):
    if tree.next == 0:
        return tree

    choices = []
    for move in tree.next:
        choices = choices + [minimaxTree(move)]

    if tree.turn == "Player 1":
        result = max(choices, key=score)
    else:
        result = min(choices, key=score)

    return result


def score(item):
    return item.player1 - item.player2


def treeString(tree: Game, level):
    string = ""
    for i in range(0, level):
        string = string + " "

    string = string + str(tree) + "\n"
    for subtree in tree.next:
        string = treeString(subtree, level + 1)

    return string


coins = []
stack1 = []
stack2 = []
for i in range(len(coins)):
    stack1.append(False)
    stack2.append(False)


