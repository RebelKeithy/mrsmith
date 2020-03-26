import random
import constants
import importlib.resources

class NameList:
    def __init__(self, filename=None):
        self.names = []
        self.totals = []
        if filename is not None:
            self.load(filename)

    def load(self, filename):
        self.names = []
        self.totals = [0, 0, 0, 0, 0, 0, 0]
        with importlib.resources.open_text('mrsmith', filename) as f:
            f.readline()
            for line in f:
                name = line.strip().split(',')
                entry = [name[0].capitalize(), int(name[1])] + [int(int(name[1]) * (float(prob)/100)) for prob in name[2:]]
                self.names.append(entry)
                for i in range(0, 7):
                    self.totals[i] += entry[i+1]

    def random(self, race=constants.RACE_ALL):
        roll = random.randint(0, int(self.totals[race]))
        sum = 0
        for name in self.names:
            sum += name[1+race]
            if sum > roll:
                return name[0]