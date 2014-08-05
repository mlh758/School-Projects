#pragma once
#define MAX_SIZE 160
#define INITIAL_SIZE 10
#include "animal.h"
#include "Herbivore.h"
#include <vector>
#include <time.h>


class Carnivore :
	public Animal
{
public:
	Carnivore(void) 
		{ Birth(INITIAL_SIZE); SetMaxSize(MAX_SIZE); Carnivore::totalMass += mass; }
	/*@Precondition: eatMe has been initialized
	  @Postcondition: Increases amountEaten by eatMe's mass*/
	void Hunt(Herbivore &eatMe);
	void Grow();
	void Die() { totalMass-=mass; Organism::Die(); }
	/*@Precondition: None
	  @Postcondition: Increases size of Carnivores by 10%, uses random numbers to determine
	  whether fractional remainder becomes additional Carnivore*/
	static void Reproduce(std::vector<Carnivore> &Carnivores);
	static double getTotalMass() { return totalMass; }

private:
	static double totalMass;
};

