class SparseMatrix:
  def __init__(self, file_path=None, rows=0, cols=0):
    self.file_path = file_path
    self.num_rows = rows
    self.num_cols = cols
    self.elements = {} # # Dictionary to store non-zero values as {(row, col): value}
    if file_path:
      self.load_data(file_path)


  def load_data(self, file_path):
    try:
      with open(file_path, 'r') as f:
        data = f.readlines()

      # Process rows and columns
      self.num_rows = int(data[0].split('=')[1].strip())
      self.num_cols = int(data[1].split('=')[1].strip())

      # Lets process the remaining data points
      for item in data[2:]:
        item = item.strip()
        if not item:
          continue
        if not (item.startswith('(') and item.endswith(')')):
          raise ValueError('Input file has wrong format')
        
        row, col, value = map(int, item[1:-1].split(','))
        self.elements[(row, col)] = value

    except Exception as e:
      raise ValueError(f"Error reading file: {e}")
    
  def get_element(self, row, col):
    return self.elements.get((row, col), 0)
  
  def set_element(self, row, col, value):
    if value != 0:
      self.elements[(row, col)] = value
    elif (row, col) in self.elements:
      del self.elements[(row, col)]

  def add(self, other):
    result = SparseMatrix(rows=max(self.num_rows, other.num_rows), cols=max(self.num_cols, other.num_cols))
    
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
        print("Select operation: 1 for Addition, 2 for Subtraction, 3 for Multiplication")
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
        else:
            raise ValueError("Invalid operation choice")

        print("Result:")
        print(result)

    except Exception as e:
        print(f"Error: {e}")


