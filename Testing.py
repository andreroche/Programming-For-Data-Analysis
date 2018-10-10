# do not run this script / it does not run. This is just copied from the ipython editor for reference


In [1]: a= 3

In [2]: a+1
Out[2]: 4

In [3]: type(2)
Out[3]: int

In [4]: type(4.1)
Out[4]: float

In [5]: int(3.8)
Out[5]: 3

In [6]: int(3.9)
Out[6]: 3

In [7]: float(3.9)
Out[7]: 3.9

In [8]: from fractions import Fraction

In [9]: f = Fraction(3,4)

In [10]: f
Out[10]: Fraction(3, 4)

In [11]: float (f)
Out[11]: 0.75

In [12]: int(f)
Out[12]: 0

In [13]: Fration(3,4) +1 +1.5
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-13-3ebcb20b62d0> in <module>()
----> 1 Fration(3,4) +1 +1.5

NameError: name 'Fration' is not defined

In [14]: Fraction(3,4) +1 +1.5
Out[14]: 3.25

In [15]: Fraction (3,4) +1 + Fraction(1/4)
Out[15]: Fraction(2, 1)

In [16]: Float(2/1)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-16-52cdbd904e11> in <module>()
----> 1 Float(2/1)

NameError: name 'Float' is not defined

In [17]: float(2/1)
Out[17]: 2.0

In [18]: a = 2 +3j

In [19]: type (a)
Out[19]: complex

In [20]: a = complex (2+3)

In [21]: type (a)
Out[21]: complex

In [22]: a
Out[22]: (5+0j)

In [23]: b = 3 +3j

In [24]: a+b
Out[24]: (8+3j)

In [25]: a-b
Out[25]: (2-3j)

In [26]: a*b
Out[26]: (15+15j)

In [27]: a/b
Out[27]: (0.8333333333333334-0.8333333333333334j)

In [28]: a / b
Out[28]: (0.8333333333333334-0.8333333333333334j)

In [29]: z = 2 + 3j

In [30]: z.real
Out[30]: 2.0

In [31]: z.float
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-31-0719e513ad2a> in <module>()
----> 1 z.float

AttributeError: 'complex' object has no attribute 'float'

In [32]: z.real
Out[32]: 2.0

In [33]: z.imag
Out[33]: 3.0

In [34]: z.conjugate()
Out[34]: (2-3j)

In [35]: (z.real**2 + z.imag**2) **0.5
Out[35]: 3.605551275463989

In [36]: absolute (z)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-36-b7bbc8cddb32> in <module>()
----> 1 absolute (z)

NameError: name 'absolute' is not defined

In [37]: abs(z)
Out[37]: 3.605551275463989

In [38]: a= input()
1

In [39]: a
Out[39]: '1'

In [40]: a = input ()
45

In [41]: a
Out[41]: '45'

In [42]: b = input()
34

In [43]: b
Out[43]: '34'

In [44]: a+b
Out[44]: '4534'

In [45]: a=input()
2

In [46]: b=input()
4

In [47]: b
Out[47]: '4'

In [48]: a
Out[48]: '2'

In [49]: a + b
Out[49]: '24'

In [50]: a = input (int)
<class 'int'>a

In [51]: a
Out[51]: 'a'

In [52]: a = input (int a)
  File "<ipython-input-52-b329725decda>", line 1
    a = input (int a)
                   ^
SyntaxError: invalid syntax


In [53]: a
Out[53]: 'a'

In [54]:  a = '1'

In [55]: int(a) + 1
Out[55]: 2

In [56]: float(a) +1
Out[56]: 2.0

