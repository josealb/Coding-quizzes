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

def distance_is_between(p_min,p,p_max):
    return p>=p_min and p<=p_max

class BoundingBox:
    def __init__(self,p_min,p_max,alpha_min,alpha_max):
        self.p_min = p_min
        self.p_max = p_max
        self.alpha_min = alpha_min
        self.alpha_max = alpha_max

    def check_box_corner(self,p2,alpha2):
        if distance_is_between(self.p_min,p2,self.p_max):
                if angle_is_between (self.alpha_min,self.alpha_max,alpha2):
                    return True

def check_box_overlap(p1,alpha1,l1,delta1,p2,alpha2,l2,delta2):
    #Assumption: length in meters is positive
    if l1<=0 or l2<=0:
        raise ValueError('Box length has to be larger than zero')
    if delta1 <=0 or delta2 <= 0:
        raise ValueError('Box width has to be larger than zero')

    p1_min = p1
    p1_max = p1 + l1

    alpha1_min = normalize_angle(alpha1-delta1/2)
    alpha1_max = normalize_angle(alpha1+delta1/2)

    p2_min = p2
    p2_max = p2 + l2

    alpha2_min = normalize_angle(alpha2-delta2/2)
    alpha2_max = normalize_angle(alpha2+delta2/2)
    #Create a bounding box object with the first bounding bod
    #We will test the second bounding box against this one
    bbox1 = BoundingBox(p1_min,p1_max,alpha1_min,alpha1_max)

    #Check if any of 4 corners in box 2 overlap with box 1
    #Check top left corner
    if bbox1.check_box_corner(p2_min,alpha2_max) == True:
        return True
    #Check bottom left corner
    elif bbox1.check_box_corner(p2_min,alpha2_min) == True:
        return True
    #Check top right corner
    elif bbox1.check_box_corner(p2_max,alpha2_max) == True:
        return True
    #Check bottom right corner
    elif bbox1.check_box_corner(p2_max,alpha2_min) == True:
        return True
    else:
        return False

if __name__ == '__main__':
    #If the function is called as main, test cases are run
    
    #Vector of boxes (test cases)
    p1 = [10,10,10,10,10,10,10]
    alpha1 = [320,320,100,100,320,320,320]
    l1 = [30,30,20,20,30,30,30]
    delta1= [100,100,30,30,100,100,100]

    p2 = [-5,-15,40,30,35,35,35]
    alpha2 = [11,11,100,100,11,265,260]
    l2 = [20,20,20,20,20,20,20]
    delta2 = [5,5,30,30,5,10,5]

    ground_truth = [True,False,False,True,True,True,False]

    failed_tests_cases = 0
    for i in range(len(ground_truth)):
        if check_box_overlap(p1[i],alpha1[i],l1[i],delta1[i],p2[i],alpha2[i],l2[i],delta2[i]) == ground_truth[i]:
            print ('Test case ' + str(i) + ' passed')
        else:
            print ('Test case ' + str(i) + ' failed')
            failed_tests_cases += 1

    if failed_tests_cases == 0:
        print('All test cases passed successfully')
    else:
        print('Some test cases present errors')
