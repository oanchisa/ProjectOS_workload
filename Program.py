from tkinter import * 
from tkinter import ttk
import customtkinter as ctk
from policy import FIFO,RANDOM,LRU,MRU,LFU
from workload import x_ywork,no_local,loop
import tkinter.font as font
import functools

root = ctk.CTk()
root.geometry("1200x400")
root.resizable(0, 0)
root.title("Swapping: Policies")

frame = Frame(root)
bottomframe = Frame(root)
poliframe = Frame(root)
addframe = Frame(root)
listframe = Frame(root)
T = Text(root, height=40, width=1000)
global status
status=0

def back(cur,prev):
    cur,prev
    add2_b.pack_forget()
    listframe.pack_forget()
    T.pack_forget()
    cur.pack_forget()
    prev.pack()
    global status
    print("back",status)
    if status == 3:
        policy_but(p)
    # elif status == 3:
    #    frame.pack_forget()
    #    loadlist()

    print(cur)
    print(prev)
    
def firstpage():
    frame.pack()
    bottomframe.pack(side = BOTTOM)

def policy_but(po):
    global p
    p=po
    global status
    #print(status)
    status=1
    print("policy",status)
    frame.pack_forget()
    poliframe.pack()
    addframe.pack_forget()
  
#load list/ list frame    
def loadlist(wtype=2, poli=1 ,csize=5 ,total=20 ,limit=5 ,per_hwork=80, per_hpage=20):
    T.delete(1.0, END)
    Tview.delete(*Tview.get_children())
    poliframe.pack_forget()
    q = [FIFO(csize),RANDOM(csize),LRU(csize),MRU(csize),LFU(csize)]
    wl_nl = [no_local(limit,total),x_ywork(limit,total, per_hwork, per_hpage),loop(limit,total)]
    p = ["FIFO","RANDOM","LRU","MRU","LFU"]
    wl = ["no-local",str(per_hwork)+"-"+str(per_hpage)+" Workload","loop"]
    hit=commiss=j=0
    allwork = []
    
    for i in wl_nl[wtype]:
        j+=1
        ret = q[poli].use(i)
        if(ret == -1):
            hit+=1
            Tview.insert(parent='',index='end',iid=j-1,text='',values=[j,i,'Hit',' ',q[poli].list])
            #tablerow = [i,j,'Hit',' ',q[p_select].list]
        elif(ret == -2):
            Tview.insert(parent='',index='end',iid=j-1,text='',values=[j,i,'Miss',' ',q[poli].list])
            #tablerow = [i,j,'Miss',' ',q[p_select].list]
        else:
            Tview.insert(parent='',index='end',iid=j-1,text='',values=[j,i,'Miss',ret,q[poli].list])
            #tablerow = [i,j,'Miss',ret,q[p_select].list]
        if(i not in allwork):
            allwork.append(i)
    Tview.pack()
    
    listframe.pack()
    
    word = "policy : "+p[poli]+"\nworload type : "+wl[wtype]+"\ntotal pages accessed : "+str (total) +"\ntotal unique pages : "+str (
        limit) + "\nCache size : "+str(csize) + "\nhit rate = "+str(hit)+"/"+str(total)+ " = {0:.02f}".format(
            hit/total) + "\nhit rate(compulsory miss) = "+str(hit)+"/("+str(total)+"-"+str(len(allwork))+") = {0:.02f}".format(hit/(total-len(allwork)))
    T.insert(END, word)
    T.pack()
    

    global status
    status=2
    print("loadlist",status)



