class Solution:
    def isValid(self, s: str) -> bool:
        count_op_par = 0
        count_cl_par = 0
        count_op_sh = 0
        count_cl_sh = 0
        count_op_del = 0
        count_cl_del = 0

        in_dict = {"{" : "}", "(" : ")", "[": "]"}
        # for i in s:
        #     if (i == '('):
        #         count_op_par += 1
        #     elif (i == ')'):
        #         count_cl_par += 1
        #     elif (i == '{'):
        #         count_op_sh += 1
        #     elif (i == '}'):
        #         count_cl_sh += 1
        #     elif (i == '['):
        #         count_op_del += 1
        #     elif (i == ']'):
        #         count_cl_del += 1
        
        # if (count_op_par != count_cl_par):
        #     return False
        # if (count_op_sh != count_cl_sh):
        #     return False
        # if (count_op_del != count_cl_del):
        #     return False
        # return True
        # if (len(s) % 2 != 0):
        #     return False
        
        # i = 0
        # start = 0
        # end = 0
        # break_here = True
        # while i < len(s):
        #     if (s[i] == '(' or s[i] == '{' or s[i] == '['):
        #         start = i
        #         end = start + 1
        #         while break_here:
        #             if (s[end] == ')' or s[end] == '}' or s[end] == ']'):
        #                 if (in_dict[s[start]] != s[end]):
        #                     return False
        #                 elif(in_dict[s[start]] == s[end]):
        #                     break
        #             if ( (end + 1) < len(s) ):
        #                 end += 1
        #         if (start + 1 == end):
        #             i = start + 2
        #         else:
        #             i = start + 1
        #     else:
        #         return False

        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
