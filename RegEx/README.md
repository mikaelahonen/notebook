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

## Find all `<p>` and `</p>` tags
### RegEx
`</?p>`
### Expalantion
* `<` Match string "<".
* `/?` Match character "/" if it exists.
* `p>` Match string "p>".

## Find string at the end of a line
### RegEx
`some text$`
### Expalantion
* `some text` Match string "some text".
* `$` Match the end of a line.

## Find string at the beginning of a line
### RegEx
`^some text`
### Expalantion
* `^` Match the beginning of a line.
* `some text` Match string "some text".

## Find email at and domain
### RegEx
`@.+$`
### Explanation
* `@` Match string "@".
* `.+` Dot matches any character. Plus requires any number of characters, but at least one.
* `$` End of line. Might be also space or a separator character depenging on your list's structure.

## Replace the first character with Capital
### RegeEX
Find `^(.)`
Replace `\u\1`
### Explanation
<b>Find</b>
* `^` The beginning of line.
* `(.)` Any single character. Use brackets to capture the value.
<b>Replace</b>
* `\u` Capitalize the next character.
* `\1` Return the first captured value.