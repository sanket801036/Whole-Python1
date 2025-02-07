ems_view
### **1. Imports and Setup**
from django.http import HttpResponse  # HttpResponse → Used to return a simple HTTP response (like plain text or HTML
from django.shortcuts import render # render → Renders an HTML template.                                                                         
from rest_framework.response import Response # Response from rest_framework→ A DRF class that formats responses automatically in JSON
from rest_framework.decorators import api_view # @api_view → A decorator that specifies which HTTP methods are allowed for a function.      
from EMSapp.models import Admin, Question, Result, Users # Importing models which represent database tables.                                                   
from EMSapp.serializers import QuestionSerilizer, ResultSerilizers, UsersSerilizers # Importing serializers (QuestionSerilizer, ResultSerilizers, UsersSerilizers) which convert model instances into JSON and vice versa.#
### **2. Simple View for Rendering HTML**
def hello(request): # This function returns an input.html file.
    #return HttpResponse("Hello World") # it would return a plain text response.
    return render(request,"input.html") # Loads an HTML page.

### **3. Fetching All Questions Based on Subject**

@api_view(['GET']) # @api_view(['GET']) → Only GET HTTP method allow in function
def getAllQuestions(request, subject): # Fetching All Questions Based on Subject
    allquestions = Question.objects.filter(subject=subject) # Fetches all questions with the given subject from the database.
    serilizer = QuestionSerilizer(allquestions, many=True) # The QuestionSerilizer Converts queryset into JSON format.
    return Response(serilizer.data) # The serialized data is return as a JSON response using Response.

### **4. Fetching All Unique Subjects**
@api_view(['GET'])
def getAllSubjects(request): # This view fetches all unique subjects from the `Question` model.
    allquestions = Question.objects.all() # Fetches all questions from the database.
    mapresult = map(lambda question: question.subject, allquestions) # - `map` is used to extract the `subject` field from each question.
    return Response(set(mapresult)) #   - `set` is used to remove duplicates, ensuring only unique subjects are returned.

### **5. Saving User Data**
@api_view(['POST'])
def saveUser(request): # This view saves user data to the database.
    serilizer = UsersSerilizers(data=request.data) # `UsersSerilizers` deserializes incoming JSON data into a Users model instance.
    if serilizer.is_valid(): #`is_valid()` Checks if the data is valid.
        serilizer.save() # If valid, Saves the data to the database.
    return Response(request.data) # Returns the input data as a response.

### **6. Validating User Login**
@api_view(['POST'])
def validate(request): #  This view validates user login credentials.
    userfromclient = request.data # Data coming from the browser during login.
    userfromdb = Users.objects.get(username=userfromclient["username"]) # Fetches the user from the database.
    if userfromclient["username"] == userfromdb.username and userfromclient["password"] == userfromdb.password:# It compares the username and password from the client with the data stored in the database.
        return Response(True) # Returns True if credentials match.
    else:
        return Response(False) # Returns False if credentials don't match.

### **7. Saving Results**
@api_view(['POST'])
def saveResult(request): # This view saves quiz results to the database.
    serilizer = ResultSerilizers(data=request.data) # `ResultSerilizers` deserializes the incoming JSON data into a `Result` model instance.
    if serilizer.is_valid(): # Checks if the data is valid.
        serilizer.save() # Saves the data to the database.
    return Response(request.data) # Returns the input data as a response.

### **8. Fetching Results with Pagination**
@api_view(["GET"])
def getResults2(request, subject, pageno): # This view fetches paginated results for a specific subject.
    myresult = Result.objects.filter(subject=subject) # Fetches results for the given subject.
    noofrecords = myresult.__len__() # Calculates the total number of records.
    pagenumber = 1
    while (3 * pagenumber) < noofrecords: # Calculates the number of pages required.
        pagenumber += 1
    indexlist = list() # Stores start indexes for each page.
    count = 0
    for i in range(0, pagenumber):
        indexlist.append(count)
        count += 3
    startindex = indexlist[int(pageno) - 1] # Determines the start index for the requested page.
    allrecords = list(Result.objects.filter(subject=subject)) # Fetches all records for the subject.
    if pageno == pagenumber: # Handles the last page.
        totalrecordsshown = 3 * (pagenumber - 1)
        recordstoshow = noofrecords - totalrecordsshown
        endindex = startindex + recordstoshow
        allresults = allrecords[startindex:endindex]
    else: # Handles other pages.
        endindex = startindex + 3
        allresults = allrecords[startindex:endindex]
    serilizer = ResultSerilizers(allresults, many=True) # Serializes the results.
    return Response(serilizer.data) # Returns the serialized data as a JSON response.

