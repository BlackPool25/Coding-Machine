#include <stdio.h>
#include <string.h>

#define MAX_PLANETS 100

struct atmosphere
{
    float oxygen;
    float carbonDioxide;
    float nitrogen;
};

struct planet
{
    char planetName[50];
    float distanceFromEarth;
    float gravity;
    struct atmosphere atmo;
    char habitable;
};

// Function to check habitability
char isHabitable(float gravity, float oxygen)
{
    if (gravity >= 0.8 && gravity <= 1.2 && oxygen >= 18 && oxygen <= 25)
        return 'Y';
    return 'N';
}

// Function to swap two planets (used in sorting)
void swap(struct planet *a, struct planet *b)
{
    struct planet temp = *a;
    *a = *b;
    *b = temp;
}

// Selection Sort function to sort planets by distance
void selectionSort(struct planet planets[], int n)
{
    int i, j, min_idx;
    for (i = 0; i < n - 1; i++)
    {
        min_idx = i;
        for (j = i + 1; j < n; j++)
        {
            if (planets[j].distanceFromEarth < planets[min_idx].distanceFromEarth)
            {
                min_idx = j;
            }
        }
        swap(&planets[min_idx], &planets[i]);
    }
}

int main()
{
    int n, i, in;
    char nameKeyword[50];
    float oxyThreshold, co2Threshold;

    printf("Enter the number of planets: ");
    scanf("%d", &n);

    struct planet planets[MAX_PLANETS];

    // Input handling for planet details
    for (i = 0; i < n; i++)
    {
        printf("Enter Planet Name: ");
        scanf("%s", planets[i].planetName);

        printf("Enter Distance from Earth (in light-years): ");
        scanf("%f", &planets[i].distanceFromEarth);

        printf("Enter Planet Gravity (in terms of g): ");
        scanf("%f", &planets[i].gravity);

        printf("Enter Atmosphere Composition (Oxygen, Carbon Dioxide, Nitrogen) as percentages: ");
        scanf("%f %f %f", &planets[i].atmo.oxygen, &planets[i].atmo.carbonDioxide, &planets[i].atmo.nitrogen);

        // Check habitability and store result in 'habitable' field
        planets[i].habitable = isHabitable(planets[i].gravity, planets[i].atmo.oxygen);
    }

    while (1)
    {
        // Menu options
        printf("\nMENU\n1. Find and print all habitable planets\n2. Search by oxygen and carbon dioxide levels\n3. Search by keyword in planet names\n4. Exit\n");
        scanf("%d", &in);

        switch (in)
        {
        case 1:
            // Sort planets by distance using Selection Sort
            selectionSort(planets, n);
            printf("Habitable planets (sorted by distance from Earth):\n");
            for (i = 0; i < n; i++)
            {
                if (planets[i].habitable == 'Y')
                {
                    printf("%s - %.2f light-years\n", planets[i].planetName, planets[i].distanceFromEarth);
                }
            }
            break;

        case 2:
            printf("Enter minimum oxygen level threshold: ");
            scanf("%f", &oxyThreshold);

            printf("Enter maximum carbon dioxide level threshold: ");
            scanf("%f", &co2Threshold);

            printf("Planets with oxygen > %.2f%% and carbon dioxide < %.2f%%:\n", oxyThreshold, co2Threshold);
            for (i = 0; i < n; i++)
            {
                if (planets[i].atmo.oxygen > oxyThreshold && planets[i].atmo.carbonDioxide < co2Threshold)
                {
                    printf("%s\n", planets[i].planetName);
                }
            }
            break;

        case 3:
            printf("Enter a keyword to search in planet names: ");
            scanf("%s", nameKeyword);

            printf("Planets matching the keyword \"%s\":\n", nameKeyword);
            for (i = 0; i < n; i++)
            {
                if (strstr(planets[i].planetName, nameKeyword) != NULL)
                {
                    printf("%s\n", planets[i].planetName);
                }
            }
            break;

        case 4:
            printf("Exiting...\n");
            return 0;

        default:
            printf("Invalid input\n");
            break;
        }
    }
}
