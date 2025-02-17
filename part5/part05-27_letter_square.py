def generate_layers(layers):
    # Matrix size (always a square with side length 2*layers - 1)
    size = 2 * layers - 1  
 
    # Creating an empty matrix (filled with spaces)
    matrix = []
    for i in range(size):
        row = [" "] * size  # Create an empty row
        matrix.append(row)  # Add this row to the matrix
 
    # Filling the matrix with letters, layer by layer
    for camada in range(layers):
        letra = chr(65 + (layers - 1 - camada))  # Finds the correct letter
        inicio = camada  # Starting position of the layer
        fim = size - camada - 1  # Ending position of the layer
 
        # Fill the borders of the layer with the corresponding letter
        for i in range(inicio, fim + 1):
            matrix[inicio][i] = letra  # Top row
            matrix[fim][i] = letra  # Bottom row
            matrix[i][inicio] = letra  # Left column
            matrix[i][fim] = letra  # Right column
 
    # Printing the matrix
    for linha in matrix:
        for caractere in linha:
            print(caractere, end="")  # Prints each letter without space
        print()  # Moves to the next line
 
layers = int(input("Layers: "))
 
# Validating the input to ensure it is between 1 and 26
if 1 <= layers <= 26:
    generate_layers(layers)
else:
    print("Invalid number of layers! Please enter a value between 1 and 26.")
 