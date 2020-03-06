

class BracketsVerification:

    def read(self):
        to_verify = input()
        self.to_verify = to_verify

    def checkRightSymbols(self):
        right_symbols = "{}[]()<>"
        for i in self.to_verify:
            if i not in right_symbols:
                return False
        return True

    def correctBracketSequence(self):
        if not self.checkRightSymbols():
            return False
        to_verify_copy = self.to_verify
        while '()' in to_verify_copy or '[]' in to_verify_copy or '{}' in to_verify_copy or '<>' in to_verify_copy:
            to_verify_copy = to_verify_copy.replace('()', '')
            to_verify_copy = to_verify_copy.replace('[]', '')
            to_verify_copy = to_verify_copy.replace('{}', '')
            to_verify_copy = to_verify_copy.replace('<>', '')
        if len(to_verify_copy):
            return False
        return True


if __name__ == '__main__':
    verificator = BracketsVerification()
    verificator.read()
    print(verificator.checkRightSymbols())
    print(verificator.correctBracketSequence())





