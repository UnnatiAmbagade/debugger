import streamlit as st
import subprocess
import dbg  # Import the custom debugger

st.title("Python Debugger (Web-based)")

code = st.text_area("Enter Python Code to Debug:", '''def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

breakpoint()
print(fib(5))
''')

if st.button("Run Debugger"):
    with open("temp_script.py", "w") as f:
        f.write(code)

    result = subprocess.run(["python", "temp_script.py"], capture_output=True, text=True)
    
    st.subheader("Output:")
    st.code(result.stdout)

    st.subheader("Debugger Variables:")
    st.json(dbg.get_variables())  # Show local variables from the breakpoint
