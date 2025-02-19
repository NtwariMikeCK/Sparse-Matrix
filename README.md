# Sparse Matrix Operations Project

## Overview
This project is a Python-based application to handle sparse matrices efficiently. Sparse matrices are data structures where most of the elements are zeros. By only storing non-zero values, this project ensures memory and computational efficiency. The application supports essential matrix operations such as addition, subtraction, and multiplication.

## Features
- **Matrix Representation**: Uses a dictionary to store non-zero elements in the form `{(row, col): value}`.
- **File Input**: Loads matrix data from a formatted text file.
- **Matrix Operations**:
  - **Addition**: Adds two sparse matrices.
  - **Subtraction**: Subtracts one sparse matrix from another.
  - **Multiplication**: Multiplies two sparse matrices.
- **Interactive CLI**: Users can perform operations by specifying input files.

## Installation

### Prerequisites
- Python 3.6 or higher

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/NtwariMikeCK/Sparse-Matrix
   cd sparse-matrix-operations
   ```
2. Run the program:
   ```bash
   python sparse_matrix.py
   ```

## Usage
1. Prepare input files containing the sparse matrix data. The file format should be:
   ```
   rows=<number_of_rows>
   cols=<number_of_columns>
   (row, col, value)
   (row, col, value)
   ```
   Example:
   ```
   rows=3
   cols=3
   (0, 1, 5)
   (1, 2, 8)
   ```

2. Run the program and follow the prompts:
   ```bash
   python sparse_matrix.py
   ```
   - Enter the operation (1 for addition, 2 for subtraction, 3 for multiplication).
   - Provide the file paths for the matrices.

3. View the result printed in the console.

## Example
### Input Files
**Matrix 1 (`matrix1.txt`)**:
```
rows=2
cols=2
(0, 0, 1)
(1, 1, 3)
```
**Matrix 2 (`matrix2.txt`)**:
```
rows=2
cols=2
(0, 0, 4)
(1, 1, 6)
```

### Operation
Choose addition (1):
```bash
Enter your choice: 1
Enter the path for the first matrix file: matrix1.txt
Enter the path for the second matrix file: matrix2.txt
```

### Output
```
SparseMatrix(2x2):
(0, 0, 5)
(1, 1, 9)
```

## Code Structure
- **`SparseMatrix` Class**:
  - `__init__`: Initializes a sparse matrix, either from a file or with given dimensions.
  - `load_data`: Reads and processes matrix data from a file.
  - `get_element`: Retrieves the value at a specified position.
  - `set_element`: Sets or removes a non-zero value at a specified position.
  - `add`: Adds two sparse matrices.
  - `subtract`: Subtracts one sparse matrix from another.
  - `multiply`: Multiplies two sparse matrices.
  - `__str__`: Formats the matrix for easy visualization.
- **Main Program**: Provides an interactive CLI for matrix operations.

## Contribution
We welcome contributions! Follow these steps:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.
   
