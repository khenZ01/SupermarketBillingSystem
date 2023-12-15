from tkinter import * #FOR CREATING GUI
from tkinter import messagebox #USED TO DISPLAY THE A MESSAGEBOX
import random,os,tempfile, smtplib #RANDOM-generate random numbers, OS-

#Functionality Part

def clear():
    bathsoapEntry.delete(0, END)
    toothbrushEntry.delete(0, END)
    sanitizerEntry.delete(0, END)
    tissueEntry.delete(0, END)
    perfumeEntry.delete(0, END)
    deodorantEntry.delete(0, END)
    toothpasteEntry.delete(0, END)

    riceEntry.delete(0,END)
    sugarEntry.delete(0, END)
    oilEntry.delete(0, END)
    cannedgoodsEntry.delete(0, END)
    condimentEntry.delete(0, END)
    veggiesEntry.delete(0, END)
    fishEntry.delete(0, END)

    mountaindewEntry.delete(0, END)
    cokeEntry.delete(0, END)
    spriteEntry.delete(0, END)
    pepsiEntry.delete(0, END)
    alcoholEntry.delete(0, END)
    mojitoEntry.delete(0, END)

    bathsoapEntry.insert(0,0)
    toothbrushEntry.insert(0, 0)
    sanitizerEntry.insert(0, 0)
    tissueEntry.insert(0, 0)
    perfumeEntry.insert(0, 0)
    deodorantEntry.insert(0, 0)
    toothpasteEntry.insert(0, 0)

    riceEntry.insert(0, 0)
    sugarEntry.insert(0, 0)
    oilEntry.insert(0, 0)
    cannedgoodsEntry.insert(0, 0)
    condimentEntry.insert(0, 0)
    veggiesEntry.insert(0, 0)
    fishEntry.insert(0, 0)

    mountaindewEntry.insert(0, 0)
    cokeEntry.insert(0, 0)
    spriteEntry.insert(0, 0)
    pepsiEntry.insert(0, 0)
    alcoholEntry.insert(0, 0)
    mojitoEntry.insert(0, 0)

    HygienePriceEntry.delete(0, END)
    GroceryPriceEntry.delete(0, END)
    DrinksPriceEntry.delete(0, END)

    HygieneTaxEntry.delete(0, END)
    GroceryTaxEntry.delete(0, END)
    DrinksTaxEntry.delete(0, END)

    NameEntry.delete(0,END)
    PhoneEntry.delete(0,END)
    BillNumberEntry.delete(0,END)

    TextArea.delete(1.0,END)

