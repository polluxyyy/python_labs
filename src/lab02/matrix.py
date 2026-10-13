def check_matrix(mat: list[list[float | int]]) -> None:
    for row in mat:
        if len(row)!=len(mat[0]):
            raise ValueError("не ровная(рваная) матрица")
        
def transpoce(mat: list[list[float | int]]) -> list[list]:
    check_matrix(mat)
    result=[]
    if len(mat)==0:
        return result
    for j in range(len(mat[0])):
        new_row=[]
        for row in mat:
            new_row.append(row[j])
        result.append(new_row)
    return result

def row_sums(mat: list[list[float | int]]) -> list[float]:
    check_matrix(mat)
    result=[]
    for row in mat:
        result.append(sum(row,0))
    return result

def col_sums(mat: list[list[float | int]]) -> list[float]:
    return row_sums(transpoce(mat))

if __name__=="__main__":
    m=[[1, 2], [3]]
    print(f"транспонирование\n ввод:{m}\nвывод:{transpoce(m)}")
    print(f"суммы строк\n ввод:{m}\nвывод:{row_sums(m)}")
    print(f"суммы столбцов\n ввод:{m}\nвывод:{col_sums(m)}")
