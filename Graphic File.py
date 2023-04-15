import matplotlib.pyplot as plot
# set up your lists
numlist = [9, 7, 4, 3]
namelist = ['freshmen', 'sophomores', 'juniors', 'seniors']
colorlist = ['grey', 'blue', 'pink', 'yellow' ]
explodelist = [0.2, 0.1, 0.0, 0.0]
# make the pie chart
plot.pie(numlist, labels=namelist, autopct='%.1f%%', colors=colorlist,
    	explode = explodelist, startangle = 120)
plot.axis('equal')
plot.savefig('piechart.png')