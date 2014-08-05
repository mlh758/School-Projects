#pragma once
#pragma warning ( disable : 4290 ) //Visual Studios doesn't like throws in function
                                  //declarations. This just shuts up the warning messages
#include "EcosystemError.h"

class Organism
{
public:
	Organism() {}
	/*@Precondition: StartMass is a number type
	  @Postcondition: Initializes an Organism with initial mass
	   Sets alive to true*/
	Organism(double StartMass);
	/*@Precondition: StartMass is a number type
	  @Postcondition: Initializes an Organism with initial mass
	   Sets alive to true*/
	virtual void Birth(double StartMass);
	/*@Precondition: Calling object has been initialized
	  @Returns: Mass of object */
	virtual double GetMass() const { return mass; }
	/*@Precondition: Mass is a number type
	  @Postcondition: Sets the mass of the calling object*/
	virtual void SetMass(double Mass) throw(EcosystemError);
	/*@Precondition: Calling object has been initialized
	  @Returns: Valuve of alive*/
	virtual bool IsAlive() const {return alive; }
	/*@Precondition: Calling object has been initialized
	  @Postcondition: Sets alive to false, sets mass to zero*/
	virtual void Die();
	/*@Precondition: Calling object has been initialized
	  @Postcondition: Organism grows by specified guidelines*/
	virtual void Grow() = 0;
private:
	bool alive;
protected:
	double mass;

};

