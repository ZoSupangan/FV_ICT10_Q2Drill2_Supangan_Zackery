from pyscript import document, display

grade_7 = {"Diego concengo", "Jane doe", "Kyle tan"}
grade_8 = {"Willow Alien", "Chris Pratt", "Rafael Ichigo"}
grade_9 = {"Milo Bear", "Freddy Fazbear", "Madeline McCarthy"}
grade_10 = {"Kenny Park", "Ren Kim", "Lily Evans"}

# Combine all grade sets into an master set 
all_members = grade_7 | grade_8 | grade_9 | grade_10

def add_member_function(event):
    # use of the global master set variable
    global all_members

    # get values from the input text boxes in the HTML
    first_name = document.getElementById("fname").value
    last_name = document.getElementById("lname").value

    # make a set containing the new member's full name into list
    new_member_set = {f"{first_name} {last_name}"}

    # Using (|) to add the new member set into the master set
    all_members = all_members | new_member_set

    #  use in list
    members_list = "<br>".join(sorted(all_members))
    total_members = len(all_members)

    # Output the full list and total members as HTML using an f-string i guess
    result_html = f"""
    <h3>Total Number of Members: {total_members}</h3>
    <p><b>Full List of All Members:</b><br>{members_list}</p>
    """
    
   
    document.getElementById("output").innerHTML = result_html