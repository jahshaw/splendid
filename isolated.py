from geopy.distance import distance
from itertools import combinations


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


ALL_CAPS_TEST_SET = [
Capital("Kabul", 34.5553, 69.2075),
Capital("Tirana", 41.3275, 19.8187),
Capital("Algiers", 36.7538, 3.0588),
Capital("Andorra la Vella", 42.5063, 1.5218),
Capital("Luanda", -8.84, 13.2894)
]

ALL_CAPS_REAL_SET = [
Capital("Kabul", 34.5553, 69.2075),
Capital("Tirana", 41.3275, 19.8187),
Capital("Algiers", 36.7538, 3.0588),
Capital("Andorra la Vella", 42.5063, 1.5218),
Capital("Luanda", -8.84, 13.2894),
Capital("Saint Johns", 17.1274, -61.8468),
Capital("Buenos Aires", -34.6037, -58.3816),
Capital("Yerevan", 40.1792, 44.4991),
Capital("Canberra", -35.2809, 149.13),
Capital("Vienna", 48.2082, 16.3738),
Capital("Baku", 40.4093, 49.8671),
Capital("Nassau", 25.048, -77.3554),
Capital("Manama", 26.2285, 50.586),
Capital("Dhaka", 23.8103, 90.4125),
Capital("Bridgetown", 13.0969, -59.6145),
Capital("Minsk", 53.9045, 27.5615),
Capital("Brussels", 50.8503, 4.3517),
Capital("Belmopan", 17.251, -88.759),
Capital("PortoNovo", 6.4969, 2.6289),
Capital("Thimphu", 27.4728, 83.6393),
Capital("Sucre", -19.0196, -65.262),
Capital("La Paz", -16.4897, -68.1193),
Capital("Sarajevo", 43.8563, 18.4131),
Capital("Gaborone", -24.6282, 25.9231),
Capital("Brasilia", -15.8267, -47.9218),
Capital("Bandar Seri Begawan", 4.9031, 114.9398),
Capital("Sofia", 42.6977, 23.3219),
Capital("Ouagadougou", 12.3714, -1.5197),
Capital("Bujumbura", -3.3614, 29.3599),
Capital("Praia", 14.933, -23.5133),
Capital("Phnom Penh", 11.5564, 104.9282),
Capital("Yaounde", 3.848, 11.5021),
Capital("Ottawa", 45.4215, -75.6972),
Capital("Bangui", 4.3947, 18.5582),
Capital("NDjamena", 12.1348, 15.0557),
Capital("Santiago", -33.4489, -70.6693),
Capital("Beijing", 39.9042, 116.4074),
Capital("Bogota", 4.711, -74.0721),
Capital("Moroni", -11.7172, 43.2473),
Capital("Kinshasa", -4.4419, 15.2663),
Capital("Brazzaville", -4.2634, 15.2429),
Capital("San Jose", 37.3382, -121.8863),
Capital("Yamoussoukro", 6.8276, -5.2893),
Capital("Zagreb", 45.815, 15.9819),
Capital("Havana", 23.1136, -82.3666),
Capital("Nicosia", 35.1856, 33.3823),
Capital("Prague", 50.0755, 14.4378),
Capital("Copenhagen", 55.6761, 12.5683),
Capital("Djibouti", 11.5721, 43.1456),
Capital("Roseau", 15.3092, -61.3794),
Capital("Santo Domingo", 18.4861, -69.9312),
Capital("Quito", -0.1807, -78.4678),
Capital("Cairo", 30.0444, 31.2357),
Capital("San Salvador", 13.7942, -88.8965),
Capital("Malabo", 3.7504, 8.7371),
Capital("Oyala", 1.589, 10.8226),
Capital("Asmara", 15.3229, 38.9251),
Capital("Tallinn", 59.437, 24.7536),
Capital("Mbabane", -26.3054, 31.1367),
Capital("Lobamba", -26.4004, 31.1825),
Capital("Addis Ababa", 8.9806, 38.7578),
Capital("Suva", -18.1248, 178.4501),
Capital("Helsinki", 60.1699, 24.9384),
Capital("Paris", 48.8566, 2.3522),
Capital("Libreville", 0.4162, 9.4673),
Capital("Banjul", 13.4549, -16.579),
Capital("Tbilisi", 41.7151, 44.8271),
Capital("Berlin", 52.52, 13.405),
Capital("Accra", 5.6037, -0.187),
Capital("Athens", 37.9838, 23.7275),
Capital("Saint Georges", 12.0561, -61.7488),
Capital("Guatemala City", 14.6349, -90.5069),
Capital("Conakry", 9.6412, -13.5784),
Capital("Bissau", 11.8817, -15.6178),
Capital("Georgetown", 6.8013, -58.1551),
Capital("PortauPrince", 18.5944, -72.3074),
Capital("Tegucigalpa", 14.0723, -87.1921),
Capital("Budapest", 47.4979, 19.0402),
Capital("Reykjavik", 64.1265, -21.8174),
Capital("New Delhi", 28.6139, 77.209),
Capital("Jakarta", -6.1751, 106.865),
Capital("Tehran", 35.6892, 51.389),
Capital("Baghdad", 33.3128, 44.3615),
Capital("Dublin", 53.3498, -6.2603),
Capital("Jerusalem", 31.7683, 35.2137),
Capital("Rome", 41.9028, 12.4964),
Capital("Kingston", 18.0179, -76.8099),
Capital("Tokyo", 35.6895, 139.6917),
Capital("Amman", 31.9454, 35.9284),
Capital("Astana", 51.1605, 71.4704),
Capital("Nairobi", -1.2921, 36.8219),
Capital("Tarawa", 1.4518, 172.9717),
Capital("Pristina", 42.667542, 21.166191),
Capital("Kuwait City", 29.3759, 47.9774),
Capital("Bishkek", 42.8746, 74.5698),
Capital("Vientiane", 17.9757, 102.6331),
Capital("Riga", 56.9496, 24.1052),
Capital("Beirut", 33.8938, 35.5018),
Capital("Maseru", -29.3151, 27.4869),
Capital("Monrovia", 6.2907, -10.7605),
Capital("Tripoli", 32.8872, 13.1913),
Capital("Vaduz", 47.141, 9.5209),
Capital("Vilnius", 54.6872, 25.2797),
Capital("Luxembourg", 49.6116, 6.1319),
Capital("Skopje", 41.9973, 21.428),
Capital("Antananarivo", -18.8792, 47.5079),
Capital("Lilongwe", -13.9626, 33.7741),
Capital("Kuala Lumpur", 3.139, 101.6869),
Capital("Male", 4.1755, 73.5093),
Capital("Bamako", 12.6392, -8.0029),
Capital("Valletta", 35.8989, 14.5146),
Capital("Majuro", 7.1164, 171.1858),
Capital("Nouakchott", 18.0735, -15.9582),
Capital("Port Louis", -20.1609, 57.5012),
Capital("Mexico City", 23.6345, -102.5528),
Capital("Palikir", 6.9147, 158.161),
Capital("Chisinau", 47.0105, 28.8638),
Capital("Monaco", 43.7384, 7.4246),
Capital("Ulaanbaatar", 47.8864, 106.9057),
Capital("Podgorica", 42.4304, 19.2594),
Capital("Rabat", 33.9716, -6.8498),
Capital("Maputo", -25.9692, 32.5732),
Capital("Naypyidaw", 19.7633, 96.0785),
Capital("Windhoek", -22.5609, 17.0658),
Capital("Yaren District", -0.5467, 166.9211),
Capital("Kathmandu", 27.7172, 85.324),
Capital("Amsterdam", 52.3702, 4.8952),
Capital("Wellington", -41.2865, 174.7762),
Capital("Managua", 12.1333, -86.25),
Capital("Niamey", 13.5167, 2.1167),
Capital("Abuja", 9.0833, 7.5333),
Capital("Pyongyang", 39.0167, 125.75),
Capital("Oslo", 59.9167, 10.75),
Capital("Muscat", 23.6167, 58.5833),
Capital("Islamabad", 33.6833, 73.05),
Capital("Ngerulmud", 7.5004, 134.6243),
Capital("East Jerusalem", 31.78336, 35.23388),
Capital("Panama City", 8.9667, -79.5333),
Capital("Port Moresby", -9.45, 147.1833),
Capital("Asuncion", -25.2667, -57.6667),
Capital("Lima", -12.05, -77.05),
Capital("Manila", 14.6, 120.9667),
Capital("Warsaw", 52.25, 21),
Capital("Lisbon", 38.7167, -9.1333),
Capital("Doha", 25.2833, 51.5333),
Capital("Bucharest", 44.4333, 26.1),
Capital("Moscow", 55.75, 37.6),
Capital("Kigali", -1.95, 30.05),
Capital("Basseterre", 17.3, -62.7167),
Capital("Castries", 14.0, -61.0),
Capital("Kingstown", 13.1333, -61.2167),
Capital("Apia", -13.8167, -171.7667),
Capital("San Marino", 43.9333, 12.4167),
Capital("Sao Tome", 0.3333, 6.7333),
Capital("Riyadh", 24.65, 46.7),
Capital("Dakar", 14.7333, -17.6333),
Capital("Belgrade", 44.8333, 20.5),
Capital("Victoria", -4.6167, 55.45),
Capital("Freetown", 8.483, -13.2333),
Capital("Singapore", 1.2833, 103.85),
Capital("Bratislava", 48.15, 17.1167),
Capital("Ljubljana", 46.05, 14.5167),
Capital("Honiara", -9.4333, 159.95),
Capital("Mogadishu", 2.0667, 45.3333),
Capital("Pretoria", -25.7, 28.2167),
Capital("Cape Town", -33.9249, 18.4241),
Capital("Bloemfontein", -29.08522, 26.1596),
Capital("Seoul", 37.55, 126.9833),
Capital("Juba", 4.85, 31.6167),
Capital("Madrid", 40.4, -3.6833),
Capital("Sri Jayawardenepura Kotte", 6.8868, 79.9187),
Capital("Khartoum", 15.6, 32.5333),
Capital("Paramaribo", 5.8333, -55.1667),
Capital("Stockholm", 59.3333, 18.05),
Capital("Bern", 46.9167, 7.4667),
Capital("Damascus", 33.5, 36.3),
Capital("Taipei", 25.0333, 121.5167),
Capital("Dushanbe", 38.55, 68.7667),
Capital("Dodoma", -6.163, 35.7516),
Capital("Bangkok", 13.75, 100.5167),
Capital("Dili", -8.5833, 125.6),
Capital("Lome", 6.1167, 0.12167),
Capital("Nukualofa", -21.1333, -175.2),
Capital("Port of Spain", 10.65, -61.5167),
Capital("Tunis", 36.8, 10.1833),
Capital("Ankara", 39.9333, 32.8667),
Capital("Askabat", 37.95, 58.3833),
Capital("Funafuti", -8.5167, 179.2167),
Capital("Kampala", 0.3167, 32.55),
Capital("Kyiv", 50.4333, 30.5167),
Capital("Abu Dhabi", 24.4667, 54.3667),
Capital("London", 51.5, -0.0833),
Capital("Washington DC", 38.8833, -77),
Capital("Montevideo", -34.85, -56.1667),
Capital("Tashkent", 41.3167, 69.25),
Capital("Port Vila", -17.7333, 168.3167),
Capital("Vatican City", 41.9, 12.45),
Capital("Caracas", 10.4806, -66.9036),
Capital("Hanoi", 21.0278, 105.8342),
Capital("Sanaa", 15.3694, 44.191),
Capital("Lusaka", 15.3872, 28.3228),
Capital("Harare", 17.8252, 31.0335)
]

