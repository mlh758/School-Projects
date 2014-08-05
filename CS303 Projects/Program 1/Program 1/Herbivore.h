#pragma once
#define MAX_SIZE 80
#define INITIAL_SIZE 10
#include "Animal.h"
#include "Plant.h"
#include <vector>
#include <time.h>
class Herbivore : public Animal
{
public:
	Herbivore(void) 
		{ Birth(INITIAL_SIZE); SetMaxSize(MAX_SIZE); Herbivore::totalMass += mass; }
	/*@Precondition: eatMe has been initialized
	  @Postcondition: amountEaten increases by amount taken from Plant object*/
	void Graze(Plant &eatMe);
	void Grow();
	void Die() { Herbivore::totalMass-=mass; Organism::Die(); }
	/*@Precondition: None
	  @Postcondition: Increases size of Herbies by 20%, uses random numbers to determine
	  whether fractional remainder becomes additional Herbivore*/
	static void Reproduce(std::vector<Herbivore> &Herbies);
	/*@Precondition: None
	  @Returns: Total mass of Herbivores*/
	static double getTotalMass() { return totalMass; }
private:
	static double totalMass;
};

