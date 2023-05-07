import os
from tkinter import filedialog
import customtkinter as ctk
from customtkinter import *
from os import listdir
audioDir="Audios"
imageDir="Images"
videoDir="Videos"
documentDir="Documents"
dirs=[audioDir,imageDir,videoDir,documentDir]
fileExtensions={
    ".mp3":"audio",
    ".wav":"audio",
    ".ogg":"audio",
    ".m4a":"audio",
    ".flac":"audio",
    ".wma":"audio",
    ".jpg":"image",
    ".jpeg":"image",
    ".png":"image",
    ".tiff":"image",
    ".tif":"image",
    ".gif":"image",
    ".bmp":"image",
    ".mp4":"video",
    ".mov":"video",
    ".avi":"video",
    ".wmv":"video",
    ".m4v":"video",
    ".flv":"video",
    ".3gp":"video",
    ".pptx":"document",
    ".docx":"document",
    ".pdf":"document",
    ".doc":"document",
    ".rtf":"document",
    ".txt":"document"
}

class App(CTk):
    ctk.set_appearance_mode("dark")
    def chooseDirectory(self):
        self.directoryEntry.delete(0,'end')
        self.directoryEntry.insert(0,filedialog.askdirectory())

    def organize(self):
        dirEntry=self.directoryEntry.get().strip()
        if dirEntry!="":dirEntry+="/"
        else:dirEntry=os.getcwd()+"/"
        if os.path.exists(dirEntry) or dirEntry=="":
            entries=[self.audioEntry,self.imageEntry,self.videoEntry,self.documentEntry]
            entriesGets=[]
            for i in range(len(entries)):
                if entries[i].get().strip()=="":
                    entries[i].insert(0,dirs[i])
                entriesGets.append(entries[i].get().strip())
            for i in listdir(dirEntry):
                match fileExtensions.get(os.path.splitext(i)[1].lower()):
                    case "audio":
                        if self.audioCheck.get():
                            if os.path.exists(dirEntry+entriesGets[0]):
                                os.rename(dirEntry+i,dirEntry+entriesGets[0]+"/"+i)
                            else: 
                                os.mkdir(dirEntry+entriesGets[0])
                                os.rename(dirEntry+i,dirEntry+entriesGets[0]+"/"+i)
                    
                    case "image":
                        if self.imageCheck.get():
                            if os.path.exists(dirEntry+entriesGets[1]):
                                os.rename(dirEntry+i,dirEntry+entriesGets[1]+"/"+i)
                            else: 
                                os.mkdir(dirEntry+entriesGets[1])
                                os.rename(dirEntry+i,dirEntry+entriesGets[1]+"/"+i)
                    case "video":
                        if self.videoCheck.get():
                            if os.path.exists(dirEntry+entriesGets[2]):
                                os.rename(dirEntry+i,dirEntry+entriesGets[2]+"/"+i)
                            else: 
                                os.mkdir(dirEntry+entriesGets[2])
                                os.rename(dirEntry+i,dirEntry+entriesGets[2]+"/"+i)
                    case "document":
                        if self.documentCheck.get():
                            if os.path.exists(dirEntry+entriesGets[3]):
                                os.rename(dirEntry+i,dirEntry+entriesGets[3]+"/"+i)
                            else: 
                                os.mkdir(dirEntry+entriesGets[3])
                                os.rename(dirEntry+i,dirEntry+entriesGets[3]+"/"+i)
        
    def __init__(self):
        super().__init__()

        self.audioCheck=ctk.IntVar()
        self.audioCheck.set(True)
        self.imageCheck=ctk.IntVar()
        self.imageCheck.set(True)
        self.videoCheck=ctk.IntVar()
        self.videoCheck.set(True)
        self.documentCheck=ctk.IntVar()
        self.documentCheck.set(True)

        set_default_color_theme("dark-blue")
        
        self.geometry("500x325")
        self.resizable(False,False)
        self.title("File Organizer")

        self.checkBoxStyle={"fg_color":"#ffc1c1","checkmark_color":"#000000","hover_color":"#ffffff"}
        self.buttonStyle={"fg_color":"#ffc1c1","text_color":"#000000","hover_color":"#ffffff"}
        self.entryStyle={"fg_color":"#282828","border_color":"#ffc1c1","border_width":1}

        self.frame1=CTkFrame(self)
        self.frame1.place(relx=0.5,rely=0.5,anchor=ctk.CENTER)
        self.frame1.configure(border_width=1,border_color="#ffc1c1")

        self.checks=CTkFrame(self.frame1,fg_color="transparent")
        self.checks.grid(row=1,column=0,padx=20,pady=(0,20))
        CTkCheckBox(self.checks,text="Audio",variable=self.audioCheck,**self.checkBoxStyle).grid(row=0,column=0,pady=5)
        CTkCheckBox(self.checks,text="Image",variable=self.imageCheck,**self.checkBoxStyle).grid(row=1,column=0,pady=5)
        CTkCheckBox(self.checks,text="Video",variable=self.videoCheck,**self.checkBoxStyle).grid(row=2,column=0,pady=5)
        CTkCheckBox(self.checks,text="Document",variable=self.documentCheck,**self.checkBoxStyle).grid(row=3,column=0,pady=5)
        CTkLabel(self.checks,text="Folder name for audio files:").grid(row=0,column=1,sticky=W,padx=15)
        CTkLabel(self.checks,text="Folder name for image files:").grid(row=1,column=1,sticky=W,padx=15)
        CTkLabel(self.checks,text="Folder name for video files:").grid(row=2,column=1,sticky=W,padx=15)
        CTkLabel(self.checks,text="Folder name for document files:").grid(row=3,column=1,sticky=W,padx=15)
        self.audioEntry=CTkEntry(self.checks,placeholder_text=audioDir,**self.entryStyle)
        self.audioEntry.grid(row=0,column=2)
        self.audioEntry.insert(0,audioDir)

        self.imageEntry=CTkEntry(self.checks,placeholder_text=imageDir,**self.entryStyle)
        self.imageEntry.grid(row=1,column=2)
        self.imageEntry.insert(0,imageDir)

        self.videoEntry=CTkEntry(self.checks,placeholder_text=videoDir,**self.entryStyle)
        self.videoEntry.grid(row=2,column=2)
        self.videoEntry.insert(0,videoDir)

        self.documentEntry=CTkEntry(self.checks,placeholder_text=documentDir,**self.entryStyle)
        self.documentEntry.grid(row=3,column=2)
        self.documentEntry.insert(0,documentDir)

        CTkLabel(self.frame1,text="File organizer",font=CTkFont(size=24,weight="bold")).grid(row=0,column=0,pady=(10,20))

        CTkLabel(self.checks,text="Directory to organize (leave empty for current):").grid(row=4,column=0,columnspan=2,padx=(0,24),sticky=W)
        self.directoryEntry=CTkEntry(self.checks,**self.entryStyle)
        self.directoryEntry.grid(row=4,column=2,pady=(10,5))
        CTkButton(self.checks,text="Choose",**self.buttonStyle,command=self.chooseDirectory).grid(row=5,column=2,pady=(0,5))
        CTkButton(self.checks,text="Organize!",**self.buttonStyle,command=self.organize).grid(row=6,column=2,pady=(0,0))

    
if __name__=="__main__":
    app=App()
    app.mainloop()