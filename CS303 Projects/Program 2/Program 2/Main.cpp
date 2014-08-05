/*
Michael Harris
CS303
mlh758@mail.umkc.edu

Used AVL Tree based on code from textbook with some modifications
Primarily:
  1. Removed inheritence for simplicity and to prevent need for casting
     nodes to child type
  2. Find is written iteratively
  3. Implemented lazy deletion
  4. Tree clears itself recursively by creating a Node destructor
  5. Rotations have an extra step to prevent temp nodes from destroying tree when destructor is called
*/
#include <iostream>
#include <fstream>
#include "MemUtilities.h"
#include "BST.h"

//@precondition: There is memory available in the manager
//@throws: runtime error if manager is empty
//@postcondition: directory is created at dirPath with the name after the final '/'
void md(std::string dirPath, Directory& root, Manager& man, std::ostream& out);

//@precondition: There is memory available in the manager
//@throws: runtime error if manager is empty
//@postcondition: file is created at dirPath with the name after the final '/'
void sf(std::string dirPath, int size, Directory& root, Manager& man, std::ostream& out);

//@precondition: None
//@postcondition: file is removed at dirPath with the name after the final '/'
void rf(std::string dirPath, Directory& root, Manager& man, std::ostream& out);

//@precondition: None
//@postcondition: directory is removed at dirPath with the name after the final '/'
void rd(std::string dirPath, Directory& root, Manager& man, std::ostream& out);

using std::cout;

int main()
{
	std::ifstream fin("input1.txt");
	std::ofstream fout("log.txt");
	std::ofstream disk("diskmap.txt");
	std::string command, path;
	int size;
	Manager man(52428800, 16384);
	Directory root(man);
	while(fin >> command >> path)
	{
		if(command == "md")
			md(path, root, man, fout);

		else if(command == "sf")
		{
			fin >> size;
			sf(path, size, root, man, fout);
		}
		else if(command == "rf")
			rf(path, root, man, fout);

		else if(command == "rd")
			rd(path, root, man, fout);
		else
			fout << "INVALID COMMAND\n";
	}
	fout << man.getSize() << " blocks free on disk.\n";
	disk << man;
	fout.close();
	disk.close();
	system("PAUSE");
	return 0;
}

void md(std::string dirPath, Directory& root, Manager& man, std::ostream& out)
{
	out << "Attempting to make directory " << dirPath <<"...";
	bool result = root.MkDir(dirPath, man);
	out << (result ? "SUCESS\n" : "FAILED\n");
}

void sf(std::string dirPath, int size, Directory& root, Manager& man, std::ostream& out)
{
	out << "Attempting to save file " << dirPath <<"...";
	File object(dirPath, size);
	try
	{
	root.AddFile(object, man);
	out << "SUCCESS\n";
	}
	catch(std::runtime_error e)
	{
		out << "FAILED\n";
	}
}

void rf(std::string dirPath, Directory& root, Manager& man, std::ostream& out)
{
	out << "Attempting to remove file " << dirPath <<"...";
	root.Delete(dirPath, man);
	out << "SUCCESS\n";
}

void rd(std::string dirPath, Directory& root, Manager& man, std::ostream& out)
{
	out << "Attempting to remove directory " << dirPath <<"...";
	bool result = root.RmDir(dirPath, man);
	out << (result ? "SUCESS\n" : "FAILED\n");
}