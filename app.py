import streamlit as st

def find_largest(num1, num2, num3):
  """This function finds the largest number among three numbers."""
  largest = max(num1, num2, num3)
  return largest

st.title("Find the Largest Number")

# Get user input for the three numbers
number1 = st.number_input("Enter first number:")
number2 = st.number_input("Enter second number:")
number3 = st.number_input("Enter third number:")

# Call the function to find the largest number
if st.button("Find Largest"):
  if number1 == "" or number2 == "" or number3 == "":
    st.error("Please enter all three numbers.")
  else:
    largest_number = find_largest(number1, number2, number3)
    st.write("The largest number is:", largest_number)

