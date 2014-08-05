#include "MemUtilities.h"


Manager::Manager(unsigned long size, unsigned int blockSize)
{
	this->blockSize = blockSize;
	total = size;
	unsigned long start = 1;
	unsigned long finish = blockSize;
	while(finish <= size)
	{
		freeSpace.push_front(Block(start, finish));
		start = finish + 1;
		finish += blockSize;
	}
}//Manager Constructor

void Manager::Free(std::list<Block> freeMe)
{
	std::list<Block>::iterator itr;
	while(freeMe.size() > 0)
	{
		freeSpace.push_front(freeMe.front());
		freeMe.pop_front();
	}
}//free

std::list<Block>Manager::Malloc(int bytes)
{
	if(freeSpace.size() == 0)
		throw std::runtime_error("Out of memory!");
	int blocksNeeded = ceil(bytes/static_cast<double>(blockSize));
	std::list<Block> returnValue;
	for(int i = 0; i < blocksNeeded; i++)
	{
		if(freeSpace.size() == 0)
			throw std::runtime_error("Out of memory!");
		returnValue.push_front(freeSpace.front());
		freeSpace.pop_front();
	}
	return returnValue;
}//malloc

Block Manager::getBlock()
{
	if(freeSpace.size() == 0)
		throw std::runtime_error("Out of memory!");
	Block returnValue = freeSpace.front();
	freeSpace.pop_front();
	return returnValue;
}

void Directory::AddFile(File& file, Manager& man)
{
	std::istringstream ss(file.name);
	if(ss.peek() == '/')
		ss.get();
	std::string sub;
	std::getline(ss, sub, '/');
	const Directory *temp = Directories.find(sub);
	file.sectors = man.Malloc(file.size);
	//Process string for child directory
	while(!ss.eof())
	{
		std::getline(ss, sub, '/');
		if(ss.eof()) break;
		temp = temp->Directories.find(sub);
		//Directory chain is invalid, cannot add file
		if(temp == nullptr)
			throw std::runtime_error("Invalid file path");
		
	}
	if(temp)
	{
		//Free parent directory for modification
		Directory* parent = const_cast<Directory*>(temp);
		file.name = sub;
		parent->Files.insert(file);
		parent->dirSize++;
		parent->biggifyDir(man);		
	}
	else //inserting into root directory
	{
		file.name = sub;
		Files.insert(file);
		dirSize++;
		biggifyDir(man);
	}
}

void Directory::Delete(std::string fileName, Manager& man)
{
	std::istringstream ss(fileName);
	if(ss.peek() == '/')
		ss.get();
	std::string sub;
	std::getline(ss, sub, '/');
	const Directory *temp = Directories.find(sub);
	//Process string for child directory
	while(!ss.eof())
	{
		std::getline(ss, sub, '/');
		if(ss.eof()) break;
		temp = temp->Directories.find(sub);
		//Directory chain is invalid, cannot remove file
		if(temp == nullptr)
			return;
		
	}
	if(temp)
	{
		//Free parent directory for modification
		Directory* parent = const_cast<Directory*>(temp);
		if(parent->Files.find(sub))
		{
			//File is here, erase it and free the memory
			File *file = const_cast<File*>(parent->Files.find(sub));
			man.Free(file->sectors);
			parent->Files.erase(*file);
			parent->dirSize--;
			parent->reduceDir(man);
		}
	}
	else //removing from root
	{
		File *file = const_cast<File*>(Files.find(sub));
		man.Free(file->sectors);
		Files.erase(*file);
		dirSize--;
		reduceDir(man);
	}

}//Delete

bool Directory::MkDir(std::string dirName, Manager& man)
{
	std::istringstream ss(dirName);
	if(ss.peek() == '/')
		ss.get();
	std::string sub;
	std::getline(ss, sub, '/');
	const Directory *temp = nullptr;
	//Process string for child directory
	while(!ss.eof())
	{
		if(temp)
			temp = temp->Directories.find(sub);
		else
			temp = Directories.find(sub);
		//Directory chain is invalid, cannot insert
		if(temp == nullptr)
			return false;
		std::getline(ss, sub, '/');
		
	}
	if(temp)
	{
		Directory* parent = const_cast<Directory*>(temp);
		parent->Directories.insert(Directory(sub, man));
		parent->dirSize++;
		parent->biggifyDir(man);
		return true;
	}
	else //inserting into root directory
	{
		Directories.insert(Directory(sub, man));
		dirSize++;
		biggifyDir(man);
		return true;
	}
}//mkdir

