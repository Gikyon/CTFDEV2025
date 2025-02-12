# How Good are You?

<p>Hey Intern, I see from your resume that you’re a whiz at analysis. Well, here’s your first real test: we’ve just received an alert about a potential malware download. Your task is to confirm if it’s true and dig deeper to figure out exactly what the payload is. Time to put those skills to work!<p>

---
[Goal](#goal)
[Development](#development)
[Solution](#solution)

## Goal:

The purpose of this challenge is for the participants to learn how to use **wireshark** and any **hex-editor**.

## Development:

A little background story: During my second CTF participation, I met a sponsor specializing in **malware analysis**. At the time, I was unsure about which cybersecurity path to pursue (to be honest, I still am). He helped me break down different career paths and how to approach them. One example he shared was the journey to becoming a malware analyst.

When I got home, I started learning the topics he suggested. The first thing I explored was how to create a **trojan**, which introduced me to the concept of **code caves**. That discovery inspired me to create this challenge.

Okay now, let's get into it:

**The first step** is to create an executable, but I wanted it to also provide hints to participants about the code cave concept. To achieve this, I decided to use the WinAPI to display a Windows alert message box. [(source for the code below)](https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxa)

```
#include <windows.h>

int main(){
    MessageBoxA(
        NULL,
        "I AM INSIDE A CAVE!!!",
        "ERROR",
        MB_OK | MB_ICONERROR
    );

    return 0;
} \\ you can download the file (code.C)
```

The code above will result in this simple message box:
\
<img src=img/msgBox.jpg>

**The second step** is to open the executable in Hex Editor (**HxD**):

<img src=img/hxd.jpg>

At the **end of the executable** I created a **code cave** by inserting lines of **nullbytes**

<img src=img/nullbytes.jpg></br>

Next step is to defined the flag which is **"why is it so dark in here"**, and I encode it in **base 64**. While I was developing this one of my teammate mentions that they can just use the **string** command to retrieve the information, thus i break the ciphertext into **small chunks** so that it won't be picked up by the string command. Now we can just insert the flag into the cave!

<img src=img/flag.jpg>

Now that we’ve finished the **'trojan'**, we can move on to simulating the **delivery**. In this scenario, I imagined the victim **downloading the trojan**. To simulate this, I set up a simple **Python server** on another machine and downloaded the file while **capturing the traffic using Wireshark**.

The Final result should be a **PCAP** file.

<img src=img/pcap.jpg>

## Solution
The solution apparently is pretty simple, **export the object** from **HTTP** protocol. You will find an executable named **done.exe**.

<img src=img/export.png>

\
Now if you decided to **run the executable**, it will give you a **hint** to where the **flag** is.

<img src=img/msgBox.jpg>

\
A **code cave** is a section in an executable filled with null bytes. Attackers can **inject malicious code** into this space, which poses a security risk. To visualize this, let's use a hex editor to examine the executable and find the flag.


<img src=img/hxd.jpg>

\
After analyzing the **decoded text** section, you should notice a couple of **base64 encoded cipher text** (show by '=' at the end of the cipher text). Decode this and try to put it as the flag.

**Answer: bhbureauCTF{why is it so dark in here}**