def Employee_Info():
    d = {}
    d['Employee Name'] = input("Enter Employee Name : ")
    d['Employee Id'] = input("Enter Employee Id : ")
    d['Designation'] = input("Enter Employee Designation : ")
    d['Department'] = input("Enter Employee Department : ")
    d['DOJ'] = input("Enter Employee Date Of Joining : ")
    d['ESI Number'] = input("Enter Employee ESI Number : ")
    d['PF Number'] = input("Enter Employee PF Number : ")
    d['UAN'] = input("Enter Employee UAN Number : ")
    d['Work Location'] = input("Enter Employee Work Location : ")
    d['Bank A/c No'] = input("Enter Employee Bank A/c No : ")
    return d


def Employee_HR_Info():
    d = {}
    d['CTC'] = int(input("Enter Employee CTC  : "))
    d['LOP'] = int(input("Enter Employee LOP Days : "))
    d['Worked Days'] = int(input("Enter Employee Worked Days : "))
    return d


def calc_earnings(ctc):
    basic = (50 / 100) * ctc
    hra = (50 / 100) * basic
    medical = 1250
    conveyance = 800
    lta = (8.33 / 100) * basic
    spl_allowance = ctc - (basic + hra + medical + conveyance + lta)
    pf = (12 / 100) * basic
    total = basic + hra + medical + conveyance + lta + spl_allowance

    d = {}
    d['basic'] = basic
    d['hra'] = hra
    d['medical'] = medical
    d['conveyance'] = conveyance
    d['lta'] = lta
    d['spl_allowance'] = spl_allowance
    d['pf'] = pf
    d['total'] = total
    return d


def calc_income_tax(tax_slab):
    tax = 0
    if (tax_slab > 250000 and tax_slab <= 500000):
        tax = (5 / 100) * (tax_slab - 250000) + (4 / 100) * (tax_slab - 250000)
    elif (tax_slab > 500000 and tax_slab <= 1000000):
        tax = 12500 + (20 / 100) * (tax_slab - 500000) + (4 / 100) * (tax_slab - 500000)
    elif (tax_slab > 1000000):
        tax = 112500 + (30 / 100) * (tax_slab - 1000000) + (4 / 100) * (tax_slab - 1000000)

    return tax


def calc_salary(ctc, lop, tax):
    earnings = calc_earnings(ctc)
    monthly_earnings = earnings['total'] / 12
    day_earnings = monthly_earnings / 30
    net_pay = monthly_earnings - ((day_earnings * lop) + (tax / 12))
    return net_pay


def display_report(emp_input, salary, net_pay):
    print('-' * 30)
    print(f'Employee Name  :  {emp_input["Employee Name"]}')
    print(f'Employee Id  :  {emp_input["Employee Id"]}')
    print(f'Designation  :  {emp_input["Designation"]}')
    print(f'Employee Id  :  {emp_input["Employee Id"]}')
    print(f'Department  :  {emp_input["Department"]}')
    print(f'Date Of Joining  :  {emp_input["DOJ"]}')
    print(f'ESI Number  :  {emp_input["ESI Number"]}')
    print(f'PF Number  :  {emp_input["PF Number"]}')
    print(f'UAN  :  {emp_input["UAN"]}')
    print(f'Work Location  :  {emp_input["Work Location"]}')
    print(f'Bank A/c No  :  {emp_input["Bank A/c No"]}')
    print('-' * 30)
    print(f'Basic  :  {salary["basic"] / 12}')
    print(f'HRA  :  {salary["hra"] / 12}')
    print(f'Medical  :  {salary["medical"] / 12}')
    print(f'Conveyance  :  {salary["conveyance"] / 12}')
    print(f'LTA  :  {salary["lta"] / 12}')
    print(f'Special Allowance  :  {salary["spl_allowance"] / 12}')
    print(f'Total Earnings  :  {salary["total"] / 12}')
    print(f'Income Tax  :  {calc_income_tax(salary["total"])}')
    print('-' * 30)
    print(f'Total Net Pay  :  {net_pay}')


def main():
    emp_input = Employee_Info()
    emp_hr_input = Employee_HR_Info()
    earnings = calc_earnings(emp_hr_input['CTC'])
    tax = calc_income_tax(earnings['total'])
    net_pay = calc_salary(emp_hr_input['CTC'], emp_hr_input['LOP'], tax)
    display_report(emp_input, earnings, net_pay)


main()