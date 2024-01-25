## Links

[Extended Backus–Naur form](https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form)

[Context-Free grammar](https://en.wikipedia.org/wiki/Context-free_grammar)

[Formal grammar](https://en.wikipedia.org/wiki/Formal_grammar)

[Chomsky hierarchy](https://en.wikipedia.org/wiki/Chomsky_hierarchy)

[Finite-state machine](https://en.wikipedia.org/wiki/Finite-state_machine)

### A Grammar for Lox expressions

***Literals.*** Numbers, strings, Booleans, and nil.

***Unary expressions.*** A prefix ! to perform a logical not, and - to negate a number.

***Binary expressions.*** The infix arithmetic (+, -, *, /) and logic operators (==, !=, <, <=, >, >=)

***Parentheses.*** A pair of ( and ) wrapped around an expression.

```1 - (2 * 3) < 4 == false```

Grammar for those:

```bazaar

expression     → literal
               | unary
               | binary
               | grouping ;
               
literal        → NUMBER | STRING | "true" | "false" | "nil" ;
grouping       → "(" expression ")" ;
unary          → ( "-" | "!" ) expression ;
binary         → expression operator expression ;
operator       → "==" | "!=" | "<" | "<=" | ">" | ">="
               | "+"  | "-"  | "*" | "/" ;
```

