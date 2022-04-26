# Project 1 for CITS1401
# A program that computes data based upon measured elements of countries and compares it after being normalised
# Comparisons are done through ranking (in descending order) or using the Spearman Rank Coefficient
# Authour: Jaimin Kirankumar Kerai (22718975)

import os

def main('hey'):
    # This main function will ask for inputs and take action
    filename = input("Enter name of file containing World Happiness computation data: ")
    # If the file is found the statement below will hold true
    if os.path.isfile(filename) == True:
        # As soon as a file is found the values will be normalised
        Normalise(filename)
        metric = input("Choose metric to be tested (min, mean, median, harmonic_mean): ")
        if metric == 'mean':
            specified_metric = input("Chose action to be performed on the data using the specified metric (list, correlation): ")
            if specified_metric == 'list':
                # This will call the mean function and print a descending list of the countries normalised means
                Mean()
                print("Ranked list of countries' happiness scores based on the mean metric")
                # A loop to print in values in dictionary ordered in descedning order
                for key, value in sorted(mean_dict.items(), reverse=True, key=lambda item: item[1]):
                    print("{}: {}".format(key, round(value,4)))
            elif specified_metric == 'correlation':
                # This will calculate the Correlation coefficient between Life Ladder and Mean scores
                SpearmanRank_Mean()
            else:
                # The program will exit when there is no valid collection of inputs
                exit()
        elif metric == 'harmonic_mean':
            specified_metric = input("Chose action to be performed on the data using the specified metric (list, correlation): ")
            if specified_metric == 'list':
                # This will call the harmonic mean function and print a descending list of the countries normalised harmonic means
                Harmonic_Mean()
                print("Ranked list of countries' happiness scores based on the harmonic mean metric")
                # A loop to print in values in dictionary ordered in descedning order
                for key, value in sorted(Hmean_dict.items(), reverse=True, key=lambda item: item[1]):
                    print("{}: {}".format(key, round(value,4)))
            elif specified_metric == 'correlation':
                # This will calculate the Correlation coefficient between Life Ladder and Harmonic Mean scores
                SpearmanRank_HarmonicMean()
            else:
                # The program will exit when there is no valid collection of inputs
                exit()
        elif metric == 'median':
            specified_metric = input("Chose action to be performed on the data using the specified metric (list, correlation): ")
            if specified_metric == 'list':
                # This will call the median function and print a descending list of the countries normalised median
                Median()
                print("Ranked list of countries' happiness scores based on the median metric")
                # A loop to print in values in dictionary ordered in descedning order
                for key, value in sorted(median_dict.items(), reverse=True, key=lambda item: item[1]):
                    print("{}: {}".format(key, round(value,4)))
            elif specified_metric == 'correlation':
                # This will calculate the Correlation coefficient between Life Ladder and Median scores
                SpearmanRank_Median()
            else:
                # The program will exit when there is no valid collection of inputs
                exit()
        elif metric == 'min':
            specified_metric = input("Chose action to be performed on the data using the specified metric (list, correlation): ")
            if specified_metric == 'list':
                # This will call the min function and print a descending list of the countries normalised min
                Min()
                print("Ranked list of countries' happiness scores based on the min metric")
                # A loop to print in values in dictionary ordered in descedning order
                for key, value in sorted(min_dict.items(), reverse=True, key=lambda item: item[1]):
                    print("{}: {}".format(key, round(value,4)))
            elif specified_metric == 'correlation':
                # This will calculate the Correlation coefficient between Life Ladder and Minimum scores
                SpearmanRank_Min()
            else:
                # The program will exit when there is no valid collection of inputs
                exit()
        else:
            #if no file exists the function exits
            exit()
            
            
def Normalise(filename):
    # Initialising and opening our file
    input_file = open(filename, 'r')
    # Skipping the first line
    input_file.readline()
    # Creating lists to add the values of each column
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    column5 = []
    column6 = []
    # Looping through the lines removing irrelevant strings and turning values into floats
    for string in input_file:
        file_output = []
        string = string.strip('\n').split(',')
        for element in string:
            file_output.append(element)        
        for i in range(1, len(file_output)):
            if file_output[i] != '':
                file_output[i] = float(file_output[i])
            else:
                file_output[i] = ''
        # Adds value of columns into lists; to be able to find maximums and minimums of each
        if file_output[2] != "":
            column1.append(file_output[2])
        if file_output[3] != "":        
            column2.append(file_output[3])
        if file_output[4] != "":        
            column3.append(file_output[4])
        if file_output[5] != "":        
            column4.append(file_output[5])
        if file_output[6] != "":        
            column5.append(file_output[6])
        if file_output[7] != "":
            column6.append(file_output[7])
    input_file.close()
    min_max = [min(column1),max(column1),min(column2),max(column2),min(column3),max(column3),min(column4),max(column4),min(column5),max(column5),min(column6),max(column6)]
    # Reinitialising the lines, and using the max and min values to normalise the values
    input_file = open(filename, 'r')
    new_file = open('NewLines.txt', 'w')
    input_file.readline()
    for lines in input_file:
        new_lines = []
        lines = lines.strip('\n').split(',')
        for elements in lines:
            new_lines.append(elements)        
        for i in range(1, len(new_lines)):
            if new_lines[i] != '':
                new_lines[i] = float(new_lines[i])
            else:
                new_lines[i] = ''          
        for i in range(0,len(new_lines)-2):
            if new_lines[i+2] != '':
                new_lines[i+2] = (new_lines[i+2]-min_max[2*i])/(min_max[2*i+1]-min_max[2*i])
            else:
                new_lines[i+2] = ''
        # Saving our normalised values into a new file, line-by-line
        print(new_lines, file=new_file)
    input_file.close()
    new_file.close()
        
