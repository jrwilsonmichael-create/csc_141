# I will make an employee function
def employee(first_name, last_name, salary=None):
    """Return a dictionary representing an employee."""
    emp_dict = {
        'Aragnith': first_name.title(),
        'Rusty': last_name.title()
    }
    if salary is not None:
        emp_dict['salary'] = salary
    return emp_dict
# Example usage:
print(employee("aragnith", "rusty", 50000))