# หน้า loadlist
ta = IntVar()
totalacress = Label(poliframe, text = 'total page acress (workload)', font=('calibre',10, 'bold'))
ta_entry =Entry(poliframe,textvariable = ta, font=('calibre',10,'normal'))
ta_entry.delete(0,END)
ta_entry.get()
totalacress.pack()
ta_entry.pack()
up = IntVar()
uqpage = Label(poliframe, text = 'total unique page', font=('calibre',10, 'bold'))
up_entry =Entry(poliframe,textvariable = up, font=('calibre',10,'normal'))
up_entry.delete(0,END)
up_entry.get()
uqpage.pack()
up_entry.pack()
cs = IntVar()
csize = Label(poliframe, text = 'cache size', font=('calibre',10, 'bold'))
cs_entry =Entry(poliframe,textvariable = cs, font=('calibre',10,'normal'))
cs_entry.delete(0,END)
cs_entry.get()
csize.pack()
cs_entry.pack()
perhw = IntVar()
perhotwork = Label(poliframe, text = 'percentage of hotwork compared to all work (n)', font=('calibre',10, 'bold'))
phw_entry =Entry(poliframe,textvariable = perhw , font=('calibre',10,'normal'))
phw_entry.delete(0,END)
phw_entry.get()
perhotwork.pack()
phw_entry.pack()
perhp = IntVar()
perhotpage = Label(poliframe, text = 'percentage of hotpage compared to all page (m)', font=('calibre',10, 'bold'))
php_entry =Entry(poliframe,textvariable = perhp, font=('calibre',10,'normal'))
php_entry.delete(0,END)
php_entry.get()
perhotpage.pack()
php_entry.pack()
    

#workload / poliframe
nolocal_b = ctk.CTkButton(poliframe,text="no local",height= 50, width=100, fg_color ='blue',
                          hover_color='gray',command=lambda:loadlist(poli=p,wtype=0,csize=cs.get(),total=ta.get(),limit=up.get()))
nolocal_b.pack()
nolocal_b['font'] = font.Font(size=20)

w80_20_b = ctk.CTkButton(poliframe, text = 'n-m workload',height= 50, width=100, fg_color ='blue',hover_color='gray',
                            command=lambda: loadlist(poli=p,wtype=1,csize=cs.get(),total=ta.get(),limit=up.get(),
                                           per_hwork=perhw.get(), per_hpage=perhp.get()))
w80_20_b.pack()
w80_20_b['font'] = font.Font(size=20)

loop_b = ctk.CTkButton(poliframe, text ='loop',height= 50, width=100, fg_color ='blue',hover_color='gray',
                command=lambda: loadlist(poli=p,wtype=2,csize=cs.get(),total=ta.get(),limit=up.get()))
loop_b.pack()
loop_b['font'] = font.Font(size=20)

add1_b = ctk.CTkButton(listframe,text="ADD",height= 50, width=100, fg_color ='red',
                            hover_color='gray',command=lambda:addlist(poli=p,wtype=0,csize2=cs.get(),total=ta.get(),limit=up.get()))

add1_b.pack()
add1_b['font'] = font.Font(size=20)


nolocal_b.pack( side = LEFT)
w80_20_b.pack( side = RIGHT )
loop_b.pack( side = BOTTOM )
add1_b.pack( side = RIGHT)

# หน้า AddFrme
ta2 = IntVar()
totalacress2 = Label(root, text = 'total page acress (workload)', font=('calibre',10, 'bold'))
ta2_entry =Entry(root,textvariable = ta2, font=('calibre',10,'normal'))
ta2_entry.delete(0,END)
ta2_entry.get()

up2 = IntVar()
uqpage2 = Label(root, text = 'total unique page', font=('calibre',10, 'bold'))
up2_entry =Entry(root,textvariable = up2, font=('calibre',10,'normal'))
up2_entry.delete(0,END)
up2_entry.get()

cs2 = IntVar()
csize2 = Label(root, text = 'cache size', font=('calibre',10, 'bold'))
cs2_entry =Entry(root,textvariable = cs2, font=('calibre',10,'normal'))
cs2_entry.delete(0,END)
cs2_entry.get()

