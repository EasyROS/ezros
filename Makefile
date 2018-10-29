make:

	./easy build

install:

	./easy install

clean:

	./easy clean

novision:

	./easy build:novision

setup:

	./easy setup

cleannv:

	./easy clean:novision

test:

	./easy build:test
	
cleantest:

	./easy clean:test
