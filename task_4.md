What are the differences between “arrow” and “traditional” functions in javascript?

1. Arrow functions have a shorter syntax. They can usually be written using one-liners with the `=>` symbol. A traditional function is more code-block-oriented.
2. Arrow functions do not require an explicit return. Traditional functions do need it.
3. Traditional functions can be used as constructors, making them suitable for OOP. Arrow functions cannot be used as constructors with the `new` keyword.
4. Arrow functions are more suitable for callbacks because they retain the `this` object of the context of the scope around the function. Traditional functions retain the global `this` object.