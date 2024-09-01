def gradingStudents(grades):
    
    for i in range(len(grades)):
        x = grades[i] % 5
        if grades[i]>37 and x >2:
            grades[i] += 5 - x
                
    return grades
        
            