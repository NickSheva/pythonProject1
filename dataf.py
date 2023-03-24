import pandas as pd

Colors=['Red', 'Blue', 'Green', 'Orange']
df = pd.DataFrame(Colors)
print(df)
print()
list_values = ['English', 'Hindi', 'Mathematics', 'Science', 'Social Science']
df = pd.DataFrame(list_values, index=['i', 'ii', 'iii', 'iv', 'v'], columns=['Subjects'])
print(df)
print()
list_values = ['English', 'Hindi', 'Mathematics', 'Science', 'Social Science']
code = [20, 21, 22, 23, 24]
df = pd.DataFrame(list(zip(list_values, code)), columns=['Subjicts', 'Code'])
print(df)
print()

list_values = [['English', 4101], ['Hindi', 4102], ['Science', 4103], ['Mathematics', 4104], ['Computer', 4105]]
df = pd.DataFrame(list_values, columns=['Subjects', 'Code'])
print(df)
print()
list_values = [['Colin', 'Lassiter', 46], ['James', 'Gomez', 24],
               ['Sara', 'Charles', 34], ['Raven', 'Stewart', 24], ['Oliver', 'Osment', 21]]
df = pd.DataFrame(list_values, columns=["First_Name", 'Last_Name', 'Age'])
print(df)
print()
f_name = ['Colin', 'James', 'Sara', 'Raven', 'Oliver']
l_name = ['Lassiter', 'Gomez', 'Charles', 'Stewart', 'Osment']
age = [46, 24, 34, 24, 21]
dict = {'First_Name': f_name, 'Last_Name': l_name, 'Age': age}
df = pd.DataFrame(dict)
print(df)