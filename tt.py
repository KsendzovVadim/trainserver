import re
text = 'how are u? umberella u! u. U. U@ U# u '
print (re.sub (' [u|U][s,.,?,!,W,#,@ (^a-zA-Z)]', ' you ', text))