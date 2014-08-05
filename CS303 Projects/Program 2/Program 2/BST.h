#pragma once
#include <string>
#include <sstream>

template <class T>
class Node
{
public:
	//Constructor
	Node(T nData, Node<T>* l = nullptr, Node<T>* r = nullptr) :
		data(nData), left(l), right(r), balance(0), deleted(false) {}
	//Converts node to a string value for output
	virtual inline std::string to_string() const;
	int balance;
	bool deleted;
	T data;
	Node<T>* left;
	Node<T>* right;
	//Destructor, allows for recursive deletion of nodes in tree
	virtual ~Node() {delete left; delete right;}
};//Node

template <class T>
class BST 
{
private:
	Node<T> *R;
	
	//@precondition: local_root is a node in a tree
	//@returns: pointer to node containing the largest item in the tree
	Node<T>*& Max(const BST<T>& local_root);

	//@precondition: None
	//@returns: Left subtree of current node
	BST<T> get_left() const;

	//@precondition: None
	//@returns: Right subtree of current node
	BST<T> get_right() const;

	//Converts a tree to a string for output
	std::string to_string(const Node<T>* local_root) const;
	int size, deleted;
	
	//@precondition: None
	//@postcondition: Node is added to tree if it is not already in place
	//@returns: true if item is added to the tree
	virtual bool insert(Node<T>*& local_root, const T& item);
	bool increased;
		
	//@precondition: local_root is an unbalanced tree
	//@postcondition: Tree is rotated right around local_root
	void rotate_right(Node<T>*& local_root);
	
	//@precondition: local_root is an unbalanced tree
	//@postcondition: Tree is rotated left around local_root
	void rotate_left(Node<T>*& local_root);
	
	//@precondition: local_root is an unbalanced tree after left insertion
	//@postcondition: Tree is rebalanced around local_root
	void rebalance_left(Node<T>*& local_root);
		
	//@precondition: local_root is an unbalanced tree after right insertion
	//@postcondition: Tree is rebalanced around local_root
	void rebalance_right(Node<T>*& local_root);
		
	//@precondition: other_root is a binary tree
	//@postcondition: all non-deleted data in other_root is copied into current tree
	void copy(Node<T>* other_root);
public:
	//Constructors
	BST() : R(nullptr), size(0), deleted(0) {}
	BST(Node<T>* new_root) : R(new_root), size(1), deleted(0) {}
	inline BST(T data, const BST& left_root = BST(), const BST& right_root = BST() );
	BST(const BST& other);
	//Assignment Operator
	BST<T>& operator=(const BST<T>& rs);
		
	//@precondition: None
	//@returns: true if calling object has no child nodes
	bool is_leaf() const;
		
	//@precondition: None
	//@returns: number of active nodes in the tree
	int getSize() const {return size - deleted;}
		
	//@precondition: None
	//@postcondition: Node is added to tree if it is not already in place
	//@returns: true if item is added to the tree
	bool insert(const T& item) { return insert(this->R, item); }
		
	//@precondition: None
	//@postcondition: Node is removed from tree
	//@returns: true if item is removed from the tree
	bool erase(const T& item);

	//Converts tree to string for output
	std::string to_string() const { return to_string(this->R); }
		
	//@precondition: None
	//@returns: const pointer to value in tree if it exists, NULL if item is not in tree
	const T* find(const T& item) const;

	//Recursive destructor
	virtual ~BST();
};

template <class T>
std::string Node<T>::to_string() const
{
	std::ostringstream os;
	os <<"Balance: " << balance << " | " << data;
	return os.str();
}//Node to_string

template<class T>
BST<T>::BST(T data, const BST& left_root = BST(), const BST& right_root = BST() )
{
	size = 0; deleted = 0;
	R = new Node<T>(data, left_root.R, right_root.R);
	size = left_root.size + right_root.size;
	deleted = left_root.deleted + right_root.deleted;
}//full constructor

template<class T>
void BST<T>::copy(Node<T>* other_root)
{
	if(other_root == nullptr) return;
	if(!other_root->deleted)
		insert(other_root->data);
	copy(other_root->left);
	copy(other_root->right);
}//copy helper function

template <class T>
BST<T>::BST(const BST& other)
{
	if(other.R == nullptr)
	{
		this->R = nullptr;
		return;
	}
	size = 0;
	deleted = 0;
	copy(other.R);
}//copy constructor

template <class T>
BST<T>& BST<T>::operator=(const BST<T>& rs)
{
	if(&rs == this) return *this;
	this->~BST();
	BST<T> temp(rs);
	size = temp.getSize();
	deleted = 0;
	std::swap(this->R, temp.R);
	return *this;
}//assignment operator

template <class T>
BST<T> BST<T>::get_left() const
{
	if(R==nullptr) return nullptr;
	else
		return BST<T>(R->left);
}//get_left

template <class T>
BST<T> BST<T>::get_right() const
{
	if(R==nullptr) return nullptr;
	else
		return BST<T>(R->right);
}//get_right

template <class T>
bool BST<T>::is_leaf() const
{
	return (R==nullptr) ? true : R->left==nullptr && R->right==nullptr;
}//is_leaf

