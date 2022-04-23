# Answers-Extractor
Ever solved an MCQ assignment and felt too lazy to check it yourself? Well you have the perfect solution now.

# How to use
## Requirements for this project
1. Any version of Python 3
2. Any version of Microsoft Excel

## Steps
### Excel Side
1. Use MS Excel to solve your assignment and write only your options in one column
2. Select this column and go to conditional formatting
3. Set up a new rule and select "Use a formula to determine which cells to format"
4. Enter this formula `=AND(NOT(ISBLANK(INDIRECT("RC[1]",0))), NOT(INDIRECT("RC[0]",0)=INDIRECT("RC[1]",0)))` and select your preferred formatting
5. You should have everything ready on the excel side

### Python side
1. Save the Answer Extractor file and open `Answers.txt`
  - If the file does not exist, run the code once to create it
2. Find the answer key of the assignment you are solving and copy paste it into the above mentioned text file
3. Execute the Answer Extractor python file
4. You will now find a list of all your answers in a csv file and also printed in the console for easy copying

### For New Answers Extractor
1. Install the pyperclip module via pip to allow for the answers to be directly copied intor your clipboard
2. Copy the answers from the answer key and simply paste into the python terminal
3. The answers will be copied to your clipboard so you can directly paste into excel

### Bringing everything together
- Copy and paste the extracted answers in the column to the right of the one containing your answers and you should see the wrong answers light up
