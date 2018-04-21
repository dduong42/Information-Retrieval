txts := $(wildcard *.txt)

inverted_index: $(txts) create_inverted_index.py
	python3 create_inverted_index.py $(txts)

clean:
	rm -f inverted_index
