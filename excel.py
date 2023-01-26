import pandas as pd

def grade_percentages(file_path):
    # Read in the Excel file
    df = pd.read_excel(file_path)
    
    # Extract the scores column from the dataframe
    scores = df['scores']
    
    below_5 = 0
    between_5_and_7_5 = 0
    above_7_5 = 0
    total_students = len(scores)
    
    for score in scores:
        if score < 5:
            below_5 += 1
        elif score >= 5 and score <= 7.5:
            between_5_and_7_5 += 1
        else:
            above_7_5 += 1
    
    below_5_percent = (below_5 / total_students) * 100
    between_5_and_7_5_percent = (between_5_and_7_5 / total_students) * 100
    above_7_5_percent = (above_7_5 / total_students) * 100
    
    print("Above 7.5/10: {:.2f}%".format(below_5_percent))
    print("Between 5/10 and 7.5/10: {:.2f}%".format(between_5_and_7_5_percent))
    print("adam 5/10: {:.2f}%".format(above_7_5_percent))
    print(len(scores))

file_path = 'path/to/scores.xlsx'
grade_percentages(file_path)
