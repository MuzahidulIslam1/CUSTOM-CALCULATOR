import datetime
current_date = datetime.date.today()
formatted_date = current_date.strftime("%d-%m-%Y")

import tkinter as tk
from tkinter import messagebox

class ReturnCalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("RETURN CALCULATOR")
        master.geometry("900x1200")

        self.packets = [ "SWEET 275 G", "COCONUT 275 G", "SALTED 275 G", "NANKATA 275 G",
            "FANCY LINE 130 G", "FANCY LOOSE 160 G", "NANKATA 140 G LINE",
            "BUTTER 275 G", "JEERA SALT 275 G", "FANCY LINE 250 G",
            "FANCY LINE 320 G", "PUFF", "PACKET CAKE", "SWISS ROLL",
            "NAW CAKE PKT", "KATA", "MINI KATA(COUNTER)",
            "SPL COOKIES BOX 300 G", "DRY CAKE BOX", "PREMIUM COOKIES 300 G",
            "SPL CONTAINER 200 G", "MACROLL(COCONUT MACRON)","CREAM CAKER(CONTAINER) 170 G",
            "FANCY BOX 270G", "HATIM SPL TEMA","BATI","S COOKIES","CREAM CAKER BOX","NAGIN BOX",
            "MINI KATA","NANKATA PREMIUM BOX","JEERA SALT BOX"]

        self.prices = [38, 38, 38, 38, 15, 20, 16, 38, 38, 35, 45, 38, 38, 48, 40, 17.06,
            35, 48, 48, 58, 44, 58, 38, 38, 35,72,23,48,44,26.66,52,42]
        self.bons =["BREAD","BIG BREAD","LOAF","ITALY BON","NEW BON 20"]
        self.bonprice=[8,16,16,8,15]
        self.bhujia=["500g","100g","50g","Tupula","Nimki 150g","Mix Box","Nimki 70g","Polo"]
        self.bhujia_price=[65,150,75,35,28,38,14,12]

        self.packet_entries = []
        self.return_total = 0
        self.total_sales = 0
        self.less_amount = 0
        
        self.bon_entries= []
        self.bon_return= 0
        self.bon_total =0
        
        self.bhujia_entries= []
        self.bhujia_return= 0
        self.bhujia_total =0
        # Add Total label and entry
        self.total_label = tk.Label(master, text="Enter Total:")
        self.total_label.grid(row=0, column=0)
        self.total_entry = tk.Entry(master)
        self.total_entry.grid(row=0, column=1)
         # Add Total label for bon and entry
        self.bon_total_label = tk.Label(master, text="Enter Bon Total:")
        self.bon_total_label.grid(row=0, column=6)
        self.bon_total_entry = tk.Entry(master)
        self.bon_total_entry.grid(row=0, column=7)
        # Add Total label for bhujia and entry
        self.bhujia_total_label = tk.Label(master, text="Enter Bhujia Total:")
        self.bhujia_total_label.grid(row=0, column=4)
        self.bhujia_total_entry = tk.Entry(master)
        self.bhujia_total_entry.grid(row=0, column=5)
        # Add Total Counter label and entry
        self.counter_total_label = tk.Label(master, text="Enter Counter Total:")
        self.counter_total_label.grid(row=12, column=4)
        self.counter_total_entry = tk.Entry(master)
        self.counter_total_entry.grid(row=12, column=5)
        # Add Previous balance label and entry
        self.previous_label = tk.Label(master, text="Enter Previous Balance:")
        self.previous_label.grid(row=14, column=4)
        self.previous_entry = tk.Entry(master)
        self.previous_entry.grid(row=14, column=5)
         # Add Amount given label and entry
        self.amount_given_label = tk.Label(master, text="Enter Amount given to bakery today:")
        self.amount_given_label.grid(row=16, column=4)
        self.amount_given_entry = tk.Entry(master)
        self.amount_given_entry.grid(row=16, column=5)
        # Add packet entries for each product
        for i in range(len(self.packets)):
            label = tk.Label(master, text=self.packets[i])
            label.grid(row=i+1, column=0)
            packet_entry = tk.Entry(master)
            packet_entry.insert(0, 0)  # Set the initial value to 0
            packet_entry.grid(row=i+1, column=1)
            self.packet_entries.append(packet_entry)
         # Add bon entries for each product
        for i in range(len(self.bons)):
            label1 = tk.Label(master, text=self.bons[i])
            label1.grid(row=i+1, column=6)
            bon_entry = tk.Entry(master)
            bon_entry.insert(0, 0)  # Set the initial value to 0
            bon_entry.grid(row=i+1, column=7)
            self.bon_entries.append(bon_entry)
        # Add bon entries for each product
        for i in range(len(self.bhujia)):
            label2 = tk.Label(master, text=self.bhujia[i])
            label2.grid(row=i+1, column=4)
            bhujia_entry = tk.Entry(master)
            bhujia_entry.insert(0, 0)  # Set the initial value to 0
            bhujia_entry.grid(row=i+1, column=5)
            self.bhujia_entries.append(bhujia_entry)

        # Add Damaged Goods entry box
        self.damaged_goods_label = tk.Label(master, text="Enter Damaged Goods:")
        self.damaged_goods_label.grid(row=len(self.packets)+1, column=0)
        self.damaged_goods_entry = tk.Entry(master)
        self.damaged_goods_entry.grid(row=len(self.packets)+1, column=1)


        # Add Return Total button
        self.return_total_button = tk.Button(master, text="Calculate Return Total", command=self.calculate_return_total)
        self.return_total_button.grid(row=35, column=0)
        
        
        # Add Return Bon  button
        self.return_total_bon_button = tk.Button(master, text="Calculate Bon Return Total", command=self.calculate_return_bon_total)
        self.return_total_bon_button.grid(row=7, column=6)
        # Add Return Bhujia  button
        self.return_total_bhujia_button = tk.Button(master, text="Calculate Bhujia Return Total", command=self.calculate_return_bhujia_total)
        self.return_total_bhujia_button.grid(row=9, column=4)


        # Add Less label and entry
        self.less_label = tk.Label(master, text="Enter Less:")
        self.less_label.grid(row=35, column=4)
        self.less_entry = tk.Entry(master)
        self.less_entry.grid(row=35, column=5)

        # Add Total Sales button
        self.total_sales_button = tk.Button(master, text="Calculate Total Sales", command=self.calculate_sales_total)
        self.total_sales_button.grid(row=36 , column=1)
        
        # Add Total Sales Bon button
        self.total_sales_bon_button = tk.Button(master, text="Calculate Bon Total Sales", command=self.calculate_sales_bon_total)
        self.total_sales_bon_button.grid(row=8 , column=6)
        # Add Total Sales Bhujia button
        self.total_sales_bhujia_button = tk.Button(master, text="Calculate Bhujia Total Sales", command=self.calculate_sales_bhujia_total)
        self.total_sales_bhujia_button.grid(row=10 , column=4)

        # Add My Payment button
        self.payment_button = tk.Button(master, text="My Payment", command=self.calculate_payment)
        self.payment_button.grid(row=36, column=4)
         # Add My Payment bhujia button
        self.payment_bhujia_button = tk.Button(master, text="My Payment Bhujia", command=self.calculate_bhujia_payment)
        self.payment_bhujia_button.grid(row=9, column=5)
        # Add Total Final Calculation given  button
        self.final_button = tk.Button(master, text="Final Calculations ", command=self.calculate_final_total)
        self.final_button.grid(row=18, column=4)
        # Add Counter 3% button
        self.counter_button = tk.Button(master, text="Calculate 3% Counter", command=self.counter3)
        self.counter_button.grid(row=12, column=6)

        # Add Print button
        self.print_button = tk.Button(master, text="Print Results", command=self.print_results)
        self.print_button.grid(row=36, column=5)
        

    def calculate_return_total(self):
        self.return_total = 0
        for i in range(len(self.packet_entries)):
            try:
                packets = int(self.packet_entries[i].get())
            except ValueError:
                packets = 0
            self.return_total += packets * self.prices[i] 
            self.return_total1 = self.return_total + int(self.damaged_goods_entry.get())
        print(f"Return Total: Rs{self.return_total1  : .2f}")
    def calculate_return_bon_total(self):
        self.bon_return = 0
        for i in range(len(self.bon_entries)):
            try:
                packets = int(self.bon_entries[i].get())
            except ValueError:
                bons = 0
            self.bon_return += packets * self.bonprice[i] 
        print(f"Return bon Total: Rs{self.bon_return  : .2f}")

    def calculate_return_bhujia_total(self):
        self.bhujia_return = 0
        for i in range(len(self.bhujia_entries)):
            try:
                packets = int(self.bhujia_entries[i].get())
            except ValueError:
                bhujia = 0
            self.bhujia_return += packets * self.bhujia_price[i] 

        print(f"Return bhujia Total: Rs{self.bhujia_return  : .2f}")

        
    def calculate_sales_total(self):
        self.total_sales = float(self.total_entry.get())
        self.less_amount = float(self.less_entry.get())
        self.total_sales1 = self.total_sales - self.return_total1
        print(f"Total Sales : Rs{self.total_sales1: .2f}")
        print(f"Total Sales minus less: Rs{(self.total_sales1 - self.less_amount):.2f}")
    def calculate_sales_bon_total(self):
        self.bon_total = float(self.bon_total_entry.get())
        self.bon_total_sales = self.bon_total - self.bon_return
        print(f"Total Bon Sales : Rs{self.bon_total_sales: .2f}")
    def calculate_sales_bhujia_total(self):
        self.bhujia_total = float(self.bhujia_total_entry.get())
      
        self.bhujia_total_sales = self.bhujia_total - self.bhujia_return
        print(f"Total Bhujia Sales : Rs{self.bhujia_total_sales: .2f}")
    

    def calculate_payment(self):
        self.payment = ((self.total_sales1 - self.less_amount)-((self.total_sales1 - self.less_amount) * 0.03) - 150)
        print(f"My Payment: Rs{self.payment :.2f}")
    def calculate_bhujia_payment(self):
        self.bhujia_payment = self.bhujia_total_sales-self.bhujia_total_sales * 0.03
        print(f"My Bhujia Payment: Rs{self.bhujia_payment :.2f}")
    

    
    def counter3(self):
        self.counter=float(self.counter_total_entry.get())-float(self.counter_total_entry.get())*.03
        print(f'Counter with commisssion: Rs{ self.counter:.2f}')
        
    def calculate_final_total(self):
        self.final_payment = self.payment+ self.bon_total_sales + self.bhujia_payment+ self.counter
        self.final_payment1= (self.final_payment + float(self.previous_entry.get())- float(self.amount_given_entry.get()))
        print(f"My Final Payment: Rs{self.final_payment1 :.2f}")

    
    def print_results(self):
        
    
        results = ""
        results += f"Today's Date : {formatted_date}"
        results += f"RETURN GOODS:\n"
        for i in range(len(self.packet_entries)):
            try:
                packets = int(self.packet_entries[i].get())
            except ValueError:
                packets = 0
            if packets != 0:
                results += f"{self.packets[i]}: {packets} x {self.prices[i]} = {packets * self.prices[i]}\n"

        try:
            results += f"Total Return         : Rs{self.return_total1 :.2f}\n\n"
        except ValueError:
            self.return_total = 0
        try:
            self.less_amount = int(self.less_entry.get())
            total_sales_less = (self.total_sales - self.return_total1) - self.less_amount
            #results += f"Total Sales minus less: Rs{(self.total_sales - self.return_total)} - {self.less_amount} = Rs{total_sales_less}\n"
        except ValueError:
            self.less_amount = 0

        payment_before_deductions = (self.total_sales1 - self.less_amount)-((self.total_sales1 - self.less_amount) * 0.03)
        payment_after_deductions = self.payment
        results += f"My Payment Calculation:\n"
        results += f"Total Amount from backery : Rs{self.total_sales:.2f}\n"
        results += f"Total Amount minus Returns : Rs{self.total_sales - self.return_total1:.2f}\n"
        results += f"Less : Rs{self.less_amount}\n"
        results += f"Total Sales minus less : Rs{self.total_sales1 :.2f} - Rs{self.less_amount:.2f} = Rs{total_sales_less:.2f}\n"
        results += f"Payment with commission  : Rs{total_sales_less: .2f} - (Rs{total_sales_less:.2f}*.03) = Rs{payment_before_deductions:.2f}\n"
        results += f"Payment after driver khuraki: Rs{payment_before_deductions} - 150 = Rs{payment_after_deductions:.2f}\n\n"

        results += f"RETURN BONS :\n"
        for i in range(len(self.bon_entries)):
            try:
                bons = int(self.bon_entries[i].get())
            except ValueError:
                bons = 0
            if bons != 0:
                results += f"{self.bons[i]}: {bons} x {self.bonprice[i]} = {bons * self.bonprice[i]}\n"

        try:
            results += f"Total Return Bon       : Rs{self.bon_return :.2f}\n"
        except ValueError:
            self.return_total = 0
        try:
           
            total__bon_sales = (self.bon_total - self.bon_return) 
            results += f"Total Sales Bon: Rs{(self.bon_total - self.bon_return)} = Rs{self.bon_total_sales}\n\n"
        except ValueError:
            pass
        
        results += f"RETURN Bhujia :\n"
        for i in range(len(self.bhujia_entries)):
            try:
                bhujia = int(self.bhujia_entries[i].get())
            except ValueError:
                bhujia = 0
            if bhujia != 0:
                results += f"{self.bhujia[i]}: {bhujia} x {self.bhujia_price[i]} = {bhujia * self.bhujia_price[i]}\n"

        try:
            results += f"Total Return Bohujia      : Rs{self.bhujia_return :.2f}\n\n"
        except ValueError:
            self.return_total = 0
        try:
           
            total__bhujia_sales = (self.bhujia_total - self.bhujia_return) 
            results += f"Total Sales Bhujia: Rs{self.bhujia_total:.2f} - Rs{self.bhujia_return:.2f} = Rs{total__bhujia_sales:.2f}\n"
        except ValueError:
            pass
        
        results += f"Payment with commission bhujia  : Rs{self.bhujia_total_sales} - (Rs{self.bhujia_total_sales:.2f}*.03) = Rs{self.bhujia_payment:.2f}\n"
        results += f"\n Total Counter Sales   : Rs{float(self.counter_total_entry.get())}\n"
        results += f"\n  Counter Sales minus 3%  :Rs{float(self.counter_total_entry.get())} - Rs{float(self.counter_total_entry.get())*.03}=Rs{self.counter:.2f}\n"
        results += f"\n FINAL CALCULATIONS   : (Rs {self.payment:.2f}+ Rs{self.bon_total_sales:.2f} + Rs{self.bhujia_payment:.2f}+ Rs{self.counter}+Rs{float(self.previous_entry.get())})-Rs{ float(self.amount_given_entry.get())}=Rs{self.final_payment1:.2f}\n"
        
        
        
        
        messagebox.showinfo("Results", results)


root = tk.Tk()
my_app = ReturnCalculatorApp(root)
root.mainloop()
