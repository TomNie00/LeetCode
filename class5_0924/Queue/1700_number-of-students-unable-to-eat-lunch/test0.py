from collections import deque

class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """

        qstudent = deque(students)
        qsandwiches = deque(sandwiches)
        num = 0

        while qstudent:
            if num == len(qstudent):
                return len(qstudent)

            if qsandwiches[0] == qstudent[0]:
                num = 0
                qstudent.popleft()
                qsandwiches.popleft()
            else:
                num += 1
                qstudent.append(qstudent.popleft())

        return 0

if __name__ == "__main__":
    obj = Solution()
    students = [1, 1, 0, 0]
    sandwiches = [0, 1, 0, 1]
    res = obj.countStudents(students,sandwiches)
    print(res)
