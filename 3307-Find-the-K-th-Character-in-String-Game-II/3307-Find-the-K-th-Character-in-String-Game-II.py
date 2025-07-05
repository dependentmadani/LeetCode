class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        pos = k - 1
        shifts = 0
        
        length = 1
        op_lengths = []
        
        for op in operations:
            length *= 2
            op_lengths.append((op, length))
        
        for op, current_length in reversed(op_lengths):
            half = current_length // 2
            
            if op == 0:
                if pos >= half:
                    pos -= half
            else:
                if pos >= half:
                    pos -= half
                    shifts += 1
            
            pos %= half
        
        return chr(ord('a') + (shifts % 26))
