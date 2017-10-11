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
	  MouseClick("left", 376, 456, 1, 0)
   ElseIf $n == 3 Then
	  ; Click Medida #2
	  MouseClick("left", 475, 456, 1, 0)
   ElseIf $n == 4 Then
	  ; Click Medida #3
	  MouseClick("left", 575, 456, 1, 0)
   EndIf
   $state = $state + 1
EndFunc
