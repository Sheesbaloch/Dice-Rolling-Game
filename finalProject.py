import tkinter as tk
from PIL import Image, ImageTk
import random
import pygame
import customtkinter
#---------------------------------------------------------------------------------------------------------------------
#that class is for one (1) Dice

class one_dice:
    def one(self):
        windows = tk.Toplevel()
        
        img = Image.open('D:/python practice/background2.jpg')
        img = img.resize((windows.winfo_screenwidth(), windows.winfo_screenheight()))
        tk_img = ImageTk.PhotoImage(img)
        background = tk.Label(windows, image=tk_img)
        background.place(x=0,y=0, relheight=1, relwidth=1)
        windows.resizable(False, False)
        windows.geometry("1535x800")
        windows.title("Dice Roll")
        dice = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',]
        diceNum = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}
        
        labelCustom = customtkinter.CTkLabel(windows, text='Player1', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')
        labelCustom.place(x=330, y=100)
        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        label1 = tk.Label(windows, image= image1, padx=10)
        label1.image = image1

        label1.place(x=350, y=300)

        def roll_dice():
           image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
           label1.configure(image=image1)
           label1.image = image1
           
           image1_path = random.choice(dice)
           image1 = ImageTk.PhotoImage(Image.open(image1_path))
           label1.configure(image=image1)
           label1.image = image1
           res = diceNum[image1_path]
           label174.configure(text="You got  "+str(res))
           
        button = tk.Button(windows, bg='black', fg='white', font='Times 10 bold', text='Roll Dice', command=roll_dice)
        button.place(x=380, y=600)
        label174 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')
        label174.place(x=350,y=650)
        
#----------Right Side---------------------------------------------------------------------
        dice1 = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',]
        diceNum1 = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}
        
        labelCustom = customtkinter.CTkLabel(windows, text='Player2', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')
        labelCustom.place(x=1030, y=100)
        
        image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        label11 = tk.Label(windows, image= image11,)

        label11.image = image11

        label11.place(x=1050, y=300)

        def roll_dice():
           image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
           label11.configure(image=image11)
           label11.image = image11
           
           image1_path1 = random.choice(dice)
           image11 = ImageTk.PhotoImage(Image.open(image1_path1))
           label11.configure(image=image11)
           label11.image = image11
           res1 = diceNum1[image1_path1]
           label1745.configure(text="You got  "+str(res1))

        button1 = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)
        button1.place(x=1100, y=600)
        
        label1745 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')
        label1745.place(x=1070,y=650)
        
        
        windows.mainloop()

#----------------------------------------------------------------------------------------------------------------------
#that class is for two dice

class twoDice:
    def two(self):
        windows = tk.Toplevel()
        
        img = Image.open('D:/python practice/background2.jpg')
        img = img.resize((windows.winfo_screenwidth(), windows.winfo_screenheight()))
        tk_img = ImageTk.PhotoImage(img)
        background = tk.Label(windows, image=tk_img)
        background.place(x=0,y=0, relheight=1, relwidth=1)
        windows.geometry("1535x800")
        windows.title("Dice Roll")
        
        c = tk.Canvas(windows, width=500,height=500)
        dice = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',]
        diceNum = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}
        
        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        
        labelCustom = customtkinter.CTkLabel(windows, text='Player1', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')
        labelCustom.place(x=330, y=100)

        label1 = tk.Label(windows, image= image1)
        label2 = tk.Label(windows, image=image2)

        label1.image = image1
        label2.image = image2

        label1.place(x=250, y=280)
        label2.place(x=400,y=280)

        def roll_dice():
            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label1.configure(image=image1)
            label1.image = image1
    
            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label2.configure(image=image2)
            label2.image = image2
            
            image1_path = random.choice(dice)
            image1 = ImageTk.PhotoImage(Image.open(image1_path))
            label1.configure(image=image1)
            label1.image = image1
            
            image2_path = random.choice(dice)
            image2 = ImageTk.PhotoImage(Image.open(image2_path))
            label2.configure(image=image2)
            label2.image = image2
            res = diceNum[image1_path]+ diceNum[image2_path]
            label174.configure(text="You got  "+str(res))
        
        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)
        button.place(x=380, y=600)
        
        label174 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')
        label174.place(x=350,y=650)
        
