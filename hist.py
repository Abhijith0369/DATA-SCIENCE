import matplotlib.pyplot as plt

marks = [22, 45, 67, 89, 34, 56, 23, 12, 45, 67, 78, 67, 45, 34, 89, 100]

bins = range(0, 101, 10)  # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.figure(figsize=(9, 5))
plt.hist(marks, bins=bins, edgecolor='black', color='red')
plt.title("Distribution of Student Marks")
plt.xlabel("marks intervals")
plt.ylabel("number of students")

plt.xticks(bins)
plt.yticks(range(0,5,1))

plt.grid(axis='y',alpha=0.75)
plt.show()






