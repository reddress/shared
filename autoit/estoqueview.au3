#include <EditConstants.au3>
#include <GUIConstantsEx.au3>
#include <WindowsConstants.au3>

Global $todos = FileOpen("todoscodigos.txt", 0)

Opt("GUIOnEventMode", 1)
$mainwindow = GUICreate("Estoque View", 600, 120, 0, 580)
WinSetOnTop("Estoque View", "", 1)

GUISetOnEvent($GUI_EVENT_CLOSE, "CLOSEClicked")
$codigo = GUICtrlCreateInput("", 20, 10, 66, 19)

;$button2012 = GUICtrlCreateButton("2012", 20, 40, 60)
$buttonNext = GUICtrlCreateButton("Next", 20, 40, 60)

;$estoque = GUICtrlCreateInput("", 92, 10, 110, 19)
$notes = GUICtrlCreateEdit("", 208, 10, 348, 100)

$buttonCopy = GUICtrlCreateButton("copy", 90, 40, 45)
GUICtrlSetOnEvent($buttonNext, "fnNext")
GUICtrlSetOnEvent($buttonCopy, "fnCopy")
;GUICtrlSetOnEvent($buttonAddUC, "addUC")

;$estoque = GUICtrlCreateEdit("", 172, 10, 70, 50, BitOR($ES_AUTOVSCROLL, $ES_AUTOHSCROLL, $ES_WANTRETURN))
GUISetState(@SW_SHOW)
$oldcode = ""

While 1
   ;$newcode = GUICtrlRead($codigo)
   ;If $oldcode <> $newcode Then
;	  GUICtrlSetData($estoque, "")
;	  $oldcode = $newcode
;  EndIf
  Sleep(100)
WEnd

Func fnCopy()
   GUICtrlSetData($notes, GUICtrlRead($notes) & GUICtrlRead($codigo) & @CRLF)
EndFunc

Func fnNext()
   Local $line = FileReadLine($todos)
   If @error = -1 Then
	  GUICtrlSetData($codigo, "END")
   Else
	  GUICtrlSetData($codigo, $line)
   EndIf
   
   ; click on Produto window
   MouseClick("left", 88, 12)
   Sleep(200)
   Send("{F3}")
   Sleep(200)
   Send(GUICtrlRead($codigo))
   Send("{ENTER}")
   Sleep(200)
   MouseMove(55,655)
   
EndFunc

Func fnGen2013()
   MouseClick("left", 88, 12)
   Sleep(200)
   Send("{F3}")
   Sleep(200)
   Send(GUICtrlRead($codigo))
   Send("{ENTER}")
   Sleep(300)
   
   MouseClick("left", 210, 62)
   MouseClick("left", 210, 164)
   Sleep(200)
   
   Send("{RIGHT}01{RIGHT}")
   Sleep(500)
   Send("{ENTER}")
   ;WinWaitActive(" Ficha do Produto (PARALELO)  ")
   MouseMove(412, 77)
EndFunc

Func fnGen2012()
   MouseClick("left", 88, 12)
   Sleep(200)
   Send("{F3}")
   Sleep(200)
   Send(GUICtrlRead($codigo))
   Send("{ENTER}")
   Sleep(300)
   
   MouseClick("left", 210, 62)
   MouseClick("left", 210, 164)
   Sleep(200)
   
   Send("{RIGHT}01{RIGHT}2012")
   Sleep(100)

   ; open calendar
   MouseClick("left", 488, 271)
   
   ; move calendar to december
   ; UPDATED 9 Sept 2013
   ; ===== CHANGE THIS
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   MouseClick("left", 414, 297)
   
   ; click on 31
   MouseClick("left", 451, 437)
   
   ;WinWaitActive(" Ficha do Produto (PARALELO)  ")
   MouseMove(412, 77)
EndFunc

Func CLOSEClicked()
   Exit
EndFunc