from HRCHATBOT import *
dataframe=pd.read_csv("C:\\Users\Pankaj\Desktop\ChatBot\HRDataset_v14.csv")
class Functionalities:
    def leaves(self,ID):
        empid= int(ID)
        absences= dataframe.loc[dataframe['EmpID']==empid,'Absences'].iloc[0]
        leaves= 25-absences
        return " You have "+str(leaves)+" Leaves Left"
    

    def payslip(self,ID):
        empid= int(ID)
        salary= dataframe.loc[dataframe['EmpID']==empid,'Salary'].iloc[0]
        inhand= 12*salary
        funds= int(0.15*inhand)
        inhand_with_funds= funds + inhand
        if inhand_with_funds+0.2*inhand_with_funds>=500000 and inhand_with_funds+0.2*inhand_with_funds<=1000000:
            year_tax=int(0.2*inhand_with_funds)
            ctc= int(inhand_with_funds+0.2*inhand_with_funds)
        elif inhand_with_funds+0.3*inhand_with_funds>1000000:
            year_tax=int( 0.3*inhand_with_funds)
            ctc=int(inhand_with_funds+0.3*inhand_with_funds)
        else:
            year_tax=0
            ctc=inhand_with_funds
        return ("Your Salary status :\n  Inhand Salary:"+str(inhand)+"\n  Saving fund: "+str(funds)+"\n  Yearly Tax deduction: "+str(year_tax)+"\n  Cost to company: "+str(ctc))
    
    def reim_bill(self):
        return "Please upload your Bill documents in "+"<a href="+"https://docs.google.com/forms/d/e/1FAIpQLScirGzuTU_Y0GHR2j_K-ieTqkf1lnX-bU6KHz74_PA5bpyiXg/viewform?usp=sf_link"+" target="+"_blank" +" rel="+"noopener noreferrer"+">Bill Reimbursement</a>" 
    def reim_health(self):
        return "Please upload your Bill documents in "+"<a href="+"https://docs.google.com/forms/d/e/1FAIpQLSd2wA2LgoxvdxF4PZGGzr8JVeGRAK4UCqYC4uioViJFfd4JnA/viewform?usp=sf_link"+" target="+"_blank" +" rel="+"noopener noreferrer"+">Health Reimbursement</a>"
    def reim_travel(self):
        return "Please upload your Bill documents in "+"<a href="+"https://docs.google.com/forms/d/e/1FAIpQLSeZOdwSta9R-WsGmyeHW1zzCkLZBAjclbjy8FyesUo_twTTdw/viewform?usp=sf_link"+" target="+"_blank" +" rel="+"noopener noreferrer"+">Travel Reimbursement</a>"
def validateinput(string):
    string=string.split()
    validateset={'reimburs', 'amount', 'leav', 'cost', 'expens', 'medic', 
                 'bill', 'travel', 'insur', 'ticket', 'cab', 'health', 
                 'hospit', 'hospitalis', 'hotel', 'pass', 'pay', 'surgeri',
                 'busi', 'marriag', 'metro', 'mobil', 'money', 'offic', 
                 'oper', 'phone', 'train', 'trip', 'vacat', 'board', 
                 'bonu', 'break', 'ctc','earphon', 'payslip', 'salari', 
                 'spent', 'adapt', 'airport', 'cancer', 'charger', 'diseas',
                 'employ', 'fund', 'guest', 'holiday', 'hra', 'includ', 
                 'incom', 'incur', 'internet', 'matern', 'power', 'price', 
                 'provid', 'sick', 'suffer', 'tax','year', 'book', 'card', 
                 'chronic', 'client', 'data', 'dispensari', 'doctor', 
                 'electr', 'expenc' , 'gross', 'headphon', 'heath', 
                 'home', 'increment', 'job', 'kindli', 'leaveit', 
                 'lpa', 'net', 'pack', 'patern', 'payment', 'percentag', 
                 'sabbat', 'slip', 'studi', 'tire', 'total', 'uber', 
                 'variabl', 'work', 'absenc', 'acut', 'annual','basic', 
                 'bereav', 'broadband', 'covid', 'daili', 'diagons', 'drive',
                 'dth', 'emerg', 'employe', 'entitl', 'equip', 'exempt', 
                 'expense', 'flight', 'fuel', 'gym', 'halfday', 'higher', 
                 'highli', 'hometown', 'incash', 'institut', 'instruct', 
                 'invoic', 'laptop', 'leavei','loan', 'locat', 'lodg', 
                 'master', 'mic', 'mileag', 'notic', 'ola', 'overtim', 
                 'paid','printer', 'procedur', 'profession', 'rate', 
                 'recharg', 'rent', 'repay', 'reserv', 'tablet', 
                 'telephon', 'unwel', 'wifi'}
    counter=0
    for word in string:
        if word in validateset:
            counter+=1
    if counter>=1:
        return False
    else:
        return True
def in_func(textValue,empID):
    X=textValue
    X=textcleaning(X)
    X=textstemming(X)
    X=[X]
    print(X[0])
    if validateinput(X[0]):
        return ("Ahh didn't get that")
    dfTest=pd.DataFrame(X,columns=['Test'])
    X=cv.transform(dfTest['Test'])
    ans=clf.predict(X)
    print(ans)
    function=Functionalities()
    if ans[0]=='leaves':
        val=function.leaves(empID)
        return val
    elif ans[0]=='Payslip':
        salaries=function.payslip(empID)
        return salaries
    elif ans[0]=='reimbursement_bill':
        re_bill=function.reim_bill()
        return re_bill
    elif ans[0]=='reimbursement_health':
        re_health = function.reim_health()
        return re_health
    elif ans[0]=='reimbursement_travel':
        re_travel = function.reim_travel()        
        return re_travel