from scipy import sparse
import numpy as np
import xlwt
from numpy import linalg as la

col = [0] * 500
row = [0] * 500
data = [0] * 500
for i in range(500):
    row[i] = np.random.randint(0, 50)
    col[i] = np.random.randint(0, 200)  # 返回值的范围为【0，200)的整数,200不可取，因为是矩阵的index最大为199
    data[i] = np.random.randint(1, 6)  # 返回值的范围为【1，5】的整数，作为评分
# print(max(col))
spr_A = sparse.coo_matrix((data, (row, col)), shape=(50, 200)).toarray()  # 构造50*200的矩阵
# print(spr_A)
# 创建工作薄，并保存上述矩阵
f = xlwt.Workbook()
sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)  # 创建sheet
for c in range(200):
    for r in range(50):
        sheet1.write(r, c, int(spr_A[r, c]))  # 注意要使用int(spr_A[r,c])，直接使用spr_A[r,c]会报错
f.save('D:/excelText.xls')

print(spr_A.shape)
print(spr_A)
#
#
# u, s, v = la.svd(spr_A, full_matrices=0, compute_uv=1)
# # 还原原始的矩阵，发现四OK的
# # A=np.dot(u,np.diag(s))
# # print(np.dot(A,v))
# print("左奇异值：")
# print(u, u.shape)
# print("奇异值：")
# print(s, s.shape)
# print("右奇异值：")
# print(v, v.shape)