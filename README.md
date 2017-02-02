# lazyme
Lazy python recipes.


Install
====

```
pip install -U lazyme
```


Usage
====

```python
$ cat test.txt 
This is a text block start
This is the end

And this is another
with more than one line
and another line.

$ python
>>> from lazyme import per_section
>>> list(per_section(open('test.txt')))
[['This is a text block start', 'This is the end'], ['And this is another', 'with more than one line', 'and another line.']]
```
