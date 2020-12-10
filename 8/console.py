import re


class Console:
    def __init__(self):
        self._accumulator = 0
        self._program_counter = 0
        self._instructions = []
        self._pc_history = set()

    def _parse_code(self, code: str):
        self._instructions = []
        code = code.splitlines()
        for instruction in code:
            re_result = re.search("(acc|jmp|nop) ((?:\+|-)[0-9]+)", instruction)
            operation = re_result.group(1)
            argument = int(re_result.group(2))
            self._instructions.append((operation, argument))

    def _set_program_counter(self, offset: int):
        self._pc_history.add(self._program_counter)
        self._program_counter += offset

    def _detect_stop_condition(self) -> int:
        if self._program_counter in self._pc_history:
            return 1
        if self._program_counter == len(self._instructions):
            return 0

    def _execute_instructions(self, do_reset_state=False) -> int:
        if do_reset_state:
            self._reset_state()
        return_code = self._detect_stop_condition()
        if return_code is not None:
            return return_code
        operation, argument = self._instructions[self._program_counter]
        if operation == "acc":
            self._accumulator += argument
            self._set_program_counter(1)
        elif operation == "jmp":
            self._set_program_counter(argument)
        elif operation == "nop":
            self._set_program_counter(1)
        return self._execute_instructions()

    def _reset_state(self):
        self._accumulator = 0
        self._program_counter = 0
        self._pc_history = set()

    def _print_return_code(self, return_code: int):
        if return_code == 0:
            print("exit(0): Program execution terminated")
        elif return_code == 1:
            print("exit(1): Execution was stopped due to infinite loop")

    def run(self, code: str) -> int:
        self._reset_state()
        self._parse_code(code)
        return_code = self._execute_instructions()
        self._print_return_code(return_code)
        return self._accumulator

    def fix_loop_and_run(self, code: str) -> int:
        self._parse_code(code)
        for i, (operation, argument) in enumerate(self._instructions):
            if operation == "acc": continue
            self._instructions[i] = (
                "nop" if operation == "jmp" else "jmp", argument)
            if self._execute_instructions(do_reset_state=True) == 0:
                self._print_return_code(0)
                return self._accumulator
            else:
                self._instructions[i] = (operation, argument)
        self._print_return_code(1)
        return self._accumulator

    @property
    def accumulator(self):
        return self._accumulator
