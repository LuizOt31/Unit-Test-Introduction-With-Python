# Unit-Test-Introduction-With-Python
This repository contains a brief introduction to unit test with the Pytest framework.

There are four archives , three of them have functions to test in the main archive (test_main.py):
  - calculadora.py: it has two functios, the first return a sum of two parameter, and the second returns the subtraction. "Somar" and "Subtrair", respectively.  
  - primo.py: only one function that return if the parameter is a prime number called "Eh_primo".
  - manipulador_string.py: one function that reverses the word called "inverter".

test_main.py has eight function, two for each function of the others archives. Every function that has in the name the sufix "_erro" means it will be for wrong results in the test. The rest that doesn't have it means it will be for correct results. It is important to highlight that the test with pytest is with the method "Assert" (assert name_function(a,b) == esperado), in terminal this code have to show four errors.
Let's see what each function does!
  - test_soma: takes two variables called a and b with the value 2 both. the following variable called "esperado" is equal to 4. testing with the Assert method, Somar will return (with parameters a and b) 4, equal to "esperado".
  - test_soma_erro: takes two variables called a and b with the value 2 both. the following variable called "esperado" is equal to 5. testing with the Assert method, Somar will return (with parameters a and b) 4, different to "esperado".
  - test_sub: takes two variables called a and b with the value 1 both. the following variable called "esperado" is equal to 0. testing with the Assert method, Subtrair will return (with parameters a and b) 0, equal to "esperado".
  - test_sub_erro: takes two variables called a and b with the value 2 and 1, respectively. the following variable called "esperado" is equal to 0. testing with the Assert method, Subtrair will return (with parameters a and b) 1, differently from "esperado".
  - test_primo: takes one variable called a with the value 5. the following variable called "esperado" is equal to bolean type True. testing with the Assert method, Eh_primo will return True, same as "esperado".
  - test_primo_erro: takes one variable called a with the value 10. the following variable called "esperado" is equal to bolean type True. testing with the Assert method, Eh_primo will return False, differently as "esperado"
  - test_inverter: test the function with parameter "python", if returns same as "nohtyp", the function will return true and will not have errors.
  - test_inverter_erro: test the function with parameter "python" again, if returns "piton" the Assert method will see that don't have error. But this don't have, because "piton" is not the correct, so Assert identifies as a error.

