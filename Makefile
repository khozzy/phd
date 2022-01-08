build:
	jupyter-book build -W -n --keep-going --all book/

publish: build
	(cd book && ghp-import -n -p -f _build/html)
