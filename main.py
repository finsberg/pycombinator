def header(*args):
    print("\nHeader: ", *args)


def demo(*args):
    print("Demo: ", *args)


header("I := λx.x")
I = lambda x: x

tweet = "tweet"
chirp = "chirp"
demo("I tweet = tweet", I(tweet) == tweet)
demo("I chirp = chirp", I(chirp) == chirp)


demo("I I = I", I(I) == I)

# --- Self application

header("Mockingbird := M := ω := λf.ff")
ω = lambda fn: fn(fn)
M = ω
Mockingbird = M


demo("M I = I I = I", M(I) == I(I) and I(I) == I)

try:
    demo(M(M))
except RecursionError as ex:
    demo("M M = M M = M M = " + ex.args[0])


# --- Booleans

header("T := λxy.x")
T = lambda thn: lambda els: thn


header("F := λxy.y")
F = lambda thn: lambda els: els


def bool_value(value) -> str:
    if value == T:
        return "T"
    elif value == F:
        return "F"
    else:
        return str(value)


demo("T tweet chirp = tweet", T(tweet)(chirp) == tweet)
demo("F tweet chirp = chirp", F(tweet)(chirp) == chirp)


# --- Flipping arguments
header("Cardinal := C := flip := λfab.fba")
flip = lambda func: lambda a: lambda b: func(b)(a)
C = flip
Cardinal = C

header("F = C T")

demo("flip T tweet chirp = chirp", flip(T)(tweet)(chirp) == chirp)


# --- Negation
header("NOT := λb.bFT")
NOT = lambda chooseOne: chooseOne(F)(T)

demo("NOT T = F", NOT(T) == F)
demo("NOT F = T", NOT(F) == T)

demo("CF = T", C(F)(tweet)(chirp) == tweet)
demo("CT = F", C(T)(tweet)(chirp) == chirp)


# --- AND

header("AND := λpq.pqF")

AND = lambda p: lambda q: p(q)(F)

demo("AND F F = F", AND(F)(F) == F)
demo("AND T F = F", AND(T)(F) == F)
demo("AND F T = F", AND(F)(T) == F)
demo("AND T T = T", AND(T)(T) == T)


# --- OR

header("OR := λpq.pTq")
OR = lambda p: lambda q: p(T)(q)

demo("OR F F = F", OR(F)(F) == F)
demo("OR T F = T", OR(T)(F) == T)
demo("OR F T = T", OR(F)(T) == T)
demo("OR T T = T", OR(T)(T) == T)


demo("M F F = F", M(F)(F) == F)
demo("M T F = T", M(T)(F) == T)
demo("M F T = T", M(F)(T) == T)
demo("M T T = T", M(T)(T) == T)


# --- De Morgan's Laws

header("De Morgan: not (and P Q) = or (not P) (not Q)")


def deMorgansLawDemo(p, q):
    return NOT(AND(p)(q)) == OR(NOT(p))(NOT(q))


demo("NOT (AND F F) = OR (NOT F) (NOT F)", deMorgansLawDemo(F, F))
demo("NOT (AND T F) = OR (NOT T) (NOT F)", deMorgansLawDemo(T, F))
demo("NOT (AND F T) = OR (NOT F) (NOT T)", deMorgansLawDemo(F, T))
demo("NOT (AND T T) = OR (NOT T) (NOT T)", deMorgansLawDemo(T, T))


# --- Boolean equality

header("BEQ := λpq.p (qTF) (qFT)")
BEQ = lambda p: lambda q: p(q(T)(F))(q(F)(T))

demo("BEQ F F = T: ", bool_value(BEQ(BEQ(F)(F))(T)))
demo("BEQ F T = F: ", bool_value(BEQ(BEQ(F)(T))(F)))
demo("BEQ T F = F: ", bool_value(BEQ(BEQ(T)(F))(F)))
demo("BEQ T T = T: ", bool_value(BEQ(BEQ(T)(T))(T)))


# --- Numbers

header("Numbers")


# --- Zero

header("0 := λfx.x")


ZERO = lambda fn: lambda x: x
demo("0 M tweet = tweet", ZERO(M)(tweet) == tweet)


header("hard-coded 1 and 2")
header("1 := λfx.fx")

