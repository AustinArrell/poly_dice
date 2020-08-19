import random


class Die:

    def __init__(self,num_sides):
        self.num_sides = num_sides

    def roll(self,num_rolls):
        result_list = []
        sum = 0

        for increment in range(num_rolls):
            result = random.randint(1,self.num_sides)
            result_list.append(result)
            sum += result

        print("D"+str(self.num_sides)+":"+str(result_list))
        return(sum)


def init_dice():
    dice_dict = {}
    dice_dict["d100"] = Die(100)
    dice_dict["d20"] = Die(20)
    dice_dict["d12"] = Die(12)
    dice_dict["d8"] = Die(8)
    dice_dict["d6"] = Die(6)
    dice_dict["d4"] = Die(4)
    return dice_dict


def parse_input(input_str):
    print(input_str)
    pass


def main_loop():
    command = ""
    while command.upper() != "QUIT":
        command = input("Enter dice roll in this format (1d20+1d4+5). Type quit to quit:")
        parse_input(command)




dice = init_dice()
main_loop()
