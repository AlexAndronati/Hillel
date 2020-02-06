students = [['Krishna', 67, 68, 69], ['Arjun', 70, 98, 63], ['Malika', 52, 56, 60]]
st = {}
for i in students:
    st.update({i[0]: sum(j for j in i if isinstance(j, int))/(len(i)-1)})
name = input("Enter the student's name: ")
print(st.get(name, "No such a student"))