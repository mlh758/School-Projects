#ifndef PRNG_H
#define PRNG_H

#include <iostream>
#include <string>
#include <ctime>
#include <cmath>
using namespace std; 

/*
Portable random number generator
Brian Hare 
briankhare@gmail.com
All rights reserved. Permission granted for educational use ONLY. 

This generator uses the RC4A algorithm to generate pseudorandom 32-bit values. It 
can also return values within a specified range, or alphanumeric characters or strings. 

Although the RC4A algorithm is very good, it is not perfect, and in fact has some 
known weaknesses. Thus, this PRNG, while more than adequate for most uses including 
generating data for simulations, etc., should not be used in high-security applications
such as generating encryption keys, where it is critical that the output be as close 
to truly random as practicable. Likewise, this PRNG is purely deterministic. The Reset() 
function uses the time of day clock to produce mildly-unpredictable initialization, but 
again, this is obviously inadequate for many applications. Using the Reset(string) 
function with a radix-64 encoded initialization vector may be a better way of going about 
things, but hasn't been explored systematically (at least not by me). 

*/


#define ARRSIZE 65536

class PRNG
{
public:
    PRNG( string KeyPhrase = "I have a dog, his name is Phideaux"); 
    void Reset( string KeyPhrase); // resets generator using specified password
    void Reset();         // resets using time of day & system info as pseudorandom seed

    unsigned int randInt();        // uniform unsigned int 

    unsigned int randInt(unsigned int max); // uniform int in range 0 - (max-1)

    double randReal();    // uniform double in range [0..1)

    double randGaussian(); // double, normal distribution, mean 0, variance 1 

    double randExponential(double Mean);  // Exponentially distributed, must specify mean > 0. 
                                          // if Mean <= 0, returns -1 & gripes to cerr. 

    int randPoisson(double Mean);         // Poisson distribution with specified mean. If parameter < 0, 
                                          //  returns -1 & gripes to cerr

    string randAlphaNumeric(int length);  // randomly-generated string

    char randAlphaNumeric();  // random single character

    char randDigit(); 

    char randAlpha(); 

    string randAlpha(int length);

    string randDigit(int length);

private:
    int i, j1, j2; 
    unsigned int S1[ARRSIZE], S2[ARRSIZE]; 
    bool S1Next;
    int rand16BitInt(); 
    double tStor; 
    bool Stored;
}; 

#endif 

