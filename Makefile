.PHONY: book

book:
	jupyter-book build -W -n --keep-going --all book/

publish: book
	(cd book && ghp-import -n -p -f _build/html)

notebook:
	jupyter notebook book/