# - **Explanation**:
#   - It calculates the number of pages required and the start/end indexes for each page.
#   - Results are sliced based on the requested page number and returned as a JSON response.

### **9. CRUD Operations for Questions**
@api_view(['GET'])
def viewQuestion(request, qno, subject):
    questionfromdb = Question.objects.get(qno=qno, subject=subject) # Fetches a specific question.
    serilizer = QuestionSerilizer(questionfromdb) # Serializes the question.
    return Response(serilizer.data) # Returns the serialized data as a JSON response.

@api_view(['POST'])
def addQuestion(request):
    serilizer = QuestionSerilizer(data=request.data) # Deserializes incoming JSON data into a Question model instance.
    if serilizer.is_valid(): # Checks if the data is valid.
        serilizer.save() # Saves the data to the database.
    return Response(True) # Returns True if successful.

@api_view(['PUT'])
def updateQuestion(request):
    questionFromClient = request.data # Data coming from the client.
    questionfromdb = Question.objects.get(qno=questionFromClient["qno"], subject=questionFromClient["subject"]) # Fetches the question to update.
    serilizer = QuestionSerilizer(questionfromdb, data=questionFromClient, partial=False) # Updates the question with new data.
    if serilizer.is_valid(): # Checks if the data is valid.
        serilizer.save() # Saves the updated data to the database.
    return Response(True) # Returns True if successful.

@api_view(['DELETE'])
def deleteQuestion(request, qno, subject):
    Question.objects.filter(qno=qno, subject=subject).delete() # Deletes the specified question.
    return Response(True) # Returns True if successful.
# - **Explanation**:
#   - These views handle CRUD (Create, Read, Update, Delete) operations for the `Question` model.
#   - `viewQuestion` fetches a specific question.
#   - `addQuestion` adds a new question to the database.
#   - `updateQuestion` updates an existing question.
#   - `deleteQuestion` deletes a question.


### **Key Points to Highlight in an Interview**
# 1. **Django and DRF Basics**:
#    - Explain how Django handles HTTP requests and responses.
#    - Highlight the role of serializers in converting data between JSON and model instances.

# 2. **Database Interaction**:
#    - Discuss how Django ORM is used to query the database (e.g., `filter`, `get`, `delete`).

# 3. **API Design**:
#    - Explain the use of `@api_view` to restrict views to specific HTTP methods.
#    - Discuss the importance of pagination and how it’s implemented.

# 4. **Error Handling**:
#    - Mention how `is_valid()` ensures data integrity before saving to the database.

# 5. **Security**:
#    - Highlight the importance of validating user credentials securely (e.g., password hashing in a real-world scenario).

# 6. **Scalability**:
#    - Discuss how pagination improves performance for large datasets.

# By breaking down the code into these topics, you can demonstrate a clear understanding of Django, DRF, and backend development concepts.

hms_view.py

# Import and Setup
from django.shortcuts import render,redirect,HttpResponse # render ,Renders an HTML template. redirect,Redirect users to another URL.#                                    # type: ignore         
from dasapp.EmailBackEnd import EmailBackEnd .                                                                                                                            # type: ignore 
from django.contrib.auth import  logout,login # logout: Logs out the currently authenticated user. login: Logs in a user by creatinf session.#                            # type: ignore         
from django.contrib import messages # : used to display success or error messages in the tamplates.                                                                       # type: ignore       
from django.contrib.auth.decorators import login_required # A decorators that restrict access to authenticated users only..                                               # type: ignore       
from dasapp.models import CustomUser # it is user model that extends Djanfo built-in model.                                                                               # type: ignore       
from django.contrib.auth import get_user_model # it returns currently active user model                                                                                   # type: ignore      

User = get_user_model() # This assign the costum user model to User,allowing for user authentication and management.

# 2) Base View(Rendering the Base Template)
def BASE(request):# simply renders base.html ,which is like a hompage or layout 
    return render(request,'base.html')

# 3)Login Page View
def LOGIN(request): # it renders the login.html page where users enter their crendentials.
    return render(request,'login.html')

# 4) Logout Functionality
def doLogout(request):
    logout(request) # it Logs out the user and ends the session 
    return redirect('login') # Redirects the user to login page after logging out.

