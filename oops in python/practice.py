class course:
    
    def __init__(self,course_name,duration,mentor):
        self.course_name= course_name
        self.duration= duration
        self.mentor= mentor
    def show_mentor(self):
            print(f"mentor name is {self.mentor}")

a=course
# a= course("CSE",4,"Devansh")
