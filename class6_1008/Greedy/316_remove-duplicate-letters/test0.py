import collections
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # submit accept

        stack = []
        counter = collections.Counter(s)

        for i in s:
            if len(stack) == 0:
                stack.append(i)
                counter[i] -= 1
                continue

            if i in stack:
                counter[i] -= 1
                continue
            # have to check if i in stack if exist then skip because the stack has already sorted
            # and counter has to decrease too

            while len(stack) > 0 and stack[-1] >= i and counter[stack[-1]] > 0:
                # make sure we do not out of range and sort the elements in the stack
                # always keep the elements Ascending except the elements will never meet in the next
                stack.pop()

            stack.append(i)
            counter[i] -= 1

        return ''.join(stack)

    # def removeDuplicateLetters2(self, s: str) -> str:
    #     cnt = {}
    #     for c in s:
    #         if c in cnt:
    #             cnt[c] += 1
    #         else:
    #             cnt[c] = 1
    #
    #     res = ['0']
    #     visited = set()
    #     for c in s:
    #         cnt[c] -= 1
    #         if c in visited:
    #             continue
    #         last_one = res[-1]
    #         while last_one > c and cnt[last_one] > 0:
    #             visited.remove(res.pop())
    #             last_one = res[-1]
    #         res.append(c)
    #         visited.add(c)
    #
    #     return ''.join(res[1:])
    #
    # def recursive(self, orig_s, idx_so_far, sol_so_far, result, counter):
    #         cur_char = orig_s[idx_so_far]
    #         if counter[cur_char] == 1:
    #             sol_so_far.append(cur_char)
    #             self.recursive(orig_s, idx_so_far + 1, sol_so_far, result, counter)
    #         else:
    #             # # not added, check if it has occurrence in the future
    #             if cur_char not in orig_s[idx_so_far + 1:]:
    #                 # cur_char is the last occurrence
    #                 sol_so_far.append(cur_char)
    #                 self.recursive(orig_s, idx_so_far + 1, sol_so_far, result, counter)
    #                 sol_so_far.pop()
    #             else:
    #                 # choose cur_char
    #                 sol_so_far.append(cur_char)
    #                 self.recursive(orig_s, idx_so_far + 1, sol_so_far, result, counter)
    #                 sol_so_far.pop()
    #                 # ignore cur_char
    #                 self.recursive(orig_s, idx_so_far + 1, sol_so_far, result, counter)
    #
    # def removeDuplicateLetters3(self, s: str) -> str:
    #         result = []
    #         sol_so_far = []
    #         counter = collections.Counter(s)
    #         self.recursive(s, 0, sol_so_far, result, counter)
    #         return result


if __name__ == '__main__':
    object = Solution()

    s = "cbacdcbc"
    s1 = "bcabc"
    s2 = "bbcaac"
    s3 = "abacb"
    res = object.removeDuplicateLetters(s)
    res1 = object.removeDuplicateLetters3(s)
    print(res, res1)
