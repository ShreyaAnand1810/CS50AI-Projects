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
    Or(AKnight, AKnave), 
    Not(And(AKnight, AKnave)),
    Implication(AKnight, And(AKnight, AKnave))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),  
    Or(BKnight, BKnave),  
    Not(And(AKnight, AKnave)),  
    Not(And(BKnight, BKnave)),  
    Implication(AKnight, And(AKnave, BKnave)),  
    Implication(AKnave, Not(And(AKnave, BKnave)))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),            # A is either a knight or a knave
    Or(BKnight, BKnave),            # B is either a knight or a knave
    Not(And(AKnight, AKnave)),      # A cannot be both
    Not(And(BKnight, BKnave)),      # B cannot be both
    Implication(AKnight, Biconditional(AKnight, BKnight)),  # A's statement is true if A is a knight
    Implication(AKnave, Not(Biconditional(AKnight, BKnight))),  # A's statement is false if A is a knave
    Implication(BKnight, Biconditional(AKnight, Not(BKnight))),  # B's statement is true if B is a knight
    Implication(BKnave, Not(Biconditional(AKnight, Not(BKnight))))  # B's statement is false if B is a knave
)


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),
    Biconditional(BKnight, And(Biconditional(AKnight, AKnave), CKnave)),  # If B is a knight, their claims are true
    Implication(CKnight, AKnight),  # If C is a knight, their claim is true
    Implication(BKnave, Not(CKnave))  # If B is lying, their claim about C is false
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
