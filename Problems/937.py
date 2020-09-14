class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter = sorted([ log for log in logs if not log.split(' ')[1].isdigit()], key=lambda x:(x.split(' ')[1:],x.split(' ')[0]))
        digit = [ log for log in logs if log.split(' ')[1].isdigit()]
        return letter + digit