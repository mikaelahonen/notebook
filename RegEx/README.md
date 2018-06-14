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

<b>RegEx</b>
`</?p>`

<b>Expalantion</b>
* `<` Match string "<".
* `/?` Match character "/" if it exists.
* `p>` Match string "p>".

## Find string at the end of a line

<b>RegEx</b>
`some text$`

<b>Expalantion</b>
* `some text` Match string "some text".
* `$` Match the end of a line.

## Find string at the beginning of a line

<b>RegEx</b>
`^some text`

<b>Expalantion</b>
* `^` Match the beginning of a line.
* `some text` Match string "some text".

## Find email at and domain

<b>RegEx</b>
`@.+$`

<b>Explanation</b>
* `@` Match string "@".
* `.+` Dot matches any character. Plus requires any number of characters, but at least one.
* `$` End of line. Might be also space or a separator character depenging on your list's structure.

## Replace the first character with Capital

<b>RegeEx</b>
Find `^(.)`

Replace `\u\1`

<b>Explanation</b>
Find
* `^` The beginning of line.
* `(.)` Any single character. Use brackets to capture the value.
<b>Replace</b>
* `\u` Capitalize the next character.
* `\1` Return the first captured value.

## List to comma separated string

<b>RegEx</b>
Find `([a-z|\)])\r\n`

Replace `$1, `


<b>Explanation</b>
Find
* `([a-z|\)])` Find a character a-z or closing bracket. Add other characters if needed. This part is needed to avoid matching empty rows.
* `\r\n` Line break in Windows.

Replace
* `$1` Get the matched character.
* `, ` Replace line breaks with comma and space.

## List of numbers to comma separated string for SQL
<b>RegEx</b>
Find `([0-9]+)\r\n`

Replace `'$1',`


<b>Explanation</b>
Find
* `([0-9]+)` Find a sequence of digits.
* `\r\n` Line break in Windows.

Replace
* `'$1'` Get the matched number sequence and enclose in single quotes.
* `,` Replace line breaks with comma.

## Replace markdown header with HTML tag
<b>RegEx</b>

Find `### (.+)?$`
<br/>
Replace `<b>$1</b>`

<b>Explanation</b>

Find
* `### ` Match markdown header identifier.
* `(.+)?` Greedy match for any character combination.
* `$` End of line.  

Replace
* `<b>` HTML open tag.
* `$1` Get the matched header text.
* `</b>` HTML closing tag.
