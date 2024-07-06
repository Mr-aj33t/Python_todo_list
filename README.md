# Python_todo_list
Simple Flask Todo App using MYSQL and SQLAlchemy database.
Techonology I Use: python, flask freamwork, html, css, js

For styling [semantic-ui](https://semantic-ui.com/) is used.

### Setup
Create project with virtual environment

```console
$ mkdir myproject
$ cd myproject
$ python -m venv venv
```

Activate it
``` console
venv\scripts\activate
```

Install Flask
```console
$ pip install Flask
$ pip install Flask-SQLAlchemy
```

Set environment variables in terminal

```console
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
```

Run the app
```console
$ flask run
```

# Python_todo_list Overview
1) first we nees to start the server you can simply type in your terminal "pythone app.py"
![image alt](https://github.com/Mr-aj33t/Python_todo_list/blob/e4be1ada7bf923c9336470fbed1c7f280cd5434d/Screenshorts/1.png)

2) Now, you can open your browser and type "127.0.0.1:5000" in the address bar to view your page like this.
   ![image alt](https://github.com/Mr-aj33t/Python_todo_list/blob/77f472bb0228b7cfbae802913f0296ff208ddc92/Screenshorts/2.png)

3) If you want to add a task, simply type any task in the provided to-do title bar and click on the add button. You will see that the task has been added.
   Here is the picture, you can see that some tasks have been added.
   ![image alt](https://github.com/Mr-aj33t/Python_todo_list/blob/77f472bb0228b7cfbae802913f0296ff208ddc92/Screenshorts/3.png)

4) If you want to see whether data is being added to your database or not, you can simply log in to MySQL and check your database.
   Here are some pictures that will give you an idea of how it works.
   ![image alt](https://github.com/Mr-aj33t/Python_todo_list/blob/77f472bb0228b7cfbae802913f0296ff208ddc92/Screenshorts/1a.png)

  ![image alt](https://github.com/Mr-aj33t/Python_todo_list/blob/77f472bb0228b7cfbae802913f0296ff208ddc92/Screenshorts/4b.png)

5) If you want to complete a task, simply click on the update button, and you will see the task completion option appear in green.
   Here is a picture where you can get an idea of how it works.
   ![image alt](https://github.com/Mr-aj33t/Python_todo_list/blob/77f472bb0228b7cfbae802913f0296ff208ddc92/Screenshorts/4.png)
   
6) If you want to delete a task, you will see that the task is removed as soon as you click on the delete button.
    Here are image that will give you an idea.
    ![image alt](https://github.com/Mr-aj33t/Python_todo_list/blob/77f472bb0228b7cfbae802913f0296ff208ddc92/Screenshorts/5.png)
   
 7)  If you want to check whether the task has been removed from the database, you can go to MySQL and check the database.
      Here are image that will give you an idea.
      ![image alt](https://github.com/Mr-aj33t/Python_todo_list/blob/77f472bb0228b7cfbae802913f0296ff208ddc92/Screenshorts/6c.png)

8)  If you want to remove all tasks at once, simply click on the "Reset All Todos" button.
   As soon as you click, a pop-up message will appear for confirmation, asking if you want to reset the data or not. when you click ok button the all your todo task was removed from the app
    Here is the images, you can see it.
    ![image alt](https://github.com/Mr-aj33t/Python_todo_list/blob/77f472bb0228b7cfbae802913f0296ff208ddc92/Screenshorts/6.png)

    ![image alt](https://github.com/Mr-aj33t/Python_todo_list/blob/77f472bb0228b7cfbae802913f0296ff208ddc92/Screenshorts/7.png)

    ![image alt](https://github.com/Mr-aj33t/Python_todo_list/blob/77f472bb0228b7cfbae802913f0296ff208ddc92/Screenshorts/7d.png)

9) If you're facing difficulty installing my app on your PC, I've added a contact button.
    Simply click on it to redirect to my contact page where you can find my contact details and easily get in touch with me.
   You can see the image of my contact page here.
   ![image alt](https://github.com/Mr-aj33t/Python_todo_list/blob/77f472bb0228b7cfbae802913f0296ff208ddc92/Screenshorts/8.png)
   
10)  You can see in your terminal your all the tasks have added and deleted in the to-do app.
    Here is the image you can see.
  ![image alt](https://github.com/Mr-aj33t/Python_todo_list/blob/77f472bb0228b7cfbae802913f0296ff208ddc92/Screenshorts/9.png)
