class Node:
	
	def __init__(self, initData = None):
			self.data = initData
			self.next = None
	
class LinkedList:
	
	def __init__(self):
		self.head = Node()

	def insert(self, data):
		#insert to front of Linked List
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def delete(self, data_to_delete):
		#deleting node with given data
		cur_node = self.head
		prev_node = None

		#need to delete head
		if cur_node.data == data_to_delete:
			self.head = cur_node.next
			return

		#need to find node
		while cur_node.next is not None:
			if cur_node.data == data_to_delete:
				break
			
			prev_node = cur_node
			cur_node = cur_node.next

		prev_node.next = cur_node.next
				


	def print_List(self):
		#storing values in list 
		elements = []
		cur_node = self.head
		
		while cur_node.next != None:

			elements.append(cur_node.data)
			cur_node = cur_node.next

		print(elements)
		
	def search(self, data_to_find):
		cur_node = self.head

		while cur_node.next != None:
			if cur_node.data == data_to_find:
				print("data is in list")

			cur_node = cur_node.next
			
