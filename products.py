#輸入模組
import os #operating system

def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #仍在迴圈之中，跳過單一迴
			name, price = line.strip().split(',') #split後會變成清單
			products.append([name,price])
	return(products)
	
def user_input(products):
	#讓使用者輸入
	while True:
		name = input('請輸入商品名稱：')
		if name == 'q':
			break
		price = input('請輸入產品價格：')
		products.append([name, price])
	print(products)
	return products

def print_products(products):
	#印出購買紀錄
	for product in products:
		print(product[0],'的價格是', product[1])

def write_file(filename, products):
	#寫入檔案
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') #才是真正寫入


def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #確認檔案是否存在
		print('yeah!找到檔案了！')
		products = read_file(filename)
	else:
		print('缺少檔案！')
	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()