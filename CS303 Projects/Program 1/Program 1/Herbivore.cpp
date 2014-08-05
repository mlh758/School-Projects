#include "Herbivore.h"
#include <iostream>



void Herbivore::Graze(Plant &eatMe)
{
	if(GetAmountEaten() < mass * 2)
		Eat(eatMe.GetNibbled());
}

void Herbivore::Grow()
{ 
	if(mass < GetMaxSize())
	{
		Herbivore::totalMass -= mass;
		mass += GetAmountEaten() * .75;
		Herbivore::totalMass += mass;
	}
} 

void Herbivore::Reproduce(std::vector<Herbivore> &Herbies)
{
	double increaseBy = Herbies.size() * 0.2;
	double odds = (increaseBy - static_cast<long>(increaseBy))*100;
	//Create an additional herbivore based on the percentage in odds.
	if(rand()%100 <= odds)
		++increaseBy;
	for(int i = 0; i < increaseBy; i++)
		Herbies.push_back(Herbivore() );
}

double Herbivore::totalMass(0.0);

