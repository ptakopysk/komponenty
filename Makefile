
test:
	./compute_pmi.py -n 1000 -c 3-.konec.txt

full_david:
	./compute_pmi.py -n 100000000 -c 3-.konec.txt

COMPONENTSDIR=depot/components

tex2txt:
	mkdir -p $(COMPONENTSDIR)
	./tex2txt.py $(COMPONENTSDIR) < billion_data.tex

PMIDIR=depot/pmi

N=1000000

T=20

P=*[+-]konec.txt

txt2pmi:
	mkdir -p $(PMIDIR)
	for f in $(COMPONENTSDIR)/$P; do \
		echo Computing PMI for $$(basename $$f); \
		./compute_pmi.py -n $N -t $T -c $$f \
		> $(PMIDIR)/$$(basename $$f).$N.out \
		2> $(PMIDIR)/$$(basename $$f).$N.err \
		; done

