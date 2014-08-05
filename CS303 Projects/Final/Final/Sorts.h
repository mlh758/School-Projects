#pragma once

#include <vector>
#include <thread>
#include <future>
#include <iostream>
#include <set>
//Not necessary but it pulls in all kinds of cool OMP stuff
#include <omp.h>


inline int median(std::vector<int> &Table, int a, int b, int c)
{
	int Tmp[3]; 
	Tmp[0] = a; 
	Tmp[1] = b; 
	Tmp[2] = c; 
	if (Table[Tmp[0]] > Table[Tmp[1]]) 
		std::swap(Tmp[0], Tmp[1]);
	if (Table[Tmp[1]] > Table[Tmp[2]])
		std::swap(Tmp[1], Tmp[2]); 
	if (Table[Tmp[0]] > Table[Tmp[1]]) 
		std::swap(Tmp[0], Tmp[1]);
	
	return Tmp[1];
}
int min(int a, int b)
{
	return (a < b) ? a:b;
}


//ShellSort for QuickSort calling
void ShellSort(std::vector<int> &Table, int begin, int end)
{
	//Based on algorithm from:
	//http://www.codingbot.net/2013/05/shell-sort-c-code-and-algorithm.html
	int gaps[] = {132, 57, 23, 10, 4, 1};

	for(int g = 0; g < 6; g++)
	{
		for (int i = begin + gaps[g]; i <= end; i++)
		{
			int temp = Table[i];
			int j = i;
			for (j; j >= gaps[g] && Table[j - gaps[g]] > temp; j -= gaps[g])
			{
				Table[j] = Table[j - gaps[g]];
			}
			Table[j] = temp;
		} 
	}
}


void quicksort(std::vector<int>& Table, int begin, int end)
{
	//Essentially the quicksort we practiced in class
	if(end-begin < 100)
	{
		ShellSort(Table, begin, end); 
		return;
	}

	int idx = median(Table, begin, end, (begin+end)/2);
	int pivot = Table[idx];
	int i = begin, j = end+1;
	std::swap(Table[begin], Table[idx]);

	while(true)
	{
		//Move i and j
		while(Table[++i] < pivot && i < end);
		while(Table[--j] > pivot && j > begin);

		if(i <j)
			std::swap(Table[i], Table[j]);
		else
			break;
	}

	std::swap(Table[begin],Table[j]);
	#pragma omp parallel sections
	{
		#pragma omp section
	quicksort(Table,begin,j-1);
		#pragma omp section
	quicksort(Table,j+1,end);
	}
}
//void quicksort(std::vector<int>& Table, int begin, int end)
//{
//	//Based on your algorithm provided in the e-mail, just with shellsort
//	//Combined with algorithm that Yama used from a textbook for 
//	//more efficient segmenting
//	if(end-begin < 100)
//		{
//			ShellSort(Table, begin, end); 
//			return;
//		}
//
//	int idx = median(Table,begin,end,(begin+end)/2);
//	int pivot = Table[idx];
//	std::swap(Table[begin],Table[idx]);
//	
//	int current = begin+1, //Current item being examined
//		less = begin+1, //Rightmost item less than pivot
//		greater = end; //Leftmost item greater than pivot
//
//	while(current <= greater)
//	{
//		if(Table[current] < pivot)
//		{
//			if(less != current)
//				std::swap(Table[less],Table[current]);
//			++less; ++current;
//		}
//		else if(Table[current] > pivot)
//		{
//			std::swap(Table[greater],Table[current]);
//			--greater;
//		}
//		else
//			++current;
//	}
//	std::swap(Table[begin],Table[--less]);
//	#pragma omp parallel sections
//	{
//		#pragma omp section
//		{
//			quicksort(Table,begin,less);
//		}
//		#pragma omp section
//		{
//			quicksort(Table,greater+1,end);
//		}
//	}
//}

void QuickSort(std::vector<int>& Table, bool report = false, std::ostream& out = std::cout)
{
	if(report) out << __FUNCTION__ << std::endl;
	quicksort(Table, 0, Table.size() - 1);
}


void naivequicksort(std::vector<int>& Table, int begin, int end)
{
	//Essentially the quicksort we practiced in class
	if(end <= begin) return;

	int pivot = Table[begin];
	int i = begin, j = end+1;

	while(true)
	{
		//Move i and j
		while(Table[++i] < pivot && i < end);
		while(Table[--j] > pivot && j > begin);

		if(i <j)
			std::swap(Table[i], Table[j]);
		else
			break;
	}

	std::swap(Table[begin],Table[j]);

	naivequicksort(Table,begin,j-1);
	naivequicksort(Table,j+1,end);
}

void NaiveQuickSort(std::vector<int>& Table, bool report = false, std::ostream& out = std::cout)
{
	if(report) out << __FUNCTION__ << std::endl;
	naivequicksort(Table, 0, Table.size() - 1);
}

void quicksortmedian(std::vector<int>& Table, int begin, int end)
{
	//Essentially the quicksort we practiced in class
	//Added median of three
	if(end <= begin) return;

	int idx = median(Table, begin, end, (begin+end)/2);
	int pivot = Table[idx];
	int i = begin, j = end+1;
	std::swap(Table[begin], Table[idx]);

	while(true)
	{
		//Move i and j
		while(Table[++i] < pivot && i < end);
		while(Table[--j] > pivot && j > begin);

		if(i <j)
			std::swap(Table[i], Table[j]);
		else
			break;
	}

	std::swap(Table[begin],Table[j]);

	quicksortmedian(Table,begin,j-1);
	quicksortmedian(Table,j+1,end);
}

void QuickSortMedian(std::vector<int>& Table, bool report = false, std::ostream& out = std::cout)
{
	if(report) out << __FUNCTION__ << std::endl;
	quicksortmedian(Table, 0, Table.size() - 1);
}
