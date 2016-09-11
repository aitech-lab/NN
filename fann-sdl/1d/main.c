
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

  cortex_init(train_data);

  while(1) {
   
    while(SDL_PollEvent(&evt)) {
      
      if(evt.type == SDL_QUIT) {
        goto finish;
      }
      
      if (evt.type == SDL_KEYUP && evt.key.keysym.sym == SDLK_ESCAPE) {
        goto finish;
      }
    }

    SDL_LockSurface(screen);
    SDL_FillRect(screen, NULL, SDL_MapRGBA(screen->format, 0, 0, 0, 4)); 
    cortex_train();
    
    fann_type x[1];
    int i;
    for(i=0; i<train_data; ++i) {
      x[0] = (fann_type)i - train_data/2;
      fann_type* y = cortex_run(x);
      pixelColor(screen,
        i, SCREEN_H/2 - (int)y[0],
        0xFF7F7F7F);
    }
    
    for(i=0; i<train_data; i++) {
      fann_type* x = data->input [i];
      fann_type* y = data->output[i];
      pixelColor(screen, 
        (int)x[0]+train_data/2, SCREEN_H/2 - (int)y[0],
        0xFFFFFF7F);
    }

    SDL_FreeSurface(screen);
    SDL_Flip(screen);
  }
  
finish:
  
  cortex_destroy();
  
  SDL_FreeSurface(screen);
  SDL_Quit();

  return 0;
}
