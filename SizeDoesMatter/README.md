# Size Does Matter!!

Hey there, Intern. I have to be honest, I’m not convinced you’re ready to be part of our team yet—especially after that comment you made the other day, “size doesn’t matter.” Well, I’m here to show you just how much it really does! Let’s see if you’re up for proving me wrong.

---
## Goal
I still vaguely remember the day I attempted a challenge on **PicoCTF**. It involved **injecting a format string** into a program. I used '%x' to print the stack but was confused when the output appeared **scrambled**. Later, I realized it was due to the difference between **Big and Little Endian**. I want to show the implementation of basic computer concept to the participant.

## Development
First, I need to generate a random hex value using an online tool.

<img src=img/randHex.jpg>

Next, I want to import the hex into **CyberChef** and reformat it to easily modify the value.

<img src=img/cyberchef1.jpg>

Now, move the **string** into the **input** field and **inject the flag**. Then, use '**Swap Endianness**' to convert it to Little Endian format.

<img src=img/inject&swap.jpg>

Finally, we can add a hint to the challenge. Since the given format is in hex, it's natural for participants to convert it to text. This allows us to insert a hint in **Big Endian** format.

<img src=img/hint.jpg>

Now change the format back into hex and you got the challenge!

## Solution

Since the cipher text is in hex we can try decoding it in cyber chef.

<img src=img/hint.jpg>

We received a hint that **something is missing**. However, if we look closely, we can spot a string that **resembles** the **flag** format—but it appears **scrambled**. Now, remember the title mentioned something about **size**. Computers read data in two formats: **Big Endian and Little Endian**. To change the format, use **'Swap Endianness'** in CyberChef.

<img src=img/flag.jpg>

**Answer: bhbureau{1_4M_LiTt|_3r15ht}**