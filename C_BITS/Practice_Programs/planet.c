#include <stdio.h>
#include <string.h>

#define MAX_PLANETS 1000

typedef struct {
    char planetName[50];
    float distanceFromEarth;
    float gravity;
    struct {
        float oxygenLevel;
        float carbonDioxideLevel;
        float nitrogenLevel;
    } atmosphere;
} Planet;

int selectionSort(Planet planets[], int size) {
    for (int i = 0; i < size - 1; i++) {
        int minIndex = i;
        for (int j = i + 1; j < size; j++) {
            if (planets[j].distanceFromEarth < planets[minIndex].distanceFromEarth) {
                minIndex = j;
            }
        }
        Planet temp = planets[i];
        planets[i] = planets[minIndex];
        planets[minIndex] = temp;
    }
}

void printHabitablePlanets(Planet planets[], int size) {
    for (int i = 0; i < size; i++) {
        if (planets[i].gravity >= 0.8 && planets[i].gravity <= 1.2 &&
            planets[i].atmosphere.oxygenLevel >= 18.0 &&
            planets[i].atmosphere.oxygenLevel <= 25.0) {
            printf("%s (%f light-years)\n", planets[i].planetName, planets[i].distanceFromEarth);
        }
    }
}

void searchByOxygenCarbonDioxide(Planet planets[], int size) {
    float minOxygen = 0.0;
    float maxCarbonDioxide = 0.0;

    printf("Enter minimum oxygen level: ");
    scanf("%f", &minOxygen);

    printf("Enter maximum carbon dioxide level: ");
    scanf("%f", &maxCarbonDioxide);

    for (int i = 0; i < size; i++) {
        if (planets[i].atmosphere.oxygenLevel >= minOxygen &&
            planets[i].atmosphere.carbonDioxideLevel <= maxCarbonDioxide) {
            printf("%s\n", planets[i].planetName);
        }
    }
}

void searchByKeyword(Planet planets[], int size, char* keyword) {
    for (int i = 0; i < size; i++) {
        if (strstr(planets[i].planetName, keyword)) {
            printf("%s\n", planets[i].planetName);
        }
    }
}

int main() {
    int numPlanets;
    Planet planets[MAX_PLANETS];

    printf("Enter number of planets: ");
    scanf("%d", &numPlanets);

    for (int i = 0; i < numPlanets; i++) {
        printf("Planet %d:\n", i + 1);
        printf("Name: ");
        fgets(planets[i].planetName, sizeof(planets[i].planetName), stdin);
        planets[i].planetName[strlen(planets[i].planetName) - 1] = '\0'; // remove newline character

        printf("Distance from Earth (in light years): ");
        scanf("%f", &planets[i].distanceFromEarth);

        printf("Gravity (in g): ");
        scanf("%f", &planets[i].gravity);

        printf("Oxygen level (in %): ");
        scanf("%f", &planets[i].atmosphere.oxygenLevel);
        planets[i].atmosphere.carbonDioxideLevel = 0.04; // default carbon dioxide level
        planets[i].atmosphere.nitrogenLevel = 78.00 - planets[i].atmosphere.oxygenLevel;

        printf("\n");
    }

    while (1) {
        printf("Menu:\n");
        printf("Print habitable planets sorted by distance\n");
        printf("Find planets by oxygen and carbon dioxide levels\n");
        printf("Search for planets by keyword in their name\n");
        printf("Exit\n");

        int choice;
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                selectionSort(planets, numPlanets);
                printHabitablePlanets(planets, numPlanets);
                break;

            case 2: {
                float minOxygen = 0.0;
                float maxCarbonDioxide = 0.0;

                printf("Enter minimum oxygen level: ");
                scanf("%f", &minOxygen);

                printf("Enter maximum carbon dioxide level: ");
                scanf("%f", &maxCarbonDioxide);

                searchByOxygenCarbonDioxide(planets, numPlanets);
            }
            break;

            case 3: {
                char keyword[50];
                printf("Enter keyword to search for in planet names: ");
                fgets(keyword, sizeof(keyword), stdin);
                keyword[strlen(keyword) - 1] = '\0'; // remove newline character

                searchByKeyword(planets, numPlanets, keyword);
            }
            break;

            case 4:
                printf("Exiting Program.\n");
                return 0;

            default:
                printf("Invalid choice. Please try again.\n");
        }

        printf("\nMenu:\n");
    }

    return 0;
}