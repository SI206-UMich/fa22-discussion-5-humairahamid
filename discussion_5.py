import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in sentence:
		if i == 'a' or i == 'A':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		maxstock = 0
		for item in self.items:
			if item.stock > maxstock:
				maxstock  = item.stock
				maxstock_item = item
		return maxstock_item


	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		maxprice = 0
		for item in self.items:
			if item.price > maxprice:
				maxprice  = item.price
				maxprice_item = item
		return maxprice_item

# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("Apples are awesome"),3,"Testing count_a with a's")
		self.assertEqual(count_a("Bb bb bb"),0,"Testing count_a without a's")
		


	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		wh1 = Warehouse()
		self.assertEqual(wh1.items,[], "When list is empty")
		wh1.add_item(self.item2)
		wh1.add_item(self.item4)
		self.assertEqual(wh1.items,[self.item2, self.item4], "When list has two items")
		



	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		wh2 = Warehouse(items=[self.item1, self.item3, self.item4])
		self.assertEqual(wh2.get_max_stock(),self.item3, "Testing for item with max stock")


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		wh3 = Warehouse(items=[self.item1, self.item2, self.item3])
		self.assertEqual(wh3.get_max_price(),self.item1, "Testing for item with max price")
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()