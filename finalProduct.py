[33mcommit 24bdf0c7e58ae84838791d58b74208f4c3d32c9c[m[33m ([m[1;36mHEAD -> [m[1;32mmaster[m[33m)[m
Author: Shees Baloch <63543725+Sheesbaloch@users.noreply.github.com>
Date:   Wed Feb 21 00:08:21 2024 +0500

    That is the code for dice rolling simulation  game

[1mdiff --git a/DiceRollingGame b/DiceRollingGame[m
[1mnew file mode 160000[m
[1mindex 0000000..d628740[m
[1m--- /dev/null[m
[1m+++ b/DiceRollingGame[m
[36m@@ -0,0 +1 @@[m
[32m+[m[32mSubproject commit d6287408f645b84872745a15f6e65e9dae28b423[m
[1mdiff --git a/NewFolder b/NewFolder[m
[1mnew file mode 100644[m
[1mindex 0000000..e69de29[m
[1mdiff --git a/background1.jpg b/background1.jpg[m
[1mnew file mode 100644[m
[1mindex 0000000..564d54e[m
Binary files /dev/null and b/background1.jpg differ
[1mdiff --git a/background2.jpg b/background2.jpg[m
[1mnew file mode 100644[m
[1mindex 0000000..2b0223a[m
Binary files /dev/null and b/background2.jpg differ
[1mdiff --git a/bensound-summer_mp3_music.mp3 b/bensound-summer_mp3_music.mp3[m
[1mnew file mode 100644[m
[1mindex 0000000..48802b1[m
Binary files /dev/null and b/bensound-summer_mp3_music.mp3 differ
[1mdiff --git a/dice.png b/dice.png[m
[1mnew file mode 100644[m
[1mindex 0000000..00265aa[m
Binary files /dev/null and b/dice.png differ
[1mdiff --git a/dice1.jpg b/dice1.jpg[m
[1mnew file mode 100644[m
[1mindex 0000000..707f5d2[m
Binary files /dev/null and b/dice1.jpg differ
[1mdiff --git a/dice2.jpg b/dice2.jpg[m
[1mnew file mode 100644[m
[1mindex 0000000..1206b39[m
Binary files /dev/null and b/dice2.jpg differ
[1mdiff --git a/dice3.jpg b/dice3.jpg[m
[1mnew file mode 100644[m
[1mindex 0000000..da8deb1[m
Binary files /dev/null and b/dice3.jpg differ
[1mdiff --git a/dice4.jpg b/dice4.jpg[m
[1mnew file mode 100644[m
[1mindex 0000000..8f68459[m
Binary files /dev/null and b/dice4.jpg differ
[1mdiff --git a/dice5.jpg b/dice5.jpg[m
[1mnew file mode 100644[m
[1mindex 0000000..588bd3d[m
Binary files /dev/null and b/dice5.jpg differ
[1mdiff --git a/dice6.jpg b/dice6.jpg[m
[1mnew file mode 100644[m
[1mindex 0000000..36fad3c[m
Binary files /dev/null and b/dice6.jpg differ
[1mdiff --git a/finalProject.py b/finalProject.py[m
[1mnew file mode 100644[m
[1mindex 0000000..3f07c4b[m
[1m--- /dev/null[m
[1m+++ b/finalProject.py[m
[36m@@ -0,0 +1,949 @@[m
[32m+[m[32mimport tkinter as tk[m
[32m+[m[32mfrom PIL import Image, ImageTk[m
[32m+[m[32mimport random[m
[32m+[m[32mimport pygame[m
[32m+[m[32mimport customtkinter[m
[32m+[m[32m#---------------------------------------------------------------------------------------------------------------------[m
[32m+[m[32m#that class is for one (1) Dice[m
[32m+[m
[32m+[m[32mclass one_dice:[m
[32m+[m[32m    def one(self):[m
[32m+[m[32m        windows = tk.Toplevel()[m
[32m+[m[41m        [m
[32m+[m[32m        img = Image.open('D:/python practice/background2.jpg')[m
[32m+[m[32m        img = img.resize((windows.winfo_screenwidth(), windows.winfo_screenheight()))[m
[32m+[m[32m        tk_img = ImageTk.PhotoImage(img)[m
[32m+[m[32m        background = tk.Label(windows, image=tk_img)[m
[32m+[m[32m        background.place(x=0,y=0, relheight=1, relwidth=1)[m
[32m+[m[32m        windows.resizable(False, False)[m
[32m+[m[32m        windows.geometry("1535x800")[m
[32m+[m[32m        windows.title("Dice Roll")[m
[32m+[m[32m        dice = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',][m
[32m+[m[32m        diceNum = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}[m
[32m+[m[41m        [m
[32m+[m[32m        labelCustom = customtkinter.CTkLabel(windows, text='Player1', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')[m
[32m+[m[32m        labelCustom.place(x=330, y=100)[m
[32m+[m[32m        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        label1 = tk.Label(windows, image= image1, padx=10)[m
[32m+[m[32m        label1.image = image1[m
[32m+[m
[32m+[m[32m        label1.place(x=350, y=300)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m           image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m           label1.configure(image=image1)[m
[32m+[m[32m           label1.image = image1[m
[32m+[m[41m           [m
[32m+[m[32m           image1_path = random.choice(dice)[m
[32m+[m[32m           image1 = ImageTk.PhotoImage(Image.open(image1_path))[m
[32m+[m[32m           label1.configure(image=image1)[m
[32m+[m[32m           label1.image = image1[m
[32m+[m[32m           res = diceNum[image1_path][m
[32m+[m[32m           label174.configure(text="You got  "+str(res))[m
[32m+[m[41m           [m
[32m+[m[32m        button = tk.Button(windows, bg='black', fg='white', font='Times 10 bold', text='Roll Dice', command=roll_dice)[m
[32m+[m[32m        button.place(x=380, y=600)[m
[32m+[m[32m        label174 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')[m
[32m+[m[32m        label174.place(x=350,y=650)[m
[32m+[m[41m        [m
[32m+[m[32m#----------Right Side---------------------------------------------------------------------[m
[32m+[m[32m        dice1 = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',][m
[32m+[m[32m        diceNum1 = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}[m
[32m+[m[41m        [m
[32m+[m[32m        labelCustom = customtkinter.CTkLabel(windows, text='Player2', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')[m
[32m+[m[32m        labelCustom.place(x=1030, y=100)[m
[32m+[m[41m        [m
[32m+[m[32m        image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        label11 = tk.Label(windows, image= image11,)[m
[32m+[m
[32m+[m[32m        label11.image = image11[m
[32m+[m
[32m+[m[32m        label11.place(x=1050, y=300)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m           image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m           label11.configure(image=image11)[m
[32m+[m[32m           label11.image = image11[m
[32m+[m[41m           [m
[32m+[m[32m           image1_path1 = random.choice(dice)[m
[32m+[m[32m           image11 = ImageTk.PhotoImage(Image.open(image1_path1))[m
[32m+[m[32m           label11.configure(image=image11)[m
[32m+[m[32m           label11.image = image11[m
[32m+[m[32m           res1 = diceNum1[image1_path1][m
[32m+[m[32m           label1745.configure(text="You got  "+str(res1))[m
[32m+[m
[32m+[m[32m        button1 = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button1.place(x=1100, y=600)[m
[32m+[m[41m        [m
[32m+[m[32m        label1745 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')[m
[32m+[m[32m        label1745.place(x=1070,y=650)[m
[32m+[m[41m        [m
[32m+[m[41m        [m
[32m+[m[32m        windows.mainloop()[m
[32m+[m
[32m+[m[32m#----------------------------------------------------------------------------------------------------------------------[m
[32m+[m[32m#that class is for two dice[m
[32m+[m
[32m+[m[32mclass twoDice:[m
[32m+[m[32m    def two(self):[m
[32m+[m[32m        windows = tk.Toplevel()[m
[32m+[m[41m        [m
[32m+[m[32m        img = Image.open('D:/python practice/background2.jpg')[m
[32m+[m[32m        img = img.resize((windows.winfo_screenwidth(), windows.winfo_screenheight()))[m
[32m+[m[32m        tk_img = ImageTk.PhotoImage(img)[m
[32m+[m[32m        background = tk.Label(windows, image=tk_img)[m
[32m+[m[32m        background.place(x=0,y=0, relheight=1, relwidth=1)[m
[32m+[m[32m        windows.geometry("1535x800")[m
[32m+[m[32m        windows.title("Dice Roll")[m
[32m+[m[41m        [m
[32m+[m[32m        c = tk.Canvas(windows, width=500,height=500)[m
[32m+[m[32m        dice = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',][m
[32m+[m[32m        diceNum = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}[m
[32m+[m[41m        [m
[32m+[m[32m        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[41m        [m
[32m+[m[32m        labelCustom = customtkinter.CTkLabel(windows, text='Player1', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')[m
[32m+[m[32m        labelCustom.place(x=330, y=100)[m
[32m+[m
[32m+[m[32m        label1 = tk.Label(windows, image= image1)[m
[32m+[m[32m        label2 = tk.Label(windows, image=image2)[m
[32m+[m
[32m+[m[32m        label1.image = image1[m
[32m+[m[32m        label2.image = image2[m
[32m+[m
[32m+[m[32m        label1.place(x=250, y=280)[m
[32m+[m[32m        label2.place(x=400,y=280)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label1.configure(image=image1)[m
[32m+[m[32m            label1.image = image1[m
[32m+[m[41m    [m
[32m+[m[32m            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label2.configure(image=image2)[m
[32m+[m[32m            label2.image = image2[m
[32m+[m[41m            [m
[32m+[m[32m            image1_path = random.choice(dice)[m
[32m+[m[32m            image1 = ImageTk.PhotoImage(Image.open(image1_path))[m
[32m+[m[32m            label1.configure(image=image1)[m
[32m+[m[32m            label1.image = image1[m
[32m+[m[41m            [m
[32m+[m[32m            image2_path = random.choice(dice)[m
[32m+[m[32m            image2 = ImageTk.PhotoImage(Image.open(image2_path))[m
[32m+[m[32m            label2.configure(image=image2)[m
[32m+[m[32m            label2.image = image2[m
[32m+[m[32m            res = diceNum[image1_path]+ diceNum[image2_path][m
[32m+[m[32m            label174.configure(text="You got  "+str(res))[m
[32m+[m[41m        [m
[32m+[m[32m        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button.place(x=380, y=600)[m
[32m+[m[41m        [m
[32m+[m[32m        label174 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')[m
[32m+[m[32m        label174.place(x=350,y=650)[m
[32m+[m[41m        [m
[32m+[m[32m#---------------------Left Side--------------------------------------------------------------------------------[m
[32m+[m[32m        dice1 = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',][m
[32m+[m[32m        diceNum1 = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}[m
[32m+[m[41m        [m
[32m+[m[32m        image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[41m        [m
[32m+[m[32m        labelCustom = customtkinter.CTkLabel(windows, text='Player2', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')[m
[32m+[m[32m        labelCustom.place(x=1030, y=100)[m
[32m+[m
[32m+[m[32m        label11 = tk.Label(windows, image= image11)[m
[32m+[m[32m        label21 = tk.Label(windows, image=image21)[m
[32m+[m
[32m+[m[32m        label11.image = image11[m
[32m+[m[32m        label21.image = image21[m
[32m+[m
[32m+[m[32m        label11.place(x=980, y=280)[m
[32m+[m[32m        label21.place(x=1130,y=280)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m            image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label11.configure(image=image11)[m
[32m+[m[32m            label11.image = image11[m
[32m+[m[41m    [m
[32m+[m[32m            image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label21.configure(image=image21)[m
[32m+[m[32m            label21.image = image21[m
[32m+[m[41m            [m
[32m+[m[32m            image11_path = random.choice(dice1)[m
[32m+[m[32m            image11 = ImageTk.PhotoImage(Image.open(image11_path))[m
[32m+[m[32m            label11.configure(image=image11)[m
[32m+[m[32m            label11.image = image11[m
[32m+[m[41m            [m
[32m+[m[32m            image21_path = random.choice(dice1)[m
[32m+[m[32m            image21 = ImageTk.PhotoImage(Image.open(image21_path))[m
[32m+[m[32m            label21.configure(image=image21)[m
[32m+[m[32m            label21.image = image21[m
[32m+[m[32m            res1 = diceNum1[image11_path]+ diceNum1[image21_path][m
[32m+[m[32m            label1745.configure(text="You got  "+str(res1))[m
[32m+[m[41m    [m
[32m+[m[32m        button1 = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button1.place(x=1080, y=600)[m
[32m+[m[41m        [m
[32m+[m[32m        label1745 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')[m
[32m+[m[32m        label1745.place(x=1070,y=650)[m
[32m+[m[32m        windows.mainloop()[m
[32m+[m
[32m+[m[32m#-----------------------------------------------------------------------------------------------------------------------[m
[32m+[m[32m#that class is for three dice[m
[32m+[m
[32m+[m[32mclass ThreeDice:[m
[32m+[m[32m    def three(self):[m
[32m+[m[32m        windows = tk.Toplevel()[m
[32m+[m[41m        [m
[32m+[m[32m        img = Image.open('D:/python practice/background2.jpg')[m
[32m+[m[32m        img = img.resize((windows.winfo_screenwidth(), windows.winfo_screenheight()))[m
[32m+[m[32m        tk_img = ImageTk.PhotoImage(img)[m
[32m+[m[32m        background = tk.Label(windows, image=tk_img)[m
[32m+[m[32m        background.place(x=0,y=0, relheight=1, relwidth=1)[m
[32m+[m[32m        windows.geometry("1535x800")[m
[32m+[m[32m        windows.title("Dice Roll")[m
[32m+[m
[32m+[m[32m        dice = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',][m
[32m+[m[32m        diceNum = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}[m
[32m+[m[41m        [m
[32m+[m[32m        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[41m        [m
[32m+[m[32m        labelCustom = customtkinter.CTkLabel(windows, text='Player1', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')[m
[32m+[m[32m        labelCustom.place(x=330, y=100)[m
[32m+[m
[32m+[m[32m        label1 = tk.Label(windows, image= image1)[m
[32m+[m[32m        label2 = tk.Label(windows, image=image2)[m
[32m+[m[32m        label3 = tk.Label(windows, image=image3)[m
[32m+[m
[32m+[m[32m        label1.image = image1[m
[32m+[m[32m        label2.image = image2[m
[32m+[m[32m        label3.image = image3[m
[32m+[m
[32m+[m[32m        label1.place(x=200, y=280)[m
[32m+[m[32m        label2.place(x=350,y=280)[m
[32m+[m[32m        label3.place(x = 500, y = 280)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label1.configure(image=image1)[m
[32m+[m[32m            label1.image = image1[m
[32m+[m[41m    [m
[32m+[m[32m            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label2.configure(image=image2)[m
[32m+[m[32m            label2.image = image2[m
[32m+[m[41m    [m
[32m+[m[32m            image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label3.configure(image=image3)[m
[32m+[m[32m            label3.image = image3[m
[32m+[m[41m            [m
[32m+[m[32m            image1_path = random.choice(dice)[m
[32m+[m[32m            image1 = ImageTk.PhotoImage(Image.open(image1_path))[m
[32m+[m[32m            label1.configure(image=image1)[m
[32m+[m[32m            label1.image = image1[m
[32m+[m[41m            [m
[32m+[m[32m            image2_path = random.choice(dice)[m
[32m+[m[32m            image2 = ImageTk.PhotoImage(Image.open(image2_path))[m
[32m+[m[32m            label2.configure(image=image2)[m
[32m+[m[32m            label2.image = image2[m
[32m+[m[41m            [m
[32m+[m[32m            image3_path = random.choice(dice)[m
[32m+[m[32m            image3 = ImageTk.PhotoImage(Image.open(image3_path))[m
[32m+[m[32m            label3.configure(image=image3)[m
[32m+[m[32m            label3.image = image3[m
[32m+[m[41m            [m
[32m+[m[41m            [m
[32m+[m[32m            res = diceNum[image1_path]+ diceNum[image2_path]  + diceNum[image3_path][m
[32m+[m[32m            label174.configure(text="You got  "+str(res))[m
[32m+[m
[32m+[m[32m        label174 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')[m
[32m+[m[32m        label174.place(x=380,y=650)[m
[32m+[m[41m    [m
[32m+[m[32m        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button.place(x=380, y=600)[m
[32m+[m[41m        [m
[32m+[m[32m#--------------------------------------Right Side--------------------------------------------------------------------------[m
[32m+[m[32m        dice1 = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',][m
[32m+[m[32m        diceNum1 = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}[m
[32m+[m[41m        [m
[32m+[m[32m        image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[41m        [m
[32m+[m[32m        labelCustom = customtkinter.CTkLabel(windows, text='Player2', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')[m
[32m+[m[32m        labelCustom.place(x=1030, y=100)[m
[32m+[m
[32m+[m[32m        label11 = tk.Label(windows, image= image11)[m
[32m+[m[32m        label21 = tk.Label(windows, image=image21)[m
[32m+[m[32m        label31 = tk.Label(windows, image=image31)[m
[32m+[m
[32m+[m[32m        label11.image = image11[m
[32m+[m[32m        label21.image = image21[m
[32m+[m[32m        label31.image = image31[m
[32m+[m
[32m+[m[32m        label11.place(x=900, y=300)[m
[32m+[m[32m        label21.place(x=1050,y=300)[m
[32m+[m[32m        label31.place(x = 1200, y = 300)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m            image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label11.configure(image=image11)[m
[32m+[m[32m            label11.image = image11[m
[32m+[m[41m    [m
[32m+[m[32m            image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label21.configure(image=image21)[m
[32m+[m[32m            label21.image = image21[m
[32m+[m[41m    [m
[32m+[m[32m            image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label31.configure(image=image31)[m
[32m+[m[32m            label31.image = image31[m
[32m+[m[41m            [m
[32m+[m[32m            image11_path = random.choice(dice1)[m
[32m+[m[32m            image11 = ImageTk.PhotoImage(Image.open(image11_path))[m
[32m+[m[32m            label11.configure(image=image11)[m
[32m+[m[32m            label11.image = image11[m
[32m+[m[41m            [m
[32m+[m[32m            image21_path = random.choice(dice1)[m
[32m+[m[32m            image21 = ImageTk.PhotoImage(Image.open(image21_path))[m
[32m+[m[32m            label21.configure(image=image21)[m
[32m+[m[32m            label21.image = image21[m
[32m+[m[41m            [m
[32m+[m[32m            image31_path = random.choice(dice1)[m
[32m+[m[32m            image31 = ImageTk.PhotoImage(Image.open(image31_path))[m
[32m+[m[32m            label31.configure(image=image31)[m
[32m+[m[32m            label31.image = image31[m
[32m+[m[41m            [m
[32m+[m[41m            [m
[32m+[m[32m            res = diceNum[image11_path]+ diceNum[image21_path]  + diceNum[image31_path][m
[32m+[m[32m            label1741.configure(text="You got  "+str(res))[m
[32m+[m[41m    [m
[32m+[m[32m        button1 = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button1.place(x=1100, y=600)[m
[32m+[m[41m        [m
[32m+[m[32m        label1741 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')[m
[32m+[m[32m        label1741.place(x=1070,y=650)[m
[32m+[m[32m        windows.mainloop()[m
[32m+[m
[32m+[m[32m#-----------------------------------------------------------------------------------------------------------------------[m
[32m+[m[32m#This class is for four dice[m
[32m+[m
[32m+[m[32mclass fourDice:[m
[32m+[m[32m    def four(self):[m
[32m+[m[32m        windows = tk.Toplevel()[m
[32m+[m[41m        [m
[32m+[m[32m        img = Image.open('D:/python practice/background2.jpg')[m
[32m+[m[32m        img = img.resize((windows.winfo_screenwidth(), windows.winfo_screenheight()))[m
[32m+[m[32m        tk_img = ImageTk.PhotoImage(img)[m
[32m+[m[32m        background = tk.Label(windows, image=tk_img)[m
[32m+[m[32m        background.place(x=0,y=0, relheight=1, relwidth=1)[m
[32m+[m[32m        windows.geometry("1535x800")[m
[32m+[m[32m        windows.title("Dice Roll")[m
[32m+[m
[32m+[m[32m        dice = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',][m
[32m+[m[32m        diceNum = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}[m
[32m+[m[41m        [m
[32m+[m[32m        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[41m        [m
[32m+[m[32m        labelCustom = customtkinter.CTkLabel(windows, text='Player1', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')[m
[32m+[m[32m        labelCustom.place(x=330, y=100)[m
[32m+[m
[32m+[m[32m        label1 = tk.Label(windows, image= image1)[m
[32m+[m[32m        label2 = tk.Label(windows, image=image2)[m
[32m+[m[32m        label3 = tk.Label(windows, image=image3)[m
[32m+[m[32m        label4 = tk.Label(windows, image=image4)[m
[32m+[m
[32m+[m[32m        label1.image = image1[m
[32m+[m[32m        label2.image = image2[m
[32m+[m[32m        label3.image = image3[m
[32m+[m[32m        label4.image = image4[m
[32m+[m
[32m+[m[32m        label1.place(x=350, y=250)[m
[32m+[m[32m        label2.place(x=200,y=400)[m
[32m+[m[32m        label3.place(x = 350, y = 400)[m
[32m+[m[32m        label4.place(x =500, y = 400)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label1.configure(image=image1)[m
[32m+[m[32m            label1.image = image1[m
[32m+[m[41m    [m
[32m+[m[32m            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label2.configure(image=image2)[m
[32m+[m[32m            label2.image = image2[m
[32m+[m[41m    [m
[32m+[m[32m            image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label3.configure(image=image3)[m
[32m+[m[32m            label3.image = image3[m
[32m+[m[41m    [m
[32m+[m[32m            image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label4.configure(image=image4)[m
[32m+[m[32m            label4.image = image4[m
[32m+[m[41m            [m
[32m+[m[32m            image1_path = random.choice(dice)[m
[32m+[m[32m            image1 = ImageTk.PhotoImage(Image.open(image1_path))[m
[32m+[m[32m            label1.configure(image=image1)[m
[32m+[m[32m            label1.image = image1[m
[32m+[m[41m            [m
[32m+[m[32m            image2_path = random.choice(dice)[m
[32m+[m[32m            image2 = ImageTk.PhotoImage(Image.open(image2_path))[m
[32m+[m[32m            label2.configure(image=image2)[m
[32m+[m[32m            label2.image = image2[m
[32m+[m[41m            [m
[32m+[m[32m            image3_path = random.choice(dice)[m
[32m+[m[32m            image3 = ImageTk.PhotoImage(Image.open(image3_path))[m
[32m+[m[32m            label3.configure(image=image3)[m
[32m+[m[32m            label3.image = image3[m
[32m+[m[41m            [m
[32m+[m[32m            image4_path = random.choice(dice)[m
[32m+[m[32m            image4 = ImageTk.PhotoImage(Image.open(image4_path))[m
[32m+[m[32m            label4.configure(image=image4)[m
[32m+[m[32m            label4.image = image4[m
[32m+[m[41m            [m
[32m+[m[32m            res = diceNum[image1_path]+ diceNum[image2_path]  + diceNum[image3_path] +diceNum[image4_path][m
[32m+[m[32m            label174.configure(text="You got  "+str(res))[m
[32m+[m
[32m+[m[32m        label174 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')[m
[32m+[m[32m        label174.place(x=380,y=650)[m
[32m+[m[41m    [m
[32m+[m[32m        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button.place(x=360, y=600)[m
[32m+[m[41m        [m
[32m+[m[32m#------------------------------right side--------------------------------------------------------------------------------[m
[32m+[m[32m        dice1 = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',][m
[32m+[m[32m        diceNum1 = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}[m
[32m+[m[41m        [m
[32m+[m[32m        image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        image41 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[41m        [m
[32m+[m[32m        labelCustom = customtkinter.CTkLabel(windows, text='Player2', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')[m
[32m+[m[32m        labelCustom.place(x=1030, y=100)[m
[32m+[m
[32m+[m[32m        label11 = tk.Label(windows, image= image11)[m
[32m+[m[32m        label21 = tk.Label(windows, image=image21)[m
[32m+[m[32m        label31 = tk.Label(windows, image=image31)[m
[32m+[m[32m        label41 = tk.Label(windows, image=image41)[m
[32m+[m
[32m+[m[32m        label11.image = image11[m
[32m+[m[32m        label21.image = image21[m
[32m+[m[32m        label31.image = image31[m
[32m+[m[32m        label41.image = image41[m
[32m+[m
[32m+[m[32m        label11.place(x=1050, y=250)[m
[32m+[m[32m        label21.place(x=900,y=400)[m
[32m+[m[32m        label31.place(x = 1050, y = 400)[m
[32m+[m[32m        label41.place(x =1200, y = 400)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m            image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label11.configure(image=image11)[m
[32m+[m[32m            label11.image = image11[m
[32m+[m[41m    [m
[32m+[m[32m            image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label21.configure(image=image21)[m
[32m+[m[32m            label21.image = image21[m
[32m+[m[41m    [m
[32m+[m[32m            image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label31.configure(image=image31)[m
[32m+[m[32m            label31.image = image31[m
[32m+[m[41m    [m
[32m+[m[32m            image41 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label41.configure(image=image41)[m
[32m+[m[32m            label41.image = image41[m
[32m+[m[41m            [m
[32m+[m[32m            image11_path = random.choice(dice1)[m
[32m+[m[32m            image11 = ImageTk.PhotoImage(Image.open(image11_path))[m
[32m+[m[32m            label11.configure(image=image11)[m
[32m+[m[32m            label11.image = image11[m
[32m+[m[41m            [m
[32m+[m[32m            image21_path = random.choice(dice1)[m
[32m+[m[32m            image21 = ImageTk.PhotoImage(Image.open(image21_path))[m
[32m+[m[32m            label21.configure(image=image21)[m
[32m+[m[32m            label21.image = image21[m
[32m+[m[41m            [m
[32m+[m[32m            image31_path = random.choice(dice1)[m
[32m+[m[32m            image31 = ImageTk.PhotoImage(Image.open(image31_path))[m
[32m+[m[32m            label31.configure(image=image31)[m
[32m+[m[32m            label31.image = image31[m
[32m+[m[41m            [m
[32m+[m[32m            image41_path = random.choice(dice1)[m
[32m+[m[32m            image41 = ImageTk.PhotoImage(Image.open(image41_path))[m
[32m+[m[32m            label41.configure(image=image41)[m
[32m+[m[32m            label41.image = image41[m
[32m+[m[41m            [m
[32m+[m[32m            res1 = diceNum[image11_path]+ diceNum[image21_path]  + diceNum[image31_path] +diceNum[image41_path][m
[32m+[m[32m            label1741.configure(text="You got  "+str(res1))[m
[32m+[m
[32m+[m[32m        label1741 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')[m
[32m+[m[32m        label1741.place(x=1060,y=650)[m
[32m+[m[41m    [m
[32m+[m[32m        button1 = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button1.place(x=1100, y=600)[m
[32m+[m[41m        [m
[32m+[m[32m        windows.mainloop()[m
[32m+[m
[32m+[m[32m#-----------------------------------------------------------------------------------------------------------------------[m
[32m+[m[32m#This class is for five dice[m
[32m+[m[32mclass fiveDice:[m
[32m+[m[41m    [m
[32m+[m[32m    def five(self):[m
[32m+[m[32m        windows = tk.Toplevel()[m
[32m+[m[32m        img = Image.open('D:/python practice/background2.jpg')[m
[32m+[m[32m        img = img.resize((windows.winfo_screenwidth(), windows.winfo_screenheight()))[m
[32m+[m[32m        tk_img = ImageTk.PhotoImage(img)[m
[32m+[m[32m        background = tk.Label(windows, image=tk_img)[m
[32m+[m[32m        background.place(x=0,y=0, relheight=1, relwidth=1)[m
[32m+[m[32m        windows.geometry("1535x800")[m
[32m+[m[32m        windows.title("Dice Roll")[m
[32m+[m[41m        [m
[32m+[m
[32m+[m[32m        dice = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',][m
[32m+[m[32m        diceNum = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}[m
[32m+[m[41m        [m
[32m+[m[32m        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image5 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[41m        [m
[32m+[m[32m        labelCustom = customtkinter.CTkLabel(windows, text='Player1', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')[m
[32m+[m[32m        labelCustom.place(x=330, y=100)[m
[32m+[m[41m        [m
[32m+[m[32m        label1 = tk.Label(windows, image= image1)[m
[32m+[m[32m        label2 = tk.Label(windows, image=image2)[m
[32m+[m[32m        label3 = tk.Label(windows, image=image3)[m
[32m+[m[32m        label4 = tk.Label(windows, image=image4)[m
[32m+[m[32m        label5 = tk.Label(windows, image=image5)[m
[32m+[m
[32m+[m[32m        label1.image = image1[m
[32m+[m[32m        label2.image = image2[m
[32m+[m[32m        label3.image = image3[m
[32m+[m[32m        label4.image = image4[m
[32m+[m[32m        label5.image = image5[m
[32m+[m
[32m+[m[32m        label1.place(x=200, y=400)[m
[32m+[m[32m        label2.place(x=280,y=250)[m
[32m+[m[32m        label3.place(x = 430, y = 250)[m
[32m+[m[32m        label4.place(x =350, y = 400)[m
[32m+[m[32m        label5.place(x = 500, y = 400)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label1.configure(image=image1)[m
[32m+[m[32m            label1.image = image1[m
[32m+[m[41m    [m
[32m+[m[32m            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label2.configure(image=image2)[m
[32m+[m[32m            label2.image = image2[m
[32m+[m[41m    [m
[32m+[m[32m            image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label3.configure(image=image3)[m
[32m+[m[32m            label3.image = image3[m
[32m+[m[41m    [m
[32m+[m[32m            image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label4.configure(image=image4)[m
[32m+[m[32m            label4.image = image4[m
[32m+[m[41m    [m
[32m+[m[32m            image5 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label5.configure(image = image5)[m
[32m+[m[32m            label5.image = image5[m
[32m+[m[41m            [m
[32m+[m[32m            image1_path = random.choice(dice)[m
[32m+[m[32m            image1 = ImageTk.PhotoImage(Image.open(image1_path))[m
[32m+[m[32m            label1.configure(image=image1)[m
[32m+[m[32m            label1.image = image1[m
[32m+[m[41m            [m
[32m+[m[32m            image2_path = random.choice(dice)[m
[32m+[m[32m            image2 = ImageTk.PhotoImage(Image.open(image2_path))[m
[32m+[m[32m            label2.configure(image=image2)[m
[32m+[m[32m            label2.image = image2[m
[32m+[m[41m            [m
[32m+[m[32m            image3_path = random.choice(dice)[m
[32m+[m[32m            image3 = ImageTk.PhotoImage(Image.open(image3_path))[m
[32m+[m[32m            label3.configure(image=image3)[m
[32m+[m[32m            label3.image = image3[m
[32m+[m[41m            [m
[32m+[m[32m            image4_path = random.choice(dice)[m
[32m+[m[32m            image4 = ImageTk.PhotoImage(Image.open(image4_path))[m
[32m+[m[32m            label4.configure(image=image4)[m
[32m+[m[32m            label4.image = image4[m
[32m+[m[41m            [m
[32m+[m[32m            image5_path = random.choice(dice)[m
[32m+[m[32m            image5 = ImageTk.PhotoImage(Image.open(image5_path))[m
[32m+[m[32m            label5.configure(image=image5)[m
[32m+[m[32m            label5.image = image5[m
[32m+[m[41m            [m
[32m+[m[32m            res = diceNum[image1_path]+ diceNum[image2_path]  + diceNum[image3_path] +diceNum[image4_path]+diceNum[image5_path][m
[32m+[m[32m            label174.configure(text="You got  "+str(res))[m
[32m+[m
[32m+[m[32m        label174 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')[m
[32m+[m[32m        label174.place(x=350,y=650)[m
[32m+[m[41m    [m
[32m+[m[32m        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button.place(x=380, y=600)[m
[32m+[m[41m        [m
[32m+[m[32m#-----------------------Right Side--------------------------------------------------------------------------------------[m
[32m+[m[32m        dice1 = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',][m
[32m+[m[32m        diceNum1 = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}[m
[32m+[m[41m        [m
[32m+[m[32m        image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        image41 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        image51 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[41m        [m
[32m+[m[32m        labelCustom = customtkinter.CTkLabel(windows, text='Player2', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')[m
[32m+[m[32m        labelCustom.place(x=1030, y=100)[m
[32m+[m
[32m+[m[32m        label11 = tk.Label(windows, image= image11)[m
[32m+[m[32m        label21 = tk.Label(windows, image=image21)[m
[32m+[m[32m        label31 = tk.Label(windows, image=image31)[m
[32m+[m[32m        label41 = tk.Label(windows, image=image41)[m
[32m+[m[32m        label51 = tk.Label(windows, image=image51)[m
[32m+[m
[32m+[m[32m        label11.image = image11[m
[32m+[m[32m        label21.image = image21[m
[32m+[m[32m        label31.image = image31[m
[32m+[m[32m        label41.image = image41[m
[32m+[m[32m        label51.image = image51[m
[32m+[m
[32m+[m[32m        label11.place(x=980, y=250)[m
[32m+[m[32m        label21.place(x=1130,y=250)[m
[32m+[m[32m        label31.place(x = 1200, y = 400)[m
[32m+[m[32m        label41.place(x =900, y = 400)[m
[32m+[m[32m        label51.place(x = 1050, y = 400)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m            image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label11.configure(image=image11)[m
[32m+[m[32m            label11.image = image11[m
[32m+[m[41m    [m
[32m+[m[32m            image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label21.configure(image=image21)[m
[32m+[m[32m            label21.image = image21[m
[32m+[m[41m    [m
[32m+[m[32m            image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label31.configure(image=image31)[m
[32m+[m[32m            label31.image = image31[m
[32m+[m[41m    [m
[32m+[m[32m            image41 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label41.configure(image=image41)[m
[32m+[m[32m            label41.image = image41[m
[32m+[m[41m    [m
[32m+[m[32m            image51 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label51.configure(image = image51)[m
[32m+[m[32m            label51.image = image51[m
[32m+[m[41m            [m
[32m+[m[32m            image11_path = random.choice(dice1)[m
[32m+[m[32m            image11 = ImageTk.PhotoImage(Image.open(image11_path))[m
[32m+[m[32m            label11.configure(image=image11)[m
[32m+[m[32m            label11.image = image11[m
[32m+[m[41m            [m
[32m+[m[32m            image21_path = random.choice(dice1)[m
[32m+[m[32m            image21 = ImageTk.PhotoImage(Image.open(image21_path))[m
[32m+[m[32m            label21.configure(image=image21)[m
[32m+[m[32m            label21.image = image21[m
[32m+[m[41m            [m
[32m+[m[32m            image31_path = random.choice(dice1)[m
[32m+[m[32m            image31 = ImageTk.PhotoImage(Image.open(image31_path))[m
[32m+[m[32m            label31.configure(image=image31)[m
[32m+[m[32m            label31.image = image31[m
[32m+[m[41m            [m
[32m+[m[32m            image41_path = random.choice(dice1)[m
[32m+[m[32m            image41 = ImageTk.PhotoImage(Image.open(image41_path))[m
[32m+[m[32m            label41.configure(image=image41)[m
[32m+[m[32m            label41.image = image41[m
[32m+[m[41m            [m
[32m+[m[32m            image51_path = random.choice(dice1)[m
[32m+[m[32m            image51 = ImageTk.PhotoImage(Image.open(image51_path))[m
[32m+[m[32m            label51.configure(image=image51)[m
[32m+[m[32m            label51.image = image51[m
[32m+[m[41m            [m
[32m+[m[32m            res1 = diceNum[image11_path]+ diceNum[image21_path]  + diceNum[image31_path] +diceNum[image41_path]+diceNum[image51_path][m
[32m+[m[32m            label1741.configure(text="You got  "+str(res1))[m
[32m+[m
[32m+[m[32m        label1741 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')[m
[32m+[m[32m        label1741.place(x=1060,y=650)[m
[32m+[m[41m    [m
[32m+[m[32m        button1 = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button1.place(x=1100, y=600)[m
[32m+[m[41m        [m
[32m+[m[32m        windows.mainloop()[m
[32m+[m
[32m+[m[32m#-------------------------------------------------------------------------------------------------------------------------[m
[32m+[m[32m#This class is for six dice[m
[32m+[m
[32m+[m[32mclass sixDice:[m
[32m+[m[32m    def six(self):[m
[32m+[m[32m        windows = tk.Toplevel()[m
[32m+[m[32m        img = Image.open('D:/python practice/background2.jpg')[m
[32m+[m[32m        img = img.resize((windows.winfo_screenwidth(), windows.winfo_screenheight()))[m
[32m+[m[32m        tk_img = ImageTk.PhotoImage(img)[m
[32m+[m[32m        background = tk.Label(windows, image=tk_img)[m
[32m+[m[32m        background.place(x=0,y=0, relheight=1, relwidth=1)[m
[32m+[m[32m        windows.geometry("1535x800")[m
[32m+[m[32m        windows.title("Dice Roll")[m
[32m+[m
[32m+[m[32m        dice = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',][m
[32m+[m[32m        diceNum = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}[m
[32m+[m[41m        [m
[32m+[m[32m        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image5 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image6 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[41m        [m
[32m+[m[32m        labelCustom = customtkinter.CTkLabel(windows, text='Player1', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')[m
[32m+[m[32m        labelCustom.place(x=330, y=100)[m
[32m+[m
[32m+[m[32m        label1 = tk.Label(windows, image= image1)[m
[32m+[m[32m        label2 = tk.Label(windows, image=image2)[m
[32m+[m[32m        label3 = tk.Label(windows, image=image3)[m
[32m+[m[32m        label4 = tk.Label(windows, image=image4)[m
[32m+[m[32m        label5 = tk.Label(windows, image=image5)[m
[32m+[m[32m        label6 = tk.Label(windows, image=image6)[m
[32m+[m
[32m+[m[32m        label1.image = image1[m
[32m+[m[32m        label2.image = image2[m
[32m+[m[32m        label3.image = image3[m
[32m+[m[32m        label4.image = image4[m
[32m+[m[32m        label5.image = image5[m
[32m+[m[32m        label6.image = image6[m
[32m+[m
[32m+[m[32m        label1.place(x=200, y=250)[m
[32m+[m[32m        label2.place(x=350,y=250)[m
[32m+[m[32m        label3.place(x = 500, y = 250)[m
[32m+[m[32m        label4.place(x =200, y = 400)[m
[32m+[m[32m        label5.place(x = 350, y = 400)[m
[32m+[m[32m        label6.place(x = 500, y=400)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label1.configure(image=image1)[m
[32m+[m[32m            label1.image = image1[m
[32m+[m[41m    [m
[32m+[m[32m            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label2.configure(image=image2)[m
[32m+[m[32m            label2.image = image2[m
[32m+[m[41m    [m
[32m+[m[32m            image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label3.configure(image=image3)[m
[32m+[m[32m            label3.image = image3[m
[32m+[m[41m    [m
[32m+[m[32m            image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label4.configure(image=image4)[m
[32m+[m[32m            label4.image = image4[m
[32m+[m[41m    [m
[32m+[m[32m            image5 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label5.configure(image = image5)[m
[32m+[m[32m            label5.image = image5[m
[32m+[m[41m    [m
[32m+[m[32m            image6 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label6.configure(image=image6)[m
[32m+[m[32m            label6.image = image6[m
[32m+[m[41m            [m
[32m+[m[32m            image1_path = random.choice(dice)[m
[32m+[m[32m            image1 = ImageTk.PhotoImage(Image.open(image1_path))[m
[32m+[m[32m            label1.configure(image=image1)[m
[32m+[m[32m            label1.image = image1[m
[32m+[m[41m            [m
[32m+[m[32m            image2_path = random.choice(dice)[m
[32m+[m[32m            image2 = ImageTk.PhotoImage(Image.open(image2_path))[m
[32m+[m[32m            label2.configure(image=image2)[m
[32m+[m[32m            label2.image = image2[m
[32m+[m[41m            [m
[32m+[m[32m            image3_path = random.choice(dice)[m
[32m+[m[32m            image3 = ImageTk.PhotoImage(Image.open(image3_path))[m
[32m+[m[32m            label3.configure(image=image3)[m
[32m+[m[32m            label3.image = image3[m
[32m+[m[41m            [m
[32m+[m[32m            image4_path = random.choice(dice)[m
[32m+[m[32m            image4 = ImageTk.PhotoImage(Image.open(image4_path))[m
[32m+[m[32m            label4.configure(image=image4)[m
[32m+[m[32m            label4.image = image4[m
[32m+[m[41m            [m
[32m+[m[32m            image5_path = random.choice(dice)[m
[32m+[m[32m            image5 = ImageTk.PhotoImage(Image.open(image5_path))[m
[32m+[m[32m            label5.configure(image=image5)[m
[32m+[m[32m            label5.image = image5[m
[32m+[m[41m            [m
[32m+[m[32m            image6_path = random.choice(dice)[m
[32m+[m[32m            image6 = ImageTk.PhotoImage(Image.open(image6_path))[m
[32m+[m[32m            label6.configure(image=image6)[m
[32m+[m[32m            label6.image = image6[m
[32m+[m[41m            [m
[32m+[m[32m            res = diceNum[image1_path]+ diceNum[image2_path]  + diceNum[image3_path] +diceNum[image4_path]+diceNum[image5_path] +diceNum[image6_path][m
[32m+[m[32m            label174.configure(text="You got  "+str(res))[m
[32m+[m
[32m+[m[32m        label174 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')[m
[32m+[m[32m        label174.place(x=360,y=650)[m
[32m+[m[41m    [m
[32m+[m[32m        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button.place(x=380, y=600)[m
[32m+[m[41m        [m
[32m+[m[32m#----------------------------Right Side-----------------------------------------------------------------------------------[m
[32m+[m
[32m+[m[32m        dice1 = ['D:/python practice/dice1.jpg','D:/python practice/dice2.jpg','D:/python practice/dice3.jpg','D:/python practice/dice4.jpg','D:/python practice/dice5.jpg','D:/python practice/dice6.jpg',][m
[32m+[m[32m        diceNum1 = {'D:/python practice/dice1.jpg':1,'D:/python practice/dice2.jpg':2,'D:/python practice/dice3.jpg':3,'D:/python practice/dice4.jpg':4,'D:/python practice/dice5.jpg':5,'D:/python practice/dice6.jpg':6,}[m
[32m+[m[41m        [m
[32m+[m[32m        image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        image41 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        image51 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m        image61 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[41m        [m
[32m+[m[32m        labelCustom = customtkinter.CTkLabel(windows, text='Player2', text_font=('Times', 18), corner_radius=10, bg_color='black', fg_color='#800000', width=150, height=40, text_color='white')[m
[32m+[m[32m        labelCustom.place(x=1030, y=100)[m
[32m+[m
[32m+[m[32m        label11 = tk.Label(windows, image= image11)[m
[32m+[m[32m        label21 = tk.Label(windows, image=image21)[m
[32m+[m[32m        label31 = tk.Label(windows, image=image31)[m
[32m+[m[32m        label41 = tk.Label(windows, image=image41)[m
[32m+[m[32m        label51 = tk.Label(windows, image=image51)[m
[32m+[m[32m        label61 = tk.Label(windows, image=image61)[m
[32m+[m
[32m+[m[32m        label11.image = image11[m
[32m+[m[32m        label21.image = image21[m
[32m+[m[32m        label31.image = image31[m
[32m+[m[32m        label41.image = image41[m
[32m+[m[32m        label51.image = image51[m
[32m+[m[32m        label61.image = image61[m
[32m+[m
[32m+[m[32m        label11.place(x=900, y=250)[m
[32m+[m[32m        label21.place(x=1050,y=250)[m
[32m+[m[32m        label31.place(x = 1200, y = 250)[m
[32m+[m[32m        label41.place(x =900, y = 400)[m
[32m+[m[32m        label51.place(x = 1050, y = 400)[m
[32m+[m[32m        label61.place(x = 1200, y=400)[m
[32m+[m[41m        [m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m            image11 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label11.configure(image=image11)[m
[32m+[m[32m            label11.image = image11[m
[32m+[m[41m    [m
[32m+[m[32m            image21 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label21.configure(image=image21)[m
[32m+[m[32m            label21.image = image21[m
[32m+[m[41m    [m
[32m+[m[32m            image31 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label31.configure(image=image31)[m
[32m+[m[32m            label31.image = image31[m
[32m+[m[41m    [m
[32m+[m[32m            image41 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label41.configure(image=image41)[m
[32m+[m[32m            label41.image = image41[m
[32m+[m[41m    [m
[32m+[m[32m            image51 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label51.configure(image = image51)[m
[32m+[m[32m            label51.image = image51[m
[32m+[m[41m    [m
[32m+[m[32m            image61 = ImageTk.PhotoImage(Image.open(random.choice(dice1)))[m
[32m+[m[32m            label61.configure(image=image61)[m
[32m+[m[32m            label61.image = image61[m
[32m+[m[41m            [m
[32m+[m[32m            image11_path = random.choice(dice1)[m
[32m+[m[32m            image11 = ImageTk.PhotoImage(Image.open(image11_path))[m
[32m+[m[32m            label11.configure(image=image11)[m
[32m+[m[32m            label11.image = image11[m
[32m+[m[41m            [m
[32m+[m[32m            image21_path = random.choice(dice1)[m
[32m+[m[32m            image21 = ImageTk.PhotoImage(Image.open(image21_path))[m
[32m+[m[32m            label21.configure(image=image21)[m
[32m+[m[32m            label21.image = image21[m
[32m+[m[41m            [m
[32m+[m[32m            image31_path = random.choice(dice1)[m
[32m+[m[32m            image31 = ImageTk.PhotoImage(Image.open(image31_path))[m
[32m+[m[32m            label31.configure(image=image31)[m
[32m+[m[32m            label31.image = image31[m
[32m+[m[41m            [m
[32m+[m[32m            image41_path = random.choice(dice1)[m
[32m+[m[32m            image41 = ImageTk.PhotoImage(Image.open(image41_path))[m
[32m+[m[32m            label41.configure(image=image41)[m
[32m+[m[32m            label41.image = image41[m
[32m+[m[41m            [m
[32m+[m[32m            image51_path = random.choice(dice1)[m
[32m+[m[32m            image51 = ImageTk.PhotoImage(Image.open(image51_path))[m
[32m+[m[32m            label51.configure(image=image51)[m
[32m+[m[32m            label51.image = image51[m
[32m+[m[41m            [m
[32m+[m[32m            image61_path = random.choice(dice1)[m
[32m+[m[32m            image61 = ImageTk.PhotoImage(Image.open(image61_path))[m
[32m+[m[32m            label61.configure(image=image61)[m
[32m+[m[32m            label61.image = image61[m
[32m+[m[41m            [m
[32m+[m[32m            res1 = diceNum[image11_path]+ diceNum[image21_path]  + diceNum[image31_path] +diceNum[image41_path]+diceNum[image51_path] +diceNum[image61_path][m
[32m+[m[32m            label1741.configure(text="You got  "+str(res1))[m
[32m+[m
[32m+[m[32m        label1741 = tk.Label(windows, text='', font=('Times',20,'bold'),fg='white', bg='black')[m
[32m+[m[32m        label1741.place(x=1060,y=650)[m
[32m+[m[41m    [m
[32m+[m[32m        button1 = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button1.place(x=1100, y=600)[m
[32m+[m[32m        windows.mainloop()[m
[32m+[m
[32m+[m[32m#_---------------Main------------------------------------------------------------------------------------------------------[m
[32m+[m
[32m+[m[32m#----------------Background Music-----------------------[m
[32m+[m[32mdef play_background_music():[m
[32m+[m[32m    music_file = 'D:/python practice/bensound-summer_mp3_music.mp3'[m
[32m+[m[32m    pygame.mixer.init()[m
[32m+[m[32m    pygame.mixer.music.load(music_file)[m
[32m+[m[32m    pygame.mixer.music.set_volume(0.5)  # Set the volume (0.0 to 1.0)[m
[32m+[m[32m    pygame.mixer.music.play(-1, 0, 5000)  # Play the music in a loop (-1 for infinite loop)[m
[32m+[m
[32m+[m
[32m+[m[32mdef stop_background_music():[m
[32m+[m[32m    pygame.mixer.music.stop()[m
[32m+[m
[32m+[m[32m#-------------------------------------------------------------------------------[m
[32m+[m
[32m+[m[32mone = one_dice()[m
[32m+[m[32mtwo = twoDice()[m
[32m+[m[32mthree = ThreeDice()[m
[32m+[m[32mfour = fourDice()[m
[32m+[m[32mfive = fiveDice()[m
[32m+[m[32msix = sixDice()[m
[32m+[m
[32m+[m[32mwindows = tk.Tk()[m
[32m+[m[32micon = tk.PhotoImage(file='D:/python practice/dice.png')[m
[32m+[m[32mwindows.geometry("1920x1080")[m
[32m+[m[32mwindows.title("Dice Roll")[m
[32m+[m[32mwindows.iconphoto(True, icon)[m
[32m+[m[32mimg = Image.open('D:/python practice/background1.jpg')[m
[32m+[m[32mimg = img.resize((windows.winfo_screenwidth(), windows.winfo_screenheight()))[m
[32m+[m[32mtk_img = ImageTk.PhotoImage(img)[m
[32m+[m[32mbackground = tk.Label(windows, image=tk_img)[m
[32m+[m[32mbackground.place(x=0,y=0, relheight=1, relwidth=1)[m
[32m+[m[32mlabelCustom = customtkinter.CTkLabel(windows, text='How many dice you want to Roll?', text_font=('Times', 18), corner_radius=10, fg_color='#800000', width=500, height=50, text_color='white')[m
[32m+[m[32mlabelCustom.place(x = 550, y = 50)[m
[32m+[m
[32m+[m[32mbutton1 = customtkinter.CTkButton(fg_color='#000326',text_color='white',width=150,height=50,hover_color='Green',text_font=('Times'), text='One Dice',command=one.one)[m
[32m+[m[32mbutton2 = customtkinter.CTkButton(fg_color='#000326',text_color='white',width=150,height=50,hover_color='Green',text='Two Dice', text_font=('Times'), command= two.two )[m
[32m+[m[32mbutton3 = customtkinter.CTkButton(fg_color='#000326',text_color='white',width=150,height=50,hover_color='Green',text='Three Dice', text_font=('Times'),command=three.three)[m
[32m+[m[32mbutton4 = customtkinter.CTkButton(fg_color='#000326',text_color='white',width=150,height=50,hover_color='Green',text='Four Dice', text_font=('Times'), command=four.four)[m
[32m+[m[32mbutton5 = customtkinter.CTkButton(fg_color='#000326',text_color='white',width=150,height=50,hover_color='Green',text='Five Dice', text_font=('Times'), command=five.five)[m
[32m+[m[32mbutton6 = customtkinter.CTkButton(fg_color='#000326',text_color='white',width=150,height=50,hover_color='Green',text='Six Dice', text_font=('Times'), command=six.six)[m
[32m+[m
[32m+[m[32mvolume = tk.Button(windows,command=play_background_music, text='Music Start')[m
[32m+[m[32moff = tk.Button(windows, command=stop_background_music, text='Stop Music')[m
[32m+[m[32mvolume.place(x = 50, y = 50)[m
[32m+[m[32moff.place(x = 50, y = 100)[m
[32m+[m
[32m+[m[32mbutton1.place(x = 515, y = 250)[m
[32m+[m[32mbutton2.place(x = 517, y = 350)[m
[32m+[m[32mbutton3.place(x = 520, y = 450)[m
[32m+[m[32mbutton4.place(x = 915, y = 250)[m
[32m+[m[32mbutton5.place(x = 917, y = 350)[m
[32m+[m[32mbutton6.place(x = 920, y = 450)[m
[32m+[m
[32m+[m[32mwindows.mainloop()[m
[32m+[m[32m#--------------------------------------------------------------------------------------------[m
[32m+[m
[1mdiff --git a/slides and documentation/DOCUMENTATION OF DICE ROLLING PROJECT SCD1.docx b/slides and documentation/DOCUMENTATION OF DICE ROLLING PROJECT SCD1.docx[m
[1mnew file mode 100644[m
[1mindex 0000000..5aabaad[m
[1m--- /dev/null[m
[1m+++ b/slides and documentation/DOCUMENTATION OF DICE ROLLING PROJECT SCD1.docx[m	
[36m@@ -0,0 +1,523 @@[m
[32m+[m[32m                        "DOCUMENTATION OF DICE ROLLING SIMULATOR PROJECT"[m[41m  [m
[32m+[m[41m                                        [m
[32m+[m[32m                         Submitted To: Mam Imrana Rafiq Submitted By:[m[41m [m
[32m+[m	[32mShees Ul Haq 	    21011598-191[m[41m [m
[32m+[m[32m                             Malik Shahnawaz   21011598-190[m[41m [m
[32m+[m[32m                            Hadabia Amjad      21011598-182[m[41m [m
[32m+[m[32m                           Noor Fatima            21011598-163[m
[32m+[m[32m                                      Course Title:[m[41m [m
[32m+[m[32m                   Software Construction and Development Course Code:[m[41m [m
[32m+[m[32m                                         SE-327[m[41m [m
[32m+[m[32m                                          Semester :[m[41m [m
[32m+[m[32m                                         5th-C[m[41m [m
[32m+[m[32m                                         Department:[m[41m [m
[32m+[m[32m                                 Software Engineering[m[41m  [m
[32m+[m[41m                                        [m
[32m+[m[41m                                        [m
[32m+[m[41m [m
[32m+[m
[32m+[m[41m	 [m
[32m+[m[32mTable of content[m[41m [m
[32m+[m[32m1. Dice Rolling Simulator:	3[m
[32m+[m[32m2. Abstract	3[m
[32m+[m[32m3. Target Audience:	4[m
[32m+[m[32m4. Project Goals and Objectives:	4[m
[32m+[m[32mi) Educational Exploration:	4[m
[32m+[m[32mii) User Engagement and Interactivity:	4[m
[32m+[m[32miii) Versatility and Customization:	4[m
[32m+[m[32miv) Accessibility and Inclusivity:	4[m
[32m+[m[32mv) Integration of Technology:	5[m
[32m+[m[32m5. Tools and Technology:	5[m
[32m+[m[32ma. Visual Studio Code	5[m
[32m+[m[32mb. Python Language	5[m
[32m+[m[32mc. Tkinter Library	5[m
[32m+[m[32md. Random Module	5[m
[32m+[m[32m6. Flow Chart:	6[m
[32m+[m[32m7.  Model Architecture:	7[m
[32m+[m[32m7.1. Dice Roll Window	8[m
[32m+[m[32mPurpose:	8[m
[32m+[m[32mComponents:	8[m
[32m+[m[32mWorking:	8[m
[32m+[m[32m7.2 Dice Window	9[m
[32m+[m[32mPurpose:	9[m
[32m+[m[32mComponents:	9[m
[32m+[m[32mWorking:	9[m
[32m+[m[32m8. Source Code:	9[m
[32m+[m[32m9. Validation and Verification:	15[m
[32m+[m[32m10. Result	16[m
[32m+[m[32m11. Conclusion	16[m
[32m+[m[32m12. References:	17[m
[32m+[m
[32m+[m[32m  1. Dice Rolling Simulator:[m[41m [m
[32m+[m[41m [m
[32m+[m[32m        In a world increasingly dominated by technology, the allure of traditional games remains                                timeless. Among these, the simple act of rolling dice has been a source of entertainment        for centuries. However, with the advent of digital tools, the tangible experience of        rolling physical dice is being replaced by virtual simulations. The "Dice Rolling         Simulator" aims to bridge the gap between the traditional and the modern, providing         an engaging platform to explore the principles of randomness and probability.[m[41m  [m
[32m+[m[41m   [m
[32m+[m[32m        At its core, the dice rolling simulator is more than just a game; it's an exploration of        randomness. Randomness, a concept deeply embedded in the fabric of our universe, is        often challenging to comprehend. Through this project, we delve into the fundamental         nature of chance, discovering how a simple roll of dice can emulate the unpredictability          that governs various aspects of life.[m[41m [m
[32m+[m[41m [m
[32m+[m[32m  2. Abstract[m[41m  [m
[32m+[m[41m    [m
[32m+[m[32m   The project "Dice Roll Simulator" is designed to provide an entertaining small software for the  user. It is mainly built to let people spend their leisure time by rolling dice. In this project we  have given up to 6 dice, which a user has the full authority to choose the number of dice he  wants. He can select more than one dice at a time. In this way he can play with the system to  entertain himself.[m[41m  [m
[32m+[m[41m    [m
[32m+[m[32m   Beyond its entertainment value, the dice rolling simulator serves as an educational tool. By  engaging with the simulator, users can develop a practical understanding of probability theory.  The project encourages participants to analyze outcomes, understand distribution patterns, and  make informed predictions  -  skills applicable across various disciplines, from mathematics and  statistics to decision-making in everyday life.[m[41m [m
[32m+[m[41m    [m
[32m+[m[32m   The Dice Rolling Simulator is designed to be user-friendly yet comprehensive. Users can  customize the number and types of dice, explore different probability distributions, and even  simulate complex scenarios. The interactive nature of the simulator ensures an immersive  experience, allowing participants to experiment with variables and observe the resulting  outcomes in real-time.[m[41m [m
[32m+[m[41m   [m
[32m+[m[32m  3. Target Audience:[m[41m [m
[32m+[m[41m    [m
[32m+[m[32m   This project caters to a diverse audience. Whether you're a student seeking a hands-on approach  to probability theory, an educator looking for a dynamic teaching tool, or a casual gamer  interested in the art of chance, the Dice Rolling Simulator offers a unique and enjoyable  experience for all.[m[41m [m
[32m+[m[41m    [m
[32m+[m[32m  4. Project Goals and Objectives:[m[41m [m
[32m+[m[41m                [m
[32m+[m[32mi) Educational Exploration:[m[41m [m
[32m+[m[41m       [m
[32m+[m[32m            Foster a deeper understanding of randomness and probability among users. Develop interactive                  features that allow users to experiment with different dice combinations. Provide educational              content explaining the principles of probability theory and its real-world applications. Create               scenarios that encourage users to apply probability concepts in a practical context.[m[41m [m
[32m+[m
[32m+[m[32m  ii) User Engagement and Interactivity:[m[41m [m
[32m+[m[41m       [m
[32m+[m[32m              Create an engaging and user-friendly platform that encourages active participation. Design an               intuitive and visually appealing interface for users of all ages. Implement  customizable options               for users to choose the number and types of dice, as well as other relevant parameters.               Incorporate real-time feedback mechanisms to enhance user interaction and learning.[m[41m [m
[32m+[m
[32m+[m[32m  iii) Versatility and Customization:[m[41m [m
[32m+[m[41m       [m
[32m+[m[32m             Provide a versatile platform that caters to a diverse audience with varying levels of interest and                expertise. Allow users to simulate different dice combinations, from standard six-sided dice to               More complex variations. Enable customization of scenarios to explore specific probability                distributions or gaming scenarios. Accommodate both casual users and those seeking in-depth               exploration of probability concepts.[m[41m [m
[32m+[m
[32m+[m[32m  iv) Accessibility and Inclusivity:[m[41m [m
[32m+[m[41m       [m
[32m+[m[32m             Ensure that the simulator is accessible to a broad audience, including students, educators, and                casual gamers. Optimize the platform for usability across different devices and screen sizes.[m[41m  [m
[32m+[m[32m             Provide educational resources in multiple formats, accommodating various learning styles.               Consider inclusivity by designing features that cater to users with diverse abilities and               preferences.[m[41m [m
[32m+[m[41m [m
[32m+[m[32mv) Integration of Technology:[m[41m  [m
[32m+[m[32m            Leverage technology to enhance the user experience and expand the project's capabilities.[m[41m  [m
[32m+[m[32m            Explore possibilities for incorporating augmented reality (AR) or virtual reality (VR) elements in              future iterations.[m[41m [m
[32m+[m[41m [m
[32m+[m[32m            Consider machine learning algorithms to enhance the adaptability and intelligence of the               simulator. Integrate collaborative features, allowing users to engage with the simulator together              for shared learning experiences.[m[41m [m
[32m+[m[41m [m
[32m+[m[32m  5. Tools and Technology:[m[41m [m
[32m+[m[41m   [m
[32m+[m[32m             The following tools and technology have been used in the project:[m[41m [m
[32m+[m[32m     a. Visual Studio Code[m[41m [m
[32m+[m[32m     b. Python Language[m[41m [m
[32m+[m[32m     c. Tkinter Library[m[41m [m
[32m+[m[32m     d. Random Module[m[41m [m
[32m+[m[41m [m
[32m+[m[32m Visual Studio Code[m[41m [m
[32m+[m[32m   Visual Studio Code, also commonly referred to as VS Code, is a  [HYPERLINK: https://en.wikipedia.org/wiki/Source-code_editor]source [HYPERLINK: https://en.wikipedia.org/wiki/Source-code_editor]- [HYPERLINK: https://en.wikipedia.org/wiki/Source-code_editor]code editor [HYPERLINK: https://en.wikipedia.org/wiki/Source-code_editor]  [HYPERLINK: https://en.wikipedia.org/wiki/Source-code_editor]developed by  [HYPERLINK: https://en.wikipedia.org/wiki/Microsoft]Microsoft [HYPERLINK: https://en.wikipedia.org/wiki/Microsoft]  [HYPERLINK: https://en.wikipedia.org/wiki/Microsoft]for  [HYPERLINK: https://en.wikipedia.org/wiki/Windows]Windows [HYPERLINK: https://en.wikipedia.org/wiki/Windows], [HYPERLINK: https://en.wikipedia.org/wiki/Windows]  [HYPERLINK: https://en.wikipedia.org/wiki/Linux]Linux [HYPERLINK: https://en.wikipedia.org/wiki/Linux]  [HYPERLINK: https://en.wikipedia.org/wiki/Linux]and  [HYPERLINK: https://en.wikipedia.org/wiki/MacOS]macOS [HYPERLINK: https://en.wikipedia.org/wiki/MacOS]. [HYPERLINK: https://en.wikipedia.org/wiki/Visual_Studio_Code][[13]] [HYPERLINK: https://en.wikipedia.org/wiki/Visual_Studio_Code]  [HYPERLINK: https://en.wikipedia.org/wiki/Visual_Studio_Code]Features include support for  [HYPERLINK: https://en.wikipedia.org/wiki/Debugging]debugging [HYPERLINK: https://en.wikipedia.org/wiki/Debugging], [HYPERLINK: https://en.wikipedia.org/wiki/Debugging]  [HYPERLINK: https://en.wikipedia.org/wiki/Syntax_highlighting]syntax  [HYPERLINK: https://en.wikipedia.org/wiki/Syntax_highlighting]highlighting [HYPERLINK: https://en.wikipedia.org/wiki/Syntax_highlighting], [HYPERLINK: https://en.wikipedia.org/wiki/Syntax_highlighting]  [HYPERLINK: https://en.wikipedia.org/wiki/Intelligent_code_completion]intelligent code completion [HYPERLINK: https://en.wikipedia.org/wiki/Intelligent_code_completion], [HYPERLINK: https://en.wikipedia.org/wiki/Intelligent_code_completion]  [HYPERLINK: https://en.wikipedia.org/wiki/Snippet_(programming)]snippets [HYPERLINK: https://en.wikipedia.org/wiki/Snippet_(programming)], [HYPERLINK: https://en.wikipedia.org/wiki/Snippet_(programming)]  [HYPERLINK: https://en.wikipedia.org/wiki/Code_refactoring]code refactoring, [HYPERLINK: https://en.wikipedia.org/wiki/Code_refactoring] and embedded  [HYPERLINK: https://en.wikipedia.org/wiki/Git]Git. [HYPERLINK: https://en.wikipedia.org/wiki/Git] Users can change the  [HYPERLINK: https://en.wikipedia.org/wiki/Theme_(computing)]theme [HYPERLINK: https://en.wikipedia.org/wiki/Theme_(computing)], [HYPERLINK: https://en.wikipedia.org/wiki/Theme_(computing)]  [HYPERLINK: https://en.wikipedia.org/wiki/Keyboard_shortcut]keyboard shortcuts, [HYPERLINK: https://en.wikipedia.org/wiki/Keyboard_shortcut] preferences, and install  [HYPERLINK: https://en.wikipedia.org/wiki/Plug-in_(computing)]extensions [HYPERLINK: https://en.wikipedia.org/wiki/Plug-in_(computing)]  [HYPERLINK: https://en.wikipedia.org/wiki/Plug-in_(computing)]that add functionality.[m[41m [m
[32m+[m[32m   In the  [HYPERLINK: https://en.wikipedia.org/wiki/Stack_Overflow]Stack Overflow [HYPERLINK: https://en.wikipedia.org/wiki/Stack_Overflow]  [HYPERLINK: https://en.wikipedia.org/wiki/Stack_Overflow]2023 Developer Survey, Visual Studio Code was ranked the most popular developer environment tool among 86,544 respondents, with 73.71% reporting that they use it. The survey also found Visual Studio Code to be used more by those learning to code than by professional developers (78% vs. 74%).[m[41m [m
[32m+[m[32m Python Language[m[41m [m
[32m+[m[32m   Python is a  [HYPERLINK: https://en.wikipedia.org/wiki/High-level_programming_language]high [HYPERLINK: https://en.wikipedia.org/wiki/High-level_programming_language]- [HYPERLINK: https://en.wikipedia.org/wiki/High-level_programming_language]level [HYPERLINK: https://en.wikipedia.org/wiki/High-level_programming_language], [HYPERLINK: https://en.wikipedia.org/wiki/High-level_programming_language]  [HYPERLINK: https://en.wikipedia.org/wiki/General-purpose_programming_language]general [HYPERLINK: https://en.wikipedia.org/wiki/General-purpose_programming_language]- [HYPERLINK: https://en.wikipedia.org/wiki/General-purpose_programming_language]purpose programming language. [HYPERLINK: https://en.wikipedia.org/wiki/General-purpose_programming_language] Its design philosophy emphasizes  [HYPERLINK: https://en.wikipedia.org/wiki/Code_readability]code readability [HYPERLINK: https://en.wikipedia.org/wiki/Code_readability]  [HYPERLINK: https://en.wikipedia.org/wiki/Code_readability]with the use of  [HYPERLINK: https://en.wikipedia.org/wiki/Off-side_rule]significant indentation [HYPERLINK: https://en.wikipedia.org/wiki/Off-side_rule]. [HYPERLINK: https://en.wikipedia.org/wiki/Off-side_rule][m[41m  [m
[32m+[m[32m   Python is  [HYPERLINK: https://en.wikipedia.org/wiki/Type_system]dynamically typed [HYPERLINK: https://en.wikipedia.org/wiki/Type_system]  [HYPERLINK: https://en.wikipedia.org/wiki/Type_system]and  [HYPERLINK: https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)]garbage [HYPERLINK: https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)]- [HYPERLINK: https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)]collected. [HYPERLINK: https://en.wikipedia.org/wiki/Garbage_collection_(computer_science)] It supports multiple  [HYPERLINK: https://en.wikipedia.org/wiki/Programming_paradigm]programming paradigms [HYPERLINK: https://en.wikipedia.org/wiki/Programming_paradigm], [HYPERLINK: https://en.wikipedia.org/wiki/Programming_paradigm] including  [HYPERLINK: https://en.wikipedia.org/wiki/Structured_programming]structured [HYPERLINK: https://en.wikipedia.org/wiki/Structured_programming]  [HYPERLINK: https://en.wikipedia.org/wiki/Structured_programming](particularly  [HYPERLINK: https://en.wikipedia.org/wiki/Procedural_programming]procedural [HYPERLINK: https://en.wikipedia.org/wiki/Procedural_programming]) [HYPERLINK: https://en.wikipedia.org/wiki/Procedural_programming],  [HYPERLINK: https://en.wikipedia.org/wiki/Object-oriented_programming]object [HYPERLINK: https://en.wikipedia.org/wiki/Object-oriented_programming]- [HYPERLINK: https://en.wikipedia.org/wiki/Object-oriented_programming]oriented [HYPERLINK: https://en.wikipedia.org/wiki/Object-oriented_programming]  [HYPERLINK: https://en.wikipedia.org/wiki/Object-oriented_programming]and  [HYPERLINK: https://en.wikipedia.org/wiki/Functional_programming]functional programming. [HYPERLINK: https://en.wikipedia.org/wiki/Functional_programming] It is often described as a "batteries included" language due to its comprehensive  [HYPERLINK: https://en.wikipedia.org/wiki/Standard_library]standard library [HYPERLINK: https://en.wikipedia.org/wiki/Standard_library]. [HYPERLINK: https://en.wikipedia.org/wiki/Standard_library][m[41m  [m
[32m+[m[32m   Guido van Rossum [HYPERLINK: https://en.wikipedia.org/wiki/Guido_van_Rossum]  [HYPERLINK: https://en.wikipedia.org/wiki/Guido_van_Rossum]began working on Python in the late 1980s as a successor to the  [HYPERLINK: https://en.wikipedia.org/wiki/ABC_(programming_language)]ABC  [HYPERLINK: https://en.wikipedia.org/wiki/ABC_(programming_language)]programming language [HYPERLINK: https://en.wikipedia.org/wiki/ABC_(programming_language)]  [HYPERLINK: https://en.wikipedia.org/wiki/ABC_(programming_language)]and first released it in 1991 as Python 0.9.0. Python 2.0 was released in 2000. Python 3.0, released in 2008, was a major revision not completely  [HYPERLINK: https://en.wikipedia.org/wiki/Backward_compatibility]backward [HYPERLINK: https://en.wikipedia.org/wiki/Backward_compatibility]compatible [HYPERLINK: https://en.wikipedia.org/wiki/Backward_compatibility]  [HYPERLINK: https://en.wikipedia.org/wiki/Backward_compatibility]with earlier versions. Python 2.7.18, released in 2020, was the last release of Python 2.[m[41m  [m
[32m+[m[32m   Python consistently ranks as one of the most popular programming languages, and has gained widespread use in the  [HYPERLINK: https://en.wikipedia.org/wiki/Machine_learning]machine learning [HYPERLINK: https://en.wikipedia.org/wiki/Machine_learning]  [HYPERLINK: https://en.wikipedia.org/wiki/Machine_learning]community.[m[41m [m
[32m+[m[32m   iii) Tkinter Library[m[41m [m
[32m+[m[32m   Tkinter is a  [HYPERLINK: https://en.wikipedia.org/wiki/Python_(programming_language)]Python [HYPERLINK: https://en.wikipedia.org/wiki/Python_(programming_language)]  [HYPERLINK: https://en.wikipedia.org/wiki/Language_binding]binding [HYPERLINK: https://en.wikipedia.org/wiki/Language_binding]  [HYPERLINK: https://en.wikipedia.org/wiki/Language_binding]to the  [HYPERLINK: https://en.wikipedia.org/wiki/Tk_(software)]Tk [HYPERLINK: https://en.wikipedia.org/wiki/Tk_(software)]  [HYPERLINK: https://en.wikipedia.org/wiki/Graphical_user_interface]GUI [HYPERLINK: https://en.wikipedia.org/wiki/Graphical_user_interface]  [HYPERLINK: https://en.wikipedia.org/wiki/Graphical_user_interface]toolkit. It is the standard Python interface to the Tk GUI toolkit, and is Python's  [HYPERLINK: https://en.wikipedia.org/wiki/De_facto_standard]de facto [HYPERLINK: https://en.wikipedia.org/wiki/De_facto_standard]  [HYPERLINK: https://en.wikipedia.org/wiki/De_facto_standard]standard [HYPERLINK: https://en.wikipedia.org/wiki/De_facto_standard]  [HYPERLINK: https://en.wikipedia.org/wiki/De_facto_standard]GUI. Tkinter is included with standard  [HYPERLINK: https://en.wikipedia.org/wiki/Linux]Linux [HYPERLINK: https://en.wikipedia.org/wiki/Linux], [HYPERLINK: https://en.wikipedia.org/wiki/Linux]  [HYPERLINK: https://en.wikipedia.org/wiki/Microsoft_Windows]Microsoft Windows [HYPERLINK: https://en.wikipedia.org/wiki/Microsoft_Windows]  [HYPERLINK: https://en.wikipedia.org/wiki/Microsoft_Windows]and  [HYPERLINK: https://en.wikipedia.org/wiki/MacOS]macOS [HYPERLINK: https://en.wikipedia.org/wiki/MacOS]  [HYPERLINK: https://en.wikipedia.org/wiki/MacOS]installs of Python.[m[41m [m
[32m+[m[32m   The name Tkinter comes from Tk interface. Tkinter was written by  [HYPERLINK: https://en.wikipedia.org/w/index.php?title=Steen_Lumholt&action=edit&redlink=1]Steen Lumholt [HYPERLINK: https://en.wikipedia.org/w/index.php?title=Steen_Lumholt&action=edit&redlink=1]  [HYPERLINK: https://en.wikipedia.org/w/index.php?title=Steen_Lumholt&action=edit&redlink=1]and  [HYPERLINK: https://en.wikipedia.org/wiki/Guido_van_Rossum]Guido van  [HYPERLINK: https://en.wikipedia.org/wiki/Guido_van_Rossum]Rossum [HYPERLINK: https://en.wikipedia.org/wiki/Guido_van_Rossum], [HYPERLINK: https://en.wikipedia.org/wiki/Guido_van_Rossum] then later revised by Fredrik Lundh. Tkinter is  [HYPERLINK: https://en.wikipedia.org/wiki/Free_software]free software [HYPERLINK: https://en.wikipedia.org/wiki/Free_software]  [HYPERLINK: https://en.wikipedia.org/wiki/Free_software]released under a  [HYPERLINK: https://en.wikipedia.org/wiki/Python_license]Python  [HYPERLINK: https://en.wikipedia.org/wiki/Python_license]license [HYPERLINK: https://en.wikipedia.org/wiki/Python_license]. [HYPERLINK: https://en.wikipedia.org/wiki/Python_license][m
[32m+[m[32m    iv) Random Module:[m[41m [m
[32m+[m[32m   To achieve the randomization of numbers we have also used the random module in this project.[m[41m [m
[32m+[m[32m   This module helps the programmers to generate random numbers both real and integer in python.[m
[32m+[m[32m6. Flow Chart:[m[41m  [m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m[32m  7.  Model Architecture:[m[41m  [m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m
[32m+[m[41m   [m
[32m+[m[41m  [m
[32m+[m[41m                                                                               [m
[32m+[m[41m [m
[32m+[m[41m                                                                               [m
[32m+[m[41m                                                                               [m
[32m+[m[41m                                                                               [m
[32m+[m[41m [m
[32m+[m[41m                                                                               [m
[32m+[m[41m                                                                               [m
[32m+[m[41m                                                                               [m
[32m+[m[41m [m
[32m+[m[41m [m
[32m+[m[41m [m
[32m+[m
[32m+[m[32m7.1. Dice Roll Window[m[41m [m
[32m+[m[32mPurpose:[m[41m  [m
[32m+[m[32mThis window is designed to provide the various buttons to the user. He can select one according to his taste. He has the option of selecting various dice.[m[41m [m
[32m+[m[32mComponents:[m[41m  [m
[32m+[m[32mThis window consists of six Buttons Widgets labelled with `One Dice', `Two Dice', `Three Dice', `Four Dice', `Five Dice' and `Six Dice'. Apart from the buttons, there is a text Widget which has used to give a message to the user that how many dice he wants to roll?[m[41m [m
[32m+[m[32mWorking:[m[41m [m
[32m+[m[32mWhen a user selects a button, there opens another window, which consists of a Button Widget to let the user roll the dice.[m[41m [m
[32m+[m[32m7.2 Dice Window[m[41m [m
[32m+[m[32m Purpose:[m[41m [m
[32m+[m[32m This Window has been designed to provide the user the experience of rolling dice. The User can roll the dice in this window.[m[41m  [m
[32m+[m[32mComponents:[m[41m  [m
[32m+[m[32mThis window consists of one of more dice images and a Button Widget. The button widget allows the user to roll the dice.[m[41m [m
[32m+[m[32mWorking:[m[41m [m
[32m+[m[32mWhen a user clicks on the Roll Dice Button, it rolls the dice by generating random numbers on the dice. The user can roll the dice any number of times.[m[41m  [m
[32m+[m[32m8. Source Code:[m
[32m+[m[41m [m
[32m+[m[32mimport tkinter as tkD[m
[32m+[m[32mfrom PIL import Image, ImageTk[m
[32m+[m[32mimport random[m
[32m+[m[32m# from diceProject.dice import Dice[m
[32m+[m[32m#---------------------------------------------------------------------------------------------------------------------[m
[32m+[m[32m#that class is for one (1) Dice[m
[32m+[m
[32m+[m[32mclass one_dice:[m
[32m+[m[32m    def one(self):[m
[32m+[m[32m        windows = tk.Toplevel()[m
[32m+[m[32m        windows.geometry("500x360")[m
[32m+[m[32m        windows.title("Dice Roll")[m
[32m+[m
[32m+[m[41m        [m
[32m+[m[32m        dice = ['dice1.jpg','dice2.jpg','dice3.jpg','dice4.jpg','dice5.jpg','dice6.jpg',][m
[32m+[m[32m        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m
[32m+[m[32m        label1 = tk.Label(windows, image= image1)[m
[32m+[m
[32m+[m[32m        label1.image = image1[m
[32m+[m
[32m+[m[32m        label1.place(x=30, y=50)[m
[32m+[m
[32m+[m[41m        [m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m           image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m           label1.configure(image=image1)[m
[32m+[m[32m           label1.image = image1[m
[32m+[m
[32m+[m[32m        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button.place(x=250, y=10)[m
[32m+[m[32m        windows.mainloop()[m
[32m+[m[41m    [m
[32m+[m
[32m+[m[32m#----------------------------------------------------------------------------------------------------------------------[m
[32m+[m[32m#that class is for two dice[m
[32m+[m
[32m+[m[32mclass twoDice:[m
[32m+[m[32m    def two(self):[m
[32m+[m[32m        windows = tk.Toplevel()[m
[32m+[m[32m        windows.geometry("500x360")[m
[32m+[m[32m        windows.title("Dice Roll")[m
[32m+[m
[32m+[m[32m        dice = ['dice1.jpg','dice2.jpg','dice3.jpg','dice4.jpg','dice5.jpg','dice6.jpg',][m
[32m+[m[32m        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m
[32m+[m[32m        label1 = tk.Label(windows, image= image1)[m
[32m+[m[32m        label2 = tk.Label(windows, image=image2)[m
[32m+[m
[32m+[m[32m        label1.image = image1[m
[32m+[m[32m        label2.image = image2[m
[32m+[m
[32m+[m[32m        label1.place(x=60, y=100)[m
[32m+[m[32m        label2.place(x=300,y=100)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label1.configure(image=image1)[m
[32m+[m[32m            label1.image = image1[m
[32m+[m[41m    [m
[32m+[m[32m            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label2.configure(image=image2)[m
[32m+[m[32m            label2.image = image2[m
[32m+[m[41m    [m
[32m+[m[32m        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button.place(x=250, y=10)[m
[32m+[m[32m        windows.mainloop()[m
[32m+[m
[32m+[m[32m#-----------------------------------------------------------------------------------------------------------------------[m
[32m+[m[32m#that class is for three dice[m
[32m+[m
[32m+[m[32mclass ThreeDice:[m
[32m+[m[32m    def three(self):[m
[32m+[m[32m        windows = tk.Toplevel()[m
[32m+[m[32m        windows.geometry("500x360")[m
[32m+[m[32m        windows.title("Dice Roll")[m
[32m+[m
[32m+[m[32m        dice = ['dice1.jpg','dice2.jpg','dice3.jpg','dice4.jpg','dice5.jpg','dice6.jpg',][m
[32m+[m[32m        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m
[32m+[m[32m        label1 = tk.Label(windows, image= image1)[m
[32m+[m[32m        label2 = tk.Label(windows, image=image2)[m
[32m+[m[32m        label3 = tk.Label(windows, image=image3)[m
[32m+[m
[32m+[m[32m        label1.image = image1[m
[32m+[m[32m        label2.image = image2[m
[32m+[m[32m        label3.image = image3[m
[32m+[m
[32m+[m[32m        label1.place(x=30, y=50)[m
[32m+[m[32m        label2.place(x=180,y=50)[m
[32m+[m[32m        label3.place(x = 330, y = 50)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label1.configure(image=image1)[m
[32m+[m[32m            label1.image = image1[m
[32m+[m[41m    [m
[32m+[m[32m            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label2.configure(image=image2)[m
[32m+[m[32m            label2.image = image2[m
[32m+[m[41m    [m
[32m+[m[32m            image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label3.configure(image=image3)[m
[32m+[m[32m            label3.image = image3[m
[32m+[m[41m    [m
[32m+[m[32m        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button.place(x=250, y=10)[m
[32m+[m[32m        windows.mainloop()[m
[32m+[m
[32m+[m[32m#-----------------------------------------------------------------------------------------------------------------------[m
[32m+[m[32m#This class is for four dice[m
[32m+[m
[32m+[m[32mclass fourDice:[m
[32m+[m[32m    def four(self):[m
[32m+[m[32m        windows = tk.Toplevel()[m
[32m+[m[32m        windows.geometry("500x360")[m
[32m+[m[32m        windows.title("Dice Roll")[m
[32m+[m
[32m+[m[32m        dice = ['dice1.jpg','dice2.jpg','dice3.jpg','dice4.jpg','dice5.jpg','dice6.jpg',][m
[32m+[m[32m        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m
[32m+[m[32m        label1 = tk.Label(windows, image= image1)[m
[32m+[m[32m        label2 = tk.Label(windows, image=image2)[m
[32m+[m[32m        label3 = tk.Label(windows, image=image3)[m
[32m+[m[32m        label4 = tk.Label(windows, image=image4)[m
[32m+[m
[32m+[m[32m        label1.image = image1[m
[32m+[m[32m        label2.image = image2[m
[32m+[m[32m        label3.image = image3[m
[32m+[m[32m        label4.image = image4[m
[32m+[m
[32m+[m[32m        label1.place(x=30, y=50)[m
[32m+[m[32m        label2.place(x=180,y=50)[m
[32m+[m[32m        label3.place(x = 330, y = 50)[m
[32m+[m[32m        label4.place(x =30, y = 200)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label1.configure(image=image1)[m
[32m+[m[32m            label1.image = image1[m
[32m+[m[41m    [m
[32m+[m[32m            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label2.configure(image=image2)[m
[32m+[m[32m            label2.image = image2[m
[32m+[m[41m    [m
[32m+[m[32m            image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label3.configure(image=image3)[m
[32m+[m[32m            label3.image = image3[m
[32m+[m[41m    [m
[32m+[m[32m            image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label4.configure(image=image4)[m
[32m+[m[32m            label4.image = image4[m
[32m+[m[41m    [m
[32m+[m[32m        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button.place(x=250, y=10)[m
[32m+[m[32m        windows.mainloop()[m
[32m+[m
[32m+[m[32m#-----------------------------------------------------------------------------------------------------------------------[m
[32m+[m[32m#This class is for five dice[m
[32m+[m
[32m+[m[32mclass fiveDice:[m
[32m+[m[32m    def five(self):[m
[32m+[m[32m        windows = tk.Toplevel()[m
[32m+[m[32m        windows.geometry("500x360")[m
[32m+[m[32m        windows.title("Dice Roll")[m
[32m+[m
[32m+[m[32m        dice = ['dice1.jpg','dice2.jpg','dice3.jpg','dice4.jpg','dice5.jpg','dice6.jpg',][m
[32m+[m[32m        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image5 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m
[32m+[m[32m        label1 = tk.Label(windows, image= image1)[m
[32m+[m[32m        label2 = tk.Label(windows, image=image2)[m
[32m+[m[32m        label3 = tk.Label(windows, image=image3)[m
[32m+[m[32m        label4 = tk.Label(windows, image=image4)[m
[32m+[m[32m        label5 = tk.Label(windows, image=image5)[m
[32m+[m
[32m+[m[32m        label1.image = image1[m
[32m+[m[32m        label2.image = image2[m
[32m+[m[32m        label3.image = image3[m
[32m+[m[32m        label4.image = image4[m
[32m+[m[32m        label5.image = image5[m
[32m+[m
[32m+[m[32m        label1.place(x=30, y=50)[m
[32m+[m[32m        label2.place(x=180,y=50)[m
[32m+[m[32m        label3.place(x = 330, y = 50)[m
[32m+[m[32m        label4.place(x =30, y = 200)[m
[32m+[m[32m        label5.place(x = 180, y = 200)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label1.configure(image=image1)[m
[32m+[m[32m            label1.image = image1[m
[32m+[m[41m    [m
[32m+[m[32m            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label2.configure(image=image2)[m
[32m+[m[32m            label2.image = image2[m
[32m+[m[41m    [m
[32m+[m[32m            image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label3.configure(image=image3)[m
[32m+[m[32m            label3.image = image3[m
[32m+[m[41m    [m
[32m+[m[32m            image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label4.configure(image=image4)[m
[32m+[m[32m            label4.image = image4[m
[32m+[m[41m    [m
[32m+[m[32m            image5 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label5.configure(image = image5)[m
[32m+[m[32m            label5.image = image5[m
[32m+[m[41m    [m
[32m+[m[32m        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button.place(x=250, y=10)[m
[32m+[m[32m        windows.mainloop()[m
[32m+[m
[32m+[m[32m#-------------------------------------------------------------------------------------------------------------------------[m
[32m+[m[32m#This class is for six dice[m
[32m+[m
[32m+[m[32mclass sixDice:[m
[32m+[m[32m    def six(self):[m
[32m+[m[32m        windows = tk.Toplevel()[m
[32m+[m[32m        windows.geometry("500x360")[m
[32m+[m[32m        windows.title("Dice Roll")[m
[32m+[m
[32m+[m[32m        dice = ['dice1.jpg','dice2.jpg','dice3.jpg','dice4.jpg','dice5.jpg','dice6.jpg'][m
[32m+[m[32m        image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image5 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m        image6 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m
[32m+[m[32m        label1 = tk.Label(windows, image= image1)[m
[32m+[m[32m        label2 = tk.Label(windows, image=image2)[m
[32m+[m[32m        label3 = tk.Label(windows, image=image3)[m
[32m+[m[32m        label4 = tk.Label(windows, image=image4)[m
[32m+[m[32m        label5 = tk.Label(windows, image=image5)[m
[32m+[m[32m        label6 = tk.Label(windows, image=image6)[m
[32m+[m
[32m+[m[32m        label1.image = image1[m
[32m+[m[32m        label2.image = image2[m
[32m+[m[32m        label3.image = image3[m
[32m+[m[32m        label4.image = image4[m
[32m+[m[32m        label5.image = image5[m
[32m+[m[32m        label6.image = image6[m
[32m+[m
[32m+[m[32m        label1.place(x=30, y=50)[m
[32m+[m[32m        label2.place(x=180,y=50)[m
[32m+[m[32m        label3.place(x = 330, y = 50)[m
[32m+[m[32m        label4.place(x =30, y = 200)[m
[32m+[m[32m        label5.place(x = 180, y = 200)[m
[32m+[m[32m        label6.place(x = 330, y=200)[m
[32m+[m
[32m+[m[32m        def roll_dice():[m
[32m+[m[32m            image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label1.configure(image=image1)[m
[32m+[m[32m            label1.image = image1[m
[32m+[m[41m    [m
[32m+[m[32m            image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label2.configure(image=image2)[m
[32m+[m[32m            label2.image = image2[m
[32m+[m[41m    [m
[32m+[m[32m            image3 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label3.configure(image=image3)[m
[32m+[m[32m            label3.image = image3[m
[32m+[m[41m    [m
[32m+[m[32m            image4 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label4.configure(image=image4)[m
[32m+[m[32m            label4.image = image4[m
[32m+[m[41m    [m
[32m+[m[32m            image5 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label5.configure(image = image5)[m
[32m+[m[32m            label5.image = image5[m
[32m+[m[41m    [m
[32m+[m[32m            image6 = ImageTk.PhotoImage(Image.open(random.choice(dice)))[m
[32m+[m[32m            label6.configure(image=image6)[m
[32m+[m[32m            label6.image = image6[m
[32m+[m[41m    [m
[32m+[m[32m        button = tk.Button(windows, bg='black', fg= 'white', font='Times 10 bold', text='Roll Dice', command= roll_dice)[m
[32m+[m[32m        button.place(x=250, y=10)[m
[32m+[m[32m        windows.mainloop()[m
[32m+[m
[32m+[m[32m#_------------------------------------------------------------------------------------------------------------------------[m
[32m+[m
[32m+[m
[32m+[m[32mone = one_dice()[m
[32m+[m[32mtwo = twoDice()[m
[32m+[m[32mthree = ThreeDice()[m
[32m+[m[32mfour = fourDice()[m
[32m+[m[32mfive = fiveDice()[m
[32m+[m[32msix = sixDice()[m
[32m+[m
[32m+[m
[32m+[m[32mwindows = tk.Tk()[m
[32m+[m[32mwindows.geometry("500x360")[m
[32m+[m[32mwindows.title("Dice Roll")[m
[32m+[m
[32m+[m[32mlabel1 = tk.Label(windows, text="How many dice you want to Roll")[m
[32m+[m[32mlabel1.place(x = 180, y = 10)[m
[32m+[m
[32m+[m[32m# button = tk.Button(windows, text="One Dice", command=)[m
[32m+[m[32mbutton1 = tk.Button(windows, text='One Dice',command=one.one)[m
[32m+[m[32mbutton2 = tk.Button(windows, text='Two Dice', command= two.two )[m
[32m+[m[32mbutton3 = tk.Button(windows, text='Three Dice', command=three.three)[m
[32m+[m[32mbutton4 = tk.Button(windows, text='Four Dice', command=four.four)[m
[32m+[m[32mbutton5 = tk.Button(windows, text='Five Dice', command=five.five)[m
[32m+[m[32mbutton6 = tk.Button(windows, text='Six Dice', command=six.six)[m
[32m+[m
[32m+[m[32mbutton1.place(x = 230, y = 50)[m
[32m+[m[32mbutton2.place(x = 230, y = 100)[m
[32m+[m[32mbutton3.place(x = 230, y = 150)[m
[32m+[m[32mbutton4.place(x = 230, y = 200)[m
[32m+[m[32mbutton5.place(x = 230, y = 250)[m
[32m+[m[32mbutton6.place(x = 230, y = 300)[m
[32m+[m[32mwindows.mainloop()[m
[32m+[m
[32m+[m[41m [m
[32m+[m[32m  9. Validation and Verification:[m[41m  [m
[32m+[m
[32m+[m[32m   The verification and validation of any system is as necessary as food for human living things. Validation process includes that it meets as the[m[41m  [m
[32m+[m[41m    [m
[32m+[m[32m   Validation and verification are two critical processes in ensuring the reliability, functionality, and effectiveness of a system. These processes are often used interchangeably, but they refer to different aspects of system evaluation.[m[41m [m
[32m+[m[41m    [m
[32m+[m[32m   Verification is the process of evaluating a system or component during or after the development phase to determine whether it meets the specified requirements. We have verified the software by testing its different aspects. Each time it is rolled it generates new numbers within the specified range.[m[41m [m
[32m+[m[41m    [m
[32m+[m[32m   Whereas, validation is the process of evaluating a system or component during or after the development phase to determine whether it satisfies the intended use and meets the user requirements. This system does as we intended. It provides an entertaining game with error free.[m[41m [m
[32m+[m[41m    [m
[32m+[m[32m  10. Result[m[41m  [m
[32m+[m
[32m+[m[32m   The Dice Rolling game makes a good impression on our test users. Where they loved to play with that game. Its user friendly interface makes them to attract on the software. It's different choice of dice makes them to use the game more efficiently and it also makes a good impact on the user to make them stress free.[m[41m [m
[32m+[m[41m [m
[32m+[m[32m  11. Conclusion[m[41m  [m
[32m+[m
[32m+[m[32m   In conclusion, we have designed and implemented Dice Rolling Simulator with state to provide a verifiable, decentralized, game plateform. Now anyone can simply click on a button and get his next number on dice. It is our hope that this game will help people to get entertained. The culmination of this project brings forth a platform that not only entertains but also educates, providing users with a unique and immersive experience in the realm of probability and randomness.[m[41m [m
[32m+[m[41m    [m
[32m+[m[41m    [m
[32m+[m[41m    [m
[32m+[m[41m    [m
[32m+[m
[32m+[m[32m12. References:[m
[32m+[m
[32m+[m[32m https:/ [HYPERLINK: https://docs.python.org/3/library/tkinter.html]/docs.python.org/3/library/tkinter.html [HYPERLINK: https://docs.python.org/3/library/tkinter.html]  [HYPERLINK: https://docs.python.org/3/library/tkinter.html][m[41m [m
[32m+[m[32m https:/ [HYPERLINK: https://www.youtube.com/watch?v=CIm5vfsfgO0&ab_channel=WsCubeTech]/www.youtube.com/watch?v=CIm5vfsfgO0&ab_channel=WsCubeTech [HYPERLINK: https://www.youtube.com/watch?v=CIm5vfsfgO0&ab_channel=WsCubeTech]  [HYPERLINK: https://www.youtube.com/watch?v=CIm5vfsfgO0&ab_channel=WsCubeTech]:: 	https://www.wikipedia.org[m[41m [m
[32m+[m
[32m+[m[41m      [m
[32m+[m[32m                                                                          Page[m[41m [m
[1mdiff --git a/slides and documentation/Dice Rolling Simulation.pptx b/slides and documentation/Dice Rolling Simulation.pptx[m
[1mnew file mode 100644[m
[1mindex 0000000..fb1515a[m
Binary files /dev/null and b/slides and documentation/Dice Rolling Simulation.pptx differ