In [57]: int('a)
  File "<ipython-input-57-1554d0e628dc>", line 1
    int('a)
           ^
SyntaxError: EOL while scanning string literal


In [58]: int('a')
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-58-b3c3f4515dd4> in <module>()
----> 1 int('a')

ValueError: invalid literal for int() with base 10: 'a'

In [59]: a=float(input())
2.5

In [60]: a
Out[60]: 2.5

In [61]: b=float(input())
4.2

In [62]: a+b
Out[62]: 6.7

In [63]: try:
    ...:     a=float(input('enter number:'))
    ...:     except Value Error:
  File "<ipython-input-63-6092262737c6>", line 3
    except Value Error:
         ^
SyntaxError: invalid syntax


In [64]: try:
    ...:     a = float(input('enter a number: '))
    ...:     except ValueError:
  File "<ipython-input-64-21a19c64aadb>", line 3
    except ValueError:
         ^
SyntaxError: invalid syntax


In [65]: print('you have entered an invalid number')
you have entered an invalid number

In [66]: print('you have entered an invalid number')
you have entered an invalid number

In [67]: try:
    ...:     a = float(input('enter a number: '))
    ...:     except Value Error:
  File "<ipython-input-67-d85a213354a7>", line 3
    except Value Error:
         ^
SyntaxError: invalid syntax


In [68]: try:
    ...:     a = float(input('enter a number: '))
    ...:     Except ValueError:
  File "<ipython-input-68-27a541dd388f>", line 3
    Except ValueError:
                    ^
SyntaxError: invalid syntax


In [69]: try:
    ...:     a = float(input('enter a number: '))
    ...:     except ValueError:
  File "<ipython-input-69-21a19c64aadb>", line 3
    except ValueError:
         ^
SyntaxError: invalid syntax


In [70]: try:
    ...:     a = float(input('enter a number: '))
    ...:     ValueError:
  File "<ipython-input-70-3e1ceb8e2a95>", line 3
    ValueError:
               ^
SyntaxError: invalid syntax


In [71]: try:
    ...:     a = float(input('enter a number: '))
    ...: except ValueError:
    ...:     print (@you have entered an invalid number')
  File "<ipython-input-71-4f6e8c0712bb>", line 4
    print (@you have entered an invalid number')
           ^
SyntaxError: invalid syntax


In [72]: try:
    ...:     a = float(input('enter a number: '))
    ...: except ValueError:
    ...:     print ('you have entered an invalid number')
    ...:
enter a number: r
you have entered an invalid number

In [73]:

In [73]: try:
    ...:     a = float(input('enter a number: '))
    ...: except ValueError:
    ...:     print ('you have entered an invalid number')
    ...:
enter a number: 4

In [74]: try:
    ...:     a = float(input('enter a number: '))
    ...: except ValueError:
    ...:     print ('you have entered an invalid number')
    ...:
enter a number: 1/4
you have entered an invalid number

In [75]: try:
    ...:     a = Fraction(input('enter a number: '))
    ...: except ValueError:
    ...:     print ('you have entered an invalid number')
    ...:
enter a number: 2

In [76]: try:
    ...:     a = Fraction(input('enter a number: '))
    ...: except ValueError:
    ...:     print ('you have entered an invalid number')
    ...:
enter a number: 3/2

In [77]: try:
    ...:     a = Fraction(input('enter a number: '))
    ...: except ValueError:
    ...:     print ('you have entered an invalid number')
    ...:
enter a number: 3

In [78]: try:
    ...:     a = float(input('enter a number: '))
    ...: except ValueError:
    ...:     print ('you have entered an invalid number')
    ...:
enter a number: 4.9

In [79]: 3/4
Out[79]: 0.75

In [80]: try:
    ...:     a = float(input('enter a number: '))
    ...: except ValueError:
    ...:     print ('you have entered an invalid number')
    ...:
enter a number: 3/4
you have entered an invalid number

In [81]:
In [81]: a = input('input an interger: ')
input an interger: 1

In [82]: a
Out[82]: '1'

In [83]: a = int( input('input an interger: '))
input an interger: 1

In [84]: a
Out[84]: 1

In [85]: 1.1.is_interger()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-85-f0c28f3d134e> in <module>()
----> 1 1.1.is_interger()

AttributeError: 'float' object has no attribute 'is_interger'

In [86]: 1.is_integer()
  File "<ipython-input-86-50850b8473b0>", line 1
    1.is_integer()
               ^
SyntaxError: invalid syntax


In [87]: 1.1.is_integer()
Out[87]: False

In [88]: 1.is_integer()
  File "<ipython-input-88-50850b8473b0>", line 1
    1.is_integer()
               ^
SyntaxError: invalid syntax


In [89]: 1.0.is_integer()
Out[89]: True

In [90]: a =Fraction(input('Enter a fraction: '))
Enter a fraction: 1/2

In [91]: a
Out[91]: Fraction(1, 2)

In [92]: float(a)
Out[92]: 0.5

In [93]: try:
    ...:     a = Fraction(input('Enter a fraction: '))
    ...: except ZeroDivisionError:
    ...:     print('Invalid fraction')
    ...:
Enter a fraction: 3/0
Invalid fraction

In [94]: try:
    ...:     a = Fraction(input('Enter a fraction: '))
    ...: except ZeroDivisionError:
    ...:     print('Invalid fraction')
    ...:
Enter a fraction: 4/8

In [95]: z  = complex(input('Enter a complex number: '))
Enter a complex number: 2+3j

In [96]: z
Out[96]: (2+3j)

In [97]: z  = complex(input('Enter a complex number: '))
Enter a complex number: 2 + 3j
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-97-a3f5bc46fb80> in <module>()
----> 1 z  = complex(input('Enter a complex number: '))

ValueError: complex() arg is a malformed string

In [98]: def is factor(a,b):
  File "<ipython-input-98-6e8249d58d9e>", line 1
    def is factor(a,b):
         ^
SyntaxError: invalid syntax


In [99]: def is_factor(a,b):
    ...:     if b % a == 0:
    ...:         return true
    ...:     else:
    ...:         return false
    ...:

In [100]: is_factor(4,1024)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-100-f3736261172d> in <module>()
----> 1 is_factor(4,1024)

<ipython-input-99-a8573509fb0d> in is_factor(a, b)
      1 def is_factor(a,b):
      2     if b % a == 0:
----> 3         return true
      4     else:
      5         return false

NameError: name 'true' is not defined

In [101]: def is_factor(a,b):
     ...:     if b % a == 0:
     ...:         return True
     ...:     else:
     ...:         return False
     ...:

In [102]:

In [102]: def is_factor(a,b):
     ...:     if b % a == 0:
     ...:         return True
     ...:     else:
     ...:         return False
     ...:

In [103]: is_factor(4,1024)
Out[103]: True

In [104]: is_factor(15,1024)
Out[104]: False

In [105]: Calc_Factors.py
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-105-d44f51c9d689> in <module>()
----> 1 Calc_Factors.py

NameError: name 'Calc_Factors' is not defined

In [106]: exit()

C:\Users\aroche2\Desktop\GMIT PYTHON2>python Calc_Factors.py
  File "Calc_Factors.py", line 3
    def is_factor(a,b)
                     ^
SyntaxError: invalid syntax

C:\Users\aroche2\Desktop\GMIT PYTHON2>python Calc_Factors.py
  File "Calc_Factors.py", line 11
    except ValueError:
                     ^
IndentationError: unindent does not match any outer indentation level

C:\Users\aroche2\Desktop\GMIT PYTHON2>python Calc_Factors.py
  File "Calc_Factors.py", line 12
    print ('you have entered an invalid number')
        ^
IndentationError: expected an indented block

C:\Users\aroche2\Desktop\GMIT PYTHON2>python Calc_Factors.py
enter a number: 1
enter a number: 2
True

C:\Users\aroche2\Desktop\GMIT PYTHON2>python Calc_Factors.py
enter a number: 5
enter a number: 7
False

C:\Users\aroche2\Desktop\GMIT PYTHON2>ipython
Python 3.6.3 |Anaconda custom (64-bit)| (default, Oct 15 2017, 03:27:45) [MSC v.1900 64 bit (AMD64)]
Type 'copyright', 'credits' or 'license' for more information
IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: for i in range(1,4)
  File "<ipython-input-1-f7b63d80463d>", line 1
    for i in range(1,4)
                       ^
SyntaxError: invalid syntax


In [2]: for i in range(1,4):
   ...:     print (i)
   ...:
1
2
3

In [3]: i
Out[3]: 3

In [4]: for i in range(1,4):
   ...:     print (i)
   ...:
1
2
3

In [5]: for i in range (1,17):
   ...:     print(i)
   ...:
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16

In [6]: for i in range (1,17,2):
   ...:     print(i)
   ...:
1
3
5
7
9
11
13
15

In [7]: