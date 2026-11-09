def occurs_check(var, expr):
    if var == expr:
        return True
    elif isinstance(expr, tuple):
        return any(occurs_check(var, arg) for arg in expr[1:])
    return False

def apply_substitution(subst, expr):
    if not subst:
        return expr
    if isinstance(expr, str):
        return subst.get(expr, expr)
    if isinstance(expr, tuple):
        op = expr[0]
        args = [apply_substitution(subst, arg) for arg in expr[1:]]
        return (op, *args)
    return expr

def unify(psi1, psi2):
    is_psi1_atom = isinstance(psi1, str)
    is_psi2_atom = isinstance(psi2, str)

    if is_psi1_atom or is_psi2_atom:
        if psi1 == psi2:
            return {}
        elif is_psi1_atom and psi1.islower():
            if occurs_check(psi1, psi2):
                return "FAILURE"
            return {psi1: psi2}
        elif is_psi2_atom and psi2.islower():
            if occurs_check(psi2, psi1):
                return "FAILURE"
            return {psi2: psi1}
        else:
            return "FAILURE"

    if psi1[0] != psi2[0]:
        return "FAILURE"

    if len(psi1) != len(psi2):
        return "FAILURE"

    subst = {}

    for i in range(1, len(psi1)):
        arg1 = apply_substitution(subst, psi1[i])
        arg2 = apply_substitution(subst, psi2[i])

        s = unify(arg1, arg2)

        if s == "FAILURE":
            return "FAILURE"

        if s != {}:
            for key, value in s.items():
                subst[key] = value

    return subst


exp1 = ('Eats', 'x', 'Apple')
exp2 = ('Eats', 'Riya', 'y')
print(unify(exp1, exp2))

exp3 = ('P', 'x', ('h', 'y'))
exp4 = ('P', 'a', ('f', 'z'))
print(unify(exp3, exp4))

exp5 = ('Knows', 'John', 'x')
exp6 = ('Knows', 'x', 'Elisabeth')
print(unify(exp5, exp6))

print()
print("SHRIHARI SUDHAKAR BADIGER: 1BM25CS522")