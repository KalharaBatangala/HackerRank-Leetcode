def catAndMouse(x, y, z):
    dist_A = abs(x - z)  # distance from cat A to mouse
    dist_B = abs(y - z)  # distance from cat B to mouse
    
    if dist_A == dist_B:
        return "Mouse C"
    elif dist_A < dist_B:
        return "Cat A"
    else:
        return "Cat B"


if __name__ == "__main__":
    q = int(input("Enter number of queries: "))

    for _ in range(q):
        x, y, z = map(int, input("Enter positions (catA catB mouse): ").split())
        result = catAndMouse(x, y, z)
        print(result)
