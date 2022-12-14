import serial
import time
import tkinter
# Ce programme est une interface graphique pour le board dumbvalve pour PI3

# Définition du bouton quit
def quit():
    global tkTop
    ser.write(bytes('M', 'UTF-8'))
    tkTop.destroy()
# Définition du bouton Main On
def set_button1_state():
        varLabel.set("Main ON ")
        ser.write(bytes('Q', 'UTF-8'))
    
# Définition du bouton Main OFF
def set_button2_state():
        varLabel.set("Main OFF")
        ser.write(bytes('W', 'UTF-8'))
# Définition du bouton Bleed ON
def set_button3_state():
        varLabel.set("Bleed ON")
        ser.write(bytes('E', 'UTF-8'))
# Définition du bouton Bleed OFF
def set_button4_state():
    varLabel.set("Bleed OFF")
    ser.write(bytes('R', 'UTF-8'))
# Définition du bouton Supply ON
def set_button5_state():
    varLabel.set("Supply ON")
    ser.write(bytes('T', 'UTF-8'))
# Définition du bouton Supply OFF
def set_button6_state():
    varLabel.set("Supply OFF")
    ser.write(bytes('Y', 'UTF-8'))
# Définition du bouton Tirggers1 ON
def set_button7_state():
    varLabel.set("Triggers1 ON")
    ser.write(bytes('U', 'UTF-8'))
# Définition du bouton Triggers1 OFF
def set_button8_state():
    varLabel.set("Triggers1 OFF")
    ser.write(bytes('I', 'UTF-8'))
# Définition du bouton Triggers2 ON
def set_button9_state():
    varLabel.set("Triggers2 ON")
    ser.write(bytes('A', 'UTF-8'))
# Définition du bouton Triggers2 OFF
def set_button10_state():
    varLabel.set("Triggers2 OFF")
    ser.write(bytes('S', 'UTF-8'))
# Définition du bouton Shunt ON
def set_button11_state():
    varLabel.set("Shunt ON")
    ser.write(bytes('D', 'UTF-8'))
# Définition du bouton Shunt OFF
def set_button12_state():
    varLabel.set("Shunt OFF")
    ser.write(bytes('F', 'UTF-8'))
# Définition du bouton 1s délais
def set_button13_state():
    varLabel.set("1s delais")
    ser.write(bytes('Z', 'UTF-8'))
# Définition du bouton 2s délais
def set_button14_state():
    varLabel.set("2s delais")
    ser.write(bytes('X', 'UTF-8'))
# Définition du bouton 3s délais
def set_button15_state():
    varLabel.set("3s delais")
    ser.write(bytes('C', 'UTF-8'))
# Définition du bouton ALL OFF qui éteint tout
def set_button16_state():
    varLabel.set("ALL OFF")
    ser.write(bytes('M', 'UTF-8'))
# Définition du port COM utilisé et baudrate
ser = serial.Serial('COM5', 9600)
# Affiche DumbValve ON sur le terminal
print("DumbValve ON")
time.sleep(3)
# Envoi un message d'éteindre (low) les GPIO
ser.write(bytes('M', 'UTF-8')
)
#Initialisation de la page pour l'interface 
tkTop = tkinter.Tk()
tkTop.geometry('1700x1400')
tkTop.title("DumbValve")
label3 = tkinter.Label(text = 'DumbValve system',font=("Courier", 12,'bold')).pack()

varLabel = tkinter.IntVar()
tkLabel = tkinter.Label(textvariable=varLabel, )
tkLabel.pack()
# Définition des boutons sur l'interface
button1 = tkinter.IntVar()
button1state = tkinter.Button(tkTop,
    text="Main ON",
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button1state.pack(side='left', ipadx=10, padx=10, pady=15)

button2 = tkinter.IntVar()
button2state = tkinter.Button(tkTop,
    text=" MAIN OFF",
    command=set_button2_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5
)
button2state.pack(side='left', ipadx=10, padx=10, pady=15)

button3 = tkinter.IntVar()
button3state = tkinter.Button(tkTop,
    text="Bleed ON",
    command=set_button3_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button3state.pack(side='left', ipadx=10, padx=10, pady=15)

button4 = tkinter.IntVar()
button4state = tkinter.Button(tkTop,
    text=" Bleed OFF",
    command=set_button4_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5
)
button4state.pack(side='left', ipadx=10, padx=10, pady=15)

button5 = tkinter.IntVar()
button5state = tkinter.Button(tkTop,
    text="Supply ON",
    command=set_button5_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button5state.pack(side='left', ipadx=10, padx=10, pady=15)

button6 = tkinter.IntVar()
button6state = tkinter.Button(tkTop,
    text=" Supply OFF",
    command=set_button6_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5
)
button6state.pack(side='left', ipadx=10, padx=10, pady=15)

button7 = tkinter.IntVar()
button7state = tkinter.Button(tkTop,
    text="Triggers1 ON",
    command=set_button7_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button7state.pack(side='right', ipadx=20, padx=20, pady=20)

button8 = tkinter.IntVar()
button8state = tkinter.Button(tkTop,
    text=" Triggers1 OFF",
    command=set_button8_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5
)
button8state.pack(side='right', ipadx=20, padx=20, pady=20)

button9 = tkinter.IntVar()
button9state = tkinter.Button(tkTop,
    text="Triggers2 ON",
    command=set_button9_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button9state.pack(side='right', ipadx=20, padx=20, pady=20)

button10 = tkinter.IntVar()
button10state = tkinter.Button(tkTop,
    text=" Triggers2 OFF",
    command=set_button10_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5
)
button10state.pack(side='right', ipadx=20, padx=20, pady=20)

button11 = tkinter.IntVar()
button11state = tkinter.Button(tkTop,
    text="Shunt ON",
    command=set_button11_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button11state.pack(side='right', ipadx=20, padx=20, pady=20)

button12 = tkinter.IntVar()
button12state = tkinter.Button(tkTop,
    text=" Shunt OFF",
    command=set_button12_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5
)
button12state.pack(side='right', ipadx=20, padx=20, pady=20)

button13 = tkinter.IntVar()
button13state = tkinter.Button(tkTop,
    text="1s délai",
    command=set_button13_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button13state.pack(side='bottom', ipadx=20, padx=20, pady=20)

button14 = tkinter.IntVar()
button14state = tkinter.Button(tkTop,
    text="2 sec délai ",
    command=set_button14_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button14state.pack(side='bottom', ipadx=20, padx=20, pady=20)

button15 = tkinter.IntVar()
button15state = tkinter.Button(tkTop,
    text="3 sec délai ",
    command=set_button15_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button15state.pack(side='bottom', ipadx=20, padx=20, pady=20)

button16 = tkinter.IntVar()
button16state = tkinter.Button(tkTop,
    text="ALL OFF ",
    command=set_button16_state,
    height = 4,
    fg = "black",
    width = 8,
    bg = 'red',
    bd = 5,
    
)
button16state.pack(side='bottom', ipadx=20, padx=20, pady=20)
tkButtonQuit = tkinter.Button(
    tkTop,
    text="Quit",
    command=quit,
    height = 4,
    fg = "black",
    width = 8,
    bg = 'yellow',
    bd = 5
)
tkButtonQuit.pack(side='bottom', ipadx=10, padx=10, pady=15)

tkinter.mainloop()