all: reliable_dict/reliabledict.so

reliable_dict/reliabledict.so: reliable_dict/reliable_dict/build_reliabledict.py
	python3 $<