#---------------------Left Side--------------------------------------------------------------------------------
        dice1 = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',]
        diceNum1 = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}
        
        image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        
        labelCustom = customtkinter.CTkLabel(windows, text='Player2', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')
        labelCustom.place(x=1030, y=100)

        label11 = tk.Label(windows, image= image11)
        label21 = tk.Label(windows, image=image21)

        label11.image = image11
        label21.image = image21

        label11.place(x=980, y=280)
        label21.place(x=1130,y=280)

        def roll_dice():
            image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label11.configure(image=image11)
            label11.image = image11
    
            image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label21.configure(image=image21)
            label21.image = image21
            
            image11_path = random.choice(dice1)
            image11 = ImageTk.PhotoImage(Image.open(image11_path))
            label11.configure(image=image11)
            label11.image = image11
            
            image21_path = random.choice(dice1)
            image21 = ImageTk.PhotoImage(Image.open(image21_path))
            label21.configure(image=image21)
            label21.image = image21
            res1 = diceNum1[image11_path]+ diceNum1[image21_path]
            label1745.configure(text="You got  "+str(res1))
    
        button1 = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)
        button1.place(x=1080, y=600)
        
        label1745 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')
        label1745.place(x=1070,y=650)
        windows.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
#that class is for three dice

class ThreeDice:
    def three(self):
        windows = tk.Toplevel()
        
        img = Image.open('D:/python practice/background2.jpg')
        img = img.resize((windows.winfo_screenwidth(), windows.winfo_screenheight()))
        tk_img = ImageTk.PhotoImage(img)
        background = tk.Label(windows, image=tk_img)
        background.place(x=0,y=0, relheight=1, relwidth=1)
        windows.geometry("1535x800")
        windows.title("Dice Roll")

        dice = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',]
        diceNum = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}
        
        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        
        labelCustom = customtkinter.CTkLabel(windows, text='Player1', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')
        labelCustom.place(x=330, y=100)

        label1 = tk.Label(windows, image= image1)
        label2 = tk.Label(windows, image=image2)
        label3 = tk.Label(windows, image=image3)

        label1.image = image1
        label2.image = image2
        label3.image = image3

        label1.place(x=200, y=280)
        label2.place(x=350,y=280)
        label3.place(x = 500, y = 280)

        def roll_dice():
            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label1.configure(image=image1)
            label1.image = image1
    
            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label2.configure(image=image2)
            label2.image = image2
    
            image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label3.configure(image=image3)
            label3.image = image3
            
            image1_path = random.choice(dice)
            image1 = ImageTk.PhotoImage(Image.open(image1_path))
            label1.configure(image=image1)
            label1.image = image1
            
            image2_path = random.choice(dice)
            image2 = ImageTk.PhotoImage(Image.open(image2_path))
            label2.configure(image=image2)
            label2.image = image2
            
            image3_path = random.choice(dice)
            image3 = ImageTk.PhotoImage(Image.open(image3_path))
            label3.configure(image=image3)
            label3.image = image3
            
            
            res = diceNum[image1_path]+ diceNum[image2_path]  + diceNum[image3_path]
            label174.configure(text="You got  "+str(res))

        label174 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')
        label174.place(x=380,y=650)
    
        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)
        button.place(x=380, y=600)
        
