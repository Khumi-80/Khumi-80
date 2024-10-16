import streamlit as st
import math

# Function to handle scientific calculator operations
def scientific_calculator():
    st.title("Scientific Calculator")

    # Select the operation
    operation = st.selectbox("Select operation:", 
                             ["Addition", "Subtraction", "Multiplication", "Division", 
                              "Power", "Square Root", "Logarithm (Base 10)", "Exponential", 
                              "Sine", "Cosine", "Tangent"])

    if operation == "Addition":
        num1 = st.number_input("Enter first number", format="%.5f")
        num2 = st.number_input("Enter second number", format="%.5f")
        if st.button("Calculate"):
            st.write(f"Result: {num1} + {num2} = {num1 + num2}")

    elif operation == "Subtraction":
        num1 = st.number_input("Enter first number", format="%.5f")
        num2 = st.number_input("Enter second number", format="%.5f")
        if st.button("Calculate"):
            st.write(f"Result: {num1} - {num2} = {num1 - num2}")

    elif operation == "Multiplication":
        num1 = st.number_input("Enter first number", format="%.5f")
        num2 = st.number_input("Enter second number", format="%.5f")
        if st.button("Calculate"):
            st.write(f"Result: {num1} * {num2} = {num1 * num2}")

    elif operation == "Division":
        num1 = st.number_input("Enter first number", format="%.5f")
        num2 = st.number_input("Enter second number", format="%.5f")
        if st.button("Calculate"):
            if num2 != 0:
                st.write(f"Result: {num1} / {num2} = {num1 / num2}")
            else:
                st.write("Error! Division by zero.")

    elif operation == "Power":
        base = st.number_input("Enter base", format="%.5f")
        exponent = st.number_input("Enter exponent", format="%.5f")
        if st.button("Calculate"):
            st.write(f"Result: {base} ^ {exponent} = {math.pow(base, exponent)}")

    elif operation == "Square Root":
        num = st.number_input("Enter a number", format="%.5f")
        if st.button("Calculate"):
            if num >= 0:
                st.write(f"Result: Square root of {num} = {math.sqrt(num)}")
            else:
                st.write("Error! Cannot take square root of a negative number.")

    elif operation == "Logarithm (Base 10)":
        num = st.number_input("Enter a number", format="%.5f")
        if st.button("Calculate"):
            if num > 0:
                st.write(f"Result: Log base 10 of {num} = {math.log10(num)}")
            else:
                st.write("Error! Logarithm undefined for zero or negative numbers.")

    elif operation == "Exponential":
        num = st.number_input("Enter a number", format="%.5f")
        if st.button("Calculate"):
            st.write(f"Result: e^{num} = {math.exp(num)}")

    elif operation == "Sine":
        angle = st.number_input("Enter angle in degrees", format="%.5f")
        if st.button("Calculate"):
            st.write(f"Result: sin({angle}) = {math.sin(math.radians(angle))}")

    elif operation == "Cosine":
        angle = st.number_input("Enter angle in degrees", format="%.5f")
        if st.button("Calculate"):
            st.write(f"Result: cos({angle}) = {math.cos(math.radians(angle))}")

    elif operation == "Tangent":
        angle = st.number_input("Enter angle in degrees", format="%.5f")
        if st.button("Calculate"):
            st.write(f"Result: tan({angle}) = {math.tan(math.radians(angle))}")

# Run the calculator
if __name__ == "__main__":
    scientific_calculator()
