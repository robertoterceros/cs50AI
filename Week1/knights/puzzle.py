from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    #And(AKnight, AKnave), # A says "I am both a knight and a knave."
    Not(And(AKnight, AKnave)), # A cannot be a knight and knave at the same time
    Not(And(BKnave, BKnight)), # B cannot be a knight and knave at the same time
    Or(AKnight, AKnave), # A has to be a knight or a knave
    Or(BKnight, BKnave), # The same for b
    Or(Not(AKnight), And(AKnight, AKnave)) # if A is a Knight then the first sentence is truth 
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # And(AKnave, BKnave),       # A says "We are both knaves"
    Not(And(AKnight, AKnave)), # A cannot be a knight and knave at the same time
    Not(And(BKnave, BKnight)), # B cannot be a knight and knave at the same time
    Or(AKnight, AKnave), # A has to be a knight or a knave
    Or(BKnight, BKnave), # The same for b
    Implication(AKnight, And(AKnave, BKnave)), # A says "We are both knaves" is truth is A is knight
    Implication(AKnave, Not(And(AKnave, BKnave))) 
        # TOD
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # Or(And(AKnave, BKnave), And(AKnight, BKnight)), # A says "We are the same kind."
    # Or(And(AKnight, BKnave), And(AKnave, BKnight)), # We are of different kinds
    Not(And(AKnight, AKnave)), # A cannot be a knight and knave at the same time
    Not(And(BKnave, BKnight)), # B cannot be a knight and knave at the same time
    Or(AKnight, AKnave), # A has to be a knight or a knave
    Or(BKnight, BKnave), # The same for b
    Implication(AKnight, Or(And(AKnave, BKnave), And(AKnight, BKnight))), # If A is not a Knight then the first truth
    Implication(AKnave, Not(Or(And(AKnave, BKnave), And(AKnight, BKnight)))),
    Implication(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight))), # B is not a knight or the second is truth
    Implication(BKnave, Not(Or(And(AKnight, BKnave), And(AKnave, BKnight))))



    # TODO
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    
    # B says "A said 'I am a knave'."
    #Implication(BKnight, 'I am a knave'),

    # B says "C is a knave"
    Implication(BKnight, CKnave),
    Implication(BKnave, CKnight),

    # C says "A is a knight"
    Implication(CKnight, AKnight),
    Implication(CKnave, AKnave),

    Not(And(AKnight, AKnave)), # A cannot be a knight and knave at the same time
    Not(And(BKnave, BKnight)), # B cannot be a knight and knave at the same time
    Not(And(CKnave, CKnight)), # C cannot be a knight and knave at the same time
    Or(AKnight, AKnave), # A has to be a knight or a knave
    Or(BKnight, BKnave), # The same for b
    Or(CKnight, CKnave), # The same for c

    # TODO
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