#--------------------------------------Right Side--------------------------------------------------------------------------
        dice1 = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',]
        diceNum1 = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}
        
        image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        
        labelCustom = customtkinter.CTkLabel(windows, text='Player2', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')
        labelCustom.place(x=1030, y=100)

        label11 = tk.Label(windows, image= image11)
        label21 = tk.Label(windows, image=image21)
        label31 = tk.Label(windows, image=image31)

        label11.image = image11
        label21.image = image21
        label31.image = image31

        label11.place(x=900, y=300)
        label21.place(x=1050,y=300)
        label31.place(x = 1200, y = 300)

        def roll_dice():
            image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label11.configure(image=image11)
            label11.image = image11
    
            image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label21.configure(image=image21)
            label21.image = image21
    
            image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label31.configure(image=image31)
            label31.image = image31
            
            image11_path = random.choice(dice1)
            image11 = ImageTk.PhotoImage(Image.open(image11_path))
            label11.configure(image=image11)
            label11.image = image11
            
            image21_path = random.choice(dice1)
            image21 = ImageTk.PhotoImage(Image.open(image21_path))
            label21.configure(image=image21)
            label21.image = image21
            
            image31_path = random.choice(dice1)
            image31 = ImageTk.PhotoImage(Image.open(image31_path))
            label31.configure(image=image31)
            label31.image = image31
            
            
            res = diceNum[image11_path]+ diceNum[image21_path]  + diceNum[image31_path]
            label1741.configure(text="You got  "+str(res))
    
        button1 = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)
        button1.place(x=1100, y=600)
        
        label1741 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')
        label1741.place(x=1070,y=650)
        windows.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
#This class is for four dice

class fourDice:
    def four(self):
        windows = tk.Toplevel()
        
        img = Image.open('D:/python practice/background2.jpg')
        img = img.resize((windows.winfo_screenwidth(), windows.winfo_screenheight()))
        tk_img = ImageTk.PhotoImage(img)
        background = tk.Label(windows, image=tk_img)
        background.place(x=0,y=0, relheight=1, relwidth=1)
        windows.geometry("1535x800")
        windows.title("Dice Roll")

        dice = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',]
        diceNum = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}
        
        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        
        labelCustom = customtkinter.CTkLabel(windows, text='Player1', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')
        labelCustom.place(x=330, y=100)

        label1 = tk.Label(windows, image= image1)
        label2 = tk.Label(windows, image=image2)
        label3 = tk.Label(windows, image=image3)
        label4 = tk.Label(windows, image=image4)

        label1.image = image1
        label2.image = image2
        label3.image = image3
        label4.image = image4

        label1.place(x=350, y=250)
        label2.place(x=200,y=400)
        label3.place(x = 350, y = 400)
        label4.place(x =500, y = 400)

        def roll_dice():
            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label1.configure(image=image1)
            label1.image = image1
    
            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label2.configure(image=image2)
            label2.image = image2
    
            image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label3.configure(image=image3)
            label3.image = image3
    
            image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label4.configure(image=image4)
            label4.image = image4
            
            image1_path = random.choice(dice)
            image1 = ImageTk.PhotoImage(Image.open(image1_path))
            label1.configure(image=image1)
            label1.image = image1
            
            image2_path = random.choice(dice)
            image2 = ImageTk.PhotoImage(Image.open(image2_path))
            label2.configure(image=image2)
            label2.image = image2
            
            image3_path = random.choice(dice)
            image3 = ImageTk.PhotoImage(Image.open(image3_path))
            label3.configure(image=image3)
            label3.image = image3
            
            image4_path = random.choice(dice)
            image4 = ImageTk.PhotoImage(Image.open(image4_path))
            label4.configure(image=image4)
            label4.image = image4
            
            res = diceNum[image1_path]+ diceNum[image2_path]  + diceNum[image3_path] +diceNum[image4_path]
            label174.configure(text="You got  "+str(res))

        label174 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')
        label174.place(x=380,y=650)
    
        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)
        button.place(x=360, y=600)
        
