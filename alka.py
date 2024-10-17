import streamlit as st
st.title('Loan Applications App')
l=st.number_input("Please Enter your number for loan")
s=st.number_input("Please Enter your number for salary")
c=st.number_input("Please Enter your number for credit score")
if s>=40000 and c>=500:
    st.write("Congratulations!")
else:
    st.write("We are sorry")

a=[1,2,3,4,5]
z=st.selectbox('which book',a)
y=st.button('Confirm')
if y==1:
    st.write('you can apply for this book')
m=st.radio('Are you a student',options=['yes','no','working'])
if m=='yes':
    st.write('student')
elif m=='no':
    st.write('okay')
n=st.checkbox('you want this book')