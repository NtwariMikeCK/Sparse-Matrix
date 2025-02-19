class SparseMatrix:
  def __init__(self, file_path=None, rows=0, cols=0):
    # Innitialize all the variables to be used 
    self.file_path = file_path #The file to read
    self.num_rows = rows
    self.num_cols = cols
    self.elements = {} # Dictionary to store non-zero values as {(row, col): value}
    if file_path:
      # If the file exists, load all the data using load_data function
      self.load_data(file_path)


  def load_data(self, file_path):
    # function to load or read the data in files
    try:
      with open(file_path, 'r') as f:
        data = f.readlines()

      # Process rows and columns which are found on row1 and row2
      self.num_rows = int(data[0].split('=')[1].strip())
      self.num_cols = int(data[1].split('=')[1].strip())

      # Lets process the remaining data points from row3 downwards
      for item in data[2:]:
        item = item.strip()
        if not item:
          continue
        # check if data is in the correct format ex: (row, col, value)
        if not (item.startswith('(') and item.endswith(')')):
          raise ValueError('Input file has wrong format')
        
        # if data in correct format, then separate into row, col, value 
        # then make a dict (row, col) = value
        row, col, value = map(int, item[1:-1].split(','))
        self.elements[(row, col)] = value

    except Exception as e:
      raise ValueError(f"Error reading file: {e}")
    

  def get_element(self, row, col):
    # get the value at (row and col), default = 0
    return self.elements.get((row, col), 0)
  
  def set_element(self, row, col, value):
    # updates the value of an element in the sparse matrix 
    # at the specified row and column (row, col
    if value != 0:
      # check if the value is a non zero, then add or update
      self.elements[(row, col)] = value
    elif (row, col) in self.elements:
      # if the (row, col) exists, and the value is zero, remove it
      # since we are only keeping non zero values
      del self.elements[(row, col)]

  def add(self, other):
    # creates an new instance of SparceMatrix called result to store the new matrix and sets 
    # its row and col from getting the maximum rows and col from both files
    result = SparseMatrix(rows=max(self.num_rows, other.num_rows), cols=max(self.num_cols, other.num_cols))
    
    # Check if key(row, col) from self is present in other.items. If found, conduct the operat
    for (row, col), value in self.elements.items():
      if (row, col) in other.elements:
        result.set_element(row, col, value + other.get_element(row, col))
    return result


  def subtract(self, other):
    result = SparseMatrix(rows=max(self.num_rows, other.num_rows), cols=max(self.num_cols, other.num_cols))
    
    for (row, col), value in self.elements.items():
      if (row, col) in other.elements:
        result.set_element(row, col, value - other.get_element(row, col))
    
    return result


  def multiply(self, other):
    if self.num_cols != other.num_rows:
      raise ValueError("Invalid dimensions for matrix multiplication")

    result = SparseMatrix(rows=self.num_rows, cols=other.num_cols)

    for (row, col), value in self.elements.items():
      for k in range(other.num_cols):
        if (col, k) in other.elements:
          result.set_element(row, k, result.get_element(row, k) + value * other.get_element(col, k))
    
    return result

  def __str__(self):
        elements = [f"({row}, {col}, {value})" for (row, col), value in self.elements.items()]
        return f"SparseMatrix({self.num_rows}x{self.num_cols}):\n" + "\n".join(elements)

if __name__ == "__main__":
    try:
        print("Select operation: 1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Getting the value at (row, key)")
        operation = int(input("Enter your choice: "))

        # filea = 'sample_inputs/matrixfile1.txt'
        # fileb = 'sample_inputs/matrixfile3.txt'

        # matrix1 = SparseMatrix(filea)
        # matrix2 = SparseMatrix(fileb)

        file1 = input("Enter the path for the first matrix file: ")
        file2 = input("Enter the path for the second matrix file: ")

        matrix1 = SparseMatrix(file1)
        matrix2 = SparseMatrix(file2)

        if operation == 1:
            result = matrix1.add(matrix2)
        elif operation == 2:
            result = matrix1.subtract(matrix2)
        elif operation == 3:
            result = matrix1.multiply(matrix2)
        elif operation == 4:
            row = int(input("Enter the row: "))
            col = int(input("Enter the col: "))
            value = int(input("Whci file do you want to use: "))
            if value == 1:
               result = matrix1.get_element(row, col)
            elif value == 2:
               result = matrix2.get_element(row, col)
            else:
               result = matrix1.get_element(row, col)
        else:
            raise ValueError("Invalid operation choice")

        print("Result:")
        print(result)

    except Exception as e:
        print(f"Error: {e}")
