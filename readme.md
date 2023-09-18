# Stable Marriage Solver

This program uses the Gale-Shapley algorithm to solve a fun problem: matching people into stable couples. If you want to understand how it works and use it yourself, follow these easy steps.

## Input

1. **Open the `Input.txt` file.** This is where you tell the program who likes whom. Here's what the file should look like:

    ```
    3
    MAN_1 WOMAN_1 WOMAN_2 WOMAN_3
    MAN_2 WOMAN_3 WOMAN_2 WOMAN_1
    MAN_3 WOMAN_2 WOMAN_1 WOMAN_3
    WOMAN_1 MAN_2 MAN_3 MAN_1
    WOMAN_2 MAN_3 MAN_1 MAN_2
    WOMAN_3 MAN_2 MAN_1 MAN_3
    ```

    - The first line (`3`) is the number of people on each side (men and women).
    - The next lines show how much each person likes the others. For example, `MAN_1` likes `WOMAN_1` the most, then `WOMAN_2`.

2. **You can edit the `Input.txt` file** to match your preferences or add more people.

## Running the Program

1. **Make sure you have Python installed on your computer.**

2. **Open your computer's command prompt or terminal.**

3. **Navigate to the folder where the program is located.**

4. **Run the program** in cmd run command: `python assignment1.py`

## Output

1. **Open the `Output.txt` file.** It will look something like this:

    ```
    MAN_1 WOMAN_1
    MAN_2 WOMAN_2
    MAN_3 WOMAN_3
    ```

    - Each line shows a man and the woman they're matched with.

2. The program finds the best matches based on your preferences, making sure that no one wants to change partners.

## Testing

In the "Tests" folder, you'll find more example input and output files (like `Input1.txt` and `Output1.txt`). You can use these to practice and see how the program works with different preferences.

That's it! You've just used the Gale-Shapley algorithm to solve the Stable Marriage Problem. Have fun matching people! 😊