perhw2 = IntVar()
perhotwork2 = Label(root, text = 'percentage of hotwork compared to all work (n)', font=('calibre',10, 'bold'))
phw2_entry =Entry(root,textvariable = perhw2 , font=('calibre',10,'normal'))
phw2_entry.delete(0,END)
phw2_entry.get()

perhp2 = IntVar()
perhotpage2 = Label(root, text = 'percentage of hotpage compared to all page (m)', font=('calibre',10, 'bold'))
php2_entry =Entry(root,textvariable = perhp2, font=('calibre',10,'normal'))
php2_entry.delete(0,END)
php2_entry.get()

add2_b = ctk.CTkButton(root,text="ADD",height= 50, width=100, fg_color ='blue',
                            hover_color='gray',command=lambda:loadlist2(poli=p,wtype=0,csize2=cs.get(),total2=ta.get(),limit=up.get()))

add2_b['font'] = font.Font(size=20)

# def addlist(wtype=2, poli=1 ,csize=5 ,total=20 ,limit=5 ,per_hwork=80, per_hpage=20):
def addlist(wtype=2, poli=1 ,csize2=5 ,total=20 ,limit=5 ,per_hwork=80, per_hpage=20):
    data = []
    for item in Tview.get_children():
        data.append(Tview.item(item)["values"])
        print(Tview.item(item)["values"])

    T.pack_forget()
    Tview.pack_forget()
    listframe.pack_forget()
    totalacress2.pack()
    ta2_entry.pack()
    uqpage2.pack()
    up2_entry.pack()
    csize.pack()
    cs2_entry.pack()
    perhotwork2.pack()
    phw2_entry.pack()
    perhotpage2.pack()
    php2_entry.pack()
    add2_b.pack()
    global status
    status=3
    print("addlist",status)
    # listframe.pack_forget()


def loadlist2(wtype=2, poli=1, csize2=5, total2=20, limit=5, per_hwork2=80, per_hpage2=20):
    q = [FIFO(csize2),RANDOM(csize2),LRU(csize2),MRU(csize2),LFU(csize2)]
    wl_nl = [no_local(limit,total2),x_ywork(limit,total2, per_hwork2, per_hpage2),loop(limit,total2)]
    p = ["FIFO","RANDOM","LRU","MRU","LFU"]
    wl = ["no-local",str(per_hwork2)+"-"+str(per_hpage2)+" Workload","loop"]
    hit=commiss=j=0
    allwork = []

    j=len(Tview.get_children())

    for i in wl_nl[wtype]:
        j+=1
        ret = q[poli].use(i)
        if(ret == -1):
            hit+=1
            Tview.insert(parent='',index='end',iid=j-1,text='',values=[j,i,'Hit',' ',q[poli].list])
            #tablerow = [i,j,'Hit',' ',q[p_select].list]
        elif(ret == -2):
            Tview.insert(parent='',index='end',iid=j-1,text='',values=[j,i,'Miss',' ',q[poli].list])
            #tablerow = [i,j,'Miss',' ',q[p_select].list]
        else:
            Tview.insert(parent='',index='end',iid=j-1,text='',values=[j,i,'Miss',ret,q[poli].list])
            #tablerow = [i,j,'Miss',ret,q[p_select].list]
        if(i not in allwork):
            allwork.append(i)
    Tview.pack()
    
    listframe.pack()

    word = "\npolicy : "+p[poli]+"\nworload type : "+wl[wtype]+"\ntotal pages accessed : "+str (total2) +"\ntotal unique pages : "+str (
        limit) + "\nCache size : "+str(csize2) + "\nhit rate = "+str(hit)+"/"+str(total2)+ " = {0:.02f}".format(
            hit/total2) + "\nhit rate(compulsory miss) = "+str(hit)+"/("+str(total2)+"-"+str(len(
                allwork))+") = {0:.02f}".format(hit/(total2-len(allwork)))
    T.insert(END, word)
    T.pack()

    global status
    status=4
    print("loadlist2",status)

    data2 = []
    for item2 in Tview.get_children():
        data2.append(Tview.item(item2)["values"])
        print(Tview.item(item2)["values"])

    totalacress2.pack_forget()
    ta2_entry.pack_forget()
    uqpage2.pack_forget()
    up2_entry.pack_forget()
    # csize2.pack_forget()
    cs2_entry.pack_forget()
    perhotwork2.pack_forget()
    phw2_entry.pack_forget()
    perhotpage2.pack_forget()
    php2_entry.pack_forget()
    add2_b.pack_forget()
    # T.pack()
    Tview.pack()
    listframe.pack()
    T.pack()