#------------------------------right side--------------------------------------------------------------------------------
        dice1 = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',]
        diceNum1 = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}
        
        image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        image41 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        
        labelCustom = customtkinter.CTkLabel(windows, text='Player2', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')
        labelCustom.place(x=1030, y=100)

        label11 = tk.Label(windows, image= image11)
        label21 = tk.Label(windows, image=image21)
        label31 = tk.Label(windows, image=image31)
        label41 = tk.Label(windows, image=image41)

        label11.image = image11
        label21.image = image21
        label31.image = image31
        label41.image = image41

        label11.place(x=1050, y=250)
        label21.place(x=900,y=400)
        label31.place(x = 1050, y = 400)
        label41.place(x =1200, y = 400)

        def roll_dice():
            image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label11.configure(image=image11)
            label11.image = image11
    
            image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label21.configure(image=image21)
            label21.image = image21
    
            image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label31.configure(image=image31)
            label31.image = image31
    
            image41 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label41.configure(image=image41)
            label41.image = image41
            
            image11_path = random.choice(dice1)
            image11 = ImageTk.PhotoImage(Image.open(image11_path))
            label11.configure(image=image11)
            label11.image = image11
            
            image21_path = random.choice(dice1)
            image21 = ImageTk.PhotoImage(Image.open(image21_path))
            label21.configure(image=image21)
            label21.image = image21
            
            image31_path = random.choice(dice1)
            image31 = ImageTk.PhotoImage(Image.open(image31_path))
            label31.configure(image=image31)
            label31.image = image31
            
            image41_path = random.choice(dice1)
            image41 = ImageTk.PhotoImage(Image.open(image41_path))
            label41.configure(image=image41)
            label41.image = image41
            
            res1 = diceNum[image11_path]+ diceNum[image21_path]  + diceNum[image31_path] +diceNum[image41_path]
            label1741.configure(text="You got  "+str(res1))

        label1741 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')
        label1741.place(x=1060,y=650)
    
        button1 = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)
        button1.place(x=1100, y=600)
        
        windows.mainloop()

#-----------------------------------------------------------------------------------------------------------------------
#This class is for five dice
class fiveDice:
    
    def five(self):
        windows = tk.Toplevel()
        img = Image.open('D:/python practice/background2.jpg')
        img = img.resize((windows.winfo_screenwidth(), windows.winfo_screenheight()))
        tk_img = ImageTk.PhotoImage(img)
        background = tk.Label(windows, image=tk_img)
        background.place(x=0,y=0, relheight=1, relwidth=1)
        windows.geometry("1535x800")
        windows.title("Dice Roll")
        

        dice = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',]
        diceNum = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}
        
        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image5 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        
        labelCustom = customtkinter.CTkLabel(windows, text='Player1', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')
        labelCustom.place(x=330, y=100)
        
        label1 = tk.Label(windows, image= image1)
        label2 = tk.Label(windows, image=image2)
        label3 = tk.Label(windows, image=image3)
        label4 = tk.Label(windows, image=image4)
        label5 = tk.Label(windows, image=image5)

        label1.image = image1
        label2.image = image2
        label3.image = image3
        label4.image = image4
        label5.image = image5

        label1.place(x=200, y=400)
        label2.place(x=280,y=250)
        label3.place(x = 430, y = 250)
        label4.place(x =350, y = 400)
        label5.place(x = 500, y = 400)

        def roll_dice():
            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label1.configure(image=image1)
            label1.image = image1
    
            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label2.configure(image=image2)
            label2.image = image2
    
            image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label3.configure(image=image3)
            label3.image = image3
    
            image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label4.configure(image=image4)
            label4.image = image4
    
            image5 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label5.configure(image = image5)
            label5.image = image5
            
            image1_path = random.choice(dice)
            image1 = ImageTk.PhotoImage(Image.open(image1_path))
            label1.configure(image=image1)
            label1.image = image1
            
            image2_path = random.choice(dice)
            image2 = ImageTk.PhotoImage(Image.open(image2_path))
            label2.configure(image=image2)
            label2.image = image2
            
            image3_path = random.choice(dice)
            image3 = ImageTk.PhotoImage(Image.open(image3_path))
            label3.configure(image=image3)
            label3.image = image3
            
            image4_path = random.choice(dice)
            image4 = ImageTk.PhotoImage(Image.open(image4_path))
            label4.configure(image=image4)
            label4.image = image4
            
            image5_path = random.choice(dice)
            image5 = ImageTk.PhotoImage(Image.open(image5_path))
            label5.configure(image=image5)
            label5.image = image5
            
            res = diceNum[image1_path]+ diceNum[image2_path]  + diceNum[image3_path] +diceNum[image4_path]+diceNum[image5_path]
            label174.configure(text="You got  "+str(res))

        label174 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')
        label174.place(x=350,y=650)
    
        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)
        button.place(x=380, y=600)
        
