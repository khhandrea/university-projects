#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define K 6
#define SAMPLE_NUM 500

unsigned int g(float Y, float* m_range);
float p_X(unsigned int X, float* m);

int main(void)
{
    // randomize seed
    srand(time(NULL));
    
    // declare variables
    unsigned int i, X;
    float Y;
    float m[K + 1], m_range[K + 1];
    m[0] = (float)2/38;
    m[1] = (float)4/38;
    m[2] = (float)7/38;
    m[3] = (float)12/38;
    m[4] = (float)7/38;
    m[5] = (float)4/38;
    m[6] = (float)2/38;
    for(i=0; i<K+1; i++)
    {
        // m[i] = (float)i/15; // define m_k
        m_range[i] = m[i] + ( i<1 ? 0 : m_range[i-1] );
    }
    int freq[K + 1] = {};

    // implement a function
    for(i=0; i<SAMPLE_NUM; i++)
    {
        Y = (float)rand() / RAND_MAX; // Y : [0, 1]
        X = g(Y, m_range);
        freq[X] += 1;
    }

    // print the result
    for(i=0; i<K+1; i++)
        printf("p_X(%2d) : %.2f, Empirical p_X(%2d) : %.2f\n", i, m[i], i, (float)freq[i]/SAMPLE_NUM);

    return 0;
}

unsigned int g(float Y, float* m_range)
{
    unsigned int i;
    for(i=0; Y > m_range[i]; i++){}
    return i;
}

float p_X(unsigned int X, float* m)
{
    return m[X];
}
