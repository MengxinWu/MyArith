# You pass an array in, and it gets converted to a set.

import pdb
import collections

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = collections.OrderedDict()

stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = []

# pdb.set_trace()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.append(best_station)

print(final_stations)