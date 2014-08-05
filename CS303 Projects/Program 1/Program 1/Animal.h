#pragma once
#include "Organism.h"
class Animal : public Organism
{
public:
	/*@Precondition: Calling object has been initialized, Amount is a number type
	  @Postcondition: Increases amountEaten by Amount*/
	void Eat(double Amount) { amountEaten += Amount; }
	/*@Precondition: Calling object has been initialized
	  @Postcondition: Returns amount eaten during that week cycle*/
	double GetAmountEaten() const {return amountEaten; }
	/*@Precondition: None
	  @Postcondition: Initializes amountEaten to 0 for that week cycle*/
	void StartWeek() {amountEaten = 0;}
protected:
	/*@Precondition: max is a number type
	  @Postcondition: Sets maxSize to max*/
	void SetMaxSize(double max) { maxSize = max; }
	/*@Precondition: Calling object has been initialized
	  @Postcondition: Returns value of maxSize*/
	double GetMaxSize() const { return maxSize; }
private:
	double amountEaten;
	double maxSize;
};

