
def parse_request(text):
    if not isinstance(text, str):
        raise ValueError("Request must be a string.")

    parts = text.split("->")

    if len(parts) != 2:
        raise ValueError("Request must follow FROM->TO format.")

    try:
        start = int(parts[0].strip())
        end = int(parts[1].strip())
    except ValueError:
        raise ValueError("Floor numbers must be integers.")

    return start, end


def total_travel(floors_csv):
    if not isinstance(floors_csv, str) or not floors_csv.strip():
        raise ValueError("Floor list cannot be empty.")

    try:
        floors = [int(f.strip()) for f in floors_csv.split(",")]
    except ValueError:
        raise ValueError("All floors must be valid integers.")

    return sum(
        abs(floors[i + 1] - floors[i])
        for i in range(len(floors) - 1)
    )


def load_percent(text):
    if not isinstance(text, str):
        raise ValueError("Load input must be a string.")

    parts = text.split("of")

    if len(parts) != 2:
        raise ValueError("Load must follow X of Y format.")

    try:
        load = int(parts[0].strip())
        capacity = int(parts[1].strip())
    except ValueError:
        raise ValueError("Load and capacity must be integers.")

    if load < 0:
        raise ValueError("Load cannot be negative.")

    if capacity <= 0:
        raise ValueError("Capacity must be greater than zero.")

    return load * 100 // capacity


def main():
    try:
        print("==== Running parse_request ====")
        user_input = input("Enter a request as FROM->TO (e.g. 5->9): ")
        result = parse_request(user_input)
        print("From and To:", result)

        print("\n==== Running total_travel ====")
        user_input = input("Enter floors visited as CSV (e.g. 1,5,3,9): ")
        result = total_travel(user_input)
        print("Floors Travelled:", result)

        print("\n==== Running load_percent ====")
        user_input = input("Enter load as 'X of Y' (e.g. 450 of 630): ")
        result = load_percent(user_input)
        print("Load Percent:", result)

    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
