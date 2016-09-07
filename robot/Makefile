CC=gcc
CFLAGS=-c -Wall -I/usr/local/include
LDFLAGS=-lSDL_gfx -lSDLmain -lSDL -lfann -lm
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