#-----------------------Right Side--------------------------------------------------------------------------------------
        dice1 = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',]
        diceNum1 = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}
        
        image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        image41 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        image51 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        
        labelCustom = customtkinter.CTkLabel(windows, text='Player2', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')
        labelCustom.place(x=1030, y=100)

        label11 = tk.Label(windows, image= image11)
        label21 = tk.Label(windows, image=image21)
        label31 = tk.Label(windows, image=image31)
        label41 = tk.Label(windows, image=image41)
        label51 = tk.Label(windows, image=image51)

        label11.image = image11
        label21.image = image21
        label31.image = image31
        label41.image = image41
        label51.image = image51

        label11.place(x=980, y=250)
        label21.place(x=1130,y=250)
        label31.place(x = 1200, y = 400)
        label41.place(x =900, y = 400)
        label51.place(x = 1050, y = 400)

        def roll_dice():
            image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label11.configure(image=image11)
            label11.image = image11
    
            image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label21.configure(image=image21)
            label21.image = image21
    
            image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label31.configure(image=image31)
            label31.image = image31
    
            image41 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label41.configure(image=image41)
            label41.image = image41
    
            image51 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label51.configure(image = image51)
            label51.image = image51
            
            image11_path = random.choice(dice1)
            image11 = ImageTk.PhotoImage(Image.open(image11_path))
            label11.configure(image=image11)
            label11.image = image11
            
            image21_path = random.choice(dice1)
            image21 = ImageTk.PhotoImage(Image.open(image21_path))
            label21.configure(image=image21)
            label21.image = image21
            
            image31_path = random.choice(dice1)
            image31 = ImageTk.PhotoImage(Image.open(image31_path))
            label31.configure(image=image31)
            label31.image = image31
            
            image41_path = random.choice(dice1)
            image41 = ImageTk.PhotoImage(Image.open(image41_path))
            label41.configure(image=image41)
            label41.image = image41
            
            image51_path = random.choice(dice1)
            image51 = ImageTk.PhotoImage(Image.open(image51_path))
            label51.configure(image=image51)
            label51.image = image51
            
            res1 = diceNum[image11_path]+ diceNum[image21_path]  + diceNum[image31_path] +diceNum[image41_path]+diceNum[image51_path]
            label1741.configure(text="You got  "+str(res1))

        label1741 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')
        label1741.place(x=1060,y=650)
    
        button1 = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)
        button1.place(x=1100, y=600)
        
        windows.mainloop()

#-------------------------------------------------------------------------------------------------------------------------
#This class is for six dice

