class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        for hour in range(0,12):
            for minute in range(0,60):
                if (bin(hour) + bin(minute)).count('1') == num:
                    result.append('%d:%02d' % (hour, minute))
                    
        return result