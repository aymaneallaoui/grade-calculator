import tkinter as tk

def calculate_grades():
    scores = []
    try:
        scores = [float(score.get()) for score in score_entries]
    except ValueError:
        result_label.config(text="Please enter valid numbers.")
        return
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

    result_label.config(text="Below 5/10: {:.2f}%\nBetween 5/10 and 7.5/10: {:.2f}%\nAbove 7.5/10: {:.2f}%".format(below_5_percent, between_5_and_7_5_percent, above_7_5_percent))

def add_score():
    for i in range(1):
        score_entry = tk.Entry(root)
        score_entry.pack()
        score_entries.append(score_entry)

def subtract_score():
    for i in range(1):
        score_entries[-1].destroy()
        score_entries.pop()

root = tk.Tk()
root.title("Grade Percentage Calculator")

score_entries = []

# Add 29 default student scores
for i in range(10):
    score_entry = tk.Entry(root)
    score_entry.pack()
    score_entries.append(score_entry)

calculate_button = tk.Button(root, text="Calculate", command=calculate_grades)
calculate_button.pack()

add_button = tk.Button(root, text="Add Score", command=add_score)
add_button.pack()

subtract_button = tk.Button(root, text="Subtract Score", command=subtract_score)
subtract_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()
