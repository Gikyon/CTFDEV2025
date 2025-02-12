# Tune To Perfection DO

Hey Agent, the SOC team just reported a compromised host. Fortunately, the CSIRT team acted fast, contained the breach, and pulled the memory dump. Now, it’s your turn. Your mission is to dive into the dump and figure out exactly what the attacker did inside that host. Time to track down the traces and uncover their moves.

---

## Goal

In this challenge, I want to introduce the basics of **memory forensics** in a beginner-friendly way. The plan is to **hide the flag inside the command line (CLI) history**, encouraging participants to explore forensic techniques.

## Development

For development, I set up a fresh **Windows Virtual Machine (VM)** and wrote a simple **PowerShell script** to simulate **attacker execution from reverse shell**.

<img src=img/susFile.png>

The flag will be the **name of the file** itself. Next, I ran the **PowerShell** **script** inside the **command prompt** and **captured the memory dump** using **FTK Imager**.

<img src=img/captureMem.png>

\
Finally, I tested the challenge using **Volatility Workbench** to verify if the flag was present in the **memory dump**.

<img src=img/testing.png>

## Solution

The solution involves using the **Volatility tool** to enumerate and find the **filename**. There are several ways to approach this, but one method is to check the **CLI history**.

<img src=img/testing.png>