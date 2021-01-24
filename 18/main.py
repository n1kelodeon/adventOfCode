class Expression:
    def __init__(self, expression: str, is_root: bool, is_part_2: bool):
        self.left_expression = None
        self.right_expression = None
        self.value = None
        self.operator = None
        self._parse(expression, is_root, is_part_2)

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

    def _parse(self, expression: str, is_root: bool, is_part_2: bool):
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
                if is_part_2 and char == "+" and self._count_factors(expression) > 0:
                    continue
                self.operator = char
                left_expression_str = self._remove_outer_parantheses(expression[:i])
                right_expression_str = self._remove_outer_parantheses(
                    expression[i + 1 :]
                )
                self.left_expression = Expression(
                    left_expression_str, is_root=False, is_part_2=is_part_2
                )
                self.right_expression = Expression(
                    right_expression_str, is_root=False, is_part_2=is_part_2
                )
                break

    def _count_factors(self, expression: str) -> int:
        depth = 0
        factor_count = 0
        for token in expression:
            if token == "(":
                depth += 1
            elif token == ")":
                depth -= 1
            if token == "*" and depth == 0:
                factor_count += 1
        return factor_count

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


class Expression2(Expression):
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
                if char == "+" and self._count_factors(expression) > 0:
                    continue
                self.operator = char
                left_expression_str = self._remove_outer_parantheses(expression[:i])
                right_expression_str = self._remove_outer_parantheses(
                    expression[i + 1 :]
                )
                self.left_expression = Expression2(left_expression_str, is_root=False)
                self.right_expression = Expression2(right_expression_str, is_root=False)
                break

    def _count_factors(self, expression: str):
        depth = 0
        factor_count = 0
        for token in expression:
            if token == "(":
                depth += 1
            elif token == ")":
                depth -= 1
            if token == "*" and depth == 0:
                factor_count += 1
        return factor_count


def get_sum(expression_strings: list[str], is_part_2: bool) -> int:
    sum = 0
    for expression_str in expression_strings:
        sum += Expression(
            expression_str, is_root=True, is_part_2=is_part_2
        ).get_result()
    return sum


if __name__ == "__main__":
    with open("input.txt", "r") as file:
        expression_strings = file.read().splitlines()

    print("Part 1:", get_sum(expression_strings, is_part_2=False))
    print("Part 2:", get_sum(expression_strings, is_part_2=True))


# %%
