#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>


int main(int argc, char *argv[])
{

  long inputDifficulty = strtol(argv[1], NULL, 10);
  int difficultyFactor = inputDifficulty;
  //developer 'trusts' the input argument to be within the range 0-10000, creating a clear vector for a buffer overflow when setting the monsters array

  srand(1); 
  populateEnemies(difficultyFactor);

}

void populateEnemies( int difficultyFactor){
    int monsterHitpoints[10000]; 
    monsterHitpoints[0] = 0;

    for(int tile = 1 ; tile < difficultyFactor ; tile++){

    monsterHitpoints[tile] = spawn(monsterHitpoints[tile-1],difficultyFactor);
    printf("Monster on tile %i will have %i hitpoints\n",tile, monsterHitpoints[tile]);

  }
}

int spawn( int previousMonstersHitpoints, int difficultyFactor){
  //here tiles array is pass by reference

  int hitpoints = 0;
  while(1){
    hitpoints = rand() % difficultyFactor;

    int delta1 = hitpoints - previousMonstersHitpoints;
    int delta2 = previousMonstersHitpoints - hitpoints;

    if(delta1 <= 50 &&  delta1 > 0 ){
      return hitpoints;
    }

    if(delta2 <= 50 &&  delta2 > 0){
     return hitpoints;
    }

  }

}



