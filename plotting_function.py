# all plotting functions

#Function for the first program
import matplotlib.pyplot as plt
def hist_graph(data):
    plt.hist(data,bins=7)

    plt.ylabel('Counts')
    plt.title('Frequency of letters') 

    plt.show()

#Function for dictionary
def dict_new(word):
    d = dict()
    for char in word:
        d[char] = d.get(char,0) + 1  #the zero is what is returned if char is not in d
    return d


#Function for second plotting program
def bar_graph(d):
    
        plt.bar(list(d.keys()), d.values())
        plt.ylabel('Counts')
        plt.title('Frequency of letters') 
        plt.show()

# New Program for today
fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"
d = dict()
fh = open(fname)
count = 0
for line in fh:
    words = line.split()  
    if len(words) == 0:
        continue
    first_word = words[0]  
    if first_word == 'From:':
        d['From:']  = d.get('From:',0) + 1
        #count=count+1
    elif first_word == 'From':
        d['From']  = d.get('From',0) + 1
        #count+=1
    else:
        d['other']=d.get('other',0)+1
        #count+=1
for key,val in d.items():
    print("There are",key,"counts of", val)
  
