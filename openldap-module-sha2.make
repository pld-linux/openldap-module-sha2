# $Id$

CFLAGS = -Wall -g

slapd-sha2.so: slapd-sha2.o sha2.o
	$(CC) -I$(OPENLDAPINC) -shared -Wall -g $^ -o $@

%.o: %.c
	$(CC) -I$(OPENLDAPINC) $(CFLAGS) -fPIC -c $<

clean:
	@rm -f slapd-sha2.so *.o
