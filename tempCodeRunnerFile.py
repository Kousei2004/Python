import pandas as pd

# Đọc file CSV
df = pd.read_csv('Data_Loan.csv')

# Tạo df_number chỉ chứa các cột số
numeric_columns = ['loan_amnt', 'int_rate', 'emp_length', 'annual_inc', 
                  'dti', 'delinq_2yrs', 'revol_util', 'total_acc', 
                  'bad_loan', 'longest_credit_line']
df_number = df[numeric_columns]

# Tạo df_object chỉ chứa các cột object
object_columns = ['term', 'home_ownership', 'purpose', 'addr_state', 
                 'verification_status']
df_object = df[object_columns]

# Hiển thị 5 dòng đầu tiên của df_number
print("5 dòng đầu tiên của df_number:")
print(df_number.head())

print("\n5 dòng đầu tiên của df_object:")
print(df_object.head())

# Kiểm tra kiểu dữ liệu của các cột
print("\nKiểu dữ liệu của các cột trong df_number:")
print(df_number.dtypes)

print("\nKiểu dữ liệu của các cột trong df_object:")
print(df_object.dtypes)