def Mean():
    # Opening the newly made file 
    new_file = open('NewLines.txt', 'r')
    # Initialising a dictionary to store the countries as keys and our columns as values
    global mean_dict
    mean_dict = {}
    # Looping each line in our file, removing irrelevant strings and turning values into floats
    for lines in new_file:
        total = 0
        counter = 0
        mean_output = []
        lines = lines.strip().strip('[').strip(']').strip('"').split(", ")
        for elements in lines:
            mean_output.append(elements)
        for i in range(1, len(mean_output)):
            if mean_output[i] != "''":
                mean_output[i] = float(mean_output[i])
            else:
                mean_output[i] = ''
        # Adding each value in the row and dividing it by the count of the present values
        for i in range(2, len(mean_output)):
            if mean_output[i] != '':
                total += mean_output[i]
                counter += 1
                mean = total/counter
        # Associating the key (country) to the value (mean)
        mean_dict[mean_output[0].strip('"').strip("'")] = mean
    new_file.close()
    
def Harmonic_Mean():
    # Opening the newly made file
    new_file = open('NewLines.txt', 'r')
    # Initialising a dictionary to store the countries as keys and our columns as values
    global Hmean_dict
    Hmean_dict = {}
    # Looping each line in our file, removing irrelevant strings and turning values into floats
    for lines in new_file:
        total = 0
        counter = 0
        Hmean_output = []
        lines = lines.strip().strip('[').strip(']').strip('"').split(", ")
        for elements in lines:
            if elements != "''":
                Hmean_output.append(elements)
        for i in range(1, len(Hmean_output)):
            Hmean_output[i] = float(Hmean_output[i])
        # Finding the reciprocal of the sum of the reciprocal of each value divided by the number of values 
        for i in range(2, len(Hmean_output)):
            if Hmean_output[i] > 0.0:
                total += 1/(Hmean_output[i])
                counter += 1
        harmonic_mean = counter/total
        # Associating the key (country) to the value (harmonic mean)
        Hmean_dict[Hmean_output[0].strip('"').strip("'")] = harmonic_mean
    new_file.close()
        
def Median():
    # Opening the newly made file
    new_file = open('NewLines.txt', 'r')
    # Initialising a dictionary to store the countries as keys and our columns as values
    global median_dict
    median_dict = {}
    # Looping each line in our file, removing irrelevant strings and turning values into floats and sorting in ascending order
    for lines in new_file:
        median_output = []
        lines = lines.strip().strip('[').strip(']').strip('"').split(", ")
        for elements in lines:
            if elements != "''":
                median_output.append(elements)
                median_output.sort()
        # Finding the median value in the case of both an even or odd count of numbers
        for i in range(1, len(median_output)):
            median_output[i] = float(median_output[i])
        median_calc = median_output[1:-1]
        size = len(median_calc)
        midPos = size//2
        if size%2 == 0:
            median = (median_calc[midPos]+median_calc[midPos-1])/2
        else:
            median = median_calc[midPos]
        # Associating the key (country) to the value (median)
        median_dict[median_output[0].strip('"').strip("'")] = median    
    new_file.close()

def Min():
    # Opening the newly made file
    new_file = open('NewLines.txt', 'r')
    # Initialising a dictionary to store the countries as keys and our columns as values
    global min_dict
    min_dict = {}
    # Looping each line in our file, removing irrelevant strings and turning values into floats
    for lines in new_file:
        min_output = []
        lines = lines.strip().strip('[').strip(']').strip('"').split(", ")
        for elements in lines:
            if elements != "''":
                min_output.append(elements)
        # Using min function to find smallest value in row
        for i in range(1, len(min_output)):
            min_output[i] = float(min_output[i])
        min_calc = min_output[2:]
        min_Line = min(min_calc)
        # Associating the key (country) to the value (min)
        min_dict[min_output[0].strip('"').strip("'")] = min_Line
    new_file.close()

def SpearmanRank():
    # Opening the newly made file
    new_file = open('NewLines.txt', 'r')
    # Initialising a dictionary to store the countries as keys and our Life Ladder scores as values
    global lifeladder_dict
    lifeladder_dict = {}
    # Looping each line in our file, removing irrelevant strings and turning values into floats
    for lines in new_file:
        SpearmanRank_output = []
        lines = lines.strip().strip('[').strip(']').strip('"').split(", ")
        for elements in lines:
            if elements != "''":
                SpearmanRank_output.append(elements)
        for i in range(1, len(SpearmanRank_output)):
            SpearmanRank_output[i] = float(SpearmanRank_output[i])
        lifeladder = SpearmanRank_output[1]
        # Associating the key (country) to the value (life ladder score)
        lifeladder_dict[SpearmanRank_output[0].strip('"').strip("'")] = lifeladder
    new_file.close()
    
