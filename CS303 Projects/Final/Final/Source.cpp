/*
Michael Harris
mlh758@mail.umkc.edu
Final Project

The plain old quicksort with naive implementation runs fairly well on random numbers and with a larger
set of data to choose from the 3 way partitioning method I was using for the homework generated too much
overhead. I switched to the algorithm we used in class to demonstrate quicksort and noticed significant
improvement in runtime. On pre-sorted data or data with a lot of duplicates this algorithm isn't as effective
but for this project it seemed optimal.

Adding the median of three improvement gives more reliablility when there is some order to the data but the
overhead cost of finding medians on random data actually slowed the execution time down by roughly two seconds.
	An interesting note here is that if you call median of three ONLY to select your initial pivot and then just
	use the first item in the vector / array from that point forward you get a consistent speed increase. This
	method offers less protection from worst case scenarios though.

Adding Shell Sort for smaller data sets and multithreading the recursive calls offers a significant performance
increase. This dropped the runtime by nearly ten seconds in some cases. This method even beats the built in
sort function on both computers I tried it on. It should be noted however that while my method is faster on
random data sets it is highly likely that the built in sort does a better job avoiding worst case execution
times.

Since fewer tests are being done I send output to the console instead of the tests.txt file. Changing some comments
and a letter can set it back though if that is your preference.


*/

#include "Sorts.h"
#include "PRNG.h"
#include <iostream>
#include <ctime>
#include <fstream>

using std::cout;

void SortOperation (std::vector<int> &Table, void (*func)(std::vector<int>&, bool, std::ostream&), std::ostream& out)
{
	clock_t start = clock();
	(*func)(Table, false, out);
	clock_t finish = clock();
	out << (static_cast<double>(finish - start) / static_cast<double>(CLOCKS_PER_SEC));
}

int main()
{
	//std::ofstream fout("Tests.txt");
	PRNG randoms;
	//Build vector of functions for later use
	std::vector<void (*)(std::vector<int>&, bool, std::ostream&)> fasts;
	fasts.push_back(NaiveQuickSort);
	fasts.push_back(QuickSortMedian);
	fasts.push_back(QuickSort);

	//Test the multithreaded algorithms
	cout <<"\n----Testing Algorithms----\n";
	for(unsigned int i = 0; i < fasts.size(); i++)
	{
		//Build test vectors
		std::vector<int> rands;
		for(unsigned int j = 0; j < 10000000; j++)
		{
			rands.push_back(randoms.randInt());
		}
		if(i==0)
			cout << "Naive Algorithm----\n";
		if(i==1)
			cout << "Adding Median of Three----\n";
		if(i==2)
			cout << "Multithreading, Median of Three, ShellSort on small data---\n";
		SortOperation(rands, fasts[i], cout);
		cout << "\n";
	}
	//Test the std::sort method as well
	std::vector<int> rands;
	for(unsigned int j = 0; j < 10000000; j++)
	{
		rands.push_back(randoms.randInt());
	}
	cout << "Testing std::sort---\n";
	clock_t start = clock();
	std::sort(rands.begin(),rands.end());
	clock_t finish = clock();
	cout << (static_cast<double>(finish - start) / static_cast<double>(CLOCKS_PER_SEC));
	cout << std::endl;

	//fout.close();
	system("PAUSE");
	return 0;
}