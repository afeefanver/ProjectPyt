row1 = int(input("Enter the number of rows in the first matrix: "))
col1 = int(input("Enter the number of columns in the first matrix: "))
row2 = int(input("Enter the number of rows in the second matrix: "))
col2 = int(input("Enter the number of columns in the second matrix: "))

if col1 != row2:
    print("Matrix multiplication is not possible.")
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
        for j in range(col2):
            sum_element = 0
            for k in range(col1):
                sum_element += mat1[i][k] * mat2[k][j]
            row.append(sum_element)
        result.append(row)

    print("Result of matrix multiplication:")
    for row in result:
        print(row)
