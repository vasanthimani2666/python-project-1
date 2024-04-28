import random

def roll_dice(num_dice, num_sides):
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    return rolls, sum(rolls)

def main():
    num_dice = int(input("Enter the number of dice: "))
    num_sides = int(input("Enter the number of sides per die: "))
    
    rolls, total = roll_dice(num_dice, num_sides)
    print("Results of each roll:", rolls)
    print("Total sum of all dice:", total)
    
    reroll = input("Do you want to reroll any dice? (yes/no): ").lower()
    if reroll == "yes":
        dice_to_reroll = list(map(int, input("Enter the indices of the dice to reroll (space-separated): ").split()))
        for idx in dice_to_reroll:
            if idx < 1 or idx > num_dice:
                print("Invalid dice index.")
                return
            rolls[idx-1] = random.randint(1, num_sides)
        print("Results after reroll:", rolls)
        print("Total sum after reroll:", sum(rolls))
if __name__ == "__main__":
    main()

