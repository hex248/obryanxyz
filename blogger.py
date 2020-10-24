import os
import time
import tkinter as tk
from tkinter import ttk

start = time.perf_counter()

root = tk.Tk()
root.geometry("1280x720")
root.title("blogger")

class Scrollable(tk.Frame):
    """
       Make a frame scrollable with scrollbar on the right.
       After adding or removing widgets to the scrollable frame, 
       call the update() method to refresh the scrollable area.
    """

    def __init__(self, frame, width=16):

        self.frame = frame

        scrollbar = tk.Scrollbar(frame, width=16)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

        self.canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set, width = 1280, height = 600)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.canvas.yview)

        self.canvas.bind('<Configure>', self.__fill_canvas)

        # base class initialization
        tk.Frame.__init__(self, frame, height = 350)

        # assign this obj (the inner frame) to the windows item of the canvas
        self.windows_item = self.canvas.create_window(0,0, window=self, anchor=tk.NW)

        # Title Label
        # self.titleLabel = tk.Label(frame, font = ("Arial", 15), text = "Title:").grid(row = 0, padx = 2, pady = 2)
        # # self.titleLabel.place(relx = 0.02, y = 6, anchor = "nw")

        # # Title Entry
        # self.titleEntry = tk.Entry(frame, font = ("Arial", 15)).grid(row = 1, padx = 2, pady = 2)
        # # self.titleEntry.place(relx = 0.02, y = 39, relwidth = 0.7, anchor = "nw")

        # # Section list
        # self.sections = []
        # # Heading 1 Label
        # self.headingLabel = tk.Label(frame, font = ("Arial", 15), text = "Heading:").grid(row = 2, padx = 2, pady = 2)
        # # self.headingLabel.place(relx = 0.02, y = 90, anchor = "nw")

        # # Heading 1 Entry
        # self.headingEntry = tk.Entry(frame, font = ("Arial", 15)).grid(row = 3, padx = 2, pady = 2)
        # # self.headingEntry.place(relx = 0.02, y = 123, relwidth = 0.7, anchor = "nw")

        # # Body 1 Label
        # self.bodyLabel = tk.Label(frame, font = ("Arial", 15), text = "Body:").grid(row = 4, padx = 2, pady = 2)
        # # self.bodyLabel.place(relx = 0.02, y = 174, anchor = "nw")

        # # Body 1 Entry
        # self.bodyEntry = tk.Text(frame, font = ("Arial", 15)).grid(row = 5, padx = 2, pady = 2)
        # # self.bodyEntry.place(relx = 0.02, y = 207, relwidth = 0.7, relheight = 0.6, anchor = "nw")

        # # First section
        # self.sections.append([self.headingEntry, self.bodyEntry, 207])


    def __fill_canvas(self, event):

        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)        

    def update(self):

        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))


body = ttk.Frame(root)
body.pack()
scrollable_body = Scrollable(body, width = 500)

titleLabel = tk.Label(scrollable_body, font = ("Arial", 15), text = "Title:")
titleLabel.grid(row = 0, padx = 2, pady = 2, sticky = "w")
# self.titleLabel.place(relx = 0.02, y = 6, anchor = "nw")

# Title Entry
titleEntry = tk.Entry(scrollable_body, font=("Arial", 30), width = 56)
titleEntry.grid(row=1, padx=2, pady=2, sticky = "w")
# self.titleEntry.place(relx = 0.02, y = 39, relwidth = 0.7, anchor = "nw")

# Section list
sections = []
# Heading 1 Label
headingLabel = tk.Label(scrollable_body, font=("Arial", 15), text="Heading:")
headingLabel.grid(row=2, padx=2, pady=2, sticky = "w")
# self.headingLabel.place(relx = 0.02, y = 90, anchor = "nw")

# Heading 1 Entry
headingEntry = tk.Entry(scrollable_body, font=("Arial", 15), width = 112)
headingEntry.grid(row=3, padx=2, pady=2, sticky = "w")
# self.headingEntry.place(relx = 0.02, y = 123, relwidth = 0.7, anchor = "nw")

# Body 1 Label
bodyLabel = tk.Label(scrollable_body, font=("Arial", 15), text="Body:")
bodyLabel.grid(row=4, padx=2, pady=2, sticky = "w")
# self.bodyLabel.place(relx = 0.02, y = 174, anchor = "nw")

# Body 1 Entry
bodyEntry = tk.Text(scrollable_body, font=("Arial", 15), width = 112)
bodyEntry.grid(row=5, padx=2, pady=2, sticky = "w")
# self.bodyEntry.place(relx = 0.02, y = 207, relwidth = 0.7, relheight = 0.6, anchor = "nw")

# First section
sections.append([headingEntry, bodyEntry, 5])

scrollable_body.update()

