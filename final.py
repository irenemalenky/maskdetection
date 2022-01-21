# final project
# covid-19 questionnaire
# name, dob, street, city, state, zip, email, phone, vax status, vax type, vax date, vax lot, symptoms
# have results inserted into mysql
# have a mask check thru webcam
# mask detection code derived from @saurabh.shaligram

import cv2
import tkinter as tk
import mysql.connector
import numpy as np
import random

gui = tk.Tk()
gui.title("covid-19 questionnaire")

# function for submitting information
def submitToFile():
    list = (name_entry.get(), dob_entry.get(), street_entry.get(), city_entry.get(), state_entry.get(),zip_entry.get(),
            email_entry.get(), phone_entry.get(), var.get(), var1.get(), var2.get(),date_entry.get(), lot_entry.get(),
            date2_entry.get(), lot2_entry.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(), var9.get())

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="CompSci2021",
    database="ics211"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO people (name, dob, address, city, state, zip, email, phone, vax  yes, vax no, pos, neg, pfizer, moderna, jj, date, lot, date2, lot2, symptom yes, symptom no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (name_entry.get(), dob_entry.get(), street_entry.get(), city_entry.get(), state_entry.get(),zip_entry.get(),
            email_entry.get(), phone_entry.get(), var.get(), var1.get(), var2.get(),date_entry.get(), lot_entry.get(),
            date2_entry.get(), lot2_entry.get(), var3.get(), var4.get(), var5.get(), var6.get(), var7.get(), var8.get(), var9.get())
    mycursor.execute(sql, val)

    mydb.commit()

def readFromFile():

    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="CompSci2021",
    database="ics211"
    )

    mycursor = mydb.cursor()

    sql = "select * from people"
    mycursor.execute(sql)

    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

# greeting
intro = tk.Label(gui, text="please submit the following:")
intro.grid(row=0, column=0)
# blank space for even column
intro2 = tk.Label(gui, text="                                                       ")
intro2.grid(row=0, column=2)
# blank space for even column
intro3 = tk.Label(gui, text="                                                       ")
intro3.grid(row=0, column=3)


# name
name = tk.Label(gui, text="full legal name")
name.grid(row=1, column=0)
# name entry
name_entry = tk.Entry(gui)
name_entry.grid(row=1, column=1)

# birthday
dob = tk.Label(gui, text="date of birth")
dob.grid(row=2, column=0)
# birthday entry
dob_entry = tk.Entry(gui)
dob_entry.grid(row=2, column=1)

# street address
street = tk.Label(gui, text="street address")
street.grid(row=3, column=0)
# street address entry
street_entry = tk.Entry(gui)
street_entry.grid(row=3, column=1)

# city
city = tk.Label(gui, text="city")
city.grid(row=4, column=0)
# city entry
city_entry = tk.Entry(gui)
city_entry.grid(row=4, column=1)

# state
state = tk.Label(gui, text="state")
state.grid(row=5, column=0)
# state entry
state_entry = tk.Entry(gui)
state_entry.grid(row=5, column=1)

# zip code
zip = tk.Label(gui, text="zip code")
zip.grid(row=6, column=0)

# exception handling
while True:
    try:
        # zip code entry
        zip_entry = tk.Entry(gui)
        zip_entry.grid(row=6, column=1)
        break
    except ValueError:
        print("number format only! please enter again.")

# email
email = tk.Label(gui, text="email")
email.grid(row=7, column=0)
# email entry
email_entry = tk.Entry(gui)
email_entry.grid(row=7, column=1)

# phone number
phone = tk.Label(gui, text="phone #")
phone.grid(row=8, column=0)

# exception handling
while True:
    try:
        # phone number entry
        phone_entry = tk.Entry(gui)
        phone_entry.grid(row=8, column=1)
        break
    except ValueError:
        print("number format only! please enter again.")

# vax status
vax = tk.Label(gui, text="have you received the covid-19 vaccine?")
vax.grid(row=9, column=0)
# vax status check
var1 = tk.IntVar()
tk.Checkbutton(gui, text="yes", variable=var1).grid(row=9, column=1)
var2 = tk.IntVar()
tk.Checkbutton(gui, text="no", variable=var2).grid(row=9, column=2)

# test status
neg = tk.Label(gui, text="if unvaccinated, what are the results?")
neg.grid(row=10, column=0)
# vax status check
var3 = tk.IntVar()
tk.Checkbutton(gui, text="positive", variable=var3).grid(row=10, column=1)
var4 = tk.IntVar()
tk.Checkbutton(gui, text="negative", variable=var4).grid(row=10, column=2)

