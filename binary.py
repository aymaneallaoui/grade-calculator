def grade_percentages(scores):
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

scores = [7.00,5.25,5.25,5.50,5.00,6.00,4.75,7.50,5.50,6.25,6.50,5.25,4.75,8.25,7.75,6.75,7.50,7.25,6.50,6.50,8.00,8.00,4.50,6.25,7.25,5.00,8.25,7.25,5.00]
grade_percentages(scores)



