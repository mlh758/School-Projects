/*
Michael Harris
CS303
mlh758@mail.umkc.edu
Reproduction was made as a static member function within the respective animal classes.
Plant has a static member variable that keeps track of all plant mass to prevent having to iterate
  through the entire vector building a sum when it is needed. The same was done for Herbivore and Carnivore
The primary iterators in Graze and Hunt are incremented at the end of the for loop instead of
  within the declaration. When an herbivore or carnivore dies and erase is called, the iterator
  is incremented by the nature of erase. Moving the increment operation to a conditional statement
  prevents the skipping of items.
I used vector indecies instead of an iterator for the herbivore vector in Hunt to reduce complexity.
  Random access iterators - iter[n] immediately return a value rather than an iterator and didn't work
  well in that instance.
*/
#include <time.h>
#include <vector>
#include "Plant.h"
#include "Carnivore.h"
#include "Herbivore.h"
#include <algorithm>
#include <fstream>
using std::vector;
/*Precondition: herbies and plants are vectors of Herbivore and Plant respectively
  Postcondition: Every Herbivore in herbies will feed on Plant objects. Herbivores may starve
  and be removed from vector. Plants may die.*/
void Graze(vector<Herbivore> &herbies, vector<Plant> &plants);
/*Precondition: carnivores and herbies are vectors of Carnivore and Plant respectively
  Postcondition: Every Carnivore in carnivores will feed on herbivore objects from herbies. Carnivores may starve
  and be removed from vector. Herbivores may be eaten and removed from vector.*/
void Hunt(vector<Carnivore> &carnivores, vector<Herbivore> &herbies);
/*Precondition: out is a valid ostream, all integer inputs are initialized
  Postcondition: Weekly report information is placed in output stream in readable format*/
void Report(const int week, const int carnivores, const int herbivores, std::ostream& out);


int main () 
{
	srand(time(NULL));
	vector<Plant> Plants(30000);
	vector<Herbivore> Herbies(100);
	vector<Carnivore> Carnivores(5);

	std::ofstream fout("output.txt");
	fout.setf(std::ios::fixed);
	fout.setf(std::ios::showpoint);
	fout.precision(2);

	//Loop controlling iteration of weeks
	for(int i = 1; i <= 50; ++i)
	{
		std::for_each(Plants.begin(), Plants.end(), [](Plant &x) {x.Grow(); if(!x.IsAlive()) x.Sprout();} );
		Graze(Herbies, Plants);
		Hunt(Carnivores,Herbies);
		std::for_each(Carnivores.begin(), Carnivores.end(), [](Carnivore &x) {x.Grow();} );
		std::for_each(Herbies.begin(), Herbies.end(), [](Herbivore &x) {x.Grow();} );
		Herbivore::Reproduce(Herbies); 
		Carnivore::Reproduce(Carnivores);
		Report(i,Carnivores.size(), Herbies.size(), fout);
	}
	fout.close();
	return 0;
}

void Graze(vector<Herbivore> &herbies, vector<Plant> &plants)
{
	vector<Herbivore>::iterator herb;
	vector<Plant>::iterator eatMe = plants.begin();
	for(herb = herbies.begin(); herb != herbies.end();)
	{
		herb->StartWeek();
		for(int i = 0; i < 50 && (herb->GetAmountEaten() < herb->GetMass()*2); ++i)
			herb->Graze(eatMe[rand()%plants.size()]);
		//If herbivore hasn't eaten enough after it's 50 attempts, it dies
		if(herb->GetAmountEaten() < herb->GetMass()*2)
		{
			herb->Die();
			herb = herbies.erase(herb);
		}
		else
			++herb;
	}
}

void Hunt(vector<Carnivore> &carnivores, vector<Herbivore> &herbies)
{
	vector<Carnivore>::iterator carn; int eatMe;
	for(carn = carnivores.begin(); carn != carnivores.end();)
	{
		carn->StartWeek();
		for(int i = 0; i < 15 && (carn->GetAmountEaten() < carn->GetMass()); ++i)
		{
			double odds = (static_cast<double>(herbies.size())/5.0)*10;
			if(rand() % 1000 <= static_cast<int>(odds) )
			{
				if(herbies.size() == 0) break; //Prevent divide by zero errors
				//Eat an herbivore, swap it to the end of the vector and pop it off.
				eatMe = rand() % herbies.size();
				carn->Hunt(herbies[eatMe]);
				herbies[eatMe].Die();
				std::swap(herbies[eatMe], herbies.back());
				herbies.pop_back();
			}

		}
		//If the carnivore hasn't eaten enough it starves here.
		if(carn->GetAmountEaten() < carn->GetMass() )
		{
			carn->Die();
			carn = carnivores.erase(carn);
		}
		else
			++carn;
	}
}

void Report(const int week, const int carnivores, const int herbivores, std::ostream& out)
{
	out << "WEEK: " << week << "\n" 
		<< "PLANT MASS: " << Plant::getTotalMass() << "\n"
		<< "HERBIVORES: " << herbivores << "\t"
		<< "Average Mass: " << Herbivore::getTotalMass()/herbivores << "\n"
		<< "CARNIVORES: " << carnivores << "\t"
		<< "Average Mass: " << Carnivore::getTotalMass()/carnivores << "\n";
	out << std::endl;
}