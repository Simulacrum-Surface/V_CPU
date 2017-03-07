# V_CPU

About this tool:

Its an emulator for a notional assembly language, used in "Theoretische Informatik" by Hoffmann, Dirk W. (eISBN: 978-3-446-42854-6) 

For the syntax and more information, please refer to the book.

NOTE: </br>
This code was hacked together without a straight concept! Do NOT use this as an example of good coding style. Do NOT read the sourcecode if you want to learn something python-specific. A reimplementation is planned. I released this to command a view.
 
Please forgive me PEP.

Known Errors: </br>

- (FIXED) No Error when user tries to use uninitialized register
- (FIXED) When generation a 0 terminated number sequenz, it's possible that a 0 sneaked in before the actual end is reached
- Displaying the register is a desaster :D (-> a better overview will appear in the rewritten code)
- (FIXED) Zero-Division will be detectet only if you divide by 0 with DIV #0. </br>
LDA #0 </br>
STA 1 </br>
LDA #10 </br>
DIV 1</br>
OUT</br>
END</br></br>
In this case, it wont be detected.


Greetings,
Simulacrum
