import csv

noOfItems=int(input("Enter the number of completed items(Pack of 4 Dozens): "))
print("\t\t\t\t\t\tPrepartion of Chocolate Cookies")
print(" Ingredients")
print("*************")
with open('BOM-Cookies.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    count=0
    cost=0.0
    for row in readCSV:
        if count>0:
            print(int(row[2])*noOfItems,row[3],"of",row[1])
            cost=cost+float(row[4])
        count=count+1
print("Expected cost of completing each item is $",cost)
totalCost=cost*noOfItems
print("Total Cost of producing the",noOfItems,"Pack of 4 Dozens Cokkies is $",cost)

print("\n Preparation Steps")
print("*********************")
print("Step1:")
print("\tSift together flour and baking soda and set aside. In the bowl of a standing electric mixer fitted with the paddle attachment, cream butter until lemony yellow, about 2 minutes. Scrape down sides of bowl and paddle. Add sugar, brown sugar and salt. Continue creaming mixture on medium speed until it is smooth and lump free, about 1 minute. Stop mixer and scrape down sides of bowl and paddle.")
print("Step2:")
print("\tAdd egg and vanilla and beat on low speed for 15 seconds, or until they are fully incorporated. Do not over-beat. Scrape down sides of bowl and paddle.")
print("Step3:")
print("\tOn low speed, add sifted flour mixture. Beat slowly until all of the flour is incorporated. Scrape down sides of bowl. Add chocolate chunks and mix in.")
print("Step4:")
print("\tHeat oven to 350 degrees with the rack positioned in the lower third of the oven. Line 2 baking sheets with parchment. Spoon heaping teaspoons of dough 2 inches apart onto baking sheets. If not baking right away, remove small handfuls or spoonfuls of dough from mixer and plop them down on the middle of a sheet of parchment or wax paper, creating a log about 1 1/2 inches wide and 12 inches long.\n Fold parchment over, creating a sausage. Chill for at least 1 hour, preferably overnight. Using a serrated knife, slice chilled dough into 1/3-inch-thick rounds and place them 2 inches apart, in staggered rows, on parchment-lined sheets and proceed. (Dough will keep nicely, tightly wrapped, in the refrigerator for 1 week, or in the freezer for up to 1 month. Thaw frozen dough at room temperature for 30 minutes before slicing.)")
print("Step5:")
print("\tBake one sheet at a time for 12 to 15 minutes, until lightly browned, rotating the baking sheet front to back halfway through. Remove from heat and slide parchment off baking sheet and onto a work surface. Allow cookies to cool for at least 5 minutes before serving, or for at least 20 minutes before storing in an airtight container. They will keep for up to 3 days at room temperature.")

