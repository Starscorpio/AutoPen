import subprocess

hostname = input("Enter name of host: ")
ip = input("Enter your IP: ")

print("\n")
print("\033[1;35;40m                                                    _____ ")
print("\033[1;35;40m             |\     |  |\      /|        / \       |     |")
print("\033[1;35;40m             | \    |  | \    / |       /   \      |     |")
print("\033[1;35;40m             |  \   |  |  \  /  |      /     \     |_____|")
print("\033[1;35;40m             |   \  |  |   \/   |     /_______\    |")
print("\033[1;35;40m             |    \ |  |        |    /         \   |")
print("\033[1;35;40m             |     \|  |        |   /           \  |")

print("\n			Made by: Vedant Tare                  ")

print("\033[1;33;40m")
print("\n\n\n Let's run nmap!!!")
tool_2 = subprocess.run(["sudo", "nmap", "-p", "80", "-oA", "nmap/%s" % hostname, "%s" % ip])
output=subprocess.check_output(["sudo", "nmap", "-p", "80", "-oA", "nmap/%s" % hostname, "%s" % ip], universal_newlines=True)
if "80/tcp open" in output:
	directory_enum = input("\nAs port 80 is open, which tool do you want to use to bust those directories [dirb/gobuster]:  ")
	if directory_enum == "dirb":
		print("\n")
		print("Let's get some directories!!!")
		dirb = subprocess.run(["dirb", "http://%s/" % ip, "/usr/share/wordlists/dirb/common.txt"])
	elif directory_enum == "gobuster":
		print("\n")
		gobuster = subprocess.run(["gobuster", "dir", "-u", "http://%s" %ip, "-w", "/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt"])
elif "80/tcp closed" in output:
	print("\n")
	print("Looks like port 80 is closed")
elif "21/tcp open" in output:
	print("\n")
	print("Let's get those file")
	tool_3 = subprocess.run(["ftp", "%s" % ip])
elif "22/tcp open" in output:
	print("\n")
	ssh = input("Do you want to bruteforce ssh creds using hydra: ")
elif "139/tcp open" in output:
	print("\n")
	print("As you can see port 139 open(smb), running smbclient to list shares")
	smb = subprocess.run(["smbclient", "-L", "%s" % ip])
	output_smb = subprocess.check_output(["smbclient", "-L", "%s" % ip], universal_newlines=True)
	smb_1 = input("Do you want to run enum4linux to enumerate samba more [Y/n]: ")
	if smb_1 == "Y":
		print("\n")
		print("Enum4linux")
		tool_6 = subprocess.run(["enum4linux", "-a", "%s" % ip])
elif "443/tcp open" in output:
	print("\n")
	ssl = input("Do you want to run the same tools as we did for http  [Y/n]: ")
elif "135/tcp open" in output:
	print("\n")
	rpc = input("Since rpc port is open lets run rpclient")
	tool_5 = subprocess.run(["rpcclient", "-a", "%s" % ip])

#else
#print("\n\n")
#print("\033[1;31;40m")
#print("Looks like our 1000 normal ports are closed")

full_scan = input("Do you want to run a full port scan and look for other open ports: [Y/n] ")
if full_scan == "Y":
	print("\n")
	nmap_full = subprocess.run(["sudo", "nmap", "-sC", "-sV", "-p-", "-oA", "nmap/%sfull" % hostname,  "%s" % ip])
	output_full = subprocess.check_output(["sudo", "nmap", "-sC", "-sV", "-p-", "-oA", "nmap/%sfull" % hostname,  "%s" % ip], universal_newlines=True)
elif full_scan == "n":
	udp = input("Do you want to run a udp scan: [Y/n]")
	if udp == "Y":
		print("\n")
		nmap_udp = subprocess.run(["sudo", "nmap", "-sU", "-O", "-oA", "nmap/%sudp" % hostname, "%s" % ip])
		output_udp = subprocess.check_output(["sudo", "nmap", "-sU", "-O", "-oA", "nmap/%sudp" % hostname, "%s" % ip], universal_newlines=True)
	elif udp == "n":
		print("\n")
		additional = input("Do you want to run additonal nmap scripts on the target: Y/n ")
		if additional == "Y":
			script = input("Which script do you want to run: ")
			tool_7 = subprocess.run(["sudo", "nmap", "--script=" % script, "%s" % ip])
		elif additional == "n":
			tools = input("Which other tool do you want to run?")
