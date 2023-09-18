from datetime import datetime
from datetime import date

reason_list = ("annual service", "cosmetic repair", "mechanical repair - body", 
                "mechanical repair - wing", "mechanical repair - engine")

outcome_list = ("return to service", "further action(S) required", "grounded - do not fly")


def get_job_date():
    now = datetime.now()
    job_date = now.date()

    return job_date 

def get_previous_date():
    
    flag = True
    
    while flag:
        user_date = input('Please enter date of the previous maintenance job (DD/MM/YYYY): ')

        try:
           datetime.strptime(user_date, "%d/%m/%Y").date()
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            return datetime.strptime(user_date, "%d/%m/%Y").date()

def next_service_date():
    now = datetime.now()
    job_day = now.strftime("%d")
    job_month = now.strftime("%m")
    job_year = now.strftime("%Y")

    temp_year = int(job_month) + 1 
    print(job_day)
    print(job_month)
    print(job_year)
    next_date = str(job_day) + "/" + str(job_month) + "/" + str(temp_year) 

    return next_date


def cal_difference(prev, curr):
    prev_job = prev
    current_job = curr

    diff = current_job - prev_job

    return diff.days

def check_serial_num(): 
    flag = True
    
    while flag:
        print("###############################################")
        ser_num = input('Please enter the plane reference number: ')

        if len(ser_num) == 12: 
            flag = True
        else:    
            print('Serial number accepted!')
            flag = False
                
    return ser_num



def record_job_reason():
        
        print("")
        print("################################################")
        print("#### Please choose a reason for current job ####")
        print('## 1. Annual service')
        print("## 2. Cosmetic repair")
        print("## 3. Mechanical repair - body")
        print("## 4. Mechanical repair - wing")
        print("## 5. Mechanical repair - engine")        
        print("") 
        
        flag = True

        while flag:
            
            reason_choice = input('Enter reason choice here:  ')

            try:
                int(reason_choice)
            except:
                print("Sorry, you did not enter a valid option number")
                flag = True
            else:
                local_choice = int(reason_choice) - 1
                if local_choice < 1 or local_choice > 5: 
                    print("Sorry, you did not choose an option within the given range")
                    flag = True
                else:
                    job_reason = reason_list[local_choice]
                    flag = False
        
        return job_reason      
    

def record_job_outcomes(diff):
    
    if int(diff) < 40: 
        job_outcome = "grounded - do not fly"
        print("")
        print("#############")
        print("WARNING!!!!!")
        print("#############")
        print("This plane has had more than one maintenance job in less than 30 days")
        print("The plane must undergo a safety investigation")
        print("Job outcome has been set to: grounded - do not fly ")
    
    else:
        print("")
        print("###############################################")
        print("######### Please choose a job outcome #########")
        print('## 1. Return to service')
        print("## 2. Further action(s) required")
        print("## 3. Grounded - do not fly")
        print("")
        
        flag = True

        while flag:
            
            out_choice = input('Enter outcome choice here:  ')

            try:
                int(out_choice)
            except:
                print("Sorry, you did not enter a valid option number")
                flag = True
            else:
                local_choice = int(out_choice) - 1
                if local_choice < 0 or local_choice > 2:
                    print("Sorry, you did not choose an option within the given range")
                    flag = True
                else:
                    job_outcome = outcome_list[local_choice]
                    flag = False
                
    
    return job_outcome
        
def get_job_time():
    flag = True

    while flag:
        print("###############################################")
        print("Please enter the number of hours spent on the job to the nearest 1/4 hour as a decimal" )
        print( "e.g 1 hour 15 minutes = 1.25")
        print("")
        time = input('Enter time spent here: '    )

        try:
            float(time)
        except:
            print("Sorry, you did not enter a time in a valid format")
            flag = True
        else:    
            print('Time value accepted!')
            flag = False
                
    return time


def output_summary(name, sn, jr, jd, pjd, ts, jo, ns):

    print("#################################################")
    print("######### Maintenance system job summary ########")
    print("")
    print("Engineer Name: {}".format(name))
    print("Plane Serial Number: {}".format(sn))
    print("Reason for Job: {}".format(jr))
    print("Date of Maintenance Job: {}".format(jd))
    print("Date of Previous Job: {}".format(pjd))
    print("Time spent on job: {} hours".format(ts))
    print("Job outcome: {}".format(jo))
    print("Date of next scheduled service: {}".format(ns))


    with open('job_summaries.txt', 'a') as job_summaries:
        job_summaries.write("Engineer Name: {}".format(name))
        job_summaries.write("Plane Serial Number: {}".format(sn))
        job_summaries.write("Reason for job: {}".format(jr))
        job_summaries.write("Date of Maintenance Job: {}".format(jd))
        job_summaries.write("Date of Previous Job: {}".format(pjd))
        job_summaries.write("Time spent on job: {} hours\n".format(ts))
        job_summaries.write("Job outcome: {}".format(jo))
        job_summaries.write("Date of next scheduled service: {}".format(ns))
        job_summaries.write("")


print("               .__                                  __                  .__                                .__                        .__        __                                                                     __                   ")
print("__  _  __ ____ |  |   ____  ____   _____   ____   _/  |_  ____     ____ |  |   ____ _____  ______   _____  |__|______    _____ _____  |__| _____/  |______    ____ _____    ____   ____  ____     _________.__. _______/  |_  ____   _____   ")
print("\ \/ \/ // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \  _/ __ \|  |  /    \\__  \ \____ \  \__  \ |  \_  __ \  /     \\__  \ |  |/    \   __\__  \  /    \\__  \  /    \_/ ___\/ __ \   /  ___<   |  |/  ___/\   __\/ __ \ /     \ ")
print(" \     /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> ) \  ___/|  |_|   |  \/ __ \|  |_> >  / __ \|  ||  | \/ |  Y Y  \/ __ \|  |   |  \  |  / __ \|   |  \/ __ \|   |  \  \__\  ___/   \___ \ \___  |\___ \  |  | \  ___/|  Y Y  \ ")
print("  \/\_/  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/   \___  >____/___|  (____  /   __/  (____  /__||__|    |__|_|  (____  /__|___|  /__| (____  /___|  (____  /___|  /\___  >___  > /____  >/ ____/____  > |__|  \___  >__|_|  / ")
print("             \/          \/            \/     \/                      \/          \/     \/|__|          \/                  \/     \/        \/          \/     \/     \/     \/     \/    \/       \/ \/         \/            \/      \/  ")
engineer_name = input('Please enter your name: ')

plane_serial_num = check_serial_num()

job_reason = record_job_reason()

job = get_job_date()

previous_job_date = get_previous_date()

difference = cal_difference(previous_job_date, job)

time_spent = get_job_time()

job_outcome = record_job_outcomes(difference)

next_service = next_service_date()

output_summary(engineer_name, plane_serial_num, job_reason, job, previous_job_date, time_spent, job_outcome, next_service)