class sixDice:
    def six(self):
        windows = tk.Toplevel()
        img = Image.open('D:/python practice/background2.jpg')
        img = img.resize((windows.winfo_screenwidth(), windows.winfo_screenheight()))
        tk_img = ImageTk.PhotoImage(img)
        background = tk.Label(windows, image=tk_img)
        background.place(x=0,y=0, relheight=1, relwidth=1)
        windows.geometry("1535x800")
        windows.title("Dice Roll")

        dice = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',]
        diceNum = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}
        
        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image5 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        image6 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
        
        labelCustom = customtkinter.CTkLabel(windows, text='Player1', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')
        labelCustom.place(x=330, y=100)

        label1 = tk.Label(windows, image= image1)
        label2 = tk.Label(windows, image=image2)
        label3 = tk.Label(windows, image=image3)
        label4 = tk.Label(windows, image=image4)
        label5 = tk.Label(windows, image=image5)
        label6 = tk.Label(windows, image=image6)

        label1.image = image1
        label2.image = image2
        label3.image = image3
        label4.image = image4
        label5.image = image5
        label6.image = image6

        label1.place(x=200, y=250)
        label2.place(x=350,y=250)
        label3.place(x = 500, y = 250)
        label4.place(x =200, y = 400)
        label5.place(x = 350, y = 400)
        label6.place(x = 500, y=400)

        def roll_dice():
            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label1.configure(image=image1)
            label1.image = image1
    
            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label2.configure(image=image2)
            label2.image = image2
    
            image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label3.configure(image=image3)
            label3.image = image3
    
            image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label4.configure(image=image4)
            label4.image = image4
    
            image5 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label5.configure(image = image5)
            label5.image = image5
    
            image6 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
            label6.configure(image=image6)
            label6.image = image6
            
            image1_path = random.choice(dice)
            image1 = ImageTk.PhotoImage(Image.open(image1_path))
            label1.configure(image=image1)
            label1.image = image1
            
            image2_path = random.choice(dice)
            image2 = ImageTk.PhotoImage(Image.open(image2_path))
            label2.configure(image=image2)
            label2.image = image2
            
            image3_path = random.choice(dice)
            image3 = ImageTk.PhotoImage(Image.open(image3_path))
            label3.configure(image=image3)
            label3.image = image3
            
            image4_path = random.choice(dice)
            image4 = ImageTk.PhotoImage(Image.open(image4_path))
            label4.configure(image=image4)
            label4.image = image4
            
            image5_path = random.choice(dice)
            image5 = ImageTk.PhotoImage(Image.open(image5_path))
            label5.configure(image=image5)
            label5.image = image5
            
            image6_path = random.choice(dice)
            image6 = ImageTk.PhotoImage(Image.open(image6_path))
            label6.configure(image=image6)
            label6.image = image6
            
            res = diceNum[image1_path]+ diceNum[image2_path]  + diceNum[image3_path] +diceNum[image4_path]+diceNum[image5_path] +diceNum[image6_path]
            label174.configure(text="You got  "+str(res))

        label174 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')
        label174.place(x=360,y=650)
    
        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)
        button.place(x=380, y=600)
        
#----------------------------Right Side-----------------------------------------------------------------------------------

        dice1 = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',]
        diceNum1 = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}
        
        image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        image41 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        image51 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        image61 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
        
        labelCustom = customtkinter.CTkLabel(windows, text='Player2', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')
        labelCustom.place(x=1030, y=100)

        label11 = tk.Label(windows, image= image11)
        label21 = tk.Label(windows, image=image21)
        label31 = tk.Label(windows, image=image31)
        label41 = tk.Label(windows, image=image41)
        label51 = tk.Label(windows, image=image51)
        label61 = tk.Label(windows, image=image61)

        label11.image = image11
        label21.image = image21
        label31.image = image31
        label41.image = image41
        label51.image = image51
        label61.image = image61

        label11.place(x=900, y=250)
        label21.place(x=1050,y=250)
        label31.place(x = 1200, y = 250)
        label41.place(x =900, y = 400)
        label51.place(x = 1050, y = 400)
        label61.place(x = 1200, y=400)
        
        def roll_dice():
            image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label11.configure(image=image11)
            label11.image = image11
    
            image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label21.configure(image=image21)
            label21.image = image21
    
            image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label31.configure(image=image31)
            label31.image = image31
    
            image41 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label41.configure(image=image41)
            label41.image = image41
    
            image51 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label51.configure(image = image51)
            label51.image = image51
    
            image61 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))
            label61.configure(image=image61)
            label61.image = image61
            
            image11_path = random.choice(dice1)
            image11 = ImageTk.PhotoImage(Image.open(image11_path))
            label11.configure(image=image11)
            label11.image = image11
            
            image21_path = random.choice(dice1)
            image21 = ImageTk.PhotoImage(Image.open(image21_path))
            label21.configure(image=image21)
            label21.image = image21
            
            image31_path = random.choice(dice1)
            image31 = ImageTk.PhotoImage(Image.open(image31_path))
            label31.configure(image=image31)
            label31.image = image31
            
            image41_path = random.choice(dice1)
            image41 = ImageTk.PhotoImage(Image.open(image41_path))
            label41.configure(image=image41)
            label41.image = image41
            
            image51_path = random.choice(dice1)
            image51 = ImageTk.PhotoImage(Image.open(image51_path))
            label51.configure(image=image51)
            label51.image = image51
            
            image61_path = random.choice(dice1)
            image61 = ImageTk.PhotoImage(Image.open(image61_path))
            label61.configure(image=image61)
            label61.image = image61
            
            res1 = diceNum[image11_path]+ diceNum[image21_path]  + diceNum[image31_path] +diceNum[image41_path]+diceNum[image51_path] +diceNum[image61_path]
            label1741.configure(text="You got  "+str(res1))

        label1741 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')
        label1741.place(x=1060,y=650)
    
        button1 = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)
        button1.place(x=1100, y=600)
        windows.mainloop()

