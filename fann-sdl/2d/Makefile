CC=gcc
CFLAGS=-c -O3 -Wall -I/usr/local/include
LDFLAGS=-lSDL_gfx -lSDLmain -lSDL -ldoublefann -lm
SOURCES=main.c cortex.c
OBJECTS=$(SOURCES:.c=.o)
EXECUTABLE=main
 
all: $(SOURCES) $(EXECUTABLE)
	
$(EXECUTABLE): $(OBJECTS) 
	$(CC) $(OBJECTS) -o $@ $(LDFLAGS)

.c.o:
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm *.o
	rm $(EXECUTABLE)