# Use this to switch to a simple test set when debugging.
# ALL_CAPS = ALL_CAPS_TEST_SET
ALL_CAPS = ALL_CAPS_REAL_SET


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


def brute_force(cardinality):
    """Attempt to brute-force all combinations of capitals for a given cardinality and report the best."""

    # Get an iterator with all the possible combinations of capitals.
    iterator = combinations(ALL_CAPS, cardinality)
    best_isol = 0
    best_rel = 0

    for combo in iterator:
        # Grab the next combination and test it.
        test_set = list(map(lambda cap: cap.name, combo))
        _, isol_dist, rel_isol, is_isolated = check_isolation(test_set)

        # Assuming it's isolated, update params
        if is_isolated:
            if isol_dist > best_isol:
                best_isol = isol_dist
                best_isol_set = test_set
            if rel_isol > best_rel:
                best_rel = rel_isol
                best_rel_set = test_set

    print("Results for cardinality " + str(cardinality))
    print("Best absolute isolation set " + str(best_isol_set) + " with dist " + str(best_isol) + "km")
    print("Best relative isolation set " + str(best_rel_set) + " with " + str(best_rel))


precompute_distances()
brute_force(2)
#print(ALL_CAPS[0].distance_to)
#print(ALL_CAPS[0].sorted_dists)
#print(check_isolation(["Kabul", "Algiers"]))