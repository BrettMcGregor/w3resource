# Write a Python program to display the examination schedule. (extract the date from exam_st_date). Go to the editor
# exam_st_date = (11, 12, 2014)
# Sample Output : The examination will start from : 11 / 12 / 2014

exam_st_date = (11, 12, 2014)  # tuple
day, month, year = exam_st_date
print("The examination will start from: {} / {} / {}".format(day,month,year))
