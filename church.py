# Implementation of Church encoding in Python
# http://en.wikipedia.org/wiki/Church_encoding

TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y
Product = lambda x: lambda y: lambda z: (z)(x)(y)
And = lambda x: lambda y: (x)(y)(x)
Not = lambda x: lambda y: lambda z: (x)(z)(y)
Boolean = (Product)(True)(False)
Succ = lambda x: lambda y: lambda z: (y)((x)(y)(z))
Pred = lambda x: lambda y: lambda z: x(lambda i: lambda j: j(i(y))) (lambda k: z) (lambda k: k)

Zero = FALSE
One = Succ(Zero)
Two = Succ(One)
Six = Succ(Succ(Succ(Succ(Two))))

Y = lambda g: (lambda z:z(z)) (lambda f: g(lambda arg: f(f)(arg)))
Nth = Y(lambda f: lambda n: Succ(f(n-1)) if n else Zero)
Dec = lambda a: (a)(lambda b: b + 1)(0)

Add = lambda x: lambda y: lambda z: lambda w: (x)(z)((y)(z)(w))
Sub = lambda x: lambda y: (y)(Pred)(x)
Mul = lambda x: lambda y: lambda z: (y)((x)(z))

Null = lambda x: x(lambda y: Zero)(TRUE)
Eq = lambda x: lambda y: (And)((Null)((Sub)(y)(x)))((Null)((Sub)(x)(y)))
Gt = lambda x: lambda y: (And)((Null)((Sub)(y)(x)))((Not)((Eq)(y)(x)))
Lt = lambda x: lambda y: (And)((Not)((Gt)(x)(y)))((Not)((Eq)(x)(y)))

IfThenElse = lambda a: lambda b: lambda c: ((a)(b))(c)
Range = lambda a,b: map(Nth,range(a,b))

Fact = Y(lambda f: lambda n: IfThenElse((Gt)(n)(One))(Mul(n)(f(Pred(n))))(One))
Fib = Y(lambda f: lambda n: Add(f(Pred(n)))(f((Sub)(n)(Two))) if (Boolean)((Gt)(n)(One)) else n)	
Fib = lambda x:(lambda a:(a)(lambda b:b+1)(0))(((lambda g:(lambda f:g(lambda arg:f(f)(arg))) (lambda f:g(lambda arg:f(f)(arg))))(lambda f:lambda n:(lambda x:lambda y:lambda z:lambda w:(x)(z)((y)(z)(w)))(f((lambda x:lambda y:lambda z:x(lambda i:lambda j:j(i(y))) (lambda k:z) (lambda k:k))(n)))(f(((lambda x:lambda y:(y)((lambda x:lambda y:lambda z:x(lambda i:lambda j:j(i(y))) (lambda k:z) (lambda k:k)))(x)))(n)(((lambda x:lambda y:lambda z:(y)((x)(y)(z)))(((lambda x:lambda y:lambda z:(y)((x)(y)(z)))((lambda x:lambda y:y)))))))) if ((((lambda x:lambda y:lambda z:(z)(x)(y)))(lambda x:lambda y:x)(False)))(((lambda x:lambda y:(lambda x:lambda y:(x)(y)(x))(((lambda x:x(lambda y:(lambda x:lambda y:y))(lambda x:lambda y:x)))(((lambda x:lambda y:(y)((lambda x:lambda y:lambda z:x(lambda i:lambda j:j(i(y))) (lambda k:z) (lambda k:k)))(x)))(y)(x)))(((lambda x:lambda y:lambda z:(x)(z)(y)))(((lambda x:lambda y:(lambda x:lambda y:(x)(y)(x))(((lambda x:x(lambda y:(lambda x:lambda y:y))(lambda x:lambda y:x)))(((lambda x:lambda y:(y)((lambda x:lambda y:lambda z:x(lambda i:lambda j:j(i(y))) (lambda k:z) (lambda k:k)))(x)))(y)(x)))(((lambda x:x(lambda y:(lambda x:lambda y:y))(lambda x:lambda y:x)))(((lambda x:lambda y:(y)((lambda x:lambda y:lambda z:x(lambda i:lambda j:j(i(y))) (lambda k:z) (lambda k:k)))(x)))(x)(y)))))(y)(x)))))(n)(((lambda x:lambda y:lambda z:(y)((x)(y)(z)))((lambda x:lambda y:y))))) else n))(((lambda g:(lambda f:g(lambda arg:f(f)(arg))) (lambda f:g(lambda arg:f(f)(arg))))(lambda f:lambda n:(lambda x:lambda y:lambda z:(y)((x)(y)(z)))(f(n-1)) if n else (lambda x:lambda y:y)))(x)))
