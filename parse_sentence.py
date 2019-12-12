


def findProduct(sentence):

    products = ["Egg", "Flour", "Sugar", "Milk", "Chocolate", "Blueberry", "Vanilla"]
    products_present = {"Egg": -1, "Flour": -1, "Sugar": -1, "Milk": -1, "Chocolate": -1, "Blueberry": -1, "Vanilla": -1}

    for i in products:

        if i in sentence:
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
