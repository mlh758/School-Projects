#include "Carnivore.h"
#include <iostream>



void Carnivore::Hunt(Herbivore &eatMe)
{
	if(GetAmountEaten() < mass)
	{
		Eat(eatMe.GetMass());
		eatMe.Die();
	}
}

void Carnivore::Grow()
{ 
	if(mass < GetMaxSize())
	{
		Carnivore::totalMass -= mass;
		mass += GetAmountEaten() * .75;
		Carnivore::totalMass += mass;
	}
} 

void Carnivore::Reproduce(std::vector<Carnivore> &Carnivores)
{
	if(Carnivores.size() <= 0)
		Carnivores.push_back(Carnivore() );
	else
	{
	double increaseBy = Carnivores.size() * 0.1;
	double odds = (increaseBy - static_cast<long>(increaseBy))*100;
	//Create the additional carnivore based on the percentage in odds.
	if(rand()%100 <= odds)
		++increaseBy;
	for(int i = 0; i < increaseBy; i++)
		Carnivores.push_back(Carnivore() );
	}
}

double Carnivore::totalMass(0.0);