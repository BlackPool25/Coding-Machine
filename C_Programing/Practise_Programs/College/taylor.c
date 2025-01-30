
#include <stdio.h>
#include <math.h>

// Function to calculate factorial
double factorial(int n) {
    double fact = 1;
    for (int i = 1; i <= n; i++) {
        fact *= i;
    }
    return fact;
}

// Function to compute sine using Taylor series
double computeSine(double x, int terms) {
    double sine = 0.0;
    for (int n = 0; n < terms; n++) {
        double term = pow(-1, n) * pow(x, 2 * n + 1) / factorial(2 * n + 1);
        sine += term;
    }
    return sine;
}

// Function to compute cosine using Taylor series
double computeCosine(double x, int terms) {
    double cosine = 0.0;
    for (int n = 0; n < terms; n++) {
        double term = pow(-1, n) * pow(x, 2 * n) / factorial(2 * n);
        cosine += term;
    }
    return cosine;
}

int main() {
    double x, taylorTan, libraryTan;
    int terms;

    // Input the angle in degrees and the number of terms for Taylor series
    printf("Enter the angle in degrees: ");
    scanf("%lf", &x);
    printf("Enter the number of terms for the Taylor series approximation: ");
    scanf("%d", &terms);

    // Convert the angle to radians
    x = x * M_PI / 180.0;

    // Compute sine and cosine using Taylor series
    double sine = computeSine(x, terms);
    double cosine = computeCosine(x, terms);

    // Avoid division by zero
    if (cosine == 0.0) {
        printf("Error: Tangent is undefined for this angle (cosine is zero).\n");
        return 1;
    }

    // Compute tangent using Taylor series
    taylorTan = sine / cosine;

    // Compute tangent using library function
    libraryTan = tan(x);

    // Print results
    printf("\nResults:\n");
    printf("Taylor series approximation of tan(x): %.10f\n", taylorTan);
    printf("Library function value of tan(x): %.10f\n", libraryTan);

    // Print inference
    printf("\nInference:\n");
    if (fabs(taylorTan - libraryTan) < 0.0001) {
        printf("The Taylor series approximation is accurate to 4 decimal places.\n");
    } else {
        printf("The Taylor series approximation deviates significantly from the library function.\n");
    }

    return 0;
}