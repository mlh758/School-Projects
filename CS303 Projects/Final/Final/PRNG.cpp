#include "PRNG.h"

/* 
This code uses the RC4 algorithm. This algorithm was kept as a trade secret and 
posted anonymously on the internet in 1994. It has since been "officially" released
to the public and formed the basis of the original Wireless Encryption Protocol
(WEP). However, weaknesses were found in it which led to its rapid abandonment. 

The RC4 algorithm has a problem in that 1 key in 256 are weak, meaning that
a few bytes of the key are strongly correlated with a few positions in the state 
table. Various other weaknesses have been found as well, including one in which 
the algorithm can be completely cracked if certain parts of the secret key are 
known.  

So RC4 may or may not be the ideal cryptographic application for high-security 
situations. However, we're primarily interested in generating some pseudo-random 
bytes and turning them into ints, floats, and chars. As a random-number generator, 
this implementation is several orders of magnitude better than the system supplied 
method: larger range of values, no sequential correlation, etc. I make no claims 
that it is the best possible method or is random "enough" for a given application. 


Late addendum: The algorithm has been modified to the much-stronger RC4A algorithm
described in 

  "A new weakness in the RC4 Keystream Generator and an approach to improve the 
    security of the cipher."  

  Souradyuti Paul and Bart Preneel
Katholieke Universiteit Leuven, Dept. ESAT/COSIC,
Kasteelpark Arenberg 10,
B-3001 Leuven-Heverlee, Belgium
{Souradyuti.Paul,Bart.Preneel}@esat.kuleuven.ac.be

http://www.esat.kuleuven.ac.be/~psourady/research/mypapers/paulv2a.pdf
    
The modified algorithm uses 2 tables with each controlling the state of the other,
to reduce correlation between output bytes and to increase independence of the
key and early output. This algorithm at least avoids some of the weaknesses of 
'original' RC4. It has not been analyzed as extensively as an encryption method, 
and so may have other, as yet undiscovered, weaknesses. However, it passes several
tests which RC4 fails, and again, our purpose here isn't finding the ultimate
encryption algorithm, it's generating some pseudorandom bits. 

Later addendum: RC4A has been broken, and the paper mentioned above has been withdrawn. 
RC4A should not be used for cryptographic purposes, period. This is still a better-than-
plain-vanilla RNG, but when C++ 11 (which uses the Mersenne Twister algorithm), comes out, 
this code should be retired.  


*/ 


PRNG::PRNG(string KeyPhrase)
{
    Reset(KeyPhrase);
}

void PRNG::Reset(string KeyPhrase)
{
    int buf[65600] = {0}; 
    int idx1, idx2, len; 

    len = int(KeyPhrase.length()); 
    idx1 = 0; 
    for (idx2 = 0; idx2 < ARRSIZE; idx2++)
    {
        S1[idx2] = S2[idx2] = idx2; 

        buf[idx2] = (KeyPhrase[idx1++]) << 8;
        idx1 %= len;
        buf[idx2] += KeyPhrase[idx1++];
        idx1 %= len;
    }
    j1 = 0; 
    for (i = 0; i < ARRSIZE; i++)
    {
        j1 = j1 + S1[i] + buf[i];
        j1 %= ARRSIZE; 
        swap(S1[i], S1[j1]);
    }
    // Now use table 1 to generate (via "standard" RC4) the next keystream
    i = j1 = 0; 
    for (idx1 = 0; idx1 < ARRSIZE; idx1++)
    {
        i = (i + 1) % ARRSIZE; 
        j1 = (j1 + S1[i]) % ARRSIZE; 
        swap(S1[i], S1[j1]);
        buf[idx1] = (S1[i] + S1[j1]) % ARRSIZE; 
    }
    // Use this keystream to initialize 2nd S-box
    for (i = 0; i < ARRSIZE; i++)
    {
        j1 = (j1 + S2[i] + buf[i]) % ARRSIZE;
        swap(S2[i], S2[j1]);
    }
    i = j1 = j2 = 0; 
    S1Next = true;

    Stored = false; 
}

void PRNG::Reset() // reset using system info
{
    string key; 
    time_t tmp; 
    errno_t result;
    struct tm newtime;
    char buf[32];

    tmp = time(NULL);
    result = localtime_s(&newtime, &tmp); 
    if (result) // something went wrong
    {
        key = "jlksfdajklasdfjklasdf";
        Reset(key);
        cerr << "Problems resetting PRNG - couldn't read time." << endl;
        return;
    }
    // Now convert the time we have stored into a string (keyphrase) 
    asctime_s(buf, 32, &newtime);
    key = string(buf);
    Reset(key);
}

