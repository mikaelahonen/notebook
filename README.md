# Regular Expressions
Regular expressions that I need relatively often.

Regular expressions are used to match 
text patterns. For example:
* Match only selected characters.
* Match a character if it exists.
* Specify only UPPERCASE characters.
* Match the string if it is at the end of line.
* And any combinations of these...

Use cases
* Replace text in a text editor such as Notepad++.
* Remove text in a text editor by replacing with empty string.
* Find one or all occurences in text editor.
* Find one or all occurences in browser by using a plugin.
* Find, replace or remove in program code.

## All `<p>` and `</p>` tags
### RegEx
`</?p>`
### Expalantion
* `<` Match string "<".
* `/?` Match character "/" if it exists.
* `p>` Match string "p>".

## String at the end of line
### RegEx
`some text$`
### Expalantion
* `some text` Match string "some text".
* `$` Match end of line.

## Email at and domain
### RegEx
`@.+$`
### Explanation
* `@` Match string "@".
* `.+` Dot matches any character. Plus requires any number of characters, but at least one.
* `$` End of line. Might be also space or a separator character depenging on your list's structure.
