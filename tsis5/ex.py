""" # task7
    text.split('_'): Метод split() вызывается для входной текстовой строки с разделителем '_'. 
Это разбивает строку на список отдельных слов, причем каждое слово является отдельным элементом в списке.
    x.capitalize() для x в тексте.split('_'): Метод capitalize() вызывается для каждого элемента списка, 
созданного на предыдущем шаге. При этом первая буква каждого слова пишется заглавной буквой, 
а остальные буквы - строчными. Цикл for выполняет итерацию по каждому элементу списка, применяет к нему 
метод capitalize() и возвращает измененную строку.
    ".join(x.capitalize() для x в тексте.split('_')): Наконец, метод join() используется для объединения 
всех измененных строк с предыдущего шага в единую строку. Метод join() вызывается для пустой строки ("), 
которая используется в качестве разделителя между словами. Это создает окончательную строку регистра camel."""

"""# task10
    (?=...) Matches if ... matches next, but doesn't consume any of the string. This is called a lookahead assertion. 
    For example, Isaac (?=Asimov) will match 'Isaac ' only if it's followed by 'Asimov'.
    (?<!...) Matches if the current position in the string is not preceded by a match for .... 
    This is called a negative lookbehind assertion. Similar to positive lookbehind assertions, 
    the contained pattern must only match strings of some fixed length. Patterns which start with negative 
    lookbehind assertions may match at the beginning of the string being searched."""