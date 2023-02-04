import instructions

inst = instructions


class User_interactions:

    def __init__(self):
        self.data = []
        self.player_count = 0
        self.player_names = []
        self.testing = True
        self.dice_on_table = [1, 2, 3, 4, 5]
        self.roll_count = 0
        self.numb = 0

    def testing_or_playing(self):
        user_response = input('''
        Hello, Welcome to Yahtzee.
        Type Start to play or Help for instruction.
        ''')
        if 'Start' != user_response:
            print(inst.full_instructions)
            self.testing_or_playing()
        else:
            print('''
        Welcome to the game!''', end="")
            self.testing = False

    def ask_player_what_to_keep(self):
        print('which dice do you want to keep?')
        print('enter the dice number or numbers to keep')
        print('just press enter to reroll all dice.')
        if self.testing:
            print('This code needs to be completed still.')
        else:
            user_selection = input('which dice do you want to keep?')

    def ask_player_count(self):
        if self.testing:
            player_count = 3
        else:
            player_count = input('''
        How many players would you like?''')

        self.player_count = int(player_count)
        if 0 >= self.player_count:
            print('''
        You don\'t want to play.''')
        elif 1 == self.player_count:
            print('''
        You want one player ''')
        elif 2 <= self.player_count:
            print(f'''
        You want {self.player_count} players.''')

    def get_player_count(self):
        return self.player_count

    def ask_player_names(self):

        if self.testing:
            self.player_names.append('bob')
            self.player_names.append('susan')
            self.player_names.append('link')
        else:
            for item in range(self.numb, self.player_count):
                name = input(f'''
        Player {self.numb + 1}, please enter your name: ''')
                if "" == name:
                    print('''
        Invalid Entry. Please try again.''')
                    self.ask_player_names()

                else:
                    self.player_names.append(name)
                    self.numb += 1

        print(f'''
        for this game, we have the following players:
        {self.player_names}
        ''')

    def get_player_name(self, player_number):
        return self.player_names[player_number]

    def roll_new_five(self):
        import random
        self.roll_count = 1
        print('New roll.')
        for die in range(0, len(self.dice_on_table)):
            self.dice_on_table[die] = random.randint(1, 6)
        print('here are the dice on the table.')
        print('\nDICE NUMBER: \t1\t2\t3\t4\t5')
        print('DICE VALUE:', end='')
        for die in self.dice_on_table:
            print(f'\t{die}', end='')
        print()
