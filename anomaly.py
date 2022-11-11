
#this function returns the ith column in a 2D list A
def get_col(A, i):
    return [float(row[i]) for row in A]

#==============================================================

#open the file
f = open("mammal_sleep_1.txt")

#read the file into a matrix
lines = [line.rstrip().split("\t") for line in f]

#get each column (attribute) in the matrix
for i in range ( 1, len(lines[0])):

    #extract all the attribute values into an array x
    x = get_col(lines, i)

    #compute mean
    mean = sum(x)/len(x)
    
    #compute stdev
    stdev = (sum([(x-mean)**2 for x in x])/len(x))**0.5
    
    #for each entry in x, check whether it is an anomaly, print anomalous values.
    for j in range (0, len(x)):
        if x[j] > mean + 2*stdev or x[j] < mean - 2*stdev:
            print(f'Anomaly found: {x[j]}')
        
        
        


