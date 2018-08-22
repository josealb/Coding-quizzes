def normalize_angle(angle):
    while angle > 360:
        angle -= 360
    while angle < 0:
        angle += 360
    return angle

def angle_is_between(alphaMin,alphaMax,angle):
    if alphaMin<alphaMax:
        return angle>=alphaMin and angle<=alphaMax
    elif alphaMin>alphaMax:
        return angle<=alphaMax or angle>=alphaMin
    #They can't be the same because the inputs are checked before

def distance_is_between(Pmin,P,Pmax):
    return P>=Pmin and P<=Pmax

def check_box_corner(P2,alpha2,P1_min,P1_max,alpha1_min,alpha1_max):
    if distance_is_between(P1_min,P2,P1_max):
            if angle_is_between (alpha1_min,alpha1_max,alpha2):
                return True

def check_box_overlap(P1,alpha1,L1,delta1,P2,alpha2,L2,delta2):
    #Assumption: length in meters is positive
    if L1<=0 or L2<=0:
        raise ValueError('Box length has to be larger than zero')
    if delta1 <=0 or delta2 <= 0:
        raise ValueError('Box width has to be larger than zero')

    P1_min = P1
    P1_max = P1 + L1

    alpha1_min = normalize_angle(alpha1-delta1/2)
    alpha1_max = normalize_angle(alpha1+delta1/2)

    P2_min = P2
    P2_max = P2 + L2

    alpha2_min = normalize_angle(alpha2-delta2/2)
    alpha2_max = normalize_angle(alpha2+delta2/2)

    #Check if any of 4 corners in box 2 overlap with box 1
    #Check top left corner
    if check_box_corner(P2_min,alpha2_max,P1_min,P1_max,alpha1_min,alpha1_max) == True:
        return True
    #Check bottom left corner
    elif check_box_corner(P2_min,alpha2_min,P1_min,P1_max,alpha1_min,alpha1_max) == True:
        return True
    #Check top right corner
    elif check_box_corner(P2_max,alpha2_max,P1_min,P1_max,alpha1_min,alpha1_max) == True:
        return True
    #Check bottom right corner
    elif check_box_corner(P2_max,alpha2_min,P1_min,P1_max,alpha1_min,alpha1_max) == True:
        return True
    else:
        return False

if __name__ == '__main__':

    #If the function is called as main, test cases are run
    
    #Vector of boxes (test cases)
    P1 = [10,10,10,10,10,10,10]
    alpha1 = [320,320,100,100,320,320,320]
    L1 = [30,30,20,20,30,30,30]
    delta1= [100,100,30,30,100,100,100]

    P2 = [-5,-15,40,30,35,35,35]
    alpha2 = [11,11,100,100,11,265,260]
    L2 = [20,20,20,20,20,20,20]
    delta2 = [5,5,30,30,5,10,5]

    ground_truth = [True,False,False,True,True,True,False]

    failed_tests_cases = 0

    for i in range(len(ground_truth)):
        if check_box_overlap(P1[i],alpha1[i],L1[i],delta1[i],P2[i],alpha2[i],L2[i],delta2[i]) == ground_truth[i]:
            print ('Test case ' + str(i) + ' passed')
        else:
            print ('Test case ' + str(i) + ' failed')
            failed_tests_cases += 1

    if failed_tests_cases == 0:
        print('All test cases passed successfully')
    else:
        print('Some test cases present errors')
