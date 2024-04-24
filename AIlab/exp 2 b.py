row1 = int(input("Enter the number of rows in the first matrix: "))
col1 = int(input("Enter the number of columns in the first matrix: "))
row2 = int(input("Enter the number of rows in the second matrix: "))
col2 = int(input("Enter the number of columns in the second matrix: "))

if row1 != row2 or col1 != col2:
    print("Matrix addition is not possible. Matrices must have the same dimensions.")
else:
    mat1 = []
    mat2 = []

    print("Enter the elements in the first matrix:")
    for i in range(row1):
        row = []
        for j in range(col1):
            element = int(input(f"mat1[{i}][{j}]: "))
            row.append(element)
        mat1.append(row)

    print("Enter the elements in the second matrix:")
    for i in range(row2):
        row = []
        for j in range(col2):
            element = int(input(f"mat2[{i}][{j}]: "))
            row.append(element)
        mat2.append(row)

    result = []

    for i in range(row1):
        row = []
        for j in range(col1):
            sum_element = mat1[i][j] + mat2[i][j]
            row.append(sum_element)
        result.append(row)

    print("Result of matrix addition:")
    for row in result:
        print(row)
