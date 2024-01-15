from flask import Flask, flash, render_template,request ,session

import secrets

from Methods import authen_user 
from Methods import create_user 
from Methods import find_usertype 
from Methods import find_email 
from decryption import decrypt
from encryption import encrypt



#create secreat key
secret = secrets.token_urlsafe(32)

app = Flask(__name__)
app.secret_key = secret

#route for load index page
@app.route("/")
def index():
    return render_template('SendMessage.html')


#route for load register page
@app.route("/register")
def register():
    return render_template('register.html')

#route for load login page
@app.route("/login")
def login():
    return render_template('login.html')

#route for load sendMessage page
@app.route("/sendmessage")
def sendMessage():
    return render_template('SendMessage.html')

    
#route for registration form action  
@app.route("/registration", methods=['POST'])
def SignUpMethod():
    email = request.form.get('UserEmail')
    userrole = request.form.get('User_Role')
    password = request.form.get('password')
    cpassword = request.form.get('cpassword')

    if password == cpassword:
        foundEmail = find_email(email)
        if foundEmail is None:
            if create_user(email, userrole, password):
                flash('Registration successful! Please login.', 'success')
                return render_template('/login.html')
            else:
                flash('Registration failed. Please try again later.', 'error')
                return render_template('/register.html')  
        else:
            flash('Registration failed. Already have Account under Email', 'error')
            return render_template('/register.html')   
    else:
        flash('Password and confirm password do not match. Please try again.', 'error')
    
    return render_template('/register.html')
        


#route for login form action    
@app.route("/loginpage", methods=['POST'])
def LoginMethod():
    email = request.form.get('UserEmail')
    password = request.form.get('password')
    if authen_user(email, password):
        #check user role of email
        userrole=find_usertype(email)
        print('usertype checked in main body.',userrole)
        if userrole is not None:
            #decrypt message method
            decrypted_Message = decrypt(userrole)
            if decrypted_Message is not None:
               flash('Decryption is  successful!', 'success')
               print("Decrypted Message in succesful in main body:", decrypted_Message)
               # Pass the decrypted_Message to the template
               return render_template('DisplayMessage.html', decrypted_Message=decrypted_Message)
            else:
               flash('Decryption failed.', 'error')
               print("Decrypted Message in failed in main body:")
               # Redirect to the HTML page to display the feedback message
               return render_template('/login.html')
   
        else:
            flash('Login failed. Invalid email or password.', 'error')
            # Redirect to the HTML page to display the feedback message
            return render_template('/login.html') 
    else:
        flash('Login failed. Invalid email or password.', 'error')
        # Redirect to the HTML page to display the feedback message
        return render_template('/login.html')



#route for sendMessage form action  
@app.route("/SendMessageMethod", methods=['POST'])
def MessageMethod():
    message = request.form.get('textareaMessage')
    user_type = request.form.get('User_Role')
    print(message)
    print(user_type)
    #Check userrole and send encrypt method
    if encrypt(message,user_type):
        flash('Message encrypted and saved.', 'success')
    else:
        flash('Message encryption failed. Please Try Again later.', 'error')
      
    #Redirect to the HTML page  to display the feedback message
    return render_template('/SendMessage.html')
    



if __name__=="__main__":
    app.run(debug=True)