ONCE = lambda fn: lambda x: fn(x)
demo("1 I tweet = tweet", ONCE(I)(tweet) == tweet)


λ = "λ"
yell = lambda s: bool_value(s) + "!"

demo("0 yell λ = λ", ZERO(yell)(λ) == "λ")
demo("1 yell λ = yell λ = λ!", ONCE(yell)(λ) == "λ!")


header("2 := λfx.f(fx)")
TWICE = lambda fn: lambda x: fn(fn(x))

demo("2 yell λ = yell (yell λ) = λ!!", TWICE(yell)(λ) == "λ!!")


# --- Successor

header("SUCCESSOR")

header("SUCCESSOR := λnfx.f(nfx)")
SUCCESSOR = lambda num: lambda fn: lambda x: fn(num(fn)(x))


newOnce = SUCCESSOR(ZERO)
newTwice = SUCCESSOR(SUCCESSOR(ZERO))  # we can use multiple successors on zero, or…
newThrice = SUCCESSOR(newTwice)  # …apply successor to already-obtained numbers.

demo("1 yell λ = λ!", newOnce(yell)(λ) == "λ!")
demo("2 yell λ = λ!!", newTwice(yell)(λ) == "λ!!")
demo("3 yell λ = λ!!!", newThrice(yell)(λ) == "λ!!!")


# --- COMPOSITION AND POINT-FREE NOTATION

header("Bluebird := B := (∘) := compose := λfgx.f(gx)")
compose = lambda f: lambda g: lambda x: f(g(x))
B = compose
Bluebird = B

demo("(B NOT NOT)  T =  NOT (NOT T)", (B(NOT)(NOT))(T) == NOT(NOT(T)))
demo("(B yell NOT) F = yell (NOT F)", (B(yell)(NOT))(F) == yell(NOT(F)))

header("SUCC := λnf.f∘(nf) = λnf.Bf(nf)")
SUCC = lambda num: lambda fn: compose(fn)(num(fn))


n0 = ZERO
n1 = SUCC(n0)
n2 = SUCC(SUCC(n0))
n3 = SUCC(SUCC(SUCC(n0)))
n4 = SUCC(n3)

demo("1 yell λ = λ!", n1(yell)(λ) == "λ!")
demo("2 yell λ = λ!!", n2(yell)(λ) == "λ!!")
demo("3 yell λ = λ!!!", n3(yell)(λ) == "λ!!!")
demo("4 yell λ = λ!!!!", n4(yell)(λ) == "λ!!!!")


# --- ARITHEMTIC


header("ADD := λab.a(succ)b")
ADD = lambda numA: lambda numB: numA(SUCC)(numB)


n5 = ADD(n2)(n3)
n6 = ADD(n3)(n3)


demo("ADD 5 2 yell λ = λ!!!!!!!", ADD(n5)(n2)(yell)(λ) == "λ!!!!!!!")
demo("ADD 0 3 yell λ = λ!!!", ADD(n0)(n3)(yell)(λ) == "λ!!!")
demo("ADD 2 2 = 4", ADD(n2)(n2)(yell)(λ) == n4(yell)(λ))


header("LC <-> JS: church & jsnum")


def church(n: int):
    """Convert python integer to Church encodings"""
    return n0 if n == 0 else SUCC(church(n - 1))


def pynum(c):
    """Convert Curch encodings to python integer"""
    return c(lambda x: x + 1)(0)


demo("church(5) = n5", church(5)(yell)(λ) == n5(yell)(λ))
demo("pynum(n5) === 5", pynum(n5) == 5)
demo("pynum(church(2)) === 2", pynum(church(2)) == 2)


# --- Multiplication

header("MULT := λab.a∘b = compose")
MULT = compose


demo("MULT 1 5 = 5", pynum(MULT(n1)(n5)) == 5)
demo("MULT 3 2 = 6", pynum(MULT(n3)(n2)) == 6)
demo("MULT 4 0 = 0", pynum(MULT(n4)(n0)) == 0)
demo("MULT 6 2 yell λ = λ!!!!!!!!!!!!", MULT(n6)(n2)(yell)(λ) == "λ!!!!!!!!!!!!")

n8 = MULT(n4)(n2)
n9 = SUCC(n8)


# --- Power

header("Thrush := POW := λab.ba")
POW = lambda numA: lambda numB: numB(numA)
