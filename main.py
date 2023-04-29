import subprocess 
import re

pass_list = []
# regex patterns 
pattern1 = r"(?<=    All User Profile     : ).*(?=\n|$)"
pattern2 = r"(?<=    Key Content            : ).*(?=\n|$)"

# Runs the command > netsh wlan show profiles
command1 = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, universal_newlines=True)

# replace ‘ with æ
command1 = command1.stdout.replace("‘", "æ")

# Matches every occurrence in the given string
match1 = re.findall(pattern1, command1)

for i in match1:
    # runs the command > netsh wlan show profile [profile name] key=clear
    command2 = subprocess.run(["netsh", "wlan", "show", "profile", f"{i}", "key=clear"], capture_output=True, universal_newlines=True)

    # Matches every occurrence in the given string
    match2 = re.findall(pattern2, command2.stdout)
    
    # passes regex matches into list
    pass_list.append(match2)

# extracts alle the sublists from the list into a list
list = [item for sublist in pass_list for item in sublist]

# output
print("\n-- Wifi Passwords -- \n")
for i in range(len(list)):
    print(f"{i+1}: {match1[i]}: {list[i]}")

print("\n")