#_---------------Main------------------------------------------------------------------------------------------------------

#----------------Background Music-----------------------
def play_background_music():
    music_file = 'D:/python practice/bensound-summer_mp3_music.mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.set_volume(0.5)  # Set the volume (0.0 to 1.0)
    pygame.mixer.music.play(-1, 0, 5000)  # Play the music in a loop (-1 for infinite loop)


def stop_background_music():
    pygame.mixer.music.stop()

#-------------------------------------------------------------------------------

one = one_dice()
two = twoDice()
three = ThreeDice()
four = fourDice()
five = fiveDice()
six = sixDice()

windows = tk.Tk()
icon = tk.PhotoImage(file='D:/python practice/dice.png')
windows.geometry("1920x1080")
windows.title("Dice Roll")
windows.iconphoto(True, icon)
img = Image.open('D:/python practice/background1.jpg')
img = img.resize((windows.winfo_screenwidth(), windows.winfo_screenheight()))
tk_img = ImageTk.PhotoImage(img)
background = tk.Label(windows, image=tk_img)
background.place(x=0,y=0, relheight=1, relwidth=1)
labelCustom = customtkinter.CTkLabel(windows, text='How many dice you want to Roll?', text_font=('Times', 18), corner_radius=10, fg_color='#800000', width=500, height=50, text_color='white')
labelCustom.place(x = 550, y = 50)

button1 = customtkinter.CTkButton(fg_color='#000326',text_color='white',width=150,height=50,hover_color='Green',text_font=('Times'), text='One Dice',command=one.one)
button2 = customtkinter.CTkButton(fg_color='#000326',text_color='white',width=150,height=50,hover_color='Green',text='Two Dice', text_font=('Times'), command= two.two )
button3 = customtkinter.CTkButton(fg_color='#000326',text_color='white',width=150,height=50,hover_color='Green',text='Three Dice', text_font=('Times'),command=three.three)
button4 = customtkinter.CTkButton(fg_color='#000326',text_color='white',width=150,height=50,hover_color='Green',text='Four Dice', text_font=('Times'), command=four.four)
button5 = customtkinter.CTkButton(fg_color='#000326',text_color='white',width=150,height=50,hover_color='Green',text='Five Dice', text_font=('Times'), command=five.five)
button6 = customtkinter.CTkButton(fg_color='#000326',text_color='white',width=150,height=50,hover_color='Green',text='Six Dice', text_font=('Times'), command=six.six)

volume = tk.Button(windows,command=play_background_music, text='Music Start')
off = tk.Button(windows, command=stop_background_music, text='Stop Music')
volume.place(x = 50, y = 50)
off.place(x = 50, y = 100)

button1.place(x = 515, y = 250)
button2.place(x = 517, y = 350)
button3.place(x = 520, y = 450)
button4.place(x = 915, y = 250)
button5.place(x = 917, y = 350)
button6.place(x = 920, y = 450)

windows.mainloop()
#--------------------------------------------------------------------------------------------