# Submit Button
submitButton = tk.Button(root, font = ("Arial", 15), text = "Submit", bg = "#b31515", relief = "flat", command = lambda: submit())
submitButton.place(relx = 0.02, rely = 0.85, relwidth = 0.46, relheight = 0.11, anchor = "nw")
# Add Section Button
addSectionButton = tk.Button(root, font = ("Arial", 15), text = "Add Section", bg = "#1569b3", relief = "flat", command = lambda: addSection(scrollable_body))
addSectionButton.place(relx = 0.5, rely = 0.85, relwidth = 0.46, relheight = 0.11, anchor = "nw")


def submit():
    beforeBlog = """
<!DOCTYPE html>
<html>
<head>
    <title>obryan.xyz</title>
    <link rel="stylesheet" href="../blogstyle.css">
</head>
</html>

<body>
    <section id="container">
        <a id="home-link" href="/home.html">
            <h1 id="title-box" href="/home.html" target = "_self" title="Go home">obryan.xyz</h1>
        </a>
        <br>
        <section class="blog">
            <header>"""

    afterBlog = """
                </div>
                <br>
                <br>
                    
            </header>
        </section>
    </section>
</body>"""

    title = titleEntry.get().strip()
    # print("Title:", title, "\n\n")

    blogTitleHTML = f"""
                <div id="blog-title-box">
                    <a id="blog-title">{title}</a>
                </div>

                <div id="blog-content">"""

    beforeBlog = beforeBlog + blogTitleHTML

    for section in sections:
        heading = section[0].get().strip()
        body = section[1].get("1.0", tk.END).strip()

        blog = f"""
                    <header id="blog-heading">{heading}</header>
                    <a id="blog-body">
                        <p>{body}</p>
                    </a>
                    <br>
                    <br>
        """
        beforeBlog = beforeBlog + blog
        # print("Heading:", heading)
        # print("Body:", body)
    blog = beforeBlog + afterBlog

    unaccepted = ["#","%","&","{","}",r'"\"',"<",">","*","?","/","$","!","'",r'"""',":","@","+","`","|","="] # A list of unnacceptable characters in a file name
    titleSanitised = title
    # for char in titleSanitised:
    #     if char in unaccepted:
    #         titleSanitised.replace(char, "")
    unacceptedStr = r'#%&{}\<>*?/$!"'"' + r'"""' r'':@+`|='
    #titleSanitised = titleSanitised.translate(None, unacceptedStr)
    titleSanitised = titleSanitised.replace(" ", "_")
    print(f"Normal Title: {title}")
    print(f"Sanitised Title: {titleSanitised}")
    
    f = open(f"blog/{titleSanitised}.html", "w")
    f.write(blog)
    print(f"Created a file at blog/{titleSanitised}.html")

    f = open("blog.html", "r")
    fHTML = f.read()

    fHTML = fHTML.split("                    </h2>")
    print(fHTML)

    blogLinkHTML = f"""
                        <a id="blog-link" href="blog/{titleSanitised}.html">{title}</a>"""
    fHTML = fHTML[0] + blogLinkHTML + "\n                    </h2>" + fHTML[1] # Sandwiches the new link inbetween the other halves of the html document

    f = open("blog.html", "w")
    f.write(fHTML)

    return

def addSection(scrollable_body):
    recentRow = sections[len(sections) - 1][2]

    # Heading 1 Label
    headingLabel = tk.Label(scrollable_body, font = ("Arial", 15), text = "Heading:")
    headingLabel.grid(row = recentRow + 1, padx=2, pady=2, sticky = "w")
    # headingLabel.place(relx = 0.02, y = y, anchor = "nw")
    # Heading 1 Entry
    headingEntry = tk.Entry(scrollable_body, font = ("Arial", 15), width = 112)
    headingEntry.grid(row = recentRow + 2, padx=2, pady=2, sticky = "w")
    # headingEntry.place(relx = 0.02, y = y + 33, relwidth = 0.7, anchor = "nw")
    # Body 1 Label
    bodyLabel = tk.Label(scrollable_body, font = ("Arial", 15), text = "Body:")
    bodyLabel.grid(row = recentRow + 3, padx=2, pady=2, sticky = "w")
    # bodyLabel.place(relx = 0.02, y = y + 84, anchor = "nw")
    # Body 1 Entry
    bodyEntry = tk.Text(scrollable_body, font = ("Arial", 15), width = 112)
    bodyEntry.grid(row = recentRow + 4, padx=2, pady=2, sticky = "w")
    # bodyEntry.place(relx = 0.02, y = y + 117, relwidth = 0.7, relheight = 0.6, anchor = "nw")
    recentRow = recentRow + 5
    # First section
    sections.append([headingEntry, bodyEntry, recentRow])
    scrollable_body.update()
    return

finish = time.perf_counter()

print(f"Exited in {round(finish-start, 2)} second(s)\n") # Prints the time taken to run

root.mainloop()
