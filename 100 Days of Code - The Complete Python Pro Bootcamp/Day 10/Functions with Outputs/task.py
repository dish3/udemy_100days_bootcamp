def format_name(first_name, last_name):
    return(f"{first_name} {last_name}")
a=input("Enter your first name: ")
b=input("Enter your last name: ")
formatted_name = format_name(a.title(), b.title())
print(formatted_name)




