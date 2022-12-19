import numpy as np
import re

class Valve:
    def __init__(self, name: str, flow_rate: int, tunnels: list) -> None:
        self.name = name
        self.flow_rate = int(flow_rate)
        self.tunnels = tunnels
        self.open = False
        
    def __repr__(self) -> str:
        return f"valve {self.name} with flow rate {self.flow_rate}"

def parse_input(inputdata: list):
    valves = list()
    for line in inputdata:
        match_all = re.match(re.compile(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)'), line)
        match_tunnels = re.findall(re.compile(r'(\w+)'), match_all.group(3))
        valves.append(Valve(match_all.group(1), match_all.group(2), match_tunnels))
    for valve in valves:
        connections_name = valve.tunnels
        valve.tunnels = list()
        for connection_name in connections_name:
            valve.tunnels.append(next(connected for connected in valves if connected.name == connection_name))
    return valves

def release_pressure(current_valve: Valve, time_left: int, pressure_released: int):
    print(time_left)
    if time_left == 0:
        return pressure_released
    # options are: if valve is not open: open or continue to different valve, if valve is open: continue to different valve
    if not current_valve.open:
        if time_left*current_valve.flow_rate > max([release_pressure(valve, time_left-1, pressure_released) for valve in current_valve.tunnels]):
            current_valve.open = True
            return pressure_released+time_left*current_valve.flow_rate
    pressure_released += max([release_pressure(valve, time_left-1, pressure_released) for valve in current_valve.tunnels])
    return pressure_released
    

if __name__ == "__main__":
    inputfile = open(r".\input\16_test.txt", 'r')
    inputdata = np.asarray([line.strip() for line in inputfile])
    valves = parse_input(inputdata)
    print(release_pressure(valves[0], 30, 0))