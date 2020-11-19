import csv
import pandas as pd

f = open('goods.csv', encoding='UTF-8')
data = csv.reader(f, delimiter=',')
for row in data:
    print(row)

### 商品クラス
class Item:
    def __init__(self,item_code,item_name,price):
        self.item_code=item_code
        self.item_name=item_name
        self.price=price
    
    def get_price(self):
        return self.price

### オーダークラス
class Order:
    def __init__(self,item_master):
        self.item_order_list=[]
        self.item_order_list2=[]
        self.item_order_list3=[]
        self.item_master=item_master
    
    def add_item_order(self,item_code):
        self.item_order_list.append(item_code)

    def add_item_order2(self, item_name):
        self.item_order_list2.append(item_name)
    
    def add_item_order3(self, price):
        self.item_order_list3.append(price)
        
    def view_item_list(self):
        for item in self.item_order_list:
            print("商品コード:{}".format(item))
        for item in self.item_order_list2:
            print("商品名:{}".format(item))
        for item in self.item_order_list3:
            print("価格:{}".format(item))
    
### メイン処理
def main():
    # マスタ登録
    item_master=[]
    item_master.append(Item("001","りんご",100))
    item_master.append(Item("002","なし",120))
    item_master.append(Item("003","みかん",150))
    item_master.append(Item(row,"",""))
    print(item_master)
    
    # オーダー登録
    order=Order(item_master)
    order.add_item_order("001")
    order.add_item_order("002")
    order.add_item_order("003")
    # order.add_item_order(input())

    order.add_item_order2("りんご")
    order.add_item_order2("なし")
    order.add_item_order2("みかん")

    order.add_item_order3(100)
    order.add_item_order3(120)
    order.add_item_order3(150)
    
    # オーダー表示
    order.view_item_list()
    
if __name__ == "__main__":
    main()
