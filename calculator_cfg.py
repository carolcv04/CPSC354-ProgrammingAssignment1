from lark import Lark, Transformer, v_args
import math, sys

@v_args(inline=True)    # Affects the signatures of the methods
class CalculateTree(Transformer):
    from operator import add, sub, mul, truediv as div, neg
    number = int

    def __init__(self):
        self.vars = {}

    def assign_var(self, name, value):
        self.vars[name] = value
        return value

    def var(self, name):
        try:
            return self.vars[name]
        except KeyError:
            raise Exception("Variable not found: %s" % name)
        
    def exp(self, base, exponent):
        return base ** exponent
    
    def log(self, a, base):
        return math.log(a,(base))


calc_parser = Lark.open("grammar.lark", parser='lalr', transformer=CalculateTree())
calc = calc_parser.parse

def main():
    if len(sys.argv) > 1:
       result = calc(sys.argv[1])
       print(result)
    else:
        print("No equation provided.")
    
if __name__ == '__main__':
    main()