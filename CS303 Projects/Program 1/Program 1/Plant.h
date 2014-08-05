#pragma once
#define INITIAL_SIZE 10
#include "Organism.h"
class Plant : public Organism
{
public:
	Plant(void) { Birth(INITIAL_SIZE);  Plant::totalMass+=mass; }
	/*@Precondition: None
	  @Postcondition: Sets alive to true, starting mass to 1, and increases totalMass*/
	void Sprout() { Birth(1); totalMass+=1; }
	/*@Precondition: Calling object has been initialized
	  @Postcondition: Plant's mass decreases and may die, decreases totalMass
	  @Returns: double representation of value removed from Plant*/
	double GetNibbled();
	void Grow();
	void Die();
	/*@Precondition: None
	  @Returns total Plant mass*/
	static double getTotalMass() { return totalMass; }
private:
	static double totalMass;
};