#Function to Send Receipt on Email
def Send_Email():
    def Send_Gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com', 587)
            ob.starttls()
            ob.login(SenderEntry.get(), PasswordEntry.get())
            message=Email_textarea.get(1.0, END)
            ob.sendmail(SenderEntry.get(), ReceiverEntry.get(), message)
            ob.quit()
            messagebox.showinfo('Success', 'Bill is Successfully Sent!'
                                ,parent=root1)
            root1.destroy()
        except:
            messagebox.showerror('Error', 'Something went wrong, Please try again'
                                 ,parent=root1)
    if TextArea.get(1.0,END)=='\n':
       messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('Send Gmail')
        root1.config(bg='gray20')
        root1.resizable(0,0)

        SenderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,
                               bg='gray20',fg='white')
        SenderFrame.grid(row=0,column=0, padx=40, pady=20)

        SenderLabel=Label(SenderFrame,text="Sender's Email",font=('arial',14,'bold'),
                          bg='gray20',fg='white')
        SenderLabel.grid(row=0,column=0,padx=10, pady=8)

        SenderEntry=Entry(SenderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        SenderEntry.grid(row=0,column=1, padx=10, pady=8)

        PasswordLabel=Label(SenderFrame,text="Password",font=('arial',14,'bold'),
                            bg='gray20',fg='white')
        PasswordLabel.grid(row=1,column=0,padx=10, pady=8)

        PasswordEntry=Entry(SenderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE, show='*')
        PasswordEntry.grid(row=1,column=1, padx=10, pady=8)


        RecipientFrame = LabelFrame(root1, text='RECIPIENT', font=('arial', 16, 'bold'),
                                    bd=6, bg='gray20', fg='white')
        RecipientFrame.grid(row=1, column=0, padx=40, pady=20)


        ReceiverLabel = Label(RecipientFrame, text="Email Address", font=('arial', 14, 'bold'),
                              bg='gray20', fg='white')
        ReceiverLabel.grid(row=0, column=0, padx=10, pady=8)

        ReceiverEntry = Entry(RecipientFrame, font=('arial', 14, 'bold'),
                              bd=2, width=23, relief=RIDGE)
        ReceiverEntry.grid(row=0, column=1, padx=10, pady=8)

        MessageLabel = Label(RecipientFrame, text="Message", font=('arial', 14, 'bold'),
                             bg='gray20', fg='white')
        MessageLabel.grid(row=1, column=0, padx=10, pady=8)

        Email_textarea=Text(RecipientFrame, font=('arial', 14, 'bold'), bd=2, relief=SUNKEN,
                            width=42, height=11)
        Email_textarea.grid(row=2, column=0, columnspan=2)
        Email_textarea.delete(1.0, END)
        Email_textarea.insert(END, TextArea.get(1.0, END).replace('=', '')
                    .replace('-','').replace('\t\t\t', '\t\t'))


        SendButton=Button(root1, text='SEND', font=('copper', 20, 'bold'),
                          width=15, command=Send_Gmail)
        SendButton.grid(row=2, column=0, pady=15)
def print_bill():
    if TextArea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(TextArea.get(1.0,END))
        os.startfile(file,'print')


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==BillNumberEntry.get():
            f= open(f'bills/{i}','r')
            TextArea.delete(1.0,END)
            for data in f:
                TextArea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill Number')
if not os.path.exists('bills'):
    os.mkdir('bills')
def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill?')
    if result:
        bill_content=TextArea.get(1.0,END)
        file=open(f'bills/{billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f' Bill Number {billnumber} is saved successfully')
        billnumber = random.randint(500,1000)
billnumber=random.randint(500,1000)
def bill_area():
    if NameEntry.get()== ' 'or PhoneEntry.get()==' ':
       messagebox.showerror('Error', 'Customer Details are Required')
    elif HygienePriceEntry.get()==' ' and GroceryPriceEntry.get()==' ' and DrinksPriceEntry.get()==' ':
       messagebox.showerror('Error', 'No Products are Selected')
    elif HygienePriceEntry.get()=='0 PHP' and GroceryPriceEntry.get()=='0 PHP' and DrinksPriceEntry.get()=='0 PHP':
       messagebox.showerror('Error', 'No Products are Selected')
    else:
        TextArea.delete(1.0,END)

    TextArea.insert(END,'\t\t**Welcome Customer**\n')
    TextArea.insert(END,f'\nBill Number: {billnumber}\n')
    TextArea.insert(END, f'\nCustomer Name: {NameEntry.get()}\n')
    TextArea.insert(END, f'\nCustomer Phone Number: {PhoneEntry.get()}\n')
    TextArea.insert(END,'\n=======================================================')
    TextArea.insert(END,'Product\t\t\tQuantity\t\t\tPrice')
    TextArea.insert(END,'\n=======================================================')

    if bathsoapEntry.get() != '0':
       TextArea.insert(END, f'\nBath Soap\t\t\t{bathsoapEntry.get()}\t\t\t{soapprice}')
    if toothbrushEntry.get() != '0':
       TextArea.insert(END, f'\nToothbrush\t\t\t{toothbrushEntry.get()}\t\t\t{toothbrushprice}')
    if sanitizerEntry.get() != '0':
       TextArea.insert(END, f'\nSanitizer\t\t\t{sanitizerEntry.get()}\t\t\t{sanitizerprice} ')
    if tissueEntry.get() != '0':
       TextArea.insert(END, f'\nTissue\t\t\t{tissueEntry.get()}\t\t\t{tissueprice}')
    if perfumeEntry.get() != '0':
       TextArea.insert(END, f'\nPerfume\t\t\t{perfumeEntry.get()}\t\t\t{perfumeprice}')
    if deodorantEntry.get() != '0':
       TextArea.insert(END, f'\nDeodorant\t\t\t{deodorantEntry.get()}\t\t\t{deodorantprice}')
    if toothpasteEntry.get() != '0':
       TextArea.insert(END, f'\nToothpaste\t\t\t{toothpasteEntry.get()}\t\t\t{toothpasteprice}')

    if riceEntry.get() != '0':
       TextArea.insert(END, f'\nRice\t\t\t{riceEntry.get()}\t\t\t{riceprice}')
    if sugarEntry.get() != '0':
       TextArea.insert(END, f'\nSugar\t\t\t{sugarEntry.get()}\t\t\t{sugarprice}')
    if oilEntry.get() != '0':
       TextArea.insert(END, f'\nOil\t\t\t{oilEntry.get()}\t\t\t{oilprice}')
    if cannedgoodsEntry.get() != '0':
       TextArea.insert(END, f'\nCannedgoods\t\t\t{cannedgoodsEntry.get()}\t\t\t{cannedgoodsprice}')
    if condimentEntry.get() != '0':
       TextArea.insert(END, f'\nCondiment\t\t\t{condimentEntry.get()}\t\t\t{condimentprice}')
    if veggiesEntry.get() != '0':
       TextArea.insert(END, f'\nVeggies\t\t\t{veggiesEntry.get()}\t\t\t{veggiesprice}')
    if fishEntry.get() != '0':
       TextArea.insert(END, f'\nFish\t\t\t{fishEntry.get()}\t\t\t{fishprice}')

    if mountaindewEntry.get() != '0':
       TextArea.insert(END, f'\nMountain Dew\t\t\t{mountaindewEntry.get()}\t\t\t{mountaindewprice}')
    if cokeEntry.get() != '0':
       TextArea.insert(END, f'\nCoke\t\t\t{cokeEntry.get()}\t\t\t{cokeprice}')
    if spriteEntry.get() != '0':
       TextArea.insert(END, f'\nSprite\t\t\t{spriteEntry.get()}\t\t\t{spriteprice}')
    if pepsiEntry.get() != '0':
       TextArea.insert(END, f'\nPepsi\t\t\t{pepsiEntry.get()}\t\t\t{pepsiprice}')
    if ginEntry.get() != '0':
       TextArea.insert(END, f'\nGin Bilog\t\t\t{ginEntry.get()}\t\t\t{ginprice}')
    if alcoholEntry.get() != '0':
       TextArea.insert(END, f'\nAlfonso\t\t\t{alcoholEntry.get()}\t\t\t{alcoholprice}')
    if mojitoEntry.get() != '0':
       TextArea.insert(END, f'\nMojito\t\t\t{mojitoEntry.get()}\t\t\t{mojitoprice}')
    TextArea.insert(END, '\n-------------------------------------------------------')

    if HygieneTaxEntry.get() != '0.0 PHP':
       TextArea.insert(END, f'\nHygiene Tax\t\t\t\t{HygieneTaxEntry.get()}')
    if GroceryTaxEntry.get() != '0.0 PHP':
       TextArea.insert(END, f'\nGrocery Tax\t\t\t\t{GroceryTaxEntry.get()}')
    if DrinksTaxEntry.get() != '0.0 PHP':
       TextArea.insert(END, f'\nDrinks Tax\t\t\t\t{DrinksTaxEntry.get()}')
    TextArea.insert(END,f'\n\nTotal Bill \t\t\t\t {totalbill}')
    TextArea.insert(END, '\n-------------------------------------------------------')
    save_bill ()
#Hygiene Price Calculation
def total():
    global soapprice,toothbrushprice,sanitizerprice,tissueprice,perfumeprice,deodorantprice,toothpasteprice
    global riceprice,sugarprice,oilprice,cannedgoodsprice,condimentprice,veggiesprice,fishprice
    global mountaindewprice,cokeprice,spriteprice,pepsiprice,ginprice,alcoholprice,mojitoprice
    global totalbill
    soapprice=int(bathsoapEntry.get())*40
    toothbrushprice = int(toothbrushEntry.get())*20
    sanitizerprice = int(sanitizerEntry.get()) * 45
    tissueprice = int(tissueEntry.get()) * 15
    perfumeprice = int(perfumeEntry.get()) * 120
    deodorantprice = int(deodorantEntry.get()) * 95
    toothpasteprice = int(toothpasteEntry.get()) * 35

    totalhygieneprice = soapprice+toothbrushprice+sanitizerprice+tissueprice+perfumeprice+deodorantprice+toothpasteprice
    HygienePriceEntry.delete(0, END)
    HygienePriceEntry.insert(0, f'{totalhygieneprice} PHP')
    HygieneTax=totalhygieneprice*0.12
    HygieneTaxEntry.delete(0, END)
    HygieneTaxEntry.insert(0, str(HygieneTax) + ' PHP')


#Grocery Price Calculation
    riceprice=int(riceEntry.get())*1500
    sugarprice = int(sugarEntry.get())*95
    oilprice = int(oilEntry.get())*30
    cannedgoodsprice = int(cannedgoodsEntry.get())*47
    condimentprice = int(condimentEntry.get())*20
    veggiesprice = int(veggiesEntry.get())*150
    fishEntryprice = int(fishEntry.get())*180

    totalgroceryprice = riceprice+sugarprice+oilprice+cannedgoodsprice+condimentprice+veggiesprice+fishEntryprice
    GroceryPriceEntry.delete(0, END)
    GroceryPriceEntry.insert(0, str(totalgroceryprice)+ ' PHP')
    GroceryTax = totalgroceryprice * 0.05
    GroceryTaxEntry.delete(0, END)
    GroceryTaxEntry.insert(0, str( GroceryTax) + ' PHP')


# Drinks Price Calculation
    mountaindewprice=int(mountaindewEntry.get())*25
    cokeprice = int(cokeEntry.get())*25
    spriteprice = int(spriteEntry.get())*25
    pepsiprice = int(pepsiEntry.get())*25
    ginprice = int(ginEntry.get())*75
    alcoholprice = int(alcoholEntry.get())*250
    mojitoprice = int(mojitoEntry.get())*150

    totaldrinksprice = mountaindewprice+cokeprice+spriteprice+pepsiprice+ginprice+alcoholprice+mojitoprice
    DrinksPriceEntry.delete(0, END)
    DrinksPriceEntry.insert(0, str(totaldrinksprice)+ ' PHP')
    DrinksTax = totaldrinksprice * 0.08
    DrinksTaxEntry.delete(0, END)
    DrinksTaxEntry.insert(0, str(DrinksTax) + ' PHP')

    totalbill=totalhygieneprice+totalgroceryprice+totaldrinksprice


root=Tk()
root.title('SuperMarket Billing System')
root.geometry('1270x685')
root.iconbitmap('icon.ico')


headingLabel=Label(root, text='Supermarket Billing System', font=('Algerian', 20, 'bold')
                   ,bg='navyblue', fg='white', bd=8, relief=GROOVE)
headingLabel.pack(fill=X)


Customer_Details_Frame=LabelFrame(root, text='Customer Details', font=('Aharoni', 15, 'bold')
                                  ,fg='white', bd=5, relief=GROOVE, bg='navyblue')
Customer_Details_Frame.pack(fill=X)


NameLabel=Label(Customer_Details_Frame, text='Name', font=('times new roman', 13, 'bold'),
                bg='navyblue', fg='white')
NameLabel.grid(row=0, column=0, padx=10)
NameEntry=Entry(Customer_Details_Frame, font=('arial', 10), bd=7, width=18)
NameEntry.grid(row=0, column=1, padx=8)


PhoneLabel=Label(Customer_Details_Frame, text='Phone Number', font=('times new roman', 13, 'bold'),
                bg='navyblue', fg='white')
PhoneLabel.grid(row=0, column=2, padx=20, pady=10)
PhoneEntry=Entry(Customer_Details_Frame, font=('arial', 10), bd=7, width=18)
PhoneEntry.grid(row=0, column=3, padx=8)


BillNumberLabel=Label(Customer_Details_Frame, text='Bill Number', font=('times new roman', 13, 'bold'),
                bg='navyblue', fg='white')
BillNumberLabel.grid(row=0, column=4, padx=20, pady=10)
BillNumberEntry=Entry(Customer_Details_Frame, font=('arial', 13), bd=7, width=18)
BillNumberEntry.grid(row=0, column=5, padx=8)

searchButton=Button(Customer_Details_Frame, text='SEARCH', font=('copper black', '13','bold'), bd=7, width=10,command=search_bill)
searchButton.grid(row=0, column=6, padx=20, pady=10)

ProductsFrame=Frame(root)
ProductsFrame.pack()

HygieneFrame=LabelFrame(ProductsFrame, text='Hygiene', font=('Aharoni', 15, 'bold')
                                  ,fg='white', bd=7, relief=GROOVE, bg='navyblue')
HygieneFrame.grid(row=0, column=0)

bathsoapLabel=Label(HygieneFrame, text='Bioderm', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
bathsoapLabel.grid(row=0, column=0)
bathsoapEntry=Entry(HygieneFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
bathsoapEntry.grid(row=0, column=1, pady=3, padx=10, sticky ='w')
bathsoapEntry.insert(0, 0)


toothbrushLabel=Label(HygieneFrame, text='OralB ToothBrush', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
toothbrushLabel.grid(row=1, column=0)
toothbrushEntry=Entry(HygieneFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
toothbrushEntry.grid(row=1, column=1, pady=3, padx=10, sticky ='w')
toothbrushEntry.insert(0, 0)

sanitizerLabel=Label(HygieneFrame, text='Ethyl Alcohol',  font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
sanitizerLabel.grid(row=2, column=0)
sanitizerEntry=Entry(HygieneFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
sanitizerEntry.grid(row=2, column=1, pady=3, padx=10, sticky ='w')
sanitizerEntry.insert(0, 0)

tissueLabel=Label(HygieneFrame, text='Joy Tissue',  font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
tissueLabel.grid(row=3, column=0)
tissueEntry=Entry(HygieneFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
tissueEntry.grid(row=3, column=1, pady=3, padx=10, sticky ='w')
tissueEntry.insert(0, 0)

perfumeLabel=Label(HygieneFrame, text='Juicy Cologne',  font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
perfumeLabel.grid(row=4, column=0)
perfumeEntry=Entry(HygieneFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
perfumeEntry.grid(row=4, column=1, pady=3, padx=10, sticky ='w')
perfumeEntry.insert(0, 0)

deodorantLabel=Label(HygieneFrame, text='Rexona Men/Women',  font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
deodorantLabel.grid(row=5, column=0)
deodorantEntry=Entry(HygieneFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
deodorantEntry.grid(row=5, column=1, pady=3, padx=10, sticky ='w')
deodorantEntry.insert(0, 0)

toothpasteLabel=Label(HygieneFrame, text='Colgate ToothPaste',  font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
toothpasteLabel.grid(row=6, column=0)
toothpasteEntry=Entry(HygieneFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
toothpasteEntry.grid(row=6, column=1, pady=3, padx=10, sticky ='w')
toothpasteEntry.insert(0, 0)

GroceryFrame=LabelFrame(ProductsFrame, text='Groceries', font=('Aharoni', 15, 'bold')
                                  ,fg='white', bd=7, relief=GROOVE, bg='navyblue')
GroceryFrame.grid(row=0, column=1)


riceLabel=Label(GroceryFrame, text='Hasmine Rice', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
riceLabel.grid(row=0, column=1)
riceEntry=Entry(GroceryFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
riceEntry.grid(row=0, column=2, pady=3, padx=10, sticky ='w')
riceEntry.insert(0, 0)

sugarLabel=Label(GroceryFrame, text='White Sugar', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
sugarLabel.grid(row=1, column=1)
sugarEntry=Entry(GroceryFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
sugarEntry.grid(row=1, column=2, pady=3, padx=10, sticky ='w')
sugarEntry.insert(0, 0)

oilLabel=Label(GroceryFrame, text='Canola Oil', font=('copper', 13, 'bold'),
               bg='navyblue', fg='white')
oilLabel.grid(row=2, column=1, pady=5)
oilEntry=Entry(GroceryFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
oilEntry.grid(row=2, column=2, pady=3, padx=10, sticky ='w')
oilEntry.insert(0, 0)


cannedgoodsLabel=Label(GroceryFrame, text='Argentina Cornbeef', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
cannedgoodsLabel.grid(row=3, column=1)
cannedgoodsEntry=Entry(GroceryFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
cannedgoodsEntry.grid(row=3, column=2, pady=3, padx=10, sticky ='w')
cannedgoodsEntry.insert(0, 0)


condimentLabel=Label(GroceryFrame, text='Magic Sarap', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
condimentLabel.grid(row=4, column=1)
condimentEntry=Entry(GroceryFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
condimentEntry.grid(row=4, column=2, pady=3, padx=10, sticky ='w')
condimentEntry.insert(0, 0)


veggiesLabel=Label(GroceryFrame, text='Chopseuy Veggies', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
veggiesLabel.grid(row=5, column=1)
veggiesEntry=Entry(GroceryFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
veggiesEntry.grid(row=5, column=2, pady=3, padx=10, sticky ='w')
veggiesEntry.insert(0, 0)


fishLabel=Label(GroceryFrame, text='Boneless Bangus', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
fishLabel.grid(row=6,column=1)
fishEntry=Entry(GroceryFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
fishEntry.grid(row=6, column=2, pady=3, padx=10, sticky ='w')
fishEntry.insert(0, 0)


DrinksFrame=LabelFrame(ProductsFrame, text='Drinks', font=('Aharoni', 15, 'bold')
                                  ,fg='white', bd=7, relief=GROOVE, bg='navyblue')
DrinksFrame.grid(row=0, column=2)

mountaindewLabel=Label(DrinksFrame, text='Mountain Dew', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
mountaindewLabel.grid(row=0, column=0)
mountaindewEntry=Entry(DrinksFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
mountaindewEntry.grid(row=0, column=1, pady=3, padx=10, sticky ='w')
mountaindewEntry.insert(0, 0)


cokeLabel=Label(DrinksFrame, text='Coke', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
cokeLabel.grid(row=1, column=0)
cokeEntry=Entry(DrinksFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
cokeEntry.grid(row=1, column=1, pady=3, padx=10, sticky ='w')
cokeEntry.insert(0, 0)


spriteLabel=Label(DrinksFrame, text='Sprite', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
spriteLabel.grid(row=2, column=0)
spriteEntry=Entry(DrinksFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
spriteEntry.grid(row=2, column=1, pady=3, padx=10, sticky ='w')
spriteEntry.insert(0, 0)


pepsiLabel=Label(DrinksFrame, text='Pepsi', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
pepsiLabel.grid(row=3, column=0)
pepsiEntry=Entry(DrinksFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
pepsiEntry.grid(row=3, column=1, pady=3, padx=10, sticky ='w')
pepsiEntry.insert(0, 0)


ginLabel=Label(DrinksFrame, text='GinBilog', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
ginLabel.grid(row=4, column=0)
ginEntry=Entry(DrinksFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
ginEntry.grid(row=4, column=1, pady=3, padx=10, sticky ='w')
ginEntry.insert(0, 0)


alcoholLabel=Label(DrinksFrame, text='Alfonso', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
alcoholLabel.grid(row=5, column=0)
alcoholEntry=Entry(DrinksFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
alcoholEntry.grid(row=5, column=1, pady=3, padx=10, sticky ='w')
alcoholEntry.insert(0, 0)

mojitoLabel=Label(DrinksFrame, text='GSM Mojito', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
mojitoLabel.grid(row=6, column=0)
mojitoEntry=Entry(DrinksFrame, font= ('times new roman', 15, 'bold'), width=6, bd=7)
mojitoEntry.grid(row=6, column=1, pady=3, padx=10, sticky ='w')
mojitoEntry.insert(0, 0)


BillFrame=Frame(ProductsFrame, bd=7, relief=GROOVE)
BillFrame.grid(row=0, column=3, padx=8)
BillAreaLabel=Label(BillFrame, text='Bill Area', font=('Aharoni', 13, 'bold'), bd=7,
                    relief=GROOVE)
BillAreaLabel.pack(fill = X)

Scrollbar=Scrollbar(BillFrame, orient=VERTICAL)
Scrollbar.pack(side=RIGHT, fill = Y)
TextArea=Text(BillFrame, height=17, width=55, yscrollcommand=Scrollbar)
TextArea.pack()
Scrollbar.config(command=TextArea.yview())

BillMenuFrame=LabelFrame(root, text='Bill Menu', font=('Aharoni', 13, 'bold')
                                  ,fg='white', bd=7, relief=GROOVE, bg='navyblue')
BillMenuFrame.pack()

HygienePriceLabel=Label(BillMenuFrame, text='Hygiene Price', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
HygienePriceLabel.grid(row=0, column=0)
HygienePriceEntry=Entry(BillMenuFrame, font= ('times new roman', 15, 'bold'),
                        width=20, bd=7)
HygienePriceEntry.grid(row=0, column=1, pady=3, padx=10, sticky ='w')


GroceryPriceLabel=Label(BillMenuFrame, text='Grocery Price', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
GroceryPriceLabel.grid(row=1, column=0)
GroceryPriceEntry=Entry(BillMenuFrame, font= ('times new roman', 15, 'bold'),
                width=20, bd=7)
GroceryPriceEntry.grid(row=1, column=1, pady=3, padx=10, sticky ='w')


DrinksPriceLabel=Label(BillMenuFrame, text='Drinks Price', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
DrinksPriceLabel.grid(row=2, column=0)
DrinksPriceEntry=Entry(BillMenuFrame, font= ('times new roman', 15, 'bold'),
                width=20, bd=7)
DrinksPriceEntry.grid(row=2, column=1, pady=3, padx=10, sticky ='w')


HygieneTaxLabel=Label(BillMenuFrame, text='HygieneTax', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
HygieneTaxLabel.grid(row=0, column=2)
HygieneTaxEntry=Entry(BillMenuFrame, font= ('times new roman', 15, 'bold'),
                width=20, bd=7)
HygieneTaxEntry.grid(row=0, column=3, pady=3, padx=10, sticky ='w')


GroceryTaxLabel=Label(BillMenuFrame, text='Grocery Tax', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
GroceryTaxLabel.grid(row=1, column=2)
GroceryTaxEntry=Entry(BillMenuFrame, font= ('times new roman', 15, 'bold'),
                width=20, bd=7)
GroceryTaxEntry.grid(row=1, column=3, pady=3, padx=10, sticky ='w')


DrinksTaxLabel=Label(BillMenuFrame, text='Drinks Tax', font=('copper', 13, 'bold'),
                bg='navyblue', fg='white')
DrinksTaxLabel.grid(row=2, column=2)
DrinksTaxEntry=Entry(BillMenuFrame, font= ('times new roman', 15, 'bold'),
                width=20, bd=7)
DrinksTaxEntry.grid(row=2, column=3, pady=5, padx=10, sticky ='w')

ButtonFrame=Frame(BillMenuFrame, bd=10, relief=GROOVE)
ButtonFrame.grid(row=0, column=4)

TotalButton=Button(ButtonFrame, text='Total', font=('arial black', 10, 'bold'),
                   bg='orange', fg='white', bd=5, width=5, padx=25, command=total)
TotalButton.grid(row=0, column=0)

BillButton=Button(ButtonFrame, text='Bill', font=('arial black', 10, 'bold'),
                   bg='black', fg='white', bd=5, width=5, padx=25, command=bill_area)
BillButton.grid(row=0, column=1)

EmailButton=Button(ButtonFrame, text='Email', font=('arial black', 10, 'bold'),
                   bg='black', fg='white', bd=5, width=5, padx=25,command=Send_Email)
EmailButton.grid(row=0, column=2)

PrintButton=Button(ButtonFrame, text='Print', font=('arial black', 10, 'bold'),
                   bg='green', fg='white', bd=5, width=5, padx=25,command=print_bill)
PrintButton.grid(row=0, column=3)

ClearButton=Button(ButtonFrame, text='Clear', font=('arial black', 10, 'bold'),
                   bg='red', fg='white', bd=5, width=5, padx=25,command=clear)
ClearButton.grid(row=0, column=4)
root.mainloop()