bool Directory::RmDir(std::string dirName, Manager& man)
{
	std::istringstream ss(dirName);
	if(ss.peek() == '/')
		ss.get();
	std::string sub;
	std::getline(ss, sub, '/');
	const Directory *temp = nullptr;
	//Process string for child directory
	while(!ss.eof())
	{
		if(temp)
			temp = temp->Directories.find(sub);
		else
			temp = Directories.find(sub);
		//Directory chain is invalid, cannot insert
		if(temp == nullptr)
			return false;
		std::getline(ss, sub, '/');
		
	}
	//If there was a child directory to be found
	if(temp)
	{
		//Free the parent for alteration, attempt to locate child for deletion
		Directory* parent = const_cast<Directory*>(temp);
		Directory* removal = const_cast<Directory*>(parent->Directories.find(sub));
		//Make sure child directory exists and is empty
		if(removal == nullptr || removal->getSize() != 0)
				return false;
		else
		{
			//Remove it
			man.Free(removal->sectors);
			parent->Directories.erase(sub);
			parent->dirSize--;
			parent->reduceDir(man);
			return true;
		}
	}
	//Directory is either not there or we are deleting a root directory
	else
	{
		temp = Directories.find(sub);
		temp = const_cast<Directory*>(temp);
		//Make sure directory exists and is empty
		if(temp == nullptr || temp->Directories.getSize() != 0 || temp->Files.getSize() != 0)
			return false;
		else
		{
		//Erase it
		man.Free(temp->sectors);
		Directories.erase(*temp);
		dirSize--;
		reduceDir(man);
		return true;
		}

	}
}//rmdir

void Directory::reduceDir(Manager& man)
{
	if(maxSize > 128 && dirSize < maxSize/2)
	{
		std::list<Block> temp;
		temp.push_back(sectors.front());
		sectors.pop_front();
		man.Free(temp);
		maxSize -= 128;
	}
}

void Directory::biggifyDir(Manager& man)
{
	if(dirSize == maxSize)
	{
		sectors.push_front(man.getBlock());
		maxSize += 128;
	}
}

//ALL the operators!
bool operator ==(const File& ls, const File& rs)
{
	return ls.name == rs.name;
}

bool operator <(const File& ls, const File& rs)
{
	return ls.name < rs.name;
}

bool operator >(const File& ls, const File& rs)
{
	return ls.name > rs.name;
}

bool operator <=(const File& ls, const File& rs)
{
	return ls.name <= rs.name;
}

bool operator >=(const File& ls, const File& rs)
{
	return ls.name >= rs.name;
}

bool operator ==(const Directory& ls, const Directory& rs)
{
	return ls.name == rs.name;
}

bool operator <(const Directory& ls, const Directory& rs)
{
	return ls.name < rs.name;
}

bool operator >(const Directory& ls, const Directory& rs)
{
	return ls.name > rs.name;
}

bool operator <=(const Directory& ls, const Directory& rs)
{
	return ls.name <= rs.name;
}

bool operator >=(const Directory& ls, const Directory& rs)
{
	return ls.name >= rs.name;
}

std::ostream& operator<<(std::ostream& out, const Directory& rs)
{
	out << rs.name;
	out << rs.Directories.to_string();
	return out;
}

std::ostream& operator<<(std::ostream& out, const File& rs)
{
	out << rs.name;
	return out;
}

bool operator <(Block& ls, Block& rs)
{
	return ls.start < rs.start;
}
bool compare(const Block& ls, const Block& rs)
{
	return ls.start < rs.start;
}

std::ostream& operator <<(std::ostream& out, const Manager& print)
{
	std::list<Block> temp(print.freeSpace);
	temp.sort([](const Block & a, const Block & b) { return a.start < b.start; });
	int blocks = print.total / print.blockSize;
	unsigned long step = print.blockSize;
	std::list<Block>::iterator itr = temp.begin();
	out << ". = Used\tX=Free\n";
	for(int i = 1; i <= blocks; i++)
	{
		if(itr != temp.end() && itr->end == step)
		{
			out << "X";
			if(itr != temp.end())
				++itr;
		}
		else
			out << ".";
		if(i % 40 == 0)
			out << "\n";
		step += print.blockSize;
	}
	return out;
}