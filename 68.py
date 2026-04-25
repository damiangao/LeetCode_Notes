class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        window = []
        buffer = 0
        ret = []
        for word in words:
            if window:
                next_buffer = buffer + 1 + len(word)
            else:
                next_buffer = buffer + len(word)
            if next_buffer > maxWidth:
                ret.append(self.add_newline(window, buffer, maxWidth))
                window = [word]
                buffer = len(word)
            elif next_buffer == maxWidth:
                window.append(word)
                ret.append(self.add_newline(window, next_buffer, maxWidth))
                window = []
                buffer = 0
            else:  
                window.append(word)
                buffer = next_buffer
        if window:
            last_line_words = " ".join(window)
            ret.append("".join([last_line_words, *[" "] * (maxWidth - len(last_line_words))]))
        return ret

    def add_newline(self, window, buffer, maxWidth):
        n = len(window)
        spaces = maxWidth - buffer + n - 1
        if n > 1:
            space_list = ["".join([" "] * (spaces // (n - 1)))] * (n - 1)
            for i in range(spaces % (n - 1)):
                space_list[i] += ' '
        else:
            space_list = ["".join([" "] * spaces)]

        space_list.append("")
        return "".join(list(itertools.chain.from_iterable(zip(window, space_list))))
