from tkinter import *


def main():  # enter main
    def goto(num):
        root.destroy()  # destroy main win
        if num == 1:
            one()  # enter win 1
        elif num == 2:
            two()  # enter win 2

    root = Tk()
    root.title('Main')
    butmain1 = Button(root, text="Go into win 1", command=lambda: goto(1))
    # enter win 1
    butmain1.pack(pady=5)
    butmain2 = Button(root, text="Go into win 2", command=lambda: goto(2))
    # enter win 2
    butmain2.pack(pady=5)

    root.mainloop()


def one():
    def gotomain():
        root1.destroy()  # close win 1
        main()  # enter main

    root1 = Tk()
    root1.geometry('300x150+888+444')
    root1.title('win 1')
    Label(root1, text='This is win 1.', bg='lightgreen').pack(fill=X)
    butone1 = Button(root1, text="Back to main", command=gotomain)
    butone1.pack(pady=10)
    root1.mainloop()


def two():
    def gotomain():
        root2.destroy()  # close win 2
        main()  # enter main

    root2 = Tk()
    root2.geometry('300x150+888+444')
    root2.title('win 2')
    Label(root2, text='This is win 2.', bg='lightblue').pack(fill=X)
    buttwo1 = Button(root2, text="Back to main", command=gotomain)
    buttwo1.pack(pady=10)
    root2.mainloop()


if __name__ == '__main__':
    main()
