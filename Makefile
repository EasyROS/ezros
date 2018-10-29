make:

	./workspace build

install:

	./workspace install

clean:

	./workspace clean

novision:

	./workspace build:novision

setup:

	./workspace setup

cleannv:

	./workspace clean:novision

test:

	./workspace build:test
	
cleantest:

	./workspace clean:test