ptitle = ctk.CTkLabel(frame, text = 'Please select Policy', font=('calibre',60, 'bold'))
ptitle.pack()
space = ctk.CTkLabel(frame, text = '',font=('calibre',50, 'bold'))
space.pack()

FIFO_b = ctk.CTkButton(frame,text="FIFO",height= 100, width=150, fg_color ='#ab2c23',hover_color='gray',command=lambda: policy_but(0))
FIFO_b.pack()
RAND_b = ctk.CTkButton(frame,text="RANDOM",height= 100, width=150, fg_color ='#c0982f',hover_color='gray',command=lambda: policy_but(1))
RAND_b.pack()
LRU_b = ctk.CTkButton(frame,text="LRU",height= 100, width=150, fg_color ='#234a1f',hover_color='gray',command=lambda: policy_but(2))
LRU_b.pack()
MRU_b = ctk.CTkButton(frame,text="MRU",height= 100, width=150, fg_color ='#443bb5',hover_color='gray',command=lambda: policy_but(3))
MRU_b.pack()
LFU_b = ctk.CTkButton(frame,text="LFU",height= 100, width=150, fg_color ='#4f2e1a',hover_color='gray',command=lambda: policy_but(4))
LFU_b.pack() 
FIFO_b.pack( side = LEFT)
RAND_b.pack( side = LEFT )
LRU_b.pack( side = LEFT )
MRU_b.pack( side = LEFT )
LFU_b.pack( side = BOTTOM )



scroll = Scrollbar(listframe)
scroll.pack(side=RIGHT, fill=Y)
Tview = ttk.Treeview(listframe,yscrollcommand=scroll.set) #สร้าง 
Tview.pack()
scroll.config(command=Tview.yview)
Tview['columns'] = ('No.', 'Access', 'Hit/Miss', 'Evict', 'Cache State')
Tview.column("#0", width=0,  stretch=NO)
Tview.column("No.",anchor=CENTER, width=100)
Tview.column("Access",anchor=CENTER,width=100)
Tview.column("Hit/Miss",anchor=CENTER,width=100)
Tview.column("Evict",anchor=CENTER,width=100)
Tview.column("Cache State",anchor=CENTER,width=800)
Tview.heading("#0",text="",anchor=CENTER)
Tview.heading("No.",text="No.",anchor=CENTER)
Tview.heading("Access",text="Access",anchor=CENTER)
Tview.heading("Hit/Miss",text="Hit/Miss",anchor=CENTER)
Tview.heading("Evict",text="Evict",anchor=CENTER)
Tview.heading("Cache State",text="Cache State",anchor=CENTER)
Tview.pack()

back1 = functools.partial(back,poliframe,frame)
back_b = ctk.CTkButton(bottomframe,text="Back",height= 50, width=100, fg_color ='black',hover_color='gray',
                command=back1)
back_b['font'] = font.Font(size=20)
back_b.pack( side = LEFT)

#lambda:back(poliframe,frame)
Exit_b = ctk.CTkButton(bottomframe,text="Exit",height= 50, width=100, fg_color ='black',hover_color='gray',
                command=root.destroy)
Exit_b['font'] = font.Font(size=20)
Exit_b.pack( side = BOTTOM)

firstpage()

root.mainloop()

