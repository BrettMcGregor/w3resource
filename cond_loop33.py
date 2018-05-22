# Write a Python program to convert month name to a number of days. Go to the editor
# Expected Output:
#
# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December
# Input the name of Month: February
# No. of days: 28/29 days


months = {
    "january": "31", "february": "28 or 29", "march": "30", "april": "30",
    "may": "31", "june": "30", "july": "31", "august": "31", "september": "30",
    "october": "31", "november": "30", "december": "31"
    }


raw_input = input("Enter a month: ")
print("Number of days in {} = {}".format(raw_input, months[raw_input.lower()]))
