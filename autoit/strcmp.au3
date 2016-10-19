
Local $str1 = "143143A"
Local $str2 = "143140"

Local $iCmp = StringCompare($str1, $str2)
MsgBox(0, "", _
"result " & $iCmp)