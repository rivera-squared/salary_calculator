def get_biweekly_salary(salary, med_costs = 1055.02):

    retention_rates = [.15, .18, .20, .25, .30]
# =============================================================================
#     med_costs = 1055.02
# =============================================================================
    
    print("\nGross year salary ${}".format(salary))
    print("Estimated medical costs ${} \n".format(med_costs))
    for rate in retention_rates:
        new_salary = salary * (1- rate)
        biweekly_salary = round(((new_salary / 12) - med_costs) / 2,2)
        print("Estimated net salary (bi-weekly) after {}% retention rate: ${}".format(rate*100, biweekly_salary))
        
# =============================================================================
# get_biweekly_salary(124000)        
# =============================================================================

salaries = [124000, 126000, 128000, 130000]
for salary in salaries:
    get_biweekly_salary(salary)