# Tune To Perfection MI

Nice job, Agent. Thanks to your efforts, we've successfully identified the **APT**'s code name. Now, it’s time to strike back. We’ve located the **APT**'s server login page, and your mission is to breach it. If you succeed, the intel you uncover will give us the upper hand and throw a serious wrench in their plans. Let’s do this—if you crack it, we’ll be one step closer to taking them down!

https://issessionsctf-tunetoprefection3.chals.io/ **(closed)**

The format for this challenge is **bhbureau{...}**

---

[Goal](#goal)
[Development](#development)
[Solution](#solution)

## Goal

The goal of this challenge is to introduce participants to **cookies** and **web inspection tools**. From my understanding, most **cookies** are **encoded** in **Base64**.

To make the challenge more engaging, I added some creative hints. One hint comes from the previous two flags: **bhbureauCTF{1L1k3Fl0W3r5}** and **bhbureau{IL0veM4r5}**. Another hint is in the challenge description, where **APT is bolded**. At the time, a popular song by Bruno Mars and Rosé called '**APT**' was trending.

The **decoded cookie** value is formatted as **male:female**, which is commonly used for **credentials**. The task is for participants to modify this value by replacing it with their first names, respectively, to obtain the flag.

## Development

To create a web challenge, the first step is to build the website (duh!). For this, I used Flask, a lightweight Python framework. Below is the `app.py` file:

```
from flask import Flask, render_template, request, make_response
import os

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def login():
    message = ''
    if request.method == 'POST':
        message = 'no account is registered'
        cookie = request.cookies.get('secret')
        if cookie == 'cGV0ZXI6cm9zZWFubmU=':
            message = 'bhbureau{dontyouwantmelikeiwantyoubaby\}'
        return render_template('login.html', message=message)
            
    else:
        res = make_response(render_template('login.html', message=message))
        res.set_cookie("secret", value="bWFsZTpmZW1hbGU")
        return res


// below is more for infrastructure
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))  # Default to 8000 if PORT is not set
    app.run(debug=False, host='0.0.0.0', port=port)

```

To explain the code above, the website **only accepts** two `HTTP` methods: `GET` and `POST`, with `/` as the only available route. If the request method is `POST` and the **cookie value** matches my desired value `cGV0ZXI6cm9zZWFubmU=`, the server will return the **flag**.

For the HTML part it is relatively simple and self explanatory:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h2>Login</h2>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <!-- i love them, i even know their first real name-->
        <button type="submit">Login</button>
    </form>
    <p>{{ message }}</p>
</body>
</html>

```

As you can see above, I intentionally included a **comment** in the code. The **purpose** of this is to **simulate** a **data leak** in the **DOM**.

Finally the **DockerFile**,
```
# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR ./www

# Install dependencies
RUN pip3 install flask

# Copy the application files into the container
COPY ./www .

# Expose port 80
EXPOSE 80
ENV PORT=80

# Set environment variable to make Flask run in production
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# Run the Flask app
CMD ["python", "app.py"]

```

This **Dockerfile** helps build the **container** I need. It sets up a **Python environment**, installs **Flask**, opens and maps port 80, and finally runs `app.py` to launch the **website**.

## Solution

When you open the website, you will see the following homepage:

<img src=img/homepage.jpg>

Notice that if you try to login, it will return an error message of: 

<img src=img/err.jpg>

This is also a **hint** that the **login page** is just a **decoy**. The next thing you should do is to check the **source**:

<img src=img/src.jpg>

Remember the **previous two flags** and the **bolded text** in the challenge **description**? If you guessed the song **APT by Rosé and Bruno Mars**, you’re correct! Now let's check the cookie.

<img src=img/secret.jpg>

What is so **secretive** about this? let's find out!

<img src=img/decoded.jpg>

Now it is starting to connect, let's find out **rose and burno's real name**:

<img src=img/name.jpg>

It's **peter and roseanne**! Now let's try putting it as the cookie format , encode it and send a POST request!

<img src=img/cookie.jpg>
<img src=img/befinal.jpg>
<img src=img/final.jpg>

**Answer: bhbureau{dontyouwantmelikeiwantyoubaby\}**