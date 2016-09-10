
//   $ clang -g -lSDL_gfx -lSDLmain -lSDL -o sdl_test sdl_test.c

#include <SDL/SDL.h>
#include <SDL/SDL_gfxPrimitives.h>

#include "cortex.h"

#define SCREEN_W  600
#define SCREEN_H  600

unsigned int train_data = 1000;

int main(int argc, char *argv[]) {

  SDL_Event evt; 
  int i,j;

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
    // SDL_FillRect(screen, NULL, 0x000080); 
    cortex_train();
    
    int scale = SCREEN_W/100;
    fann_type xy[2];
    fann_type* res;
    unsigned int col, r, g;
    
    for(i=0; i<100; ++i) {
      for(j=0; j<100; ++j) {
        xy[0] = (fann_type) i/50.0-1.0;
        xy[1] = (fann_type) j/50.0-1.0;
        res = cortex_run(xy);
        r = 0; g = 0;
        if(res[0]>0.0) {
          r = res[0]*0xA0;
        } else {
          g = -res[0]*0xA0;
        }
        col = 0x0000004F|(r<<24)|(g<<16);
        boxColor(screen,
           i   *scale, 
           j   *scale,
          (i+1)*scale, 
          (j+1)*scale, 
          col);
      }
    }

    for(i=0; i<train_data; i++) {
      fann_type x = (data->input[i][0]+1.0)*50.0;
      fann_type y = (data->input[i][1]+1.0)*50.0;
      if(data->output[i][0] > 0.1) {
        col = 0xFF00007F;
      } else if(data->output[i][0] < -0.1) {
        col = 0x00FF007F;
      } else {
        col = 0x0000FF7F;
      }
      boxColor(screen, 
        (int)  x   *scale+1, 
        (int)  y   *scale+1,
        (int) (x+1)*scale-2, 
        (int) (y+1)*scale-2, 
        col);
    }

    SDL_FreeSurface(screen);
    SDL_Flip(screen);
    // sleep(1);
  }
  
finish:
  
  cortex_destroy();
  
  SDL_FreeSurface(screen);
  SDL_Quit();

  return 0;
}
