

# if the product is in the input sentence, find a numeric value before and set the respective quantity to it
def findProduct(sentence):

    products = ["egg", "flour", "sugar", "milk", "chocolate", "blueberry", "vanilla"]
    products_present = {"egg": -1, "flour": -1, "sugar": -1, "milk": -1, "chocolate": -1, "blueberry": -1, "vanilla": -1}

    # loop through the list of products
    for i in products:

        if i.lower() in sentence:
            products_present[i] = 1

            for j in range(sentence.find(i)-1, -1, -1):
                if sentence[j].isdigit():

                    begin = j
                    while sentence[begin].isdigit():
                        begin = begin - 1

                    products_present[i] = int(sentence[begin+1:j+1])

                    break

    price = priceIdentify(sentence)

    return [products_present, price]

# find the currency is the sentence and then return the number respective to it
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