# 5) Login Functionality with Custom Authentication
def doLogin(request):
    if request.method == 'POST': # Checks if the request is a POST request.
        user = EmailBackEnd.authenticate(request,
                                         username=request.POST.get('email'),
                                         password=request.POST.get('password')
                                         ) # Authenticate the user using EmailBackend.authenticate(),passing the email and password the form.
        if user!=None: # If user exist
            login(request,user) # Logs them in using login(request,user).
            user_type = user.user_type # redirect them based on their user_type
            if user_type == '1':
                 return redirect('admin_home') # if it 1 then redirect to Admin dashboard 
            elif user_type == '2':
                 return redirect('doctor_home') # if it 2 then redirect to Doctor dashboard 
            elif user_type == '3':
                return redirect('userhome') # if it 1 then redirect to User homepage 
            
            
        else:
                messages.error(request,'Email or Password is not valid') # if authentication failed ,an error message is diplayed using message.error()
                return redirect('login') # redirect back to login page
    else:
            messages.error(request,'Email or Password is not valid')
            return redirect('login')

# 6. Profile View(Protected by Login Required Decorator)
@login_required(login_url='/') # it ensure only logged-in users can access this page; otherwise,they redirect to / (login page)
def PROFILE(request):
    user = CustomUser.objects.get(id = request.user.id) # Fetches the logged-in user's details using CustomUser.objects.get(id = request.user.id)
    context = {
        "user":user,
    }
    return render(request,'profile.html',context) # passes the user data to the profile.html template using the context dictionary.

# Profile Update Functionality
@login_required(login_url = '/')
def PROFILE_UPDATE(request):
    if request.method == "POST":
        # this function updates the user's profile information
        # it retrives form data using request.POST.get() and the  uploaded profile picture using request.FILIES.get()
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        print(profile_pic)
        
        # Updating the Database
        try:
            customuser = CustomUser.objects.get(id = request.user.id) # Fetches the logged-in user's data from the database 
            customuser.first_name = first_name
            customuser.last_name = last_name
            

            # Handling Profile Picture Upload
            if profile_pic !=None and profile_pic != "": # If new profile picture is uploded,it is updated in the database
               customuser.profile_pic = profile_pic
            customuser.save() # using this changes are saved
            messages.success(request,"Your profile has been updated successfully") # A success message is displayed
            return redirect('profile') # redirected to the profile page

        # Error Handling
        except:
            messages.error(request,"Your profile updation has been failed") # If an error occurs,an error message is displayed using messages.error().
    return render(request, 'profile.html')

# Change Password Functionality
def CHANGE_PASSWORD(request):
     context ={} # Initializes an empty context dictionary
     ch = User.objects.filter(id = request.user.id)
     
     if len(ch)>0: # Checks if a user exists with the current logged-in id.
            data = User.objects.get(id = request.user.id) # if fount
            context["data"]:data       # stored the user data in context["data"]                                                                                      .# type: ignore 

    # Handling Password Change       
     if request.method == "POST":        
        current = request.POST["cpwd"] # retrives current (old password) 
        new_pas = request.POST['npwd'] # and new_pass(new password) from the form.
        user = User.objects.get(id = request.user.id) # Fetches the logged-in user from the database.
        un = user.username
        check = user.check_password(current) # checks if the entered password is correct using check_password(current).

        # Updating the Password 
        if check == True: #If the old password matches
          user.set_password(new_pas) # Updates the password 
          user.save() # Saves the changes to database
          messages.success(request,'Password Change  Succeesfully!!!') # Display succcess message
          user = User.objects.get(username=un) 
          login(request,user) # Logs in the user again with the new password

        # Handling Incorrect Password 
        else:
          messages.success(request,'Current Password wrong!!!') # If the old password is incorrect,an error message is displayed 
          return redirect("change_password") # and the user is redirected back to the  change password page
        
    # Rendering the change Password Page
    return render(request,'change-password.html').                                                                                                                      # type: ignore 
# If the request is not POST,the change-password.html template is rendered

hms_model.py

# it is structured to manage doctors,patients,appoinments, and medical records using Django's ORM.

from django.db import models  # type: ignore 
from django.contrib.auth.models import AbstractUser # AbstractUser is Django's built-in user model that provides authentications fields like username,password,email, etc# type: ignore 

class CustomUser(AbstractUser): # this class to extends AbstractUser
    USER ={
        (1,'admin'),
        (2,'doc'),
        
    }# USER defines two types of users
    user_type = models.CharField(choices=USER,max_length=50,default=1) # user_type is a field to store user roles,with a dafault valueof 1(admin)

    profile_pic = models.ImageField(upload_to='media/profile_pic') # it will store user profile images in the provided directory

