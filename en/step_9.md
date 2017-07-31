## Displaying the result on a GUI

If you would like to make your insult generator easy to use, you could add a basic GUI. Ensure you have followed the [software installation instructions](https://learning-admin.raspberrypi.org/en/projects/shakespearean-insult-generator/what-you-will-need) to install the `guizero` library before attempting this section.

- At the start of your program, after the line of code where you imported the `random` library, import the `guizero` library:

  ```python
  from guizero import App, Text, PushButton
  ```

- Now at the very end of your program, add code to create an `App`. This is a simple GUI window where we will display your insult.

  ```python
  app = App("Shakespearean insult generator")
  app.display()
  ```

- Save your code and run it using F5. You should see a mainly blank window pop up, with the title "Shakespearean insult generator".

  ![Blank app window](images/app-window.png)

  You might notice that when you run the program, an insult is still printed out in the Python shell, even though we now want to display our insult on the GUI. This is because we coded the `insult_me()` function to *print* the insult rather than just generate it.

- Go back to your `insult_me()` function and replace the line `print(insult)` with the line `return insult`. This will cause the insult to be passed back from the function so we can use it, instead of just printing it out.

- Delete the line of code which calls the function `insult_me()`.

- Now add some `Text` to display your insult. This line of code should go between the `app =` line and the `app.display()` line:

  ```python
  message = Text(app, insult_me() )
  ```

  This line of code creates a `Text` object, adds it to the `app`, and then calls the function `insult_me()` to get an insult to display.

  ![Insult displayed in GUI](images/insult-in-gui.png)

- Now let's add a `PushButton` on the line immediately after the `Text`.

  ```python
  button = PushButton(app, new_insult, text="Insult me again")
  ```

  This code creates a `PushButton` object and adds it to the `app`. The button will call the function `new_insult` (which we haven't written yet) when it's pressed, and will display the text `"Insult me again"`.

- Write the function `new_insult()` which will be called when the button is pressed. You should put this code immediately after your `insult_me()` function, but be careful **not** to indent the first line of the function, otherwise Python will think this code is part of the `insult_me()` function too.

    ```python
    def new_insult():
        new_insult = insult_me()
        message.set(new_insult)
    ```

  This function calls the `insult_me()` function to generate a new random insult, and then sets the message on the GUI to be the newly generated insult.

  ![Insult button](images/insult-me-again.png)

- Run the program using F5 and enjoy creating a stream of Shakespearean insults at the press of a button! The finished code is [here](resources/shakespeare.py) if you want to check your code.

