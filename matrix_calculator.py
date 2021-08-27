def calculator(array1,array2,rows,columns,operation):
    result=[]
    for i in range (rows):
        col=[]
        for j in range(columns):
            col.append(0)
        result.append(col)
    if (operation==1 or operation==2):
        for i in range(rows):
            for j in range(columns):
                if(operation==1):
                    result[i][j]=array1[i][j]+array2[i][j]
                else:
                    result[i][j]=array1[i][j]-array2[i][j]
    elif (operation==3):
        for i in range (rows):
            for j in range (columns):
                for k in range (rows):
                    result[i][j]+=array1[i][k]*array2[k][j]
    return(result)  
       



print("\t\t Matrix Calculator:")
rows_col=int(input("Enter the number of rows and columns:"))
rows=rows_col
columns=rows_col
for n in range (2):
    if (n==0):
        print("The first matrix:")
    else:
        print("The second matrix:")
    arr=[]
    for i in range (rows):
        col=[]
        for j in range(columns):
            col.append(int(input("Enter the value:")))
        arr.append(col)
    if (n==0):
        array1=arr
    else:
        array2=arr
operation=int(input("Enter a number\n1.Addition\n2.Subraction\n3.Multiplication"))
result=calculator(array1,array2,rows,columns,operation)
print(result)