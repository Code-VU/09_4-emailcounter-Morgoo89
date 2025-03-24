def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
    handle = open(name)
    
    word = list()
    for line in handle:
        line = line.strip()
        if line.startswith('From '):
            words=line.split()
            email = words[1]
            word.append(email)
    
    countFrom = dict()
    
    for email in word:
        countFrom[email] = countFrom.get(email, 0) + 1
        
    bigCount = None
    bigWord = None
    for key, value in countFrom.items():
        if bigCount is None or value > bigCount:
            bigCount = value
            bigWord = key
    
    print(bigWord, bigCount)
       
        
        

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
