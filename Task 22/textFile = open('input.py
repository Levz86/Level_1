with open('input.txt', 'r') as file:
    with open('output.txt', 'w') as outfile:
        for line in file:
            # Remove newline character from the line
            line = line.strip()

            # Skip the first line of the input file
            if line.startswith('Sum:'):
                continue

            # Split the line into the operation and the list of numbers
            operation, numbers = line.split(':')
            numbers = list(map(int, numbers.split(',')))

            # Perform the operation on the list of numbers
            if operation == 'Min':
                result = min(numbers)
            elif operation == 'Max':
                result = max(numbers)
            elif operation == 'Avg':
                result = sum(numbers) / len(numbers)

            # Write the result to the output file
            outfile.write(f"The {operation.lower()} of {numbers} is {result}\n")