def SpearmanRank_Mean():
    # Initialising variables and calling the respective functions to access the dictionaries
    SpearmanRank()
    Mean()
    counter = 0
    difference_sum = 0
    # Mean - Sorting each key by descending order of value then changing the value into a rank value
    for key, value in sorted(mean_dict.items(), reverse=True, key=lambda item: item[1]):
        counter +=1
        mean_dict[key] = counter
    counter = 0
    # Life Ladder - Sorting each key by descending order of value then changing the value into a rank value
    for key, value in sorted(lifeladder_dict.items(), reverse=True, key=lambda item: item[1]):
        counter +=1
        lifeladder_dict[key] = counter
    # Finding the difference of the life ladder and metric (mean), summing the sqaure differences and applying the simple Spearman Rank Coefficient formulae
    for key, value in lifeladder_dict.items():
        d = lifeladder_dict[key] - mean_dict[key]
        difference_sum += d*d
    correlation_coefficient = 1-(6*(difference_sum))/(counter*(counter**2 - 1))
    print("The correlation coefficient between the study ranking and the ranking using the mean metric is", round(correlation_coefficient,4))
    
def SpearmanRank_Min():
    # Initialising variables and calling the respective functions to access the dictionaries
    SpearmanRank()
    Min()
    counter = 0
    difference_sum = 0
    # Minimun - Sorting each key by descending order of value then changing the value into a rank value
    for key, value in sorted(min_dict.items(), reverse=True, key=lambda item: item[1]):
        counter +=1
        min_dict[key] = counter
    counter = 0
    # Life Ladder - Sorting each key by descending order of value then changing the value into a rank value 
    for key, value in sorted(lifeladder_dict.items(), reverse=True, key=lambda item: item[1]):
        counter +=1
        lifeladder_dict[key] = counter
    # Finding the difference of the life ladder and metric (min), summing the sqaure differences and applying the simple Spearman Rank Coefficient formulae    
    for key, value in lifeladder_dict.items():
        d = lifeladder_dict[key] - min_dict[key]
        difference_sum += d*d
    correlation_coefficient = 1-(6*(difference_sum))/(counter*(counter**2 - 1))
    print("The correlation coefficient between the study ranking and the ranking using the min metric is", round(correlation_coefficient,4))
    
def SpearmanRank_Median():
    # Initialising variables and calling the respective functions to access the dictionaries
    SpearmanRank()
    Median()
    counter = 0
    difference_sum = 0
    # Median - Sorting each key by descending order of value then changing the value into a rank value
    for key, value in sorted(median_dict.items(), reverse=True, key=lambda item: item[1]):
        counter +=1
        median_dict[key] = counter
    counter = 0
    # Life Ladder - Sorting each key by descending order of value then changing the value into a rank value
    for key, value in sorted(lifeladder_dict.items(), reverse=True, key=lambda item: item[1]):
        counter +=1
        lifeladder_dict[key] = counter
    # Finding the difference of the life ladder and metric (median), summing the sqaure differences and applying the simple Spearman Rank Coefficient formulae 
    for key, value in lifeladder_dict.items():
        d = lifeladder_dict[key] - median_dict[key]
        difference_sum += d*d
    correlation_coefficient = 1-(6*(difference_sum))/(counter*(counter**2 - 1))
    print("The correlation coefficient between the study ranking and the ranking using the median metric is", round(correlation_coefficient,4))
    
def SpearmanRank_HarmonicMean():
    # Initialising variables and calling the respective functions to access the dictionaries
    SpearmanRank()
    Harmonic_Mean()
    counter = 0
    difference_sum = 0
    # Harmonic Mean - Sorting each key by descending order of value then changing the value into a rank value
    for key, value in sorted(Hmean_dict.items(), reverse=True, key=lambda item: item[1]):
        counter +=1
        Hmean_dict[key] = counter
    counter = 0
    # Life Ladder - Sorting each key by descending order of value then changing the value into a rank value
    for key, value in sorted(lifeladder_dict.items(), reverse=True, key=lambda item: item[1]):
        counter +=1
        lifeladder_dict[key] = counter
    # Finding the difference of the life ladder and metric (harmonic mean), summing the sqaure differences and applying the simple Spearman Rank Coefficient formulae
    for key, value in lifeladder_dict.items():
        d = lifeladder_dict[key] - Hmean_dict[key]
        difference_sum += d*d
    correlation_coefficient = 1-(6*(difference_sum))/(counter*(counter**2 - 1))
    print("The correlation coefficient between the study ranking and the ranking using the harmonic mean metric is", round(correlation_coefficient,4))
    
        

    
        
main()