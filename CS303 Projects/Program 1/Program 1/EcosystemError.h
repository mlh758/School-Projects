#pragma once
#include <exception>
class EcosystemError : public std::exception
{
public:
	EcosystemError(char* msg) : message(msg) {}
	const char* what() const { return message; }
	
private:
	char* message;
};

