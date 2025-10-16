# python
## 1.python 之简单输入输出
```python
print('The quick brown fox', 'jumps over', 'the lazy dog')
输出显示The quick brown fox jumps over the lazy dog
print()会依次打印每个字符串，遇到逗号,会输出一个空格，因此，输出的字符串是这样拼起来的
```
Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里.
```python
name = input()
print('hello,', name)

name = input('please enter your name: ')
print('hello,', name)

```

