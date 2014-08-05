#include<list>
#include<string>
#include "BST.h"
#include <sstream>
struct Block
{
	Block(int x, int y) : start(x), end(y) {}
	int start, end;
	friend bool operator <(Block& ls, Block& rs);
	bool compare(const Block& ls, const Block& rs);
};

struct File
{
	//Constructors
	File() : name(""), size(0) {}
	File(std::string n) : name(n), size(0) {}
	File(std::string n, int s) : name(n), size(s) {} 
	int size;
	std::string name;
	std::list<Block> sectors;
	//Comparison Operators
	friend bool operator ==(const File& ls, const File& rs);
	friend bool operator <(const File& ls, const File& rs);
	friend bool operator >(const File& ls, const File& rs);
	friend bool operator <=(const File& ls, const File& rs);
	friend bool operator >=(const File& ls, const File& rs);
	//Output Operator
	friend std::ostream& operator<<(std::ostream& out, const File& rs);
};

class Manager
{
public:
	//Constructor
	Manager(unsigned long size, unsigned int blockSize);

	//@precondition: Memory is available in freeSpace
	//@postcondition: freeSpace is reduced in size
	//@returns: list of Blocks sufficient to store required amount of data
	std::list<Block> Malloc(int bytes);
	//Reduction of Malloc, returns single block for directories
	Block getBlock();

	//@precondition: None
	//@postcondition: freeSpace is increased in size
	void Free(std::list<Block> freeMe);

	//Accessor
	int getSize() {return freeSpace.size(); }
	//Output operator
	friend std::ostream& operator <<(std::ostream& out, const Manager& print);
private:
	std::list<Block> freeSpace;
	int blockSize;
	unsigned long total;
};

class Directory
{
public:
	//Constructors
	Directory(Manager& man) : name(""), dirSize(0), maxSize(128) {sectors.push_front(man.getBlock());}
	Directory(std::string n, Manager& man) : name(n), dirSize(0), maxSize(128) {sectors.push_front(man.getBlock());}

	//@precondition: None
	//@postcondition: File is added to directory at location specified in file path if it does not already exist
	// Memory is taken from free store
	void AddFile(File& file, Manager& man);
	
	//@precondition: None
	//@postcondition: File is removed from directory specified in fileName. Memory is returned to free store
	void Delete(std::string fileName, Manager& man);

	//@precondition: None
	//@postcondition: directory is added under directory at location specified in file path if it does not already exist
	//  memory is taken from free store
	bool MkDir(std::string dirName, Manager& man);
	
	//@precondition: None
	//@postcondition: directory is removed under directory at location specified in file path
	//  memory is taken from free store
	bool RmDir(std::string dirName, Manager& man);

	//Accessor functions
	int numFiles() const { return Files.getSize(); }
	int numDirs() const { return Directories.getSize(); }
	//@returns: Number of active files and directories under this directory
	int getSize() const { return Files.getSize() + Directories.getSize(); }

	//Comparison Operators
	friend bool operator ==(const Directory& ls, const Directory& rs);
	friend bool operator <(const Directory& ls, const Directory& rs);
	friend bool operator >(const Directory& ls, const Directory& rs);
	friend bool operator <=(const Directory& ls, const Directory& rs);
	friend bool operator >=(const Directory& ls, const Directory& rs);
	friend std::ostream& operator<<(std::ostream& out, const Directory& rs);

private:
	int dirSize;
	//Conversion for find operators NOT allowed for public use
	Directory(std::string n) : name(n) {}
	int maxSize;
	std::string name;
	BST<File> Files;
	BST<Directory> Directories;
	std::list<Block> sectors;

	//@precondition: None
	//@postcondition: If directory has grown beyond base size and is less than 50% utilized 
	//  Directory surrenders one block of memory to free store and shrinks the max size
	void reduceDir(Manager& man);

	//@precondition: Memory is available in free store
	//@postcondition: If directory is at max size, one block of memory is added
	// max size increases by 128
	void biggifyDir(Manager& man);
};

