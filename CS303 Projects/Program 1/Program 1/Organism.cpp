#include "Organism.h"

Organism::Organism(double StartMass)
{
	alive = true;
	mass = (StartMass >= 0) ? StartMass : 1.0;
}

void Organism::Birth(double StartMass)
{
	alive = true;
	mass = (StartMass >= 0) ? StartMass : 1.0;
}

void Organism::Die()
{
	alive = false;
	mass = 0;
}

void Organism::SetMass(double Mass) throw(EcosystemError)
{
	if(Mass < 0) throw(EcosystemError("Invalid Mass") );
	else
		mass = Mass;
}