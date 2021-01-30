def maxMeeting(pres, n):
    ans = []
    pres.sort(key = lambda x: x[1])
    ans.append(pres[0][2])
    time_limit = pres[0][1]
     
    # Check for all meeting whether it
    # can be selected or not.
    for i in range(1, n):
        if pres[i][0] > time_limit:
            ans.append(pres[i][2])
            time_limit = pres[i][1]
             
    # Print final selected meetings
    for i in ans:
        print(i + 1, end = " ")
         
    print()

def maxEvents(arrival, duration):
    a = arrival
    b = [ arrival[i] + duration[i] for i in range(len(arrival)) ]
    pres = []
    for i in range(len(a)):
        pres.append([a[i],b[i],i])
    
    ans = []
    n = len(a)
    pres.sort(key = lambda x: x[1])
    ans.append(pres[0][2])
    time_limit = pres[0][1]
     
    for i in range(1, n):
        if pres[i][0] >= time_limit:
            ans.append(pres[i][2])
            time_limit = pres[i][1]
             
    return len(ans)



if __name__ == "__main__":
    arrival = [1,3,5]
    duration = [2,2,2]
    result = maxEvents(arrival, duration)
    print('Result = {}'.format((result)))