unsigned int PRNG::randInt()
{
    unsigned int result = 0; 
    
    result = unsigned(rand16BitInt()) << 16;
    result += unsigned(rand16BitInt());
    return result; 
}

unsigned int PRNG::randInt(unsigned int max)
{
    double temp = randReal(); 
    return static_cast<unsigned int>(temp * max);
}

double PRNG::randReal()    // double in range [0..1)
{
    unsigned int tmp; 
    double result; 

    tmp = randInt(); 
    result = static_cast<double>(tmp); 
    return (result / (0xFFFFFFFF + 1.0)); 
}

char PRNG::randAlphaNumeric()  // random single character
{
    char ch; 
    unsigned int tmp; 
    bool again; 

    do 
    {
        again = true; 
        tmp = randInt(95) + 32; 
        // this makes sure it's 0-9 or alpha (lower case), 
        // not punctuation or nonprintable
        if (tmp >= 48 && tmp <= 57) // it's a digit  
            again = false; 
        else if ( tmp >= 97 && tmp < 123) // it's a letter 
            again = false; 
    } while ( again); 
    ch = static_cast<char>(tmp); 
    return ch; 
}

string PRNG::randAlphaNumeric(int length)  // randomly-generated string
{
    string tmp; 
    for (int k = 0; k < length; k++)
        tmp += randAlphaNumeric();

    return tmp; 
} 

char PRNG::randDigit()
{
    char ch; 
    unsigned int tmp; 

    tmp = randInt(10) + 48; 
    ch = static_cast<int>(tmp); 
    return ch; 
}

char PRNG::randAlpha()
{
    char ch; 
    unsigned int tmp; 

    tmp = randInt(26) + 97; 
    ch = static_cast<int>(tmp); 
    return ch; 
}


string PRNG::randAlpha(int length)
{
    string tmp; 
    for (int k = 0; k < length; k++)
        tmp += randAlpha();

    return tmp; 
}

string PRNG::randDigit(int length)
{
    string tmp; 
    for (int k = 0; k < length; k++)
        tmp += randDigit();

    return tmp; 
}

int PRNG::rand16BitInt()
{
    int t; 

    if (S1Next)
    {
        S1Next = false;
        i = (i + 1) % ARRSIZE; 
        j1 = (j1 + S1[i]) % ARRSIZE; 
        swap(S1[i], S1[j1]);
        t = (S1[i] + S1[j1]) % ARRSIZE; 
        return S2[t];
    }
    else
    {
        S1Next = true;
        i = (i + 1) % ARRSIZE; 
        j2 = (j2 + S2[i]) % ARRSIZE;
        swap(S2[i], S2[j2]);
        t = (S2[i] + S2[j2]) % ARRSIZE; 
        return S1[t];
    }
}

double PRNG::randGaussian() // double, normal distribution, mean 0, variance 1 
{ 
    double x1, x2, y1, y2, w; 

    if (Stored)
    {
        Stored = false;
        return tStor;
    }
    else
    {
        do 
        {
            x1 = 2.0 * randReal() - 1.0;
            x2 = 2.0 * randReal() - 1.0;
            w = x1 * x1 + x2 * x2;
        } while ( w >= 1.0 );

        w = sqrt( (-2.0 * log( w ) ) / w );
        y1 = x1 * w;
        y2 = x2 * w;

        Stored = true;
        tStor = y1; 
        return y2;
    }
}


double PRNG::randExponential(double Mean)  // Exponentially distributed, must specify mean > 0. 
{                                          // if Mean <= 0, returns -1 & gripes to cerr. 
    if (Mean <= 0)
    {
        cerr << "Bad call to PRNG::randExponential(double M): M must be > 0, but " 
             << Mean << " was passed." << endl;
        return -1;
    }
    else
        return (-1 * Mean * log(randReal()));
}

int PRNG::randPoisson(double Mean)         // Poisson distribution with specified mean. If parameter < 0, 
{                                          //  returns -1 & gripes to cerr
    // Note: Running time increases linearly as mean. If this is a problem, a 
    // faster algorithm is needed. 
    // Knuth's algorithm: 
    double L, p = 1.0; 
    int k = 0; 
    
    if (Mean < 0) // Bad input, impossible request
    {
        cerr << "Error in PRNG::randPoisson(double M). M must be >= 0, but " 
             << Mean << " was received." << endl;
        return -1;
    }
    // otherwise input is legitimate & we can calculate this. 

    L = exp(-1.0 * Mean);

    do 
    {
        k++;
        p *= randReal();
    } while (p >= L); 
    return (--k);
}
