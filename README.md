# V_CPU

About this tool:

Its an emulator for a notional assembly language, used in "Theoretische Informatik" by Hoffmann, Dirk W. (eISBN: 978-3-446-42854-6) 

For the syntax and more information, please refer to the book.


Requirements:
</br> </br>
-Python 3.X</br>
-PyQt5
 </br> </br>
How To:</br>
Just execute the Main.py.
</br></br>

NOTE: </br>
>Im very grateful for every bugreport :)
This code was hacked together without a straight concept! Do NOT use this as an example of good coding style. Do NOT read the sourcecode if you want to learn something python-specific. A reimplementation is planned. I released this to command a view.
 
Please forgive me PEP.



Known Errors: </br>


- (FIXED) No Error when user tries to use uninitialized register
- (FIXED) When generating a 0 terminated number sequenz, it's possible that a 0 sneaked in before the actual end is reached
- Displaying the register is a desaster :D (-> a better overview will appear in the rewritten code)
- (FIXED) Zero-Division will be detectet only if you divide by 0 with DIV #0. </br>
LDA #0 </br>
STA 1 </br>
LDA #10 </br>
DIV 1</br>
OUT</br>
END</br></br>
In this case, it wont be detected.

Shoutout to t0mat0hater for the bug-report.

Greetings,
Simulacrum

P.S. This is only for the group of testers:
</br></br>
Die Emailadresse habt ihr ja. Verschlüsseln ist keine Pflicht, aber gern gesehen. Daher... 
</br></br></br>

...Mein pub key:


-----BEGIN PGP PUBLIC KEY BLOCK-----

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
RRecej5thzuC
=aFGI
-----END PGP PUBLIC KEY BLOCK-----