template <class T>
void BST<T>::rotate_right(Node<T>*& local_root)
{
	Node<T>* temp = local_root->left;
	local_root->left = temp->right;
	temp->right = local_root;
	local_root = temp;
	temp = nullptr;
}//rotate_right

template <class T>
void BST<T>::rotate_left(Node<T>*& local_root)
{
	Node<T>* temp = local_root->right;
	local_root->right = temp->left;
	temp->left = local_root;
	local_root = temp;
	temp = nullptr;
}//rotate_left

template<class T>
void BST<T>::rebalance_left(Node<T>*& local_root)
{
	//Left Right Case
	if(local_root->left->balance > 0)
	{
		//Left Right child left heavy (left-right case)
		if(local_root->left->right->balance < 0)
		{
			local_root->left->balance = 0;
			local_root->left->right->balance = 0;
			local_root->balance = 1;
		}
		else if(local_root->left->right->balance == 0)
		{
			//Everybody's balanced!
			local_root->left->balance = local_root->left->right->balance =
				local_root->balance = 0;
		}
		else
		{
			local_root->left->balance = -1;
			local_root->left->right->balance = 0;
			local_root->balance = 0;
		}
		rotate_left(local_root->left);
	}
	//Left Left Caase
	else
		local_root->left->balance = local_root->balance = 0;
	rotate_right(local_root);
}//rebalance_left

template<class T>
void BST<T>::rebalance_right(Node<T>*& local_root)
{
	//Right Left Case
	if(local_root->right->balance < 0)
	{
		//Right Left child left heavy (right-left case)
		if(local_root->right->left->balance < 0)
		{
			local_root->right->balance = 0;
			local_root->right->left->balance = 0;
			local_root->balance = 1;
		}
		else if(local_root->right->left->balance == 0)
		{
			//Everybody's balanced!
			local_root->right->balance = local_root->right->left->balance =
				local_root->balance = 0;
		}
		else
		{
			local_root->right->balance = -1;
			local_root->right->right->balance = 0;
			local_root->balance = 0;
		}
		rotate_right(local_root->right);
	}
	//Right Right Caase
	else
		local_root->right->balance = local_root->balance = 0;
	rotate_left(local_root);
}//rebalance_right

template<class T>
bool BST<T>::insert(Node<T>*& local_root, const T& item)
{
	if(local_root == nullptr)
	{
		local_root = new Node<T>(item);
		++size;
		increased = true;
		return true;
	}
	if(local_root->data == item)
	{
		if(local_root->deleted)
		{
			++size;
			local_root->deleted = false;
			//Update the data stored here
			local_root->data = item;
			return true;
		}
		return false;
	}
	if(item < local_root->data)
	{
		bool return_value = insert(local_root->left, item);
			if(increased)
			{
				switch (local_root->balance)
				{
				case 0:
					local_root->balance--;
					break;
				case 1:
					local_root->balance--;
					increased = false;
					break;
				case -1:
					increased = false;
					local_root->balance = 0;
					rebalance_left(local_root);
					break;

				default:
					break;
				}
			}
		return return_value;
	}//left insert
	else
	{
		bool return_value = insert(local_root->right, item);
			if(increased)
			{
				switch (local_root->balance)
				{
				case 0:
					local_root->balance++;
					break;
				case -1:
					local_root->balance++;
					increased = false;
					break;
				case 1:
					increased = false;
					local_root->balance = 0;
					rebalance_right(local_root);
					break;

				default:
					break;
				}
			}
		return return_value;
	}//right insert
}//insert

template <class T>
bool BST<T>::erase(const T& item)
{
	Node<T> *here = R;
	while(here != nullptr)
	{
		if(here->data == item)
		{
			//Item is already deleted
			if(here->deleted)
				return false;
			else
			{
				here->deleted = true;
				deleted++;
				return true;
			}
		}
		else
			here = (item < here->data) ? here->left : here->right;
	}
	return false; //here is null and item is not in tree
}//erase

template<class T>
std::string BST<T>::to_string(const Node<T>* local_root) const
{
	std::ostringstream out;
	if(local_root==nullptr)
		out << "NULL\n";
	else
	{
		if(!local_root->deleted)
			out << "Balance: " << local_root->balance << " | " << local_root->data << "\n";
		out << to_string(local_root->left);
		out << to_string(local_root->right);
	}
	return out.str();
}//to_string

template<class T>
const T* BST<T>::find(const T& item) const
{
	Node<T> *here = R;
	while(here != nullptr)
	{
		if(here->data == item)
			return (here->deleted) ? nullptr : &(here->data);
		else
			here = (item < here->data) ? here->left : here->right;
	}
	return nullptr; //here is null and item is not in tree
}//find

template <class T>
Node<T>*& BST<T>::Max(const BST<T>& local_root)
{
	if(local_root == nullptr)
		return nullptr;
	Node<T>* here = local_root;
	while(here->right != nullptr)
		here = here->right;
	return here;
}//max


template <class T>
BST<T>::~BST() 
{
	delete R;
	R = nullptr;
}//destructor