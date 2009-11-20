# $Id$

CCFLAGS = -Wall -g

slapd-sha2.so: slapd-sha2.o sha2.o
	$(CC) -I$(OPENLDAPINC) -shared -Wall -g $^ -o $@

%.o: %.c
	$(CC) -I$(OPENLDAPINC) $(CCFLAGS) -c $<

clean:
	@rm -f slapd-sha2.so *.o
