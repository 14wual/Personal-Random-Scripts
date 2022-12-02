# Create a script that applies discounts and VAT to the products in your basket, 
# the discount must be different from each other and finally add the purchase

total = 0

def productos():

    global basket

    #If you want to add more products, copy and modify any of these dictionaries
    mango = dict(price = 6.5, discount = 25, price_discount = 0, price_iva = 0, final_price = 0)
    grapes = dict(price = 4.5, discount = 10, price_discount = 0, price_iva = 0, final_price = 0)
    pears = dict(price = 0.5, discount = 0, price_discount = 0, price_iva = 0, final_price = 0)
    apple = dict(price = 2.5, discount = 5, price_discount = 0, price_iva = 0, final_price = 0)
    banana = dict(price = 3.5, discount = 15, price_discount = 0, price_iva = 0, final_price = 0)

    basket = ([apple,mango,banana,pears,grapes])

    for x in basket:
        apply_iva(x)
        apply_dis(x)
        pri_final(x)

    global total
    print(f"La basket termina su price en {total}€ con:\
        \n          1. Mango: {mango['final_price']}€\
        \n          2. apple: {apple['final_price']}€\
        \n          3. banana: {banana['final_price']}€\
        \n          3. pears: {pears['final_price']}€\
        \n          5. grapes: {grapes['final_price']}€")

def apply_iva(dic):

    #Apply VAT
    tasa_iva = 14 / 100 #Modify the 14 for the VAT you want to implement (7,21,...)
    iva = round(dic["price"] * tasa_iva,2)
    dic["price_iva"] = iva

def apply_dis(dic):
    
    #Apply discount
    tasa_desc = dic["discount"]/100
    desc = round(dic["price"] * tasa_desc,2)
    dic["price_discount"] = desc

def pri_final(dic):

    pricefinal = dic["price"] + dic["price_iva"] - dic["price_discount"]
    dic["final_price"] = pricefinal

    global total
    total += dic["final_price"]
    

if __name__ == '__main__':
    productos()