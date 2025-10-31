class LexicalError(Exception):
    pass

class ParsingError(Exception):
    pass

class TokenType:
    INTEGER = "INTEGER"
    PLUS    = "PLUS"
    MINUS   = "MINUS"
    MUL     = "MUL"
    DIV     = "DIV"
    LPAREN  = "LPAREN"
    RPAREN  = "RPAREN"
    EOF     = "EOF"

class Token:
    def __init__(self, type_, value):
        self.type  = type_
        self.value = value
    def __repr__(self):
        return f"Token({self.type}, {self.value!r})"

class Lexer:
    def __init__(self, text: str):
        self.text = text
        self.pos = 0
        self.current_char = text[self.pos] if text else None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        digits = []
        while self.current_char is not None and self.current_char.isdigit():
            digits.append(self.current_char)
            self.advance()
        if not digits:
            raise LexicalError("Очікував цифру")
        return int("".join(digits))

    def get_next_token(self):
        while self.current_char is not None:
            ch = self.current_char

            if ch.isspace():
                self.skip_whitespace()
                continue

            if ch.isdigit():
                return Token(TokenType.INTEGER, self.integer())

            if ch == '+':
                self.advance()
                return Token(TokenType.PLUS, '+')

            if ch == '-':
                self.advance()
                return Token(TokenType.MINUS, '-')

            if ch == '*':
                self.advance()
                return Token(TokenType.MUL, '*')

            if ch == '/':
                self.advance()
                return Token(TokenType.DIV, '/')

            if ch == '(':
                self.advance()
                return Token(TokenType.LPAREN, '(')

            if ch == ')':
                self.advance()
                return Token(TokenType.RPAREN, ')')

            raise LexicalError(f"Невідомий символ: {ch!r}")

        return Token(TokenType.EOF, None)

# --- AST вузли ---
class AST: pass

class Num(AST):
    def __init__(self, token: Token):
        self.token = token
        self.value = token.value

class UnaryOp(AST):
    def __init__(self, op: Token, expr: AST):
        self.op = op
        self.expr = expr

class BinOp(AST):
    def __init__(self, left: AST, op: Token, right: AST):
        self.left = left
        self.op = op
        self.right = right

# --- Parser з пріоритетами ---
class Parser:
    def __init__(self, lexer: Lexer):
        self.lexer = lexer
        self.current_token = lexer.get_next_token()

    def error(self, msg="Помилка синтаксичного аналізу"):
        raise ParsingError(msg)

    def eat(self, type_):
        if self.current_token.type == type_:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error(f"Очікував {type_}, отримав {self.current_token.type}")

    def factor(self):
        """
        factor := (PLUS|MINUS) factor | INTEGER | LPAREN expr RPAREN
        """
        tok = self.current_token

        if tok.type in (TokenType.PLUS, TokenType.MINUS):
            self.eat(tok.type)
            node = UnaryOp(tok, self.factor())
            return node

        if tok.type == TokenType.INTEGER:
            self.eat(TokenType.INTEGER)
            return Num(tok)

        if tok.type == TokenType.LPAREN:
            self.eat(TokenType.LPAREN)
            node = self.expr()
            self.eat(TokenType.RPAREN)
            return node

        self.error("factor")

    def term(self):
        """
        term := factor ((MUL|DIV) factor)*
        """
        node = self.factor()
        while self.current_token.type in (TokenType.MUL, TokenType.DIV):
            op = self.current_token
            if op.type == TokenType.MUL:
                self.eat(TokenType.MUL)
            else:
                self.eat(TokenType.DIV)
            node = BinOp(node, op, self.factor())
        return node

    def expr(self):
        """
        expr := term ((PLUS|MINUS) term)*
        """
        node = self.term()
        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token
            if op.type == TokenType.PLUS:
                self.eat(TokenType.PLUS)
            else:
                self.eat(TokenType.MINUS)
            node = BinOp(node, op, self.term())
        return node

    def parse(self):
        node = self.expr()
        if self.current_token.type != TokenType.EOF:
            self.error("Зайві символи після виразу")
        return node

# --- Інтерпретатор ---
class Interpreter:
    def visit(self, node: AST):
        method = getattr(self, f"visit_{type(node).__name__}", None)
        if not method:
            raise Exception(f"Немає методу visit_{type(node).__name__}")
        return method(node)

    def visit_Num(self, node: Num):
        return node.value

    def visit_UnaryOp(self, node: UnaryOp):
        val = self.visit(node.expr)
        if node.op.type == TokenType.PLUS:
            return +val
        else:
            return -val

    def visit_BinOp(self, node: BinOp):
        left = self.visit(node.left)
        right = self.visit(node.right)
        t = node.op.type
        if t == TokenType.PLUS:
            return left + right
        if t == TokenType.MINUS:
            return left - right
        if t == TokenType.MUL:
            return left * right
        if t == TokenType.DIV:
            return left / right
        raise Exception(f"Невідома операція: {t}")

def evaluate(text: str):
    lexer = Lexer(text)
    parser = Parser(lexer)
    tree = parser.parse()
    interp = Interpreter()
    return interp.visit(tree)

def repl():
    print('Введіть вираз (або "exit" для виходу):')
    while True:
        s = input('> ').strip()
        if s.lower() == "exit":
            print("Вихід із програми.")
            break
        try:
            print(evaluate(s))
        except Exception as e:
            print("Помилка:", e)

if __name__ == "__main__":
    repl()
