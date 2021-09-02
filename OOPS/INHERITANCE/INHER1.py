#SIngle Inheritance
class Person():
    def walk(self):
        print("person is not walking ! ")
    def  read(self):
        print("person is walking")
class Student(Person):
    def exam(self):
        print("attending the exam ")
pe=Person()
pe.walk()
pe.read()

st=Student()
st.exam()
st.walk()
st.read()