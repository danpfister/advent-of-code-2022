import numpy as np
import re

inputfile = open(r".\input\10.txt", "r")
inputdata = np.asarray([line.strip() for line in inputfile])

############################## PART 1 ##############################

class Cpu():
    def __init__(self, interesting_signals: list) -> None:
        self.interesting_signals = interesting_signals
        self.register_value = 1
        self.cycle = 0
        self.interesting_signals_strengths = 0
    
    def __repr__(self) -> str:
        return f"end of cycle {self.cycle} with register value {self.register_value}"
    
    def next_cycle(self, value: int):
        self.cycle += 1
        self.register_value += value
        if self.cycle in self.interesting_signals:
            self.interesting_signals_strengths += (self.cycle + 1) * self.register_value

interesting_signals = [19, 59, 99, 139, 179, 219] # after the cycle before is equal to during the next cycle
cpu = Cpu(interesting_signals)
for instruction in inputdata:
    if instruction == "noop":
        cpu.next_cycle(0)
        continue
    match = re.match(re.compile(r"addx (-*\d+)"), instruction)
    cpu.next_cycle(0)
    cpu.next_cycle(int(match.group(1)))
print(f"the sum of the interesting signal strengths is {cpu.interesting_signals_strengths}")