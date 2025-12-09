#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<math.h>
#define RANGE 300 // empirical cdf sort from 0.00 to 3.00 with interval 0.01

float generator();
float F_Y_inverse(float U, float lambda);

int main(void)
{
    // initialize variables
    int i, j;
    int count;
    float lambda;
    float X, U;
    int freq_index;
    int freq[RANGE] = {};
    float cdf[RANGE] = {}; // cumulation of freq

    // randomize the seed
    srand((unsigned int)time(0));

    // set the # of case and parameter for RV
    printf("count : ");
    scanf("%d", &count);
    printf("lambda : ");
    scanf("%f", &lambda);

    // sampling
    for(i=0; i<count; i++)
    {
        U = generator();
        X = F_Y_inverse(U, lambda);

        freq_index = (int)(X*100); // calibrating
        if(freq_index < RANGE) freq[freq_index] += 1;
    }
    
    // get cdf
    for(i=0; i<RANGE; i++)
        for(j=i; j<RANGE; j++)
            cdf[j] += freq[i];
    for(i=0; i<RANGE; i++)
        cdf[i] /= count;

    // print cdf from 0.00 to 3.00 with interval 0.01
    for(i=0; i<RANGE; i++)
        printf("empirical CDF(%.2f) = %.3f\n", (float)i/100, cdf[i]);
    return 0;
}

float generator()
{
    return (float)rand()/RAND_MAX;
}

float F_Y_inverse(float U, float lambda)
{
    return -log((double)1-U)/lambda;
}
