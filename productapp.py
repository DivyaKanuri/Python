"""product application
1.Add product
2. update product
3.delete product
4.get product by product id
5. get all products
6.get product by category
7.get product b/w prices"""
products=[]
# 1.Add a product in products list
def add_product(pid,name,category,price):
    product=[pid,name,category,price]
    products.append(product)
    print(" product is added")
# 2.Delete a product by id
def del_product(pid):
    for product in products:
        if pid in product:
            products.remove(product)
            print("product succesfully deleted")
# 3.Update product by id
def update_product(pid,name,category,price):
    for product in products:
        if(product[0]==pid):
            product[1]=name
            product[2]=category
            product[3]=price
            return " product is updated"
    return "product not found"
# 4.Getting product by id
def get_product_by_id(pid):
    for product in products:
        if(product[0]==pid):
            return(product)
    return("product not found")
# 5.Get all products
def get_all_products():
    return products
# 6.Get product by category
def get_pro_by_cat(cat):
    count=0
    for product in products:
        if(product[2]==cat):
            count+=1
            print(product)
    if(count==0):
        print("no product found")
# 7.Get product between prices
def get_pro_between_price(n1,n2):
    count=0
    for product in products:
        if(n1<=product[3]<=n2):
            count+=1
            print(product)
    if(count==0):
        print("no product found")
while(True):
    print("product application \n 1.Add product \n 2. delete product \n 3.update product \n 4.get product by product id \n 5. get all products \n 6.get product by category \n 7.get product b/w prices")
    match=int(input("enter choice"))
    if(match==1 or match==3):
        pid=int(input("enter product id: "))
        name=input("enter product name: ")
        category=input("enter category of a product: ")
        price=int(input("enter price: "))
        if(match==1):
            add_product(pid,name,category,price)
            print(products)
        else:
            print(update_product(pid,name,category,price))
            print(products)
    elif(match==2):
        id=int(input("enter product id: "))
        del_product(id)
        print(products)
    if(match==4):
        id=int(input("enter product id: "))
        print(get_product_by_id(id))
    if(match==5):
        print(get_all_products())
    if(match==6):
        cat=input("enter category: ")
        get_pro_by_cat(cat)
    if(match==7):
        n1=int(input("enter min range: "))
        n2=int(input("enter min range: "))
        get_pro_between_price(n1,n2)
    