# SER 101 Programming Assignment: "Sailboat Suitability Calculator" v3.0
# Made by Joseph Krause

print("\nWelcome to Joe's Sailboat Suitability Calculator!\n")


def fun(x):
    while True:
        attempt = raw_input(x)

        # make sure input is a float
        try:
            float(attempt)
        except ValueError:
            print("Please enter a number: ")
            continue

        # make sure input is positive
        if not float(attempt) > 0:
            print("Please enter a positive, non-zero number: ")
            continue

        return float(attempt)

# input
loa = fun('Input total length of the vessel: ')
lwl = fun('Input total waterline length of the vessel: ')
beam = fun('Input total width of the vessel: ')
displacement = fun('Input total displacement (lbs) of the vessel: ')
sailArea = fun('Input total sail area of the vessel: ')
print('')

# calculation
hullSpeed = 1.34 * lwl ** 0.5
displacementLength = (displacement / 2240.0) / (0.01 * lwl) ** 3.0
sailAreaDisplacement = sailArea / (displacement / 64.0) ** 0.67
capsizeIndex = beam / (displacement / 64.0) ** 0.33
comfortIndex = displacement / (0.65 * (0.7 * lwl + 0.3 * loa) * beam ** 1.33)

# output
print('LOA: ' + str(loa))
print('LWL: ' + str(lwl))
print('Beam: ' + str(beam))
print('Displacement: ' + str(displacement))
print('Sail Area: ' + str(sailArea))
print('')
print('Hull Speed: ' + str(hullSpeed))
print('D/L: ' + str(displacementLength))
print('SA/D: ' + str(sailAreaDisplacement))
print('Capsize Index: ' + str(capsizeIndex))
print('Comfort Index: ' + str(comfortIndex))
print('')

raw_input('Press enter to exit... ')
