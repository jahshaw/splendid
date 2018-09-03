from geopy.distance import distance


class Capital(object):
    def __init__(self, name, lat, long):
        self.name = name
        self.lat = lat
        self.long = long
        self.distance_to = {}
        self.sorted_dists = []

    def closest_in_set(self, capitals):
        """Given a set of other capitals (names), returns the closest and the distance"""
        for entry in self.sorted_dists:
            if entry[0] in capitals:
                return entry

    def closest_not_in_set(self, capitals):
        """Given a set of other capitals (names), returns the closest capital not in the set and the distance"""
        for entry in self.sorted_dists:
            if entry[0] not in capitals:
                return entry


# Use the following regexes to help generating this list when copy-pasting from Google Sheets:
# Find:  ([a-zA-Z ]*)\t([-0-9]*\.[0-9]*)\t([-0-9]*.[0-9]*)
# Replace with:  "$1": {'lat': $2, 'long': $3},
# or:  Capital("$1", $2, $3),

ALL_CAPS = [
Capital("Kabul", 34.5553, 69.2075),
Capital("Tirana", 41.3275, 19.8187),
Capital("Algiers", 36.7538, 3.0588),
Capital("Andorra la Vella", 42.5063, 1.5218),
Capital("Luanda", -8.84, 13.2894)
]


def precompute_distances():

    for capital in ALL_CAPS:
        print("Pre-computing for " + capital.name)
        for tgt_cap in ALL_CAPS:
            if tgt_cap != capital:
                capital.distance_to[tgt_cap.name] = calc_distance(capital, tgt_cap)

        # Create a sorted list of capitals which can be indexed.
        def DistListFn(tuple):
            return tuple[1]

        capital.sorted_dists = sorted(capital.distance_to.items(), key=DistListFn)


def calc_distance(src, dst):
    """Calculate distance between two Capital objects"""
    return int(distance((src.lat, src.long), (dst.lat, dst.long)).kilometers)


def check_isolation(capitals):
    """Take a list of capital names and report on their isolation properties
    Returns bond distance, isolation distance, relative isolation, is_isolated"""

    # Get a list of actual Capital objects in this set
    test_set = [capital for capital in ALL_CAPS if capital.name in capitals]

    # Initialise
    bond_dist = 0
    isol_dist = 999999

    # Spin through each capital in the set
    for capital in test_set:

        # Calculate bond distance (closest set member) and update set if larger
        _, this_bond = capital.closest_in_set(capitals)
        bond_dist = max(bond_dist, this_bond)

        # Calculate isolation distance (closest set non-member) and update set if smaller
        _, this_isol = capital.closest_not_in_set(capitals)
        isol_dist = min(isol_dist, this_isol)

        # Recalculate relative isolation & isolation
        rel_isol = isol_dist / bond_dist
        if rel_isol > 1:
            is_isolated = True
        else:
            is_isolated = False

    return (bond_dist, isol_dist, rel_isol, is_isolated)


precompute_distances()
#print(ALL_CAPS[0].distance_to)
#print(ALL_CAPS[0].sorted_dists)
#print(check_isolation(["Kabul", "Algiers"]))