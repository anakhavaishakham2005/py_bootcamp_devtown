import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

print("Hello, World!")
name=input("What is your name? ")
print("hello",name)
age=int(input("What is your age? "))
if age>19:
    print("You are an adult")
else:
    print("You are a minor")