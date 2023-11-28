# Description & Resources for this Repository

## Description 
Please see the [instructions.md](https://https://github.com/katforrest/roomcount/blob/main/Instructions.md) file for a description of the prompt. 

## Github Carpentries
***This repository is an exercise in learning how to use GitHub. I'm following the tutorial made available by the Smithsonian Institution called, ["Collaborating and sharing using GitHub without command line."](https://https://miketrizna.github.io/github-without-command-line/index.html)***


## Markdown
***Part of this exercise has been learning how to use Markdown.***

Save files as markdown files (.md) to utilize the formatting abilities.

To practice using Markdown, use the [The Carpentries CodiMD instance.](https://https://codimd.carpentries.org/OCiahPOvTI6zjgdu2qqTpA)

For more notes on markdown syntax, see the [Quickstart for writing on GitHub.](https://https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github)

```
Use the backtick ` character three times to offset code in it's own block in markdown.
Wrap the text in three backticks on separate lines before and after. 
Text formatted as code cannot be formatted in bold, underline, etc. 
```
>Use the > character to offset text as a block quote.


>When using the ** markup to display
**bold**
text, the asterisks must be next to the bold text with no space. The asterisks can be on the same line.

## New Code I Learned: Global()

First I had to generate a bunch of 0s and 1s to run my roomcount code on. In Python, I used a list of lists.

To do this, I had to use the global() function.
1. Create a variable name (row1, row2, row3... )
2. Create a list of 0s / 1s.
3. Used the variable name to create a new variable and define it with the list using global()[variable_name]
4. Go to the next variable name.

```
table = []
for i in range(5):
    row_name = f"row_{i + 1}"
    list = []
    for i in range(5):
        number = np.random.randint(0,2)
        list.append(number)
    globals()[row_name] = list
    table.append(globals()[row_name])
```
