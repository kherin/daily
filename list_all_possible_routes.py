port_names = ["PAN", "AMS", "CAS", "NYC", "HEL"]


def permutations(route, ports):
    # Write your recursive code here

    # Print the port names in route when the recursion terminates
    print(' '.join([port_names[i] for i in route]))


# This will start the recursion with 0 ("PAN") as the first stop
permutations([0], list(range(1, len(port_names))))