# 2) Specialization Model
class Specialization(models.Model):# this model store different medical specialization like 'Cardiologist,"Dermatologist",etc
    sname = models.CharField(max_length=200) # it store specialization name
    created_at = models.DateTimeField(auto_now_add=True)# it is automatically set when the record is created
    updated_at = models.DateTimeField(auto_now=True)# update time whenever the record is modified

    def __str__(self):# return the specialization name when referenced.
        return self.sname
   
    
# 3. DoctorReg Model
class DoctorReg(models.Model): # Represents doctors registered in the system
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True) # OneToOneField(CustomUser):Links doctor to a CustomUser record
                                                                                              # on_delete=models.CASCADEL: If user is deleted, then doctor profile also deleted
                                                                                              # null=True, blank=True: allows storing null value
    fee = models.DecimalField(max_digits=10, decimal_places=2,default=0) # It stores stores doctor consultation fee.
    mobilenumber = models.CharField(max_length=11) # Stores's doctor's mobile number
    specialization_id = models.ForeignKey(Specialization, on_delete=models.CASCADE) # Link doctor to specialization
    regdate_at = models.DateTimeField(auto_now_add=True) # Tracks registrataion time
    updated_at = models.DateTimeField(auto_now=True) # Tracks update time 
   

    def __str__(self): # Returns doctor's full name and mobile number
        if self.admin:
            return f"{self.admin.first_name} {self.admin.last_name} - {self.mobilenumber}"
        else:
            return f"User not associated - {self.mobilenumber}"

# 4) PatientReg model
class PatientReg(models.Model): # Represents Patients in the system.
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, blank=True) # OneToOneField(CustomUser):Links patients to a CustomUser account
                                                                                              # on_delete=models.CASCADE: If user is deleted, then Patients registration also deleted
                                                                                              # null=True, blank=True: allows storing null value
    mobilenumber = models.CharField(max_length=11,unique=True) # Stores unique mobile number for each patient.
    gender = models.CharField(max_length=100) # 
    address = models.TextField()
    regdate_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 5.Appointment model
class Appointment(models.Model): # Represents appointments between patients and doctors
    appointmentnumber = models.IntegerField(default=0)
    spec_id = models.ForeignKey(Specialization, on_delete=models.CASCADE,default=0) # Links an appointment to a specialization.
    pat_id = models.ForeignKey(PatientReg, on_delete=models.CASCADE,default=0) # Links an appointment to a patient.   
    date_of_appointment = models.CharField(max_length=250)
    time_of_appointment = models.CharField(max_length=250)
    doctor_id = models.ForeignKey(DoctorReg, on_delete=models.CASCADE) # # Links an appointment to a doctor. 
    additional_msg = models.TextField(blank=True) # Stores optional patients notes
    remark = models.CharField(max_length=250,default=0) # remark stores doctor comments
    status = models.CharField(default=0,max_length=200) # and status tracks appointment status
    created_at = models.DateTimeField(auto_now_add=True) # Tracks appoinment creation and modification times
    updated_at = models.DateTimeField(auto_now=True)

    
# 6. Page Model: Stores information about website
class Page(models.Model): # Represents Websites pages(like "About Us"). 
    pagetitle = models.CharField(max_length=250)# Stores page title,address,description,contact email.and phone number.
    address = models.CharField(max_length=250) 
    aboutus = models.TextField()
    email = models.EmailField(max_length=200)
    mobilenumber = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True) # Tracks when the page was created and last updated.
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.pagetitle # Return the page title. 

# 7. AddPatient model :
class AddPatient(models.Model): # Represents addtional patient details added by doctors.
    doctor_id = models.ForeignKey(DoctorReg, on_delete=models.CASCADE) # Links paients to specific doctor
    name = models.CharField(max_length=250)
    mobilenumber = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=200)
    gender = models.CharField(max_length=100)
    address = models.TextField()
    age = models.IntegerField() # stores patients details including patients history
    
    medicalhistory = models.TextField()
    regdate_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# 8. Medical History Model
class MedicalHistory(models.Model):# Represents a patients's medical records
    pat_id = models.ForeignKey(AddPatient, on_delete=models.CASCADE, related_name='medical_histories', default=0)# Links medical history to a patient.
    bloodpressure = models.CharField(max_length=250)
    weight = models.CharField(max_length=250) # Stores medical parameters and prescriptions.
    bloodsugar = models.CharField(max_length=250)
    bodytemp = models.CharField(max_length=250)
    prescription = models.TextField()
    visitingdate_at = models.DateTimeField(auto_now_add=True) # Trecks update and visit time
    updated_at = models.DateTimeField(auto_now=True)


# This model setup efficiently manages,user,doctors,patiens,appointments, and medical history. 


