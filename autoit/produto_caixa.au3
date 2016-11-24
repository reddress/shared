HotKeySet("`", "CycleProduto")

While 1 
   Sleep(100)
WEnd

; cycle through three states: Save button, Peso bruto, Medida
Global $state = 1

Func CycleProduto()
   Global $state
   Local $n = Mod($state, 5)
   If $n == 0 Then
	  ; Click Save
	  MouseClick("left", 72, 64, 1, 0)
   ElseIf $n == 1 Then
	  ; Double click Peso
	  MouseClick("left", 63, 350, 2, 0)
   ElseIf $n == 2 Then
	  ; Click Medida #1
	  MouseClick("left", 453, 551, 1, 0)
   ElseIf $n == 3 Then
	  MouseClick("left", 575, 551, 1, 0)
   ElseIf $n == 4 Then
	  MouseClick("left", 675, 551, 1, 0)
   EndIf
   $state = $state + 1
EndFunc