# vax company
list = tk.Label(gui, text="vaccine brand")
list.grid(row=11, column=0)
# pfizer checkbox
var5 = tk.IntVar()
tk.Checkbutton(gui, text="pfizer", variable=var5).grid(row=11, column=1)
# moderna checkbox
var6 = tk.IntVar()
tk.Checkbutton(gui, text="moderna", variable=var6).grid(row=11, column=2)
# j&j checkbox
var7 = tk.IntVar()
tk.Checkbutton(gui, text="johnson & johnson", variable=var7).grid(row=11, column=3)

# vax date 1
date = tk.Label(gui, text="first dose date")
date.grid(row=12, column=0)
# vax date 1 entry
date_entry = tk.Entry(gui)
date_entry.grid(row=12, column=1)

# vax date 1 lot
lot = tk.Label(gui, text="first dose lot #")
lot.grid(row=13, column=0)
# vax date 1 lot entry
lot_entry = tk.Entry(gui)
lot_entry.grid(row=13, column=1)

# vax date 2
date2 = tk.Label(gui, text="second dose date")
date2.grid(row=14, column=0)
# vax date 2 entry
date2_entry = tk.Entry(gui)
date2_entry.grid(row=14, column=1)

# vax date 2 lot
lot2 = tk.Label(gui, text="second dose lot #")
lot2.grid(row=15, column=0)
# vax date 2 lot entry
lot2_entry = tk.Entry(gui)
lot2_entry.grid(row=15, column=1)

# symptom status
symptom = tk.Label(gui, text="do you feel any of the following symptoms?")
symptom.grid(row=16, column=0)
# fever
fever = tk.Label(gui, text="fever")
fever.grid(row=17, column=0)
# cough
cough = tk.Label(gui, text="cough")
cough.grid(row=18, column=0)
# shortness of breath
breath = tk.Label(gui, text="shortness of breath")
breath.grid(row=19, column=0)
# symptom check
var8 = tk.IntVar()
tk.Checkbutton(gui, text="yes", variable=var8).grid(row=19, column=1)
var9 = tk.IntVar()
tk.Checkbutton(gui, text="no", variable=var9).grid(row=19, column=2)
# fatigue
fatigue = tk.Label(gui, text="fatigue")
fatigue.grid(row=20, column=0)
# headache
head = tk.Label(gui, text="headache")
head.grid(row=21, column=0)

def maskCheck():
    
    # cascades
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    mouth_cascade = cv2.CascadeClassifier('haarcascade_mcs_mouth.xml')
    upper_body = cv2.CascadeClassifier('haarcascade_upperbody.xml')

    # threshold
    bw_threshold = 80

    # info message to user
    font = cv2.FONT_HERSHEY_SIMPLEX
    org = (30, 30)
    weared_mask_font_color = (255, 255, 255)
    not_weared_mask_font_color = (0, 0, 255)
    thickness = 2
    font_scale = 1
    weared_mask = "thank you for wearing your mask"
    not_weared_mask = "please put on your mask"

    # read video
    cap = cv2.VideoCapture(0)

    while 1:
        # get individual frame
        ret, img = cap.read()
        img = cv2.flip(img,1)

        # convert image into gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # convert image in b&w
        (thresh, black_and_white) = cv2.threshold(gray, bw_threshold, 255, cv2.THRESH_BINARY)
        cv2.imshow('black_and_white', black_and_white)

        # detect face
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        # Face prediction for black and white
        faces_bw = face_cascade.detectMultiScale(black_and_white, 1.1, 4)

        if(len(faces) == 0 and len(faces_bw) == 0):
            cv2.putText(img, "no face found...", org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
        elif(len(faces) == 0 and len(faces_bw) == 1):
            cv2.putText(img, weared_mask, org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
        else:
            # rectangle for face
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
                roi_gray = gray[y:y + h, x:x + w]
                roi_color = img[y:y + h, x:x + w]

                # detect lips
                mouth_rects = mouth_cascade.detectMultiScale(gray, 1.5, 5)      

            if(len(mouth_rects) == 0):
                cv2.putText(img, weared_mask, org, font, font_scale, weared_mask_font_color, thickness, cv2.LINE_AA)
            else:
                for (mx, my, mw, mh) in mouth_rects:

                    if(y < my < y + h):
                        # not wearing mask
                        cv2.putText(img, not_weared_mask, org, font, font_scale, not_weared_mask_font_color, thickness, cv2.LINE_AA)
                
                        cv2.rectangle(img, (mx, my), (mx + mh, my + mw), (0, 0, 255), 3)
                        break


        # show frame with results
        cv2.imshow('mask detection', img)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

    # release video
    cap.release()
    cv2.destroyAllWindows()


# facial recognition for mask
tk.Button(gui, text='mask check', width=10, command=maskCheck).grid(row=23,column=1)
# submit
tk.Button(gui, text='submit', width=10, command=submitToFile).grid(row=24,column=1)
# show results
tk.Button(gui, text='show', width=10, command=readFromFile).grid(row=25,column=1)

gui.mainloop()
