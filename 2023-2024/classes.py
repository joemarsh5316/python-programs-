class sturdent():
    name = ""
    form = ""
    subject = ""
    student_id = ""
    def studentdata(self):
        desc_str = "%s is in form %s and is taking %s" ,(self.student_id, self.name, self.form, self.subject)
        return desc_str
    
student1 = sturdent()
student1.student_id = "0001"
student1.name = "schmonk"
student1.form = "9c"
student1.subject = "science"
print(student1.studentdata())



