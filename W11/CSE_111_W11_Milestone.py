import matplotlib.pyplot as plt
import pandas as pd 

def main():

    # Create a line break between the terminal and the program.
        print()
        
        df = pd.read_csv('W11alarms.csv')

        print(df)



main()