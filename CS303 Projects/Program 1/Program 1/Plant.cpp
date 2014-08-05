#include "Plant.h"
#include <iostream>


double Plant::GetNibbled()
{
	if(!IsAlive()) return 0;
	double nibbled = mass * .25; //25% of Mass
	mass -= nibbled;
	Plant::totalMass -= nibbled;
	if(mass < 0.5)
	{
		Die();
	}
	return nibbled;
}

void Plant::Grow()
{
	if(!IsAlive()) return;
	Plant::totalMass -= mass;
	if(mass <= 5.0)
		mass *= 2;

	else if(mass <= 10)
		mass *= 1.5;

	else
		mass *= 1.1;

	Plant::totalMass += mass;
}

void Plant::Die()
{
	Plant::totalMass -= mass;
	Organism::Die();
}

double Plant::totalMass(0.0);
