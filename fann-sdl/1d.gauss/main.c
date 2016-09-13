
//   $ clang -g -lSDL_gfx -lSDLmain -lSDL -o sdl_test sdl_test.c

#include <SDL/SDL.h>
#include <SDL/SDL_gfxPrimitives.h>

#include "cortex.h"

#define SCREEN_W 1200
#define SCREEN_H  600

unsigned int train_data = SCREEN_W;

int main(int argc, char *argv[]) {

  SDL_Event evt; 
  
  if (SDL_Init(SDL_INIT_VIDEO) != 0) {
    return -1;
  }

  SDL_Surface *screen = SDL_SetVideoMode(
    SCREEN_W, 
    SCREEN_H, 
    24, SDL_SWSURFACE | SDL_DOUBLEBUF);

  if (screen == NULL) {
    return -1;
  }

  printf("Press 'R' to randomize weights\n\n");
  
  cortex_init();
  int k = 0;
  while(1) {
   
    while(SDL_PollEvent(&evt)) {
      
      if(evt.type == SDL_QUIT) {
        goto finish;
      }
      
      if(evt.type == SDL_KEYUP){
        if(evt.key.keysym.sym == SDLK_ESCAPE) goto finish;
        if(evt.key.keysym.sym == SDLK_r) cortex_randomize();
        boxColor(screen, 0, 0, SCREEN_W, SCREEN_H, 0x00000FF); 
      }

    }

    SDL_LockSurface(screen);
    if(k%10==0) boxColor(screen, 0, 0, SCREEN_W, SCREEN_H, 0x000000F); 
    cortex_train();
    
    int i;

    unsigned int train_size = cortex_train_size();
    for(i=0; i<train_size; i++) {
      fann_type* x = data->input [i];
      fann_type* y = data->output[i];
      pixelColor(screen, 
        SCREEN_W/2.0 + (int)(x[0]*SCREEN_H/2.0), 
        SCREEN_H/2.0 - (int)(y[0]*SCREEN_H/2.0),
        0xFFFFFF1F);
    }

    fann_type x[1];
    for(i=0; i<SCREEN_W; i++) {
      x[0] = (fann_type)i/SCREEN_W*4.0-2.0;
      fann_type* y = cortex_run(x);
      pixelColor(screen,
        i, 
        SCREEN_H/2 - (int)(y[0]*SCREEN_H/2.0),
        0xFF2F2F4F);
    }

    SDL_FreeSurface(screen);
    SDL_Flip(screen);
    k++;
  }
  
finish:
  
  cortex_destroy();
  
  SDL_FreeSurface(screen);
  SDL_Quit();

  return 0;
}
