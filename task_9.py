def year_annuity_payment(loan, percent, years_quantity):
	percent = percent / 100
	coef = percent * (1 + percent) ** years_quantity / ((1 + percent) ** years_quantity - 1)
	payment = round(loan * coef, 2)
	total_payment = loan * coef * years_quantity
	year = 0
	
	while years_quantity > 0:
		if year == 3:
			add_years_quantity = int(input('\nНа сколько лет продлевается договор: '))
			add_percent = int(input('На сколько увеличивается процент: '))
			add_percent = add_percent / 100
			years_quantity = years_quantity + add_years_quantity
			percent = percent + add_percent
			coef = percent * (1 + percent) ** years_quantity / ((1 + percent) ** years_quantity - 1)
			payment = round(loan * coef, 2)
		year_debt = loan * percent
		year_loan_body = payment - year_debt
		loan = loan - year_loan_body
		year += 1
		print('\nИдёт ', year, 'й год платежей', end = '')
		print('\nУплачено процентов за год:', round(year_debt, 2))
		print('Погашённое тело долга за год:', round(year_loan_body, 2))
		print('Оставшееся тело долга', round(loan, 2))
		years_quantity -= 1
	print('Всего уплачено:', round(total_payment, 2))
		
	
loan_sum = input('Введите сумму кредита: ')
loan_sum = float(loan_sum.replace(',', '.'))
loan_years = int(input('На сколько лет берётся кредит: '))
loan_percent = int(input('Какой процент годовых: '))
 
year_annuity_payment(loan_sum, loan_percent, loan_years)
#просмотр изменений
#для коммита в другой ветке
	
	
	
	
	
	
	
	
	
	
	
	
	
