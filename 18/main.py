#%%


class Expression:
    def __init__(self, expression: str, is_root: bool):
        self.left_expression = None
        self.right_expression = None
        self.value = None
        self.operator = None
        self._parse(expression, is_root)

    def _remove_outer_parantheses(self, expression):
        if (expression[0], expression[-1]) != ("(", ")"):
            return expression
        simplified_expression = expression[1:-1]
        depth = 0
        for char in simplified_expression:
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
            if depth < 0:
                return expression
        return simplified_expression

    def _reverse_expression(self, expression: str) -> str:
        expression = expression[::-1]
        expression = expression.replace(" ", "")
        expression = expression.replace("(", "]")
        expression = expression.replace(")", "(")
        expression = expression.replace("]", ")")
        return expression

    def _parse(self, expression: str, is_root: bool):
        if expression.isdigit():
            self.value = int(expression)
            return
        if is_root:
            expression = self._reverse_expression(expression)
        depth = 0
        for i, char in enumerate(expression):
            if char == "(":
                depth += 1
            if char == ")":
                depth -= 1
            if char in ["+", "*"] and depth == 0:
                self.operator = char
                left_expression_str = self._remove_outer_parantheses(expression[:i])
                right_expression_str = self._remove_outer_parantheses(
                    expression[i + 1 :]
                )
                self.left_expression = Expression(left_expression_str, is_root=False)
                self.right_expression = Expression(right_expression_str, is_root=False)
                break

    def get_result(self) -> int:
        if self.operator is None:
            return self.value
        if self.operator == "+":
            return (
                self.left_expression.get_result() + self.right_expression.get_result()
            )
        if self.operator == "*":
            return (
                self.left_expression.get_result() * self.right_expression.get_result()
            )


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        expression_strings = file.read().splitlines()

    sum = 0
    for expression_str in expression_strings:
        sum += Expression(expression_str, is_root=True).get_result()
    print("Part 1:", sum)
