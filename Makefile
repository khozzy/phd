.PHONY: graphs book

graphs:
	find graphs/ -type f -name "*.gv" | xargs -I '{}' dot -Gdpi=200 -Tpng {} -o book/_static/{}.png

book: graphs
	jupyter-book build -W -n --keep-going --all book/

publish: book
	(cd book && ghp-import -n -p -f _build/html)

notebook:
	jupyter notebook book/