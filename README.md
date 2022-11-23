# SubwaySurfers

This is a webpage that can run be run locally once cloned and set up with the command "python3 app.py". 
This is an application that uses Flask, JavaScript, CSS, and HTML. A video will play automatically of Subway Surfers and text can be entered into a box that 
will be read out loud. This is done by the front end sending a fetch request to the Python backend. NOTE that this application expects the users 
operating system to have the command line utility "mpg321" to play the mp3 file that is through the use of the gTTS (Google Text To Speech) API.


def convert_text_speech(input, id):
    myobj = gTTS(text=input, lang='en', slow=False)
    myobj.save(str(id) + '.mp3')
    os.system("mpg321 " + str(id) + ".mp3")   <---------------------------------
    return str(id) + ".mp3"
