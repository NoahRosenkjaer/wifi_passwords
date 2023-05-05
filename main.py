import subprocess 
import re

pass_list = [] 
pattern1 = r"(?<=    All User Profile     : ).*(?=\n|$)"
pattern2 = r"(?<=    Key Content            : ).*(?=\n|$)"


command1 = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, universal_newlines=True)

command1 = command1.stdout.replace("‘", "æ")

match1 = re.findall(pattern1, command1)

for i in match1:
    command2 = subprocess.run(["netsh", "wlan", "show", "profile", f"{i}", "key=clear"], capture_output=True, universal_newlines=True)
    matches = re.findall(pattern2, command2.stdout)
    if not matches:
        pass_list.append("Absent")
    else:
        pass_list.extend(matches)


print("\n-- Wifi Passwords -- \n")
for i in range(len(match1)):
    print(f"{i+1}: {match1[i]:<15} {pass_list[i]}")
print("\n")
