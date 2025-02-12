# Tune To Perfection RE

Great work, Agent. We’ve tracked down the executed malware. Now, it’s time to connect the dots and find the culprit. The threat hunter team has gathered intel that this APT specializes in hacking **Windows OS** and tends to leave behind traces in their malware. We’ve extracted the suspicious file, and your task is to dig deep and uncover the hidden signature they left for us. Let’s catch this attacker!

The format for this challenge is **bhbureau{...}**

---

[Goal](#goal)
[Development](#development)
[Solution](#solution)

## Goal

The main goal of this challenge is to introduce participants to **Alternate Data Streams** (ADS). ADS can be used to **hide files** within the **metadata of an original file**. To preserve ADS during transmission, we need to use **WinRAR’s** archive feature.

However, while overseeing the event, one of the participants demonstrated that the hidden file within the ADS could still be listed with WinRAR. **(I learned something new !)**

## Development

The development of this is rather easy, first we want the original file.
```
notepad susFile.txt //insert anything in the notepad
```
<img src=img/ori.jpg>

Next we want to create a new file containing the flag and hide it in the ADS.
```
notepad susFile.txt:flag //hide the flag here
```

<img src=img/hidden.jpg>

Let's check if it will be listed by dir command

<img src=img/check.jpg>

Now check the Alternate Data Stream, the key here is to use **command prompt** (cmd) rather than **powershell**. **(Windows 11)**

<img src=img/solution.jpg>

Finally to preserve it we can use **WinRAR** to archive this:

<img src=img/win.png>

## Solution

The intended way to solve this challenge is by **reading the description** and conducting some **research**. Once participants understand how to access ADS, there are multiple ways to retrieve the hidden file—one of which is using **Command Prompt (cmd)**.

<img src=img/solution.jpg>

**Answer: bhbureau{IL0veM4r5}**