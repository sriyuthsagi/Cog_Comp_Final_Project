


def findProduct(sentence):
    
    products = ["egg", "flour", "sugar", "milk", "chocolate", "blueberry", "vanilla"]
    products_present = {"egg": -1, "flour": -1, "sugar": -1, "milk": -1, "chocolate": -1, "blueberry": -1, "vanilla": -1, "price": -1}
    
    for i in products:
        
        if i in sentence:
            temp = 0
            
            pos = sentence.find(i)-1
            
            for j in range(pos, -1, -1):
                if sentence[j].isdigit():
                    
                    pos2 = j
                    while sentence[pos2].isdigit():
                        pos2 = pos2 - 1
                    
                    products_present[i] = int(sentence[pos2+1:j+1])
                    
                    break
        
    products_present["price"] = priceIdentify(sentence)
    
    return products_present


def priceIdentify(sentence):
    
    currencies = ['dollar', 'yuan', 'kuai', 'RMB']
    curr = 'None'
    price = -1
    
    for i in currencies:
        if i in sentence:
            curr = i
    
    if curr != 'None':
        curr_start = sentence.find(curr) - 1
        
        temp = curr_start - 1
        
        
        while (sentence[temp] != ' '):
            temp = temp - 1
            if temp == -1:
                break
            
        temp = temp + 1
        
        try:
            price = float(sentence[curr_start : temp])
        except:
            price = -1
    
    
    if '$' in sentence:
        curr_start = sentence.find('$') + 1
        
        temp = curr_start
        
        while (sentence[temp] != ' '):
            temp = temp + 1
            if temp == len(sentence):
                break
        
        try:
            price = float(sentence[curr_start : temp])
        except:
            price = -1
        

    return price


