
test:
	./compute_pmi.py -n 1000 -c 3-.konec.txt

full_david:
	./compute_pmi.py -n 100000000 -c 3-.konec.txt

COMPONENTSDIR=depot/components

tex2txt:
	mkdir -p $(COMPONENTSDIR)
	./tex2txt.py $(COMPONENTSDIR) < billion_data.tex

PMIDIR=depot/pmi

N=1000

txt2pmi:
	mkdir -p $(PMIDIR)
	for f in $(COMPONENTSDIR)/?[+-]*.txt; do \
		echo Computing PMI for $$(basename $$f); \
		./compute_pmi.py -n $N -c $$f \
		> $(PMIDIR)/$$(basename $$f).out \
		2> $(PMIDIR)/$$(basename $$f).err \
		; done

