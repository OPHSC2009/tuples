
from tkinter import*
root=Tk()
root.geometry("1000x1000")
root.title("Profit Generator")



months=("January","February","March","April"," May","June", "July","August","September","October","November","December")
profits=(50,34,65,45,1,32,81,9,21,25,65,71)


max_lbl=Label(root)
min_lbl=Label(root)
max_lbl.place(relx=0.5,rely=0.5 ,anchor=CENTER)
min_lbl.place(relx=0.5,rely=0.6,anchor=CENTER)

def generate():
    max_profit=max(profits)
    index_profit=profits.index(max_profit)
    max_profit_month=months[index_profit]

    min_profit=min(profits)
    index_profit_min=profits.index(min_profit)
    min_profit_month=months[index_profit_min]

    print(max_profit)
    print(max_profit_month)

    print(min_profit)
    print(min_profit_month)
    
    max_lbl["text"]="The maximum profit generated by the company is "+str(max_profit)+" and it was achieved in "+max_profit_month
    min_lbl["text"]="The minimum profit generated by the company is "+str(min_profit)+" and it was achieved in "+min_profit_month
    

btn=Button(root,text="Generate Values", command=generate)
btn.place(relx=0.5,rely=0.8,anchor=CENTER)



root